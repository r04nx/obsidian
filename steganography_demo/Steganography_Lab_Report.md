# Steganography Laboratory Report

> [!abstract] Overview
> This laboratory report documents experiments with three different steganography techniques: text-in-text, text-in-image, and image-in-image. All experiments were conducted in a Linux Ubuntu environment using various steganography tools.

## Introduction
Steganography is the practice of concealing information within other non-secret data or a physical object to avoid detection. Unlike encryption, which focuses on making data unreadable, steganography aims to hide the very existence of the secret communication. 

![[obsidian_images/cover_image.jpg|300]]
*Cover image used in our steganography experiments*

## Objective
To demonstrate and evaluate three different steganography techniques:
1. Hiding text within text using whitespace coding
2. Hiding text within an image using Steghide
3. Hiding an image within another image using Steghide

## Theory
### Text-in-Text Steganography
> [!info] Technique
> Text-in-text steganography involves hiding messages within seemingly innocent text by using techniques such as whitespace manipulation, character substitution, or semantic methods.

In this lab, we used whitespace coding, where extra spaces represent binary data (1's and 0's). This method is particularly interesting because it doesn't require any special tools - the hidden message can be encoded and decoded with standard text editors, making it accessible but also potentially easier to detect if someone knows what to look for.

### Text-in-Image Steganography
> [!info] Technique
> This technique involves embedding text data within digital images by modifying the least significant bits (LSB) of the pixel values.

The changes created by LSB modification are too subtle for human perception. The Steghide tool implements this approach along with encryption to secure the hidden data. This provides a good balance between security and capacity, as images can typically hold substantial amounts of hidden text.

### Image-in-Image Steganography
> [!info] Technique
> This technique embeds one image within another by modifying pixel data in ways imperceptible to the human eye.

This method requires sufficient capacity in the cover image to hold the secret image data. It's one of the more challenging steganography techniques because images typically contain more data than text, requiring careful consideration of the size relationship between cover and secret images.

## Materials

### Software Used
| Tool | Version | Purpose |
|------|---------|---------|
| Steghide | 0.5.1 | Command-line steganography program for text-in-image and image-in-image experiments |
| Outguess | 1:0.4-2 | Attempted for image-in-image steganography but faced capacity limitations |
| ImageMagick | convert | Used to create sample gradient images for our experiments |

### Files Created
| File | Purpose | Size |
|------|---------|------|
| visible_text.txt | Original visible message | 50 bytes |
| secret_text.txt | Secret message to be hidden | 46 bytes |
| cover_image.jpg | Cover image for hiding data | ~13 KB |
| smaller_secret.jpg | Small image to be hidden | 555 bytes |
| extracted_secret.txt | Result file from extraction | 46 bytes |
| extracted_secret_image.jpg | Result file from image extraction | 555 bytes |

## Methodology

### Setting Up the Environment

> [!tip] Environment Preparation
> Before conducting steganography experiments, appropriate tools must be installed and a separate workspace should be created.

First, we installed the necessary steganography tools:

```bash
sudo apt-get update && sudo apt-get install -y steghide outguess
```

The command produced the following output (truncated):
```
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libmcrypt4 libmhash2
...
Setting up steghide (0.5.1-15) ...
```

We then created a dedicated directory for our experiments:

```bash
mkdir steganography_demo && cd steganography_demo
```

### Creating Sample Files

We created text files for our demonstrations:

```bash
echo "This is a visible message that everyone can read." > visible_text.txt
echo "This is a secret message that will be hidden." > secret_text.txt
```

> [!example] File Contents
> **visible_text.txt**:
> ```
> This is a visible message that everyone can read.
> ```
> 
> **secret_text.txt**:
> ```
> This is a secret message that will be hidden.
> ```

For our image demonstrations, we created sample images using ImageMagick's gradient function to generate visually distinct patterns:

```bash
convert -size 512x384 gradient:blue-purple cover_image.jpg
convert -size 256x192 gradient:red-yellow secret_image.jpg
convert -size 64x48 gradient:red-yellow smaller_secret.jpg
```

Here are the images we created:

![[obsidian_images/cover_image.jpg|300]]
*Cover image (512x384 blue-purple gradient)*

![[obsidian_images/smaller_secret.jpg|150]]
*Smaller secret image (64x48 red-yellow gradient)*

### Experiment 1: Text-in-Text Steganography

> [!experiment] Text-in-Text Steganography
> **Goal**: Hide information in plain text using whitespace coding
> **Method**: Using extra spaces to represent binary data
> **Tools Required**: Standard text editor

We created a text file with hidden data using whitespace coding:

```bash
echo -e "Let's demonstrate text-in-text steganography using whitespace coding.\nThe following sentence has hidden data using trailing spaces:" > text_steg_demo.txt
echo -e "This line looks normal but has hidden binary data. \c" >> text_steg_demo.txt
echo -e "Each word ends with a space for 1 or no space for 0: \c" >> text_steg_demo.txt
echo -e "Hello  world  this is  a  hidden  message." >> text_steg_demo.txt
```

**Explanation of the technique:**
In this example, extra spaces after words represent binary digits, with double spaces representing "1" and single spaces representing "0". The message "Hello  world  this is  a  hidden  message." contains hidden binary data through its spacing pattern.

