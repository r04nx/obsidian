#!/usr/bin/env python3

"""
Video Steganography Module

This module provides functionality for hiding and extracting images within video files
using frame-based steganography techniques.
"""

import cv2
import numpy as np
from typing import Tuple, Optional, Dict
import os

class VideoSteganographyError(Exception):
    """Custom exception for video steganography-related errors."""
    pass

def validate_dimensions(
    video_frame: np.ndarray,
    hidden_image: np.ndarray
) -> None:
    """
    Validate that the hidden image can fit within the video frame.

    Args:
        video_frame (np.ndarray): A video frame
        hidden_image (np.ndarray): Image to be hidden

    Raises:
        VideoSteganographyError: If dimensions are incompatible
    """
    if (hidden_image.shape[0] > video_frame.shape[0] or
        hidden_image.shape[1] > video_frame.shape[1]):
        raise VideoSteganographyError(
            "Hidden image dimensions exceed video frame dimensions"
        )

def encode_image_into_video(
    video_path: str,
    image_path: str,
    output_path: str,
    start_frame: int = 0
) -> Tuple[bool, str]:
    """
    Hide an image within a video file.

    Args:
        video_path (str): Path to the carrier video
        image_path (str): Path to the image to hide
        output_path (str): Path to save the output video
        start_frame (int): Frame number to start hiding the image (default: 0)

    Returns:
        Tuple[bool, str]: (Success status, Message)

    Raises:
        VideoSteganographyError: If encoding fails
    """
    try:
        # Open video and image
        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            raise VideoSteganographyError("Could not open video file")

        hidden_image = cv2.imread(image_path)
        if hidden_image is None:
            raise VideoSteganographyError("Could not open image file")

        # Get video properties
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        if start_frame >= total_frames:
            raise VideoSteganographyError("Start frame exceeds video length")

        # Create video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        # Write frames
        frame_number = 0
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            if frame_number == start_frame:
                # Validate dimensions
                validate_dimensions(frame, hidden_image)
                
                # Convert image to binary (LSB encoding)
                for i in range(hidden_image.shape[0]):
                    for j in range(hidden_image.shape[1]):
                        for c in range(3):  # RGB channels
                            # Clear LSB of frame and set it to MSB of hidden image
                            frame[i, j, c] = (frame[i, j, c] & 0xFE) | (
                                (hidden_image[i, j, c] & 0x80) >> 7
                            )

            out.write(frame)
            frame_number += 1

        # Clean up
        video.release()
        out.release()

        return True, f"Image successfully hidden in video at frame {start_frame}"

    except Exception as e:
        raise VideoSteganographyError(f"Encoding failed: {str(e)}")
    finally:
        if 'video' in locals():
            video.release()
        if 'out' in locals():
            out.release()

def decode_image_from_video(
    video_path: str,
    output_path: str,
    target_frame: int = 0,
    hidden_dimensions: Tuple[int, int] = None
) -> Tuple[bool, str]:
    """
    Extract a hidden image from a video file.

    Args:
        video_path (str): Path to the video containing hidden image
        output_path (str): Path to save the extracted image
        target_frame (int): Frame number containing the hidden image
        hidden_dimensions (Tuple[int, int]): Dimensions of hidden image (height, width)

    Returns:
        Tuple[bool, str]: (Success status, Message)

    Raises:
        VideoSteganographyError: If decoding fails
    """
    try:
        # Open video
        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            raise VideoSteganographyError("Could not open video file")

        # Get video properties
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

        if target_frame >= total_frames:
            raise VideoSteganographyError("Target frame exceeds video length")

        # Use provided dimensions or default to video frame size
        h_height = hidden_dimensions[0] if hidden_dimensions else height
        h_width = hidden_dimensions[1] if hidden_dimensions else width

        # Create output image
        extracted_image = np.zeros((h_height, h_width, 3), dtype=np.uint8)

        # Seek to target frame
        video.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        ret, frame = video.read()
        
        if not ret:
            raise VideoSteganographyError("Could not read target frame")

        # Extract hidden image
        for i in range(h_height):
            for j in range(h_width):
                for c in range(3):  # RGB channels
                    # Extract LSB from frame and set it as MSB in hidden image
                    extracted_image[i, j, c] = (frame[i, j, c] & 0x01) << 7

        # Save extracted image
        cv2.imwrite(output_path, extracted_image)

        return True, f"Image successfully extracted from frame {target_frame}"

    except Exception as e:
        raise VideoSteganographyError(f"Decoding failed: {str(e)}")
    finally:
        if 'video' in locals():
            video.release()

def main():
    """Example usage of video steganography functions."""
    try:
        # Example paths
        video_path = "../assets/cover_video.mp4"
        image_path = "../assets/hidden_image.png"
        encoded_video_path = "../assets/encoded_video.mp4"
        extracted_image_path = "../assets/extracted_image.png"

        # Hide image in video
        success, encode_msg = encode_image_into_video(
            video_path,
            image_path,
            encoded_video_path,
            start_frame=0
        )
        print(encode_msg)

        # Extract image from video
        success, decode_msg = decode_image_from_video(
            encoded_video_path,
            extracted_image_path,
            target_frame=0
        )
        print(decode_msg)

        # Verify extraction
        original_image = cv2.imread(image_path)
        extracted_image = cv2.imread(extracted_image_path)
        
        if original_image is not None and extracted_image is not None:
            similarity = np.mean(original_image == extracted_image)
            print(f"Image similarity: {similarity * 100:.2f}%")
        else:
            print("Could not compare images")

    except VideoSteganographyError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()

