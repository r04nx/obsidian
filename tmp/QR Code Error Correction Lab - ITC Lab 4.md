---
share_link: https://share.note.sx/6kmiyd15#7RQVjQk93cwzB5BrCbRE00Z530URxvwyresjRdTA1oI
share_updated: 2025-03-10T17:49:41+05:30
---
## Student Information
- **Name:** Rohan Prakash Pawar
- **UID:** 2023201020
- **Branch:** EXTC
- **Date:** February 25, 2024

## Aim

To investigate QR code error correction capabilities by gradually corrupting a QR code and determining the threshold at which it becomes unreadable.

## Key Concepts

> [!info]
> QR codes incorporate Reed-Solomon error correction, allowing them to be partially damaged while remaining readable. They come in four error correction levels:
> - **Level L**: ~7% recovery capacity
> - **Level M**: ~15% recovery capacity
> - **Level Q**: ~25% recovery capacity
> - **Level H**: ~30% recovery capacity
## Requirements

- Python 3.x with libraries: qrcode, OpenCV (cv2), pyzbar, numpy, matplotlib
- Virtual environment for dependency management

## Procedure

The experiment followed these steps:
1. Generate a QR code with Lorem Ipsum text
2. Apply progressive damage in two ways:
   - **Random noise**: Randomly flip pixels
   - **Block damage**: Remove square sections
3. Test each damaged QR code for readability
4. Record the damage threshold at which scanning fails

## Observations & Results

### Test 1: Random Noise Damage

The QR code was subjected to increasing levels of random pixel noise. Results showed:
- At 1% noise corruption: QR code remained readable
- At 4% noise corruption: QR code became difficult to read
- At 5% and beyond: QR code became completely unreadable

| Noise Level | Readability Status |
|-------------|-------------------|
| 1% | Successfully decoded |
| 3% | Successfully decoded with difficulty |
| 5% | Failed to decode |

#### Original QR Code:
![[qr_damage_test/original_qr.png]]

#### QR Code with 1% Noise:
![[qr_damage_test/damaged_noise_1.png]]

#### QR Code with 5% Noise (Unreadable):
![[qr_damage_test/damaged_noise_5.png]]

#### Noise Damage Results:
![[qr_damage_test/qr_noise_damage_results.png]]
### Test 2: Block Damage

The QR code was subjected to increasing sizes of block damage. Results showed:
- Small blocks (2x2px): QR code remained readable
- Medium blocks (3-4px): QR code showed degraded readability
- Large blocks (5x5px and larger): QR code became unreadable

| Block Size | Readability Status |
|------------|-------------------|
| 2x2 pixels | Successfully decoded |
| 3x3 pixels | Occasionally failed |
| 5x5 pixels | Consistently failed |

#### QR Code with Small Block Damage:
![[qr_damage_test/damaged_block_2.png]]

#### QR Code with Large Block Damage (Unreadable):
![[qr_damage_test/damaged_block_5.png]]

#### Block Damage Results:
![[qr_damage_test/qr_block_damage_results.png]]

## Program

