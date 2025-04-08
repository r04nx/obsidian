#!/usr/bin/env python3

"""
Image Steganography Module

This module provides functionality for hiding and extracting text messages within images
using LSB (Least Significant Bit) steganography technique.
"""

from PIL import Image
import numpy as np
from typing import Tuple, Optional
import os

class SteganographyError(Exception):
    """Custom exception for steganography-related errors."""
    pass

def text_to_binary(text: str) -> str:
    """Convert text to binary string."""
    return ''.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary: str) -> str:
    """Convert binary string to text."""
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))

def encode_message(
    image_path: str,
    message: str,
    output_path: str
) -> Tuple[bool, str]:
    """
    Hide a text message within an image using LSB steganography.

    Args:
        image_path (str): Path to the carrier image
        message (str): Text message to hide
        output_path (str): Path to save the output image

    Returns:
        Tuple[bool, str]: (Success status, Message)

    Raises:
        SteganographyError: If the message is too large or image processing fails
    """
    try:
        # Load the image
        img = Image.open(image_path)
        width, height = img.size
        max_bytes = (width * height * 3) // 8  # Each pixel can store 3 bits

        # Convert image to numpy array for easier manipulation
        img_array = np.array(img)

        # Prepare the message (add terminator)
        message += "§END§"
        binary_message = text_to_binary(message)
        
        if len(binary_message) > max_bytes * 8:
            raise SteganographyError(
                f"Message too large. Max size: {max_bytes} bytes"
            )

        # Flatten the image array
        flat_array = img_array.flatten()

        # Embed message bits
        for i, bit in enumerate(binary_message):
            # Clear the LSB and set it to the message bit
            flat_array[i] = (flat_array[i] & ~1) | int(bit)

        # Reshape array back to image dimensions
        modified_array = flat_array.reshape(img_array.shape)

        # Convert back to image and save
        output_img = Image.fromarray(modified_array)
        output_img.save(output_path)

        return True, f"Message successfully hidden in {output_path}"

    except Exception as e:
        raise SteganographyError(f"Encoding failed: {str(e)}")

def decode_message(image_path: str) -> Tuple[bool, str]:
    """
    Extract a hidden message from an image.

    Args:
        image_path (str): Path to the image containing hidden message

    Returns:
        Tuple[bool, str]: (Success status, Extracted message or error message)

    Raises:
        SteganographyError: If decoding fails or no valid message is found
    """
    try:
        # Load the image
        img = Image.open(image_path)
        img_array = np.array(img)

        # Extract LSBs
        binary_message = ''
        flat_array = img_array.flatten()

        # Extract bits until we find the terminator
        for i in range(len(flat_array)):
            binary_message += str(flat_array[i] & 1)
            
            # Check for terminator every 8 bits
            if len(binary_message) % 8 == 0:
                message = binary_to_text(binary_message)
                if "§END§" in message:
                    return True, message.replace("§END§", "")

        raise SteganographyError("No valid message found in image")

    except Exception as e:
        raise SteganographyError(f"Decoding failed: {str(e)}")

def main():
    """Example usage of the steganography functions."""
    try:
        # Example paths
        original_image = "../assets/cover_image.png"
        output_image = "../assets/encoded_image.png"
        
        # Example message
        secret_message = "Hello, this is a hidden message!"

        # Encode the message
        success, encode_msg = encode_message(
            original_image,
            secret_message,
            output_image
        )
        print(encode_msg)

        # Decode the message
        success, decoded_message = decode_message(output_image)
        print(f"Decoded message: {decoded_message}")

        # Verify the messages match
        assert secret_message == decoded_message, "Message mismatch!"
        print("Success: Original and decoded messages match!")

    except SteganographyError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()

