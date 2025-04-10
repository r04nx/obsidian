#!/usr/bin/env python3

"""
Download sample files for steganography demonstration
- Downloads cover image and hidden image from Unsplash
- Downloads a sample video
- Creates a SPIT-related text message
"""

import os
import requests
from tqdm import tqdm
from PIL import Image
from io import BytesIO

class DownloadError(Exception):
    pass

def download_file(url: str, output_path: str, desc: str, max_size_mb: int = 10) -> None:
    """Download a file with progress bar and size check."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Check content length
        total_size = int(response.headers.get('content-length', 0))
        if total_size > max_size_mb * 1024 * 1024:
            raise DownloadError(f"File size exceeds {max_size_mb}MB limit")

        # Download with progress bar
        with open(output_path, 'wb') as f:
            with tqdm(
                total=total_size,
                unit='iB',
                unit_scale=True,
                desc=desc
            ) as pbar:
                for data in response.iter_content(chunk_size=1024):
                    size = f.write(data)
                    pbar.update(size)
                    
        print(f"Successfully downloaded: {output_path}")
        
    except requests.RequestException as e:
        raise DownloadError(f"Download failed: {str(e)}")

def create_spit_message(output_path: str) -> None:
    """Create a text file with SPIT-related content."""
    message = """Sardar Patel Institute of Technology (SPIT)

Founded in 1995, SPIT is an autonomous engineering college affiliated with the University of Mumbai. 
Located in Andheri (West), Mumbai, the institute is known for its excellence in technical education.

Key Features:
- NBA Accredited Programs
- NAAC 'A' Grade Institution
- Ranked among top engineering colleges in Maharashtra
- Strong focus on research and innovation
- Active placement cell with excellent industry connections

This message will be used for steganography demonstration purposes.
Department of Computer Engineering
Computer and Communication Networks Laboratory
"""
    
    with open(output_path, 'w') as f:
        f.write(message)
    print(f"Created SPIT message file: {output_path}")

def main():
    # Create assets directory if it doesn't exist
    assets_dir = "../assets"
    os.makedirs(assets_dir, exist_ok=True)
    
    try:
        print("Starting downloads...")
        
        # Download cover image (nature scene)
        download_file(
            "https://images.unsplash.com/photo-1470071459604-3b5ec3a7fe05?w=1920&q=80",
            os.path.join(assets_dir, "cover_image.jpg"),
            "Downloading cover image"
        )
        
        # Download hidden image (urban scene)
        download_file(
            "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=1280&q=80",
            os.path.join(assets_dir, "hidden_image.jpg"),
            "Downloading hidden image"
        )
        
        # Download sample video
        download_file(
            "https://raw.githubusercontent.com/intel-iot-devkit/sample-videos/master/car-detection.mp4",
            os.path.join(assets_dir, "cover_video.mp4"),
            "Downloading sample video"
        )
        
        # Create SPIT message
        create_spit_message(os.path.join(assets_dir, "secret_message.txt"))
        
        print("\nAll files downloaded successfully!")
        
    except DownloadError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