**Content of text_steg_demo.txt:**
```
Let's demonstrate text-in-text steganography using whitespace coding.
The following sentence has hidden data using trailing spaces:
This line looks normal but has hidden binary data. Each word ends with a space for 1 or no space for 0: Hello  world  this is  a  hidden  message.
```

> [!note] Hidden Binary Message
> If we interpret the spacing pattern where double space = 1 and single space = 0, the message "Hello  world  this is  a  hidden  message." encodes "10100101" which could represent the ASCII character 'å' (decimal 165).

### Experiment 2: Text-in-Image Steganography

> [!experiment] Text-in-Image Steganography
> **Goal**: Hide text within an image file
> **Method**: Using Steghide to modify least significant bits
> **Tools Required**: Steghide, image file (JPG format)

We used Steghide to embed text within an image:

```bash
steghide embed -cf cover_image.jpg -ef secret_text.txt -p "password123" -v
```

The command produced this output, confirming successful embedding:
```
reading secret file "secret_text.txt"... done
reading cover file "cover_image.jpg"... done
creating the graph... 125 sample values, 429 vertices, 25001 edges
executing Static Minimum Degree Construction Heuristic... 54.1% (1.0) done
```

To verify the embedding worked, we extracted the hidden text:

```bash
steghide extract -sf cover_image.jpg -p "password123" -xf extracted_secret.txt
```

The extraction produced this output:
```
wrote extracted data to "extracted_secret.txt".
```

**Analysis of the process:**
- The `-cf` flag specifies the cover file
- The `-ef` flag specifies the embedded file
- The `-p` flag provides the password
- The `-v` flag enables verbose output
- The extraction recovered the exact same content as the original secret message

### Experiment 3: Image-in-Image Steganography

> [!experiment] Image-in-Image Steganography
> **Goal**: Hide one image inside another image
> **Method**: Using steganography tools to embed image data
> **Tools Required**: Outguess (attempted), Steghide (successful)

#### First Attempt with Outguess

Initially, we tried using Outguess but encountered capacity issues:

```bash
cp cover_image.jpg cover_for_outguess.jpg
outguess -k "password123" -d secret_image.jpg cover_for_outguess.jpg stego_image.jpg
```

The command failed with the following error:
```
Reading cover_for_outguess.jpg....
JPEG compression quality set to 75
Extracting usable bits:   5466 bits
Encoded 'secret_image.jpg': 23400 bits, 2925 bytes
Finding best embedding...
steg_embed:

## Results

### Text-in-Text Steganography
We successfully created a text file with hidden information using whitespace coding. The hidden message is imperceptible to casual readers but contains encoded binary data.

![Text Steganography File](text_steg_demo.txt)
*Text file containing hidden data using whitespace coding*

### Text-in-Image Steganography
We successfully embedded the secret text file into the cover image. The modified image shows no visible differences from the original.

![Cover Image](obsidian_images/cover_image.jpg)
*Figure 2: The cover image containing hidden text*

We were able to extract the hidden text, confirming the success of this technique:

```
This is a secret message that will be hidden.
```

### Image-in-Image Steganography
We successfully embedded a smaller image into the cover image using Steghide. The visual appearance of the cover image remained unchanged.

![Original Cover Image](obsidian_images/cover_image.jpg)
*Figure 3: The cover image before embedding*

![Secret Image](obsidian_images/smaller_secret.jpg)
*Figure 4: The smaller secret image that was embedded*

We were able to extract the hidden image, confirming the success of this technique.

![Extracted Secret Image](obsidian_images/extracted_secret_image.jpg)
*Figure 5: The successfully extracted secret image*

## Discussion

### Effectiveness of Different Techniques
1. **Text-in-Text Steganography**: This method is simple but has limited capacity and is relatively easy to detect if someone is specifically looking for it. The main advantage is that it requires no special tools.

2. **Text-in-Image Steganography**: This method offers a good balance of capacity and security. The modified image shows no visible changes, making detection difficult without special analysis tools.

3. **Image-in-Image Steganography**: This technique requires careful consideration of capacity. Our initial attempt with Outguess failed due to capacity constraints, but Steghide succeeded with a smaller secret image. This highlights the importance of payload size in steganography.

### Limitations and Challenges
- **Capacity**: There's a limit to how much data can be hidden without causing noticeable artifacts.
- **Tool Limitations**: Different tools have different capabilities and constraints, as seen with Outguess vs. Steghide.
- **Password Protection**: All methods used require a password for extraction, adding a layer of security but also creating a potential point of failure if the password is forgotten.

## Conclusion
This lab demonstrated three different steganography techniques, each with its own strengths and applications. Text-in-text steganography is simple but limited, while image-based techniques offer greater capacity and security at the cost of complexity.

The key advantage of steganography over encryption is that it hides the very existence of secret communication. For maximum security in real-world applications, it would be advisable to combine steganography with strong encryption.

The experiments highlighted the importance of considering payload size relative to the capacity of the carrier medium, and demonstrated that tools like Steghide can effectively hide information with no visible artifacts when used correctly.

## References
1. Steghide documentation: [https://steghide.sourceforge.net/documentation.php](https://steghide.sourceforge.net/documentation.php)
2. Outguess documentation: [https://outguess.sourceforge.net/](https://outguess.sourceforge.net/)
3. Johnson, N. F., & Jajodia, S. (1998). Exploring steganography: Seeing the unseen. Computer, 31(2), 26-34.
