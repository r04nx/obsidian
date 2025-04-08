# Steganography Lab Report
*Computer and Communication Networks Laboratory*
*Date: April 8, 2025*

## Overview
This laboratory experiment focuses on implementing and understanding steganography techniques using both professional tools (OpenPuff) and custom Python implementations. The lab demonstrates various methods of hiding information within digital media files.

## Aim
1. To provide confidentiality using OpenPuff: a professional steganography tool
2. To implement and understand image-in-image steganography using Python
3. To implement and understand image-in-video steganography using Python

## Software Requirements
### Operating System
- Ubuntu Linux (or any modern operating system)

### Required Software
- Python 3.12.7
- OpenPuff (for Part A)

### Python Libraries
- Pillow (PIL) - for image processing
- OpenCV (opencv-python) - for video processing
- NumPy - for numerical operations

## Theory and Introduction
Steganography is the practice of concealing information within other non-secret data or carrier files in a way that does not draw attention to the hidden information's existence. Unlike cryptography, which makes data unreadable, steganography aims to hide the very presence of the secret data.

### Key Concepts
- **Carrier File**: The file that will hold the hidden information (e.g., image, video)
- **Payload**: The secret information to be hidden
- **Embedding**: The process of hiding information in the carrier file
- **Extraction**: The process of retrieving hidden information from the carrier file

### Types of Steganography Covered
1. **Image Steganography**: Hiding information within image files
   - LSB (Least Significant Bit) modification
   - Pixel value manipulation

2. **Video Steganography**: Concealing images within video frames
   - Frame manipulation
   - Temporal steganography

## Lab Structure

### Part A: OpenPuff Steganography
- Professional steganography tool implementation
- Step-by-step demonstration of hiding and extracting information
- Analysis of supported file types and capabilities

### Part B: Python Implementation
#### Section 1: Image-in-Image Steganography
- Custom implementation using Python
- Encoding and decoding functions
- Practical demonstration and results analysis

#### Section 2: Image-in-Video Steganography
- Advanced implementation for hiding images in video
- Frame-based steganography techniques
- Performance and quality analysis

---

# Part A: OpenPuff Steganography Implementation
*(Content to be added based on OpenPuff experimentation)*

# Part B: Python Steganography Implementation

## Section 1: Image-in-Image Steganography

### Implementation Overview
The image steganography implementation uses the Least Significant Bit (LSB) technique to hide text messages within image files. This method modifies the least significant bits of the image pixels to store the hidden message while maintaining visual integrity of the carrier image.

### Technical Details
- **Encoding Process**: Each character of the message is converted to its 8-bit binary representation and embedded in the LSB of pixel values.
- **Message Termination**: A special terminator sequence ("§END§") is used to mark the end of the hidden message.
- **Bit Manipulation**: The implementation uses bitwise operations to modify pixel values without visibly affecting the image.

### Code Implementation

#### 1. Message Encoding
```python
def encode_message(
    image_path: str,
    message: str,
    output_path: str
) -> Tuple[bool, str]:
    """Hide a text message within an image using LSB steganography."""
    try:
        # Load the image
        img = Image.open(image_path)
        width, height = img.size
        max_bytes = (width * height * 3) // 8

        # Convert image to numpy array
        img_array = np.array(img)

        # Prepare message with terminator
        message += "§END§"
        binary_message = text_to_binary(message)
        
        if len(binary_message) > max_bytes * 8:
            raise SteganographyError(
                f"Message too large. Max size: {max_bytes} bytes"
            )

        # Embed message bits in LSB
        flat_array = img_array.flatten()
        for i, bit in enumerate(binary_message):
            flat_array[i] = (flat_array[i] & ~1) | int(bit)

        # Save modified image
        modified_array = flat_array.reshape(img_array.shape)
        output_img = Image.fromarray(modified_array)
        output_img.save(output_path)

        return True, f"Message successfully hidden in {output_path}"
```

#### 2. Message Extraction
```python
def decode_message(image_path: str) -> Tuple[bool, str]:
    """Extract a hidden message from an image."""
    try:
        img = Image.open(image_path)
        img_array = np.array(img)
        flat_array = img_array.flatten()

        binary_message = ''
        for i in range(len(flat_array)):
            binary_message += str(flat_array[i] & 1)
            
            if len(binary_message) % 8 == 0:
                message = binary_to_text(binary_message)
                if "§END§" in message:
                    return True, message.replace("§END§", "")

        raise SteganographyError("No valid message found in image")
```

