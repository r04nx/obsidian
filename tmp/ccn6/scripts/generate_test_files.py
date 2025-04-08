#!/usr/bin/env python3

"""
Test File Generator

Creates sample files for steganography demonstrations:
- cover_image.png: A gradient image
- hidden_image.png: A pattern image
- cover_video.mp4: A video with moving shapes
- secret_message.txt: A sample text file
"""

import numpy as np
from PIL import Image, ImageDraw
import cv2
import os

def create_gradient_image(width=800, height=600):
    """Create a gradient image for cover_image.png"""
    # Create gradient arrays
    x = np.linspace(0, 1, width)
    y = np.linspace(0, 1, height)
    X, Y = np.meshgrid(x, y)
    
    # Create RGB channels
    r = (X * 255).astype(np.uint8)
    g = (Y * 255).astype(np.uint8)
    b = ((X + Y) / 2 * 255).astype(np.uint8)
    
    # Combine channels
    img = np.dstack((r, g, b))
    return Image.fromarray(img)

def create_pattern_image(width=400, height=300):
    """Create a pattern image for hidden_image.png"""
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    # Draw some shapes
    draw.rectangle([50, 50, width-50, height-50], outline='red', width=2)
    draw.ellipse([100, 100, width-100, height-100], outline='blue', width=2)
    draw.polygon([(width//2, 50), (width-50, height-50), (50, height-50)], 
                outline='green', width=2)
    
    return img

def create_test_video(output_path, width=800, height=600, duration=5, fps=30):
    """Create a test video with moving shapes"""
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    try:
        for t in range(duration * fps):
            # Create frame
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Draw moving circle
            center = (
                int(width/2 + np.cos(t/fps * 2*np.pi) * 200),
                int(height/2 + np.sin(t/fps * 2*np.pi) * 200)
            )
            cv2.circle(frame, center, 50, (0, 255, 0), -1)
            
            # Draw moving rectangle
            rect_x = int(width/2 + np.cos(t/fps * 2*np.pi + np.pi) * 200)
            rect_y = int(height/2 + np.sin(t/fps * 2*np.pi + np.pi) * 200)
            cv2.rectangle(frame, 
                         (rect_x-40, rect_y-40),
                         (rect_x+40, rect_y+40),
                         (0, 0, 255), -1)
            
            out.write(frame)
            
    finally:
        out.release()

def create_secret_message(output_path):
    """Create a sample secret message file"""
    message = """This is a secret message for testing steganography.
It contains multiple lines of text
and some special characters: !@#$%^&*()
The message will be hidden within the cover image."""
    
    with open(output_path, 'w') as f:
        f.write(message)

def main():
    """Generate all test files"""
    # Create assets directory if it doesn't exist
    assets_dir = "../assets"
    os.makedirs(assets_dir, exist_ok=True)
    
    # Generate cover image
    cover_image = create_gradient_image()
    cover_image.save(os.path.join(assets_dir, "cover_image.png"))
    print("Created cover_image.png")
    
    # Generate hidden image
    hidden_image = create_pattern_image()
    hidden_image.save(os.path.join(assets_dir, "hidden_image.png"))
    print("Created hidden_image.png")
    
    # Generate test video
    create_test_video(os.path.join(assets_dir, "cover_video.mp4"))
    print("Created cover_video.mp4")
    
    # Create secret message file
    create_secret_message(os.path.join(assets_dir, "secret_message.txt"))
    print("Created secret_message.txt")

if __name__ == "__main__":
    main()

