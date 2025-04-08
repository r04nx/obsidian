#!/usr/bin/env python3

"""
Resource Downloader

Downloads sample media files for steganography demonstrations:
- cover_image.png: A high-resolution nature image
- hidden_image.png: A smaller urban image
- cover_video.mp4: A sample video clip
- secret_message.txt: SPIT-related content
"""

import os
import requests
from tqdm import tqdm
import sys
from PIL import Image
from io import BytesIO

class DownloadError(Exception):
    """Custom exception for download-related errors."""
    pass

def verify_image(data: bytes, min_size: tuple, max_size: tuple) -> bool:
    """
    Verify that an image meets size requirements.
    
    Args:
        data: Image data
        min_size: Minimum (width, height)
        max_size: Maximum (width, height)
    """
    try:
        img = Image.open(BytesIO(data))
        width, height = img.size
        return (width >= min_size[0] and height >= min_size[1] and
                width <= max_size[0] and height <= max_size[1])
    except Exception:
        return False

def download_file(url: str, output_path: str, description: str,
                 max_size_mb: int = 10,
                 image_size_range: tuple = None) -> None:
    """
    Download a file with progress bar and size checks.
    
    Args:
        url: URL to download from
        output_path: Path to save the file
        description: Description for the progress bar
        max_size_mb: Maximum file size in MB
        image_size_range: Tuple of ((min_w, min_h), (max_w, max_h)) for images
    """
    try:
        # First check headers
        response = requests.head(url, allow_redirects=True)
        size = int(response.headers.get('content-length', 0))
        
        if size > max_size_mb * 1024 * 1024:
            raise DownloadError(f"File too large: {size / (1024*1024):.1f}MB")
        
        # Download file
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # For images, verify dimensions before saving
        if image_size_range and not verify_image(
            response.content,
            image_size_range[0],
            image_size_range[1]
        ):
            raise DownloadError("Image dimensions out of acceptable range")
        
        # Save file with progress bar
        with open(output_path, 'wb') as f, tqdm(
            desc=description,
            total=size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for chunk in response.iter_content(chunk_size=8192):
                size = f.write(chunk)
                pbar.update(size)
                
    except Exception as e:
        if os.path.exists(output_path):
            os.remove(output_path)
        raise DownloadError(f"Failed to download {description}: {str(e)}")

def create_spit_message(output_path: str):
    """Create a text file with SPIT-related content."""
    message = """Sardar Patel Institute of Technology (SPIT)

Located in Andheri (West), Mumbai, SPIT is an autonomous engineering college affiliated 
to the University of Mumbai. Established in 1995, SPIT has been consistently ranked 
among the top engineering colleges in Maharashtra.

Key Highlights:
- NBA Accredited Programs
- NAAC 'A' Grade Accreditation
- Advanced Research Facilities
- Industry-Academia Partnerships
- State-of-the-art Infrastructure

This message demonstrates steganography implementation in the Computer and Communication 
Networks Laboratory at SPIT's Computer Engineering Department.

Course: Computer and Communication Networks Laboratory
Semester: 6
Department: Computer Engineering
Academic Year: 2024-25

Experiment: Implementation of Steganography Techniques
- Image Steganography using LSB Technique
- Video Frame Steganography
- Professional Tool (OpenPuff) Implementation"""

    try:
        with open(output_path, 'w') as f:
            f.write(message)
    except Exception as e:
        raise DownloadError(f"Failed to create message file: {str(e)}")

def main():
    """Download all required resources."""
    # Create assets directory if it doesn't exist
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    # Define image size constraints
    COVER_IMAGE_SIZE = ((1920, 1080), (4096, 2160))  # Full HD to 4K
    HIDDEN_IMAGE_SIZE = ((800, 600), (1920, 1080))   # Smaller range
    
    try:
        print("Starting downloads...")
        
        # Download cover image (landscape nature scene)
        download_file(
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb",
            os.path.join(assets_dir, "cover_image.png"),
            "Downloading cover image",
            max_size_mb=5,
            image_size_range=COVER_IMAGE_SIZE
        )
        
        # Download hidden image (city scene)
        download_file(
            "https://images.unsplash.com/photo-1449824913935-59a10b8d2000",
            os.path.join(assets_dir, "hidden_image.png"),
            "Downloading hidden image",
            max_size_mb=3,
            image_size_range=HIDDEN_IMAGE_SIZE
        )
        
        # Download sample video (small test video)
        download_file(
            "https://filesamples.com/samples/video/mp4/sample_640x360.mp4",
            os.path.join(assets_dir, "cover_video.mp4"),
            "Downloading cover video",
            max_size_mb=2
        )
        
        # Create SPIT message file
        create_spit_message(os.path.join(assets_dir, "secret_message.txt"))
        print("Created secret_message.txt with SPIT content")
        
        print("\nAll resources downloaded successfully!")
        print("Files are located in the 'assets' directory:")
        for file in os.listdir(assets_dir):
            print(f"- {file}")
            
    except DownloadError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3

"""
Resource Downloader

Downloads sample media files for steganography demonstrations:
- cover_image.png: A high-resolution nature image from Unsplash
- hidden_image.png: A smaller image from Unsplash
- cover_video.mp4: A sample video clip
- secret_message.txt: SPIT-related content
"""

import os
import requests
from tqdm import tqdm
import sys

# Unsplash API access key (you should replace this with your own)
UNSPLASH_ACCESS_KEY = "your-unsplash-access-key"

class DownloadError(Exception):
    """Custom exception for download-related errors."""
    pass

def download_file(url: str, output_path: str, description: str):
    """
    Download a file with progress bar.
    
    Args:
        url: URL to download from
        output_path: Path to save the file
        description: Description for the progress bar
    """
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        total_size = int(response.headers.get('content-length', 0))
        block_size = 8192
        
        with open(output_path, 'wb') as f, tqdm(
            desc=description,
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as pbar:
            for data in response.iter_content(block_size):
                size = f.write(data)
                pbar.update(size)
                
    except Exception as e:
        raise DownloadError(f"Failed to download {description}: {str(e)}")

def create_spit_message(output_path: str):
    """Create a text file with SPIT-related content."""
    message = """Sardar Patel Institute of Technology (SPIT)

Located in Andheri (West), Mumbai, SPIT is an autonomous engineering college affiliated 
to the University of Mumbai. Established in 1995, SPIT has been consistently ranked 
among the top engineering colleges in Maharashtra.

Key Highlights:
- NBA Accredited Programs
- NAAC 'A' Grade Accreditation
- Advanced Research Facilities
- Industry-Academia Partnerships
- State-of-the-art Infrastructure

This message demonstrates steganography implementation in the Computer and Communication 
Networks Laboratory at SPIT's Computer Engineering Department.

Course: Computer and Communication Networks Laboratory
Semester: 6
Department: Computer Engineering
Academic Year: 2024-25

Experiment: Implementation of Steganography Techniques
- Image Steganography using LSB Technique
- Video Frame Steganography
- Professional Tool (OpenPuff) Implementation"""

    try:
        with open(output_path, 'w') as f:
            f.write(message)
    except Exception as e:
        raise DownloadError(f"Failed to create message file: {str(e)}")

def main():
    """Download all required resources."""
    # Create assets directory if it doesn't exist
    assets_dir = os.path.join(os.path.dirname(__file__), "../assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    try:
        print("Starting downloads...")
        
        # Download cover image (nature scene)
        cover_image_url = "https://images.unsplash.com/photo-1472214103451-9374bd1c798e"
        download_file(
            cover_image_url,
            os.path.join(assets_dir, "cover_image.png"),
            "Downloading cover image"
        )
        
        # Download hidden image (urban scene)
        hidden_image_url = "https://images.unsplash.com/photo-1514565131-fce0801e5785"
        download_file(
            hidden_image_url,
            os.path.join(assets_dir, "hidden_image.png"),
            "Downloading hidden image"
        )
        
        # Download sample video (Creative Commons licensed)
        video_url = "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4"
        download_file(
            video_url,
            os.path.join(assets_dir, "cover_video.mp4"),
            "Downloading cover video"
        )
        
        # Create SPIT message file
        create_spit_message(os.path.join(assets_dir, "secret_message.txt"))
        print("Created secret_message.txt with SPIT content")
        
        print("\nAll resources downloaded successfully!")
        print("Files are located in the 'assets' directory:")
        for file in os.listdir(assets_dir):
            print(f"- {file}")
            
    except DownloadError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