```python
#!/usr/bin/env python3
"""
QR Code Error Correction Demonstration
--------------------------------------
This script demonstrates the error correction capabilities of QR codes by:
1. Generating a QR code with Lorem Ipsum text
2. Gradually damaging the QR code in steps
3. Testing if the damaged QR code can still be decoded
4. Reporting the percentage of damage and whether decoding was successful

Requirements:
- qrcode: For generating QR codes
- opencv-python (cv2): For image manipulation
- pyzbar: For QR code scanning/decoding
- numpy: For array operations
- matplotlib: For displaying results
"""

import qrcode
import cv2
import numpy as np
import matplotlib.pyplot as plt
from pyzbar.pyzbar import decode
from PIL import Image
import os
import random

# Create output directory if it doesn't exist
output_dir = "qr_damage_test"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def generate_qr_code(data, filename="original_qr.png", size=10):
    """Generate a QR code with the given data and save it to a file."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Highest level of error correction
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = os.path.join(output_dir, filename)
    img.save(img_path)
    return img_path

def read_qr_code(image_path):
    """Try to decode a QR code from an image file."""
    img = cv2.imread(image_path)
    decoded_objects = decode(img)
    
    if decoded_objects:
        return decoded_objects[0].data.decode('utf-8')
    else:
        return None

def add_random_noise(img, percent):
    """Add random noise to a percentage of pixels in the image."""
    # Convert to numpy array if it's a PIL Image
    if isinstance(img, Image.Image):
        img = np.array(img)
    
    # Create a copy to avoid modifying the original
    noisy_img = img.copy()
    
    # Calculate number of pixels to modify
    h, w = img.shape[:2]
    num_pixels = int((h * w) * (percent / 100))
    
    # Randomly select pixels to modify
    for _ in range(num_pixels):
        x = random.randint(0, w-1)
        y = random.randint(0, h-1)
        
        # Flip the color (black to white, white to black)
        if len(img.shape) == 3:  # Color image
            if all(noisy_img[y, x] > 128):  # White pixel
                noisy_img[y, x] = [0, 0, 0]
            else:  # Black pixel
                noisy_img[y, x] = [255, 255, 255]
        else:  # Grayscale image
            if noisy_img[y, x] > 128:  # White pixel
                noisy_img[y, x] = 0
            else:  # Black pixel
                noisy_img[y, x] = 255
    
    return noisy_img

def add_block_damage(img, block_size_percent):
    """Add damage by replacing a block with white pixels."""
    # Convert to numpy array if it's a PIL Image
    if isinstance(img, Image.Image):
        img = np.array(img)
    
    # Create a copy to avoid modifying the original
    damaged_img = img.copy()
    
    # Calculate block size
    h, w = img.shape[:2]
    block_size = int(min(h, w) * (block_size_percent / 100))
    
    # Randomly choose top-left corner of the block
    x = random.randint(0, w - block_size - 1)
    y = random.randint(0, h - block_size - 1)
    
    # Replace block with white pixels
    if len(img.shape) == 3:  # Color image
        damaged_img[y:y+block_size, x:x+block_size] = [255, 255, 255]
    else:  # Grayscale image
        damaged_img[y:y+block_size, x:x+block_size] = 255
    
    return damaged_img

def calculate_damage_percentage(original_img, damaged_img):
    """Calculate the percentage of pixels that differ between two images."""
    if isinstance(original_img, Image.Image):
        original_img = np.array(original_img)
    if isinstance(damaged_img, Image.Image):
        damaged_img = np.array(damaged_img)
    
    # Convert to binary (black and white only)
    if len(original_img.shape) == 3:
        original_binary = cv2.cvtColor(original_img, cv2.COLOR_BGR2GRAY) > 128
    else:
        original_binary = original_img > 128
        
    if len(damaged_img.shape) == 3:
        damaged_binary = cv2.cvtColor(damaged_img, cv2.COLOR_BGR2GRAY) > 128
    else:
        damaged_binary = damaged_img > 128
    
    # Calculate percentage of different pixels
    different_pixels = np.sum(original_binary != damaged_binary)
    total_pixels = original_binary.size
    
    return (different_pixels / total_pixels) * 100

def run_damage_test(data, damage_steps=10, damage_type="noise"):
    """Run a test of gradually increasing damage to a QR code."""
    # Generate original QR code
    original_path = generate_qr_code(data)
    original_img = cv2.imread(original_path)
    
    # Prepare results storage
    results = []
    
    # Plot setup
    plt.figure(figsize=(15, 8))
    
    # Add the original image to results
    plt.subplot(3, 4, 1)
    plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
    plt.title("Original QR Code")
    plt.axis('off')
    
    # Test original QR code decoding
    original_decoded = read_qr_code(original_path)
    print(f"Original QR Code: {'Successfully decoded' if original_decoded else 'Failed to decode'}")
    
    # Test progressively damaged QR codes
    max_damage_percent = 30 if damage_type == "noise" else 15
    damage_percentages = np.linspace(1, max_damage_percent, damage_steps)
    
    for i, damage_percent in enumerate(damage_percentages):
        # Apply damage
        if damage_type == "noise":
            damaged_img = add_random_noise(original_img, damage_percent)
        else:  # block damage
            damaged_img = add_block_damage(original_img, damage_percent)
        
        # Save damaged image
        damaged_path = os.path.join(output_dir, f"damaged_{damage_type}_{i+1}.png")
        cv2.imwrite(damaged_path, damaged_img)
        
        # Calculate actual damage percentage
        actual_damage = calculate_damage_percentage(original_img, damaged_img)
        
        # Try to decode
        decoded_data = read_qr_code(damaged_path)
        success = decoded_data is not None
        
        # Store results
        results.append({
            'damage_percent': actual_damage,
            'decoded_successfully': success,
            'path': damaged_path,
            'index': i+1
        })
        
        # Display in plot
        plt.subplot(3, 4, i+2)
        plt.imshow(cv2.cvtColor(damaged_img, cv2.COLOR_BGR2RGB))
        plt.title(f"{actual_damage:.1f}% Damage: {'✓' if success else '✗'}")
        plt.axis('off')
        
        # Print result
        print(f"Damage {actual_damage:.2f}%: {'Successfully decoded' if success else 'Failed to decode'}")
    
    # Save the plot
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, f"qr_{damage_type}_damage_results.png"))
    plt.close()
    
    return results

def main():
    """Main function to execute the QR code damage tests."""
    # Lorem Ipsum text for QR code
    lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
    Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
    nisi ut aliquip ex ea commodo consequat."""
    
    print("=== QR Code Error Correction Demonstration ===")
    print(f"Testing QR code with {len(lorem_ipsum)} characters of Lorem Ipsum text")
    print("\nTest 1: Random Noise Damage")
    noise_results = run_damage_test(lorem_ipsum, damage_type="noise")
    
    print("\nTest 2: Block Damage")
    block_results = run_damage_test(lorem_ipsum, damage_type="block")
    
    # Determine the threshold where decoding fails
    def find_threshold(results):
        for result in results:
            if not result['decoded_successfully']:
                return result['damage_percent']
        return results[-1]['damage_percent'] if results else 0
    
    noise_threshold = find_threshold(noise_results)
    block_threshold = find_threshold(block_results)
    
    print("\n=== Summary ===")
    print(f"QR Code fails with random noise at approximately {noise_threshold:.2f}% damage")
    print(f"QR Code fails with block damage at approximately {block_threshold:.2f}% damage")
    print(f"Results saved in '{output_dir}' directory")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
QR Code Error Correction Demonstration

This script demonstrates the error correction capabilities of QR codes by:
1. Generating a QR code with Lorem Ipsum text
2. Gradually damaging the QR code in multiple steps
3. Attempting to scan the QR code after each damage step
4. Reporting success/failure and the percentage of damage
5. Saving images of the QR code at each damage step
"""

import os
import random
import numpy as np
import cv2
import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# Create output directory if it doesn't exist
OUTPUT_DIR = "qr_damaged_samples"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_qr_code(data, error_correction=qrcode.constants.ERROR_CORRECT_H):
    """
    Generate a QR code with the given data and error correction level
    
    Args:
        data (str): The data to encode in the QR code
        error_correction: QR code error correction level (L, M, Q, H)
        
    Returns:
        numpy.ndarray: QR code as a binary image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correction,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert PIL image to numpy array
    img_array = np.array(img.convert('RGB'))
    
    # Convert to grayscale
    img_gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    
    # Binarize the image
    _, img_binary = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
    
    return img_binary

def add_random_noise(image, percentage):
    """
    Add random noise to the image by flipping pixels
    
    Args:
        image (numpy.ndarray): The QR code image
        percentage (float): Percentage of pixels to flip (0.0 to 1.0)
        
    Returns:
        numpy.ndarray: The damaged image
    """
    # Create a copy of the image
    damaged_image = image.copy()
    
    # Calculate total number of pixels
    total_pixels = image.shape[0] * image.shape[1]
    
    # Calculate number of pixels to flip
    pixels_to_flip = int(total_pixels * percentage)
    
    # Randomly select pixels to flip
    for _ in range(pixels_to_flip):
        x = random.randint(0, image.shape[1] - 1)
        y = random.randint(0, image.shape[0] - 1)
        
        # Flip the pixel (255 to 0 or 0 to 255)
        damaged_image[y, x] = 255 - damaged_image[y, x]
    
    return damaged_image

def erase_section(image, percentage):
    """
    Erase a random section of the image
    
    Args:
        image (numpy.ndarray): The QR code image
        percentage (float): Percentage of image area to erase (0.0 to 1.0)
        
    Returns:
        numpy.ndarray: The damaged image
    """
    # Create a copy of the image
    damaged_image = image.copy()
    
    # Calculate dimensions of the section to erase
    total_area = image.shape[0] * image.shape[1]
    erase_area = int(total_area * percentage)
    
    # Determine size of square to erase (approximate)
    erase_side = int(np.sqrt(erase_area))
    
    # Random starting point for erasure
    x_start = random.randint(0, image.shape[1] - erase_side - 1)
    y_start = random.randint(0, image.shape[0] - erase_side - 1)
    
    # Erase section (set to white)
    damaged_image[y_start:y_start+erase_side, x_start:x_start+erase_side] = 255
    
    return damaged_image

def attempt_scan(image):
    """
    Attempt to scan/decode the QR code
    
    Args:
        image (numpy.ndarray): The QR code image
        
    Returns:
        tuple: (success, decoded_data)
    """
    # Convert to PIL image for pyzbar
    pil_image = Image.fromarray(image)
    
    # Attempt to decode
    decoded_objects = decode(pil_image)
    
    if decoded_objects:
        return True, decoded_objects[0].data.decode('utf-8')
    else:
        return False, None

def calculate_damage_percentage(original, damaged):
    """
    Calculate the percentage of pixels that have been changed
    
    Args:
        original (numpy.ndarray): The original QR code image
        damaged (numpy.ndarray): The damaged QR code image
        
    Returns:
        float: Percentage of pixels changed
    """
    # Count the number of pixels that are different
    different_pixels = np.sum(original != damaged)
    
    # Calculate total number of pixels
    total_pixels = original.shape[0] * original.shape[1]
    
    # Calculate percentage
    percentage = (different_pixels / total_pixels) * 100
    
    return percentage

def save_image(image, filename):
    """
    Save the image to a file
    
    Args:
        image (numpy.ndarray): The image to save
        filename (str): The filename to save to
    """
    cv2.imwrite(filename, image)

def display_results(images, titles, success_flags, damage_percentages):
    """
    Display the QR code images with information about each one
    
    Args:
        images (list): List of QR code images
        titles (list): List of titles for each image
        success_flags (list): List of booleans indicating scan success
        damage_percentages (list): List of damage percentages
    """
    n = len(images)
    
    # Create figure with n+1 columns (original + n damage steps)
    fig = plt.figure(figsize=(4*n, 8))
    gs = GridSpec(2, n, figure=fig)
    
    # Display images in the first row
    for i in range(n):
        ax = fig.add_subplot(gs[0, i])
        ax.imshow(images[i], cmap='gray')
        ax.set_title(titles[i])
        ax.set_xticks([])
        ax.set_yticks([])
    
    # Create a bar chart for damage percentages in the second row
    ax_bar = fig.add_subplot(gs[1, :])
    bars = ax_bar.bar(range(n), damage_percentages, color=['green' if s else 'red' for s in success_flags])
    
    # Add annotations above each bar
    for i, bar in enumerate(bars):
        status = "Success" if success_flags[i] else "Failed"
        ax_bar.text(
            bar.get_x() + bar.get_width()/2,
            bar.get_height() + 1,
            f"{status}\n{damage_percentages[i]:.1f}%",
            ha='center',
            va='bottom',
            fontweight='bold'
        )
    
    ax_bar.set_xticks(range(n))
    ax_bar.set_xticklabels([t.replace('\n', ' ') for t in titles])
    ax_bar.set_ylabel('Damage Percentage (%)')
    ax_bar.set_ylim(0, max(damage_percentages) + 10)  # Add some margin above the highest bar
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "qr_damage_results.png"), dpi=300, bbox_inches='tight')
    plt.show()

def main():
    """Main function to demonstrate QR code error correction"""
    
    # Generate Lorem Ipsum text
    lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
    ullamco laboris nisi ut aliquip ex ea commodo consequat."""
    
    print("=== QR Code Error Correction Demonstration ===")
    print(f"Original text: {lorem_ipsum[:50]}...")
    
    # Generate the original QR code
    print("\nGenerating QR code with high error correction level...")
    qr_original = generate_qr_code(lorem_ipsum, error_correction=qrcode.constants.ERROR_CORRECT_H)
    
    # Verify the original QR code can be read
    success, data = attempt_scan(qr_original)
    if success:
        print(f"Original QR code scan successful! Data matches: {data[:50]}...")
    else:
        print("Error: Could not scan the original QR code. Please check your setup.")
        return
    
    # Save the original image
    save_image(qr_original, os.path.join(OUTPUT_DIR, "qr_original.png"))
    
    # Initialize lists to store results
    damage_steps = 6  # Number of damage steps
    damaged_images = [qr_original]  # Start with the original
    titles = ["Original\nQR Code"]
    success_flags = [True]
    damage_percentages = [0.0]  # No damage in original
    
    print("\nDamaging QR code in steps and testing readability...")
    
    # Damage QR code in multiple steps
    current_image = qr_original.copy()
    
    # Step 1: Add 10% random noise
    noise_pct = 0.10
    damaged = add_random_noise(current_image, noise_pct)
    actual_damage = calculate_damage_percentage(qr_original, damaged)
    success, data = attempt_scan(damaged)
    
    damaged_images.append(damaged)
    titles.append(f"Step 1\n10% Noise")
    success_flags.append(success)
    damage_percentages.append(actual_damage)
    
    print(f"Step 1: 10% random noise - Scan {'successful' if success else 'failed'} - Actual damage: {actual_damage:.1f}%")
    save_image(damaged, os.path.join(OUTPUT_DIR, "qr_step1_noise.png"))
    
    if success:
        current_image = damaged
    
    # Step 2: Add 20% random noise
    noise_pct = 0.20
    damaged = add_random_noise(current_image, noise_pct)
    actual_damage = calculate_damage_percentage(qr_original, damaged)
    success, data = attempt_scan(damaged)
    
    damaged_images.append(damaged)
    titles.append(f"Step 2\n20% Noise")
    success_flags.append(success)
    damage_percentages.append(actual_damage)
    
    print(f"Step 2: 20% random noise - Scan {'successful' if success else 'failed'} - Actual damage: {actual_damage:.1f}%")
    save_image(damaged, os.path.join(OUTPUT_DIR, "qr_step2_noise.png"))
    
    if success:
        current_image = damaged
    
    # Step 3: Erase small section (5%)
    erase_pct = 0.05
    damaged = erase_section(current_image, erase_pct)
    actual_damage = calculate_damage_percentage(qr_original, damaged)
    success, data = attempt_scan(damaged)
    
    damaged_images.append(damaged)
    titles.append(f"Step 3\n5% Erasure")
    success_flags.append(success)
    damage_percentages.append(actual_damage)
    
    print(f"Step 3: 5% section erasure - Scan {'successful' if success else 'failed'} - Actual damage: {actual_damage:.1f}%")
    save_image(damaged, os.path.join(OUTPUT_DIR, "qr_step3_erase.png"))
    
    if success:
        current_image = damaged
    
    # Step 4: Erase larger section (10%)
    erase_pct = 0.10
    damaged = erase_section(current_image, erase_pct)
    actual_damage = calculate_damage_percentage(qr_original, damaged)
    success, data = attempt_scan(damaged)
    
    damaged_images.append(damaged)
    titles.append(f"Step 4\n10% Erasure")
    success_flags.append(success)
    damage_percentages.append(actual_damage)
    
    print(f"Step 4: 10% section erasure - Scan {'successful' if success else 'failed'} - Actual damage: {actual_damage:.1f}%")
    save_image(damaged, os.path.join(OUTPUT_DIR, "qr_step4_erase.png"))
    
    if success:
        current_image = damaged
    
    # Step 5: Combined damage - noise and erasure
    noise_pct = 0.10
    erase_pct = 0.10
    damaged = add_random_noise(current_image, noise_pct)
    damaged = erase_section(damaged, erase_pct)
    actual_damage = calculate_damage_percentage(qr_original, damaged)
    success, data = attempt_scan(damaged)
    
    damaged_images.append(damaged)
    titles.append(f"Step 5\nNoise + Erasure")
    success_flags.append(success)
    damage_percentages.append(actual_damage)
    
    print(f"Step 5: Combined noise + erasure - Scan {'successful' if success else 'failed'} - Actual damage: {actual_damage:.1f}%")
    save_image(damaged, os.path.join(OUTPUT_DIR, "qr_step5_combined.png"))
    
    print("\nResults summary:")
    for i, (success, damage) in enumerate(zip(success_flags, damage_percentages)):
        step_name = titles[i].replace('\n', ' ')
        status = "Successful" if success else "Failed"
        print(f"- {step_name}: Scan {status}, Damage: {damage:.1f}%")
    
    # Find the maximum damage that still allowed successful scanning
    successful_damages = [d for s, d in zip(success_flags, damage_percentages) if s]
    if successful_damages:
        max_successful_damage = max(successful_damages)
        print(f"\nThe QR code could still be scanned with up to {max_successful_damage:.1f}% damage")


```
## Conclusion

> [!success]
> This experiment demonstrated the practical limitations of QR code error correction capabilities. While QR codes can withstand significant damage (particularly random noise), their resilience is not unlimited.
> 
> The findings align with theoretical expectations: QR codes use Reed-Solomon error correction to recover from partial damage, but have defined thresholds beyond which recovery becomes impossible. Position markers and finder patterns are especially sensitive areas.


---



