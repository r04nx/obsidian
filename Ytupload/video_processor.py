import cv2
import numpy as np
import moviepy.editor as mp
import os
import time
from flask_socketio import emit
import concurrent.futures
import logging

logger = logging.getLogger(__name__)

def process_image(file_path, gpu_available, force_gpu=False):
    """Process a single image with GPU acceleration if available while preserving aspect ratio"""
    img = cv2.imread(file_path)
    if img is None:
        return None
    
    # Use GPU for image processing if available and forced or detected
    use_gpu = (gpu_available or force_gpu) and cv2.cuda.getCudaEnabledDeviceCount() > 0
    
    # Calculate aspect ratio and determine how to resize
    h, w = img.shape[:2]
    aspect_ratio = w / h
    
    # Target dimensions (1920x1080)
    target_w, target_h = 1920, 1080
    target_aspect = target_w / target_h
    
    # Determine dimensions that preserve aspect ratio
    if aspect_ratio > target_aspect:  # Wider than 16:9
        new_w = target_w
        new_h = int(target_w / aspect_ratio)
    else:  # Taller than 16:9 (portrait)
        new_h = target_h
        new_w = int(target_h * aspect_ratio)
    
    # Create a black canvas of target size
    canvas = np.zeros((target_h, target_w, 3), dtype=np.uint8)
    
    # Calculate position to center the image
    x_offset = (target_w - new_w) // 2
    y_offset = (target_h - new_h) // 2
    
    if use_gpu:
        try:
            # Create a GPU matrix and upload the image
            gpu_img = cv2.cuda_GpuMat()
            gpu_img.upload(img)
            
            # Resize preserving aspect ratio
            gpu_img = cv2.cuda.resize(gpu_img, (new_w, new_h))
            
            # Download the processed image back to CPU
            resized_img = gpu_img.download()
            
            # Place the resized image on the canvas
            canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_img
            
            logger.info(f"Processed image {os.path.basename(file_path)} with GPU acceleration")
        except Exception as e:
            logger.error(f"GPU processing failed for {os.path.basename(file_path)}: {str(e)}")
            # Fallback to CPU if GPU processing fails
            resized_img = cv2.resize(img, (new_w, new_h))
            canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_img
    else:
        # CPU processing
        resized_img = cv2.resize(img, (new_w, new_h))
        canvas[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_img
    
    # Convert BGR to RGB for moviepy
    canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB)
    return canvas

def optimize_video(video_clip, preserve_aspect_ratio=True, max_resolution=(1920, 1080)):
    """Optimize video clip to reduce memory usage while preserving aspect ratio"""
    if preserve_aspect_ratio:
        # Get original dimensions
        w, h = video_clip.size
        aspect_ratio = w / h
        target_w, target_h = max_resolution
        target_aspect = target_w / target_h
        
        # Determine new dimensions that preserve aspect ratio
        if aspect_ratio > target_aspect:  # Wider than 16:9
            new_w = target_w
            new_h = int(target_w / aspect_ratio)
        else:  # Taller than 16:9 (portrait)
            new_h = target_h
            new_w = int(target_h * aspect_ratio)
        
        # Resize the video
        video_clip = video_clip.resize(width=new_w, height=new_h)
        
        # Create a black background clip
        bg = mp.ImageClip(np.zeros((target_h, target_w, 3), dtype=np.uint8), duration=video_clip.duration)
        
        # Position the video in the center
        x_pos = (target_w - new_w) // 2
        y_pos = (target_h - new_h) // 2
        
        # Composite the video on the background
        video_clip = video_clip.set_position((x_pos, y_pos))
        video_clip = mp.CompositeVideoClip([bg, video_clip], size=max_resolution)
    else:
        # Simple resize without preserving aspect ratio
        if video_clip.w > max_resolution[0] or video_clip.h > max_resolution[1]:
            video_clip = video_clip.resize(height=max_resolution[1], width=max_resolution[0])
    
    # Reduce frame rate if it's too high (over 30fps)
    if video_clip.fps > 30:
        video_clip = video_clip.set_fps(30)
    
    return video_clip