### Usage Instructions
1. Place the carrier image in the `assets` directory
2. Run the script with appropriate parameters:
```python
# Encoding example
encode_message(
    "assets/cover_image.png",
    "Secret message to hide",
    "assets/encoded_image.png"
)

# Decoding example
success, message = decode_message("assets/encoded_image.png")
print(f"Decoded message: {message}")
```

## Section 2: Image-in-Video Steganography

### Implementation Overview
The video steganography implementation embeds an entire image within video frames using a modified LSB technique. This method allows for hiding high-capacity payloads (images) within video carriers while maintaining video quality.

### Technical Details
- **Frame Selection**: The implementation can target specific frames for embedding the hidden image.
- **Bit-plane Manipulation**: Uses the Most Significant Bit (MSB) of the hidden image and embeds it in the LSB of the video frame.
- **Dimension Validation**: Ensures the hidden image dimensions are compatible with video frame size.

### Code Implementation

#### 1. Image Encoding in Video
```python
def encode_image_into_video(
    video_path: str,
    image_path: str,
    output_path: str,
    start_frame: int = 0
) -> Tuple[bool, str]:
    """Hide an image within a video file."""
    try:
        # Open video and image
        video = cv2.VideoCapture(video_path)
        hidden_image = cv2.imread(image_path)

        # Get video properties
        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(video.get(cv2.CAP_PROP_FPS))

        # Create output video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        frame_number = 0
        while video.isOpened():
            ret, frame = video.read()
            if not ret:
                break

            if frame_number == start_frame:
                # Embed image in frame
                for i in range(hidden_image.shape[0]):
                    for j in range(hidden_image.shape[1]):
                        for c in range(3):
                            frame[i, j, c] = (frame[i, j, c] & 0xFE) | (
                                (hidden_image[i, j, c] & 0x80) >> 7
                            )

            out.write(frame)
            frame_number += 1

        return True, f"Image hidden in frame {start_frame}"
```

#### 2. Image Extraction from Video
```python
def decode_image_from_video(
    video_path: str,
    output_path: str,
    target_frame: int = 0,
    hidden_dimensions: Tuple[int, int] = None
) -> Tuple[bool, str]:
    """Extract a hidden image from a video file."""
    try:
        video = cv2.VideoCapture(video_path)
        
        # Seek to target frame
        video.set(cv2.CAP_PROP_POS_FRAMES, target_frame)
        ret, frame = video.read()

        h_height = hidden_dimensions[0] if hidden_dimensions else frame.shape[0]
        h_width = hidden_dimensions[1] if hidden_dimensions else frame.shape[1]

        # Extract hidden image
        extracted_image = np.zeros((h_height, h_width, 3), dtype=np.uint8)
        for i in range(h_height):
            for j in range(h_width):
                for c in range(3):
                    extracted_image[i, j, c] = (frame[i, j, c] & 0x01) << 7

        cv2.imwrite(output_path, extracted_image)
        return True, f"Image extracted from frame {target_frame}"
```

### Usage Instructions
1. Prepare the video and image files:
   - Place the carrier video in the `assets` directory as `cover_video.mp4`
   - Place the image to hide in the `assets` directory as `hidden_image.png`

2. Run the script with appropriate parameters:
```python
# Encoding example
encode_image_into_video(
    "assets/cover_video.mp4",
    "assets/hidden_image.png",
    "assets/encoded_video.mp4",
    start_frame=0
)

# Decoding example
decode_image_from_video(
    "assets/encoded_video.mp4",
    "assets/extracted_image.png",
    target_frame=0
)
```

### Technical Considerations

#### Image Steganography
- **Capacity**: The maximum message size depends on the carrier image dimensions
- **Quality Impact**: Minimal visual impact due to LSB modification
- **Security**: Basic security through obscurity; can be enhanced with encryption

#### Video Steganography
- **Frame Selection**: Strategic frame selection can improve security
- **Capacity**: Can hide larger payloads (entire images)
- **Quality Considerations**: 
  - Video compression may affect hidden data
  - Frame synchronization is critical for successful extraction

### Limitations and Considerations
1. **Image Steganography**
   - Limited to text messages
   - Message size constrained by image dimensions
   - Vulnerable to image processing operations

2. **Video Steganography**
   - Requires careful handling of video codecs
   - Frame-accurate seeking necessary for extraction
   - Video compression may corrupt hidden data

### Potential Improvements
1. **Security Enhancements**
   - Add encryption layer for message/image
   - Implement random frame selection
   - Use multiple frames for redundancy

2. **Robustness**
   - Error correction codes
   - Compression-resistant encoding
   - Multiple bit-plane utilization
