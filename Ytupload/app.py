import os
from flask import Flask, request, render_template, jsonify, send_file
from flask_socketio import SocketIO
from werkzeug.utils import secure_filename
from video_processor import create_slideshow
from ytconnecter import get_authenticated_service, upload_video
import uuid
import json
import logging
from datetime import datetime

app = Flask(__name__)
# Increase max content length to 10GB
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 * 1024
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
app.config['AUDIO_FOLDER'] = 'audio'
app.config['CHUNK_SIZE'] = 1024 * 1024  # 1MB chunks for processing
app.secret_key = os.urandom(24)
socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=10e8)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure all required directories exist
for folder in [app.config['UPLOAD_FOLDER'], app.config['OUTPUT_FOLDER'], app.config['AUDIO_FOLDER']]:
    os.makedirs(folder, exist_ok=True)

# Allowed file extensions
ALLOWED_EXTENSIONS = {
    'image': {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'webp'},
    'video': {'mp4', 'mov', 'avi', 'mkv', 'webm'},
    'audio': {'mp3', 'wav', 'ogg', 'm4a', 'aac'}
}

def allowed_file(filename, file_type):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS.get(file_type, set())

@app.context_processor
def inject_globals():
    """Inject global variables into all templates"""
    return {
        'current_year': datetime.now().year
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def index_new():
    """Route to test the new componentized template"""
    return render_template('index_new.html')

@app.route('/test-confetti')
def test_confetti():
    """Route to test the confetti animation"""
    return render_template('test_confetti.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    try:
        if 'files[]' not in request.files:
            return jsonify({'error': 'No files provided'}), 400
        
        files = request.files.getlist('files[]')
        if not files or files[0].filename == '':
            return jsonify({'error': 'No files selected'}), 400
        
        # Check total file size
        total_size = 0
        max_size = 8 * 1024 * 1024 * 1024  # 8GB total limit
        for file in files:
            file.seek(0, os.SEEK_END)
            total_size += file.tell()
            file.seek(0)
        
        if total_size > max_size:
            return jsonify({'error': 'Total file size exceeds limit of 8GB'}), 413
        
        # Process background audio if provided
        background_audio_path = None
        if 'background_audio' in request.files and request.files['background_audio'].filename != '':
            audio_file = request.files['background_audio']
            if allowed_file(audio_file.filename, 'audio'):
                audio_filename = secure_filename(audio_file.filename)
                audio_path = os.path.join(app.config['AUDIO_FOLDER'], audio_filename)
                audio_file.save(audio_path)
                background_audio_path = audio_path
                logger.info(f"Background audio saved: {audio_path}")
            else:
                return jsonify({'error': 'Invalid audio file format'}), 400
        
        # Process media files
        file_paths = []
        for file in files:
            if file and allowed_file(file.filename, 'image') or allowed_file(file.filename, 'video'):
                filename = secure_filename(file.filename)
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(file_path)
                file_paths.append(file_path)
            else:
                return jsonify({'error': f'Invalid file format: {file.filename}'}), 400
        
        if not file_paths:
            return jsonify({'error': 'No valid files uploaded'}), 400
        
        # Get duration per item from form data (default to 3 seconds)
        try:
            duration_per_item = float(request.form.get('duration', 3.0))
        except (ValueError, TypeError):
            duration_per_item = 3.0
        
        # Get force GPU option from form data
        force_gpu = request.form.get('force_gpu', 'false').lower() == 'true'
        
        # Generate a unique filename for the output video
        output_filename = f"slideshow_{uuid.uuid4().hex}.mp4"
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        # Create the slideshow
        stats = create_slideshow(
            file_paths, 
            output_path, 
            duration_per_item=duration_per_item, 
            socketio=socketio,
            force_gpu=force_gpu,
            background_audio=background_audio_path
        )
        
        return jsonify({
            'success': True,
            'video_path': output_filename,
            'stats': stats
        })
    
    except Exception as e:
        logger.error(f"Error in upload_files: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download(filename):
    return send_file(os.path.join(app.config['OUTPUT_FOLDER'], filename), as_attachment=True)

@app.route('/upload-to-youtube', methods=['POST'])
def youtube_upload():
    try:
        data = request.json
        logging.info(f"YouTube upload request received: {data}")
        
        if not data or 'video_path' not in data:
            logging.error("No video path provided in YouTube upload request")
            return jsonify({'error': 'No video path provided'}), 400
        
        video_path = os.path.join(app.config['OUTPUT_FOLDER'], data['video_path'])
        if not os.path.exists(video_path):
            logging.error(f"Video file not found: {video_path}")
            return jsonify({'error': f'Video file not found: {data["video_path"]}'}), 404
        
        title = data.get('title', f'My Memories - {os.path.basename(video_path)}')
        description = data.get('description', 'Slideshow created with Memento')
        privacy = data.get('privacy', 'private')
        timestamps = data.get('timestamps', [])
        
        # Format timestamps for YouTube's clickable timestamp format
        if timestamps:
            # YouTube requires timestamps in the format 0:00 to be clickable
            # We'll add a special section for clickable timestamps at the top
            clickable_timestamps = "\n\n🔖 Clickable Timestamps:\n"
            for ts in timestamps:
                minutes = int(ts['time'] // 60)
                seconds = int(ts['time'] % 60)
                time_str = f"{minutes}:{seconds:02d}"
                name = ts['name']
                icon = "🎬" if ts.get('type') == 'video' else "🖼️"
                
                # Add clickable timestamp (YouTube will automatically make these clickable)
                clickable_timestamps += f"{icon} {time_str} - {name}\n"
            
            # Add the clickable timestamps at the beginning of the description for better visibility
            description = description.split("\n\n⏱️ Detailed Timestamps:")[0] + clickable_timestamps
            
            # If the original description didn't have timestamps, append them
            if "⏱️ Detailed Timestamps:" not in description:
                description += clickable_timestamps
        
        logging.info(f"Uploading video to YouTube: {title}")
        
        # Use the ytconnecter functions
        youtube = get_authenticated_service()
        if not youtube:
            return jsonify({'error': 'Failed to authenticate with YouTube. Please check your credentials.'}), 500
        
        options = {
            'file': video_path,
            'title': title,
            'description': description,
            'keywords': 'memories,slideshow,memento',
            'category': '22',  # People & Blogs
            'privacy_status': privacy
        }
        
        video_id = upload_video(youtube, options)
        
        if video_id:
            youtube_url = f"https://www.youtube.com/watch?v={video_id}"
            logging.info(f"YouTube upload successful: {youtube_url}")
            
            return jsonify({
                'success': True,
                'video_id': video_id,
                'youtube_url': youtube_url
            })
        else:
            logging.error("YouTube upload failed: No video ID returned")
            return jsonify({'error': 'YouTube upload failed. Please try again.'}), 500
            
    except Exception as e:
        logging.error(f"Error in youtube_upload: {str(e)}")
        return jsonify({'error': str(e)}), 500

@socketio.on('connect')
def handle_connect():
    logging.info("Client connected")

@socketio.on('disconnect')
def handle_disconnect():
    logging.info("Client disconnected")

if __name__ == '__main__':
    socketio.run(app, debug=True)