def check_gpu_available():
    """Check if GPU is available using multiple methods"""
    # Method 1: Check using OpenCV CUDA
    cuda_available = cv2.cuda.getCudaEnabledDeviceCount() > 0
    
    # Method 2: Try to import and check torch
    try:
        import torch
        torch_available = torch.cuda.is_available()
    except ImportError:
        torch_available = False
    
    # Method 3: Check using nvidia-smi command
    try:
        import subprocess
        result = subprocess.run(['nvidia-smi'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        nvidia_smi_available = result.returncode == 0 and 'NVIDIA-SMI' in result.stdout
    except Exception:
        nvidia_smi_available = False
    
    # Log all detection methods
    logger.info(f"GPU detection: OpenCV CUDA: {cuda_available}, PyTorch: {torch_available}, nvidia-smi: {nvidia_smi_available}")
    
    # Return True if any method detects GPU
    return cuda_available or torch_available or nvidia_smi_available

def create_slideshow(file_paths, output_path, duration_per_item=3, socketio=None, force_gpu=False, background_audio=None):
    start_time = time.time()
    total_files = len(file_paths)
    total_size_bytes = sum(os.path.getsize(f) for f in file_paths if os.path.exists(f))
    total_size_mb = total_size_bytes / (1024 * 1024)
    
    # Check for GPU availability using multiple methods
    gpu_available = check_gpu_available()
    logger.info(f"GPU available: {gpu_available}, Force GPU: {force_gpu}")

    clips = []
    image_count = 0
    video_count = 0
    timestamps = []
    current_time = 0
    
    # Process files in batches to avoid memory issues
    batch_size = 10  # Process 10 files at a time
    for batch_start in range(0, total_files, batch_size):
        batch_end = min(batch_start + batch_size, total_files)
        batch_files = file_paths[batch_start:batch_end]
        
        batch_clips = []
        for idx, file_path in enumerate(batch_files):
            if not os.path.exists(file_path):
                logger.error(f"File does not exist: {file_path}")
                continue
                
            global_idx = batch_start + idx
            # Update progress
            progress = int((global_idx / total_files) * 100)
            if socketio:
                socketio.emit('processing_progress', {
                    'progress': progress,
                    'current_file': os.path.basename(file_path),
                    'processed': global_idx,
                    'total': total_files
                })
            
            # Store timestamp information
            file_name = os.path.basename(file_path)
            timestamps.append({
                'time': current_time,
                'name': file_name,
                'type': 'video' if file_path.lower().endswith(('.mp4', '.mov', '.avi')) else 'image'
            })
            
            # Check if the file is a video
            if file_path.lower().endswith(('.mp4', '.mov', '.avi')):
                try:
                    video = mp.VideoFileClip(file_path)
                    # Optimize video to reduce memory usage while preserving aspect ratio
                    video = optimize_video(video, preserve_aspect_ratio=True)
                    batch_clips.append(video)
                    video_count += 1
                    current_time += video.duration
                    logger.info(f"Added video: {file_name}, duration: {video.duration:.2f}s")
                except Exception as e:
                    logger.error(f"Error processing video {file_name}: {str(e)}")
                    # If video fails, create a placeholder image with error message
                    img = np.zeros((1080, 1920, 3), dtype=np.uint8)
                    cv2.putText(img, f"Error: {file_name}", (100, 540), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 3)
                    image_clip = mp.ImageClip(img, duration=duration_per_item)
                    batch_clips.append(image_clip)
                    current_time += duration_per_item
            else:
                # Process images in parallel for better performance
                try:
                    img = process_image(file_path, gpu_available, force_gpu)
                    if img is not None:
                        image_clip = mp.ImageClip(img, duration=duration_per_item)
                        batch_clips.append(image_clip)
                        image_count += 1
                        current_time += duration_per_item
                        logger.info(f"Added image: {file_name}")
                    else:
                        logger.error(f"Failed to load image: {file_name}")
                except Exception as e:
                    logger.error(f"Error processing image {file_name}: {str(e)}")
        
        # Add batch clips to main clips list
        clips.extend(batch_clips)
        
        # Force garbage collection to free memory
        import gc
        gc.collect()

    if not clips:
        raise ValueError("No valid media files provided")

    # Emit message about concatenating clips
    if socketio:
        socketio.emit('processing_progress', {
            'progress': 80,
            'current_file': 'Concatenating clips...',
            'processed': total_files,
            'total': total_files
        })

    # Concatenate all clips with optimized settings
    final_clip = mp.concatenate_videoclips(clips, method="compose")
    
    # Add background audio if provided
    if background_audio and os.path.exists(background_audio):
        try:
            # Load the background audio
            bg_audio = mp.AudioFileClip(background_audio)
            
            # Make the audio loop if it's shorter than the video
            if bg_audio.duration < final_clip.duration:
                # Calculate how many loops we need
                loops_needed = int(final_clip.duration / bg_audio.duration) + 1
                # Create a list of the same audio clip repeated
                audio_clips = [bg_audio] * loops_needed
                # Concatenate them
                bg_audio = mp.concatenate_audioclips(audio_clips)
                # Trim to match video duration exactly
                bg_audio = bg_audio.set_duration(final_clip.duration)
            else:
                # Trim audio if it's longer than the video
                bg_audio = bg_audio.set_duration(final_clip.duration)
            
            # For each video clip, we need to adjust the background audio
            # If the final clip has audio, create a composite with lowered background volume
            if final_clip.audio is not None:
                # Lower the background audio volume
                bg_audio = bg_audio.volumex(0.3)  # 30% volume for background
                final_audio = mp.CompositeAudioClip([bg_audio, final_clip.audio])
                final_clip = final_clip.set_audio(final_audio)
            else:
                # Just use the background audio
                final_clip = final_clip.set_audio(bg_audio)
                
            logger.info("Added background audio with volume adjustments")
        except Exception as e:
            logger.error(f"Error adding background audio: {str(e)}")

    # Emit message about writing video
    if socketio:
        socketio.emit('processing_progress', {
            'progress': 90,
            'current_file': 'Writing final video...',
            'processed': total_files,
            'total': total_files
        })
    
    # Record start time for progress tracking
    progress_start_time = time.time()
    
    # Define a custom logger class that MoviePy 1.0.3 will accept
    from proglog import ProgressBarLogger
    
    class MyBarLogger(ProgressBarLogger):
        def __init__(self, socketio=None, total_files=0):
            super().__init__()
            self.socketio = socketio
            self.total_files = total_files
            self.start_time = time.time()
            
        def callback(self, **changes):
            # Every time the logger is updated, this is called
            super().callback(**changes)
            if 'frame' in changes and 'total' in self.bars['t']:
                t = self.bars['t']['index']
                total = self.bars['t']['total']
                if total > 0:
                    frame_percent = int((t / total) * 100)
                    progress_bar = '=' * int(frame_percent / 5) + ' ' * (20 - int(frame_percent / 5))
                    elapsed = time.time() - self.start_time
                    speed = t / elapsed if elapsed > 0 else 0
                    progress_msg = f"frame_index: {frame_percent}%|{progress_bar}| {int(t)}/{int(total)} [00:{int(elapsed)}s, {speed:.2f}it/s, now=None]"
                    
                    if self.socketio:
                        self.socketio.emit('processing_progress', {
                            'progress': 90 + int(frame_percent / 10),  # Map frame progress to 90-100% overall progress
                            'current_file': progress_msg,
                            'processed': self.total_files,
                            'total': self.total_files
                        })
    
    # Create our custom logger
    my_logger = MyBarLogger(socketio=socketio, total_files=total_files)
    
    final_clip.write_videofile(output_path, 
                             codec='libx264', 
                             audio_codec='aac',
                             fps=30,
                             threads=4,  # Use multiple threads for encoding
                             preset='faster',  # Use faster preset for better performance
                             logger=my_logger,  # Use our custom logger
                             verbose=False)  # Disable verbose output

    # Clean up
    final_clip.close()
    for clip in clips:
        try:
            clip.close()
        except:
            pass
    
    # Calculate processing time and stats
    end_time = time.time()
    processing_time = end_time - start_time
    
    stats = {
        'processing_time': round(processing_time, 2),
        'total_files': total_files,
        'image_count': image_count,
        'video_count': video_count,
        'total_size_mb': round(total_size_mb, 2),
        'gpu_used': gpu_available or force_gpu,
        'background_audio': background_audio is not None,
        'timestamps': timestamps
    }
    
    logger.info(f"Slideshow created: {output_path}")
    logger.info(f"Stats: {stats}")
    
    # Emit completion
    if socketio:
        socketio.emit('processing_complete', stats)
    
    return stats
