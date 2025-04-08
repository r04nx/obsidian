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

def save_image_with_format(response, output_path):
    """Save image with proper format conversion."""
    img = Image.open(BytesIO(response.content))
    
    # Convert to RGB if needed
    if img.mode in ('RGBA', 'LA'):
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[-1])
        img = background
    elif img.mode != 'RGB':
        img = img.convert('RGB')
    
    img.save(output_path, 'PNG', quality=95)
    return img.size

def download_file(url: str, output_path: str, description: str, max_size_mb: int = 10) -> None:
    """
    Download a file with progress bar and size checks.
    
    Args:
        url: URL to download from
        output_path: Path to save the file
        description: Description for the progress bar
        max_size_mb: Maximum file size in MB
    """
    try:
        print(f"\nDownloading {description}...")
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Get content length
        total_size = int(response.headers.get('content-length', 0))
        
        if total_size > max_size_mb * 1024 * 1024:
            raise DownloadError(f"File too large: {total_size / (1024*1024):.1f}MB")
        
        # For images, save with format conversion
        if output_path.endswith(('.png', '.jpg', '.jpeg')):
            width, height = save_image_with_format(response, output_path)
            print(f"Saved image with dimensions: {width}x{height}")
        else:
            # For non-image files, save with progress bar
            with open(output_path, 'wb') as f, tqdm(
                total=total_size,
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
        print(f"\nCreated {os.path.basename(output_path)}")
    except Exception as e:
        raise DownloadError(f"Failed to create message file: {str(e)}")

def main():
    """Download all required resources."""
    # Create assets directory if it doesn't exist
    assets_dir = os.path.join(os.path.dirname(__file__), "..", "assets")
    os.makedirs(assets_dir, exist_ok=True)
    
    try:
        print("Starting downloads...")
        
        # Download cover image (nature scene)
        download_file(
            "https://picsum.photos/2000/1500",  # Random high-quality image
            os.path.join(assets_dir, "cover_image.png"),
            "cover image",
            max_size_mb=5
        )
        
        # Download hidden image (smaller image)
        download_file(
            "https://picsum.photos/1000/800",  # Random smaller image
            os.path.join(assets_dir, "hidden_image.png"),
            "hidden image",
            max_size_mb=3
        )
        
        # Download sample video (Creative Commons video)
        download_file(
            "https://test-videos.co.uk/vids/bigbuckbunny/mp4/h264/360/Big_Buck_Bunny_360_10s_1MB.mp4",
            os.path.join(assets_dir, "cover_video.mp4"),
            "sample video",
            max_size_mb=2
        )
        
        # Create SPIT message file
        create_spit_message(os.path.join(assets_dir, "secret_message.txt"))
        
        print("\nAll resources downloaded successfully!")
        print("\nFiles are located in the 'assets' directory:")
        for file in os.listdir(assets_dir):
            file_path = os.path.join(assets_dir, file)
            size_mb = os.path.getsize(file_path) / (1024 * 1024)
            print(f"- {file} ({size_mb:.1f} MB)")
            
    except DownloadError as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

        img = Image.open(BytesIO(data))
        width, height = img.size
        
        # Convert RGBA to RGB if needed
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        
        # Check dimensions
        if not (min_size[0] <= width <= max_size[0] and 
                min_size[1] <= height <= max_size[1]):
            print(f"Image dimensions ({width}x{height}) outside allowed range "
                  f"({min_size[0]}x{min_size[1]} to {max_size[0]}x{max_size[1]})")
            return False
            
        return True
    except Exception as e:
        print(f"Error verifying image: {str(e)}")
        return False
        # For images, verify dimensions before saving
        if image_size_range:
            if not verify_image(
                response.content,
                image_size_range[0],
                image_size_range[1]
            ):
                raise DownloadError("Image dimensions out of acceptable range or format error")
    # Define image size constraints (more flexible)
    COVER_IMAGE_SIZE = ((800, 600), (4096, 2160))  # Minimum 800x600, up to 4K
    HIDDEN_IMAGE_SIZE = ((400, 300), (1920, 1080))  # Smaller range
    
    try:
        print("Starting downloads...")
        
        # Download cover image (landscape nature scene)
        # Using Unsplash source with size parameters
        download_file(
            "https://images.unsplash.com/photo-1506744038136-46273834b3fb?"
            "auto=format&fit=crop&w=2000&q=80",
            os.path.join(assets_dir, "cover_image.png"),
            "Downloading cover image",
            max_size_mb=5,
            image_size_range=COVER_IMAGE_SIZE
        )
        
        # Download hidden image (city scene)
        # Using Unsplash source with size parameters
        download_file(
            "https://images.unsplash.com/photo-1449824913935-59a10b8d2000?"
            "auto=format&fit=crop&w=1000&q=80",
            os.path.join(assets_dir, "hidden_image.png"),
            "Downloading hidden image",
            max_size_mb=3,
            image_size_range=HIDDEN_IMAGE_SIZE
        )
        
        # Download sample video (small test video)
        download_file(
            "https://filesamples.com/samples/video/mp4/sample_640x360.mp4",
