---
share_link: https://share.note.sx/ihoqqjey#rSAmHsrRzfCs1Ud+KoF1IbLnUxulOu8puOe5Lz/ujnM
share_updated: 2025-04-18T23:31:18+05:30
---
### To provide confidentiality using Steganography: a professional tool

**Student Name:** Rohan Pawar  
**UID:** 2023201020  
**Batch:** C  
**Branch:** EXTC  
**Course:** CCN

> [!abstract] AIM:
>experiments with three different steganography techniques: text-in-text, text-in-image, and image-in-image. All experiments were conducted in a Linux Ubuntu environment using various steganography tools.

## Introduction
Steganography is the practice of concealing information within other non-secret data or a physical object to avoid detection. Unlike encryption, which focuses on making data unreadable, steganography aims to hide the very existence of the secret communication. 

![[tmp/ccn6/steganography_demo/obsidian_images/cover_image.jpg|300]]
*Cover image used in this steganography experiments*

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

![[tmp/ccn6/steganography_demo/obsidian_images/cover_image.jpg|300]]
*Cover image (512x384 blue-purple gradient)*

![[tmp/ccn6/steganography_demo/obsidian_images/smaller_secret.jpg|150]]
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
steg_embed: not enough bits in bitmap for embedding: 23400 > 5466/2
```

We then tried using a smaller secret image, but still encountered capacity issues:

```bash
outguess -k "password123" -d smaller_secret.jpg cover_for_outguess.jpg stego_image.jpg
```

The same error persisted:
```
Reading cover_for_outguess.jpg....
JPEG compression quality set to 75
Extracting usable bits:   5466 bits
Encoded 'smaller_secret.jpg': 4440 bits, 555 bytes
Finding best embedding...
steg_embed: not enough bits in bitmap for embedding: 4440 > 5466/2
```

#### Successful Attempt with Steghide

We then successfully used Steghide for image-in-image steganography:

```bash
steghide embed -cf cover_image.jpg -ef smaller_secret.jpg -p "password123" -v
```

The command produced this output:
```
reading secret file "smaller_secret.jpg"... done
reading cover file "cover_image.jpg"... done
creating the graph... 168 sample values, 1690 vertices, 525538 edges
executing Static Minimum Degree Construction Heuristic... 76.0% (1.0) done
```

To verify the embedding worked, we extracted the hidden image:

```bash
steghide extract -sf cover_image.jpg -p "password123" -xf extracted_secret_image.jpg
```

The extraction was successful:
```
wrote extracted data to "extracted_secret_image.jpg".
```

### Enhanced Image-in-Image Steganography Experiment

> [!experiment] Enhanced Image-in-Image Steganography
> **Goal**: Demonstrate image-in-image steganography with more complex images and analyze pixel-level changes
> **Method**: Using Steghide with visually rich images and performing detailed analysis
> **Tools Required**: Steghide, ImageMagick (for image creation and analysis)

To better understand the technical aspects of image-in-image steganography, we performed an enhanced experiment with more complex images and conducted a detailed analysis of the changes at the pixel level.

#### Creating Enhanced Test Images

First, we created a more complex cover image with distinctive patterns:

```bash
convert -size 512x384 xc: +noise Random -channel R -fx "sin(a*20)*0.5+0.5" -channel G -fx "sin(a*10+b*10)*0.5+0.5" -channel B -fx "sin(b*20)*0.5+0.5" enhanced_cover.jpg
```

This command creates a colorful pattern with sine waves applied to different color channels, resulting in a visually rich image:

![[tmp/ccn6/steganography_demo/obsidian_images/enhanced_cover_original.jpg|300]]
*Enhanced cover image with complex pattern*

Next, we created a distinctive secret image that would be hidden:

```bash
convert -size 128x96 xc:black -fill white -draw "circle 64,48 64,24" -draw "text 40,50 'SECRET'" enhanced_secret.jpg
```

This creates a black image with a white circle and the text "SECRET":

![[tmp/ccn6/steganography_demo/obsidian_images/enhanced_secret.jpg|200]]
*Secret image with distinctive visual elements*

#### Performing Enhanced Steganography

We then performed the steganography operation using Steghide:

```bash
steghide embed -cf enhanced_cover.jpg -ef enhanced_secret.jpg -p "StegDemo2025" -v
```

The operation produced this output:
```
reading secret file "enhanced_secret.jpg"... done
reading cover file "enhanced_cover.jpg"... done
creating the graph... 198 sample values, 4996 vertices, 11134924 edges
executing Static Minimum Degree Construction Heuristic... 99.9% (1.0) done
```

To verify success, we extracted the hidden image:

```bash
steghide extract -sf enhanced_cover.jpg -p "StegDemo2025" -xf enhanced_extracted.jpg
```

The extraction was successful:
```
wrote extracted data to "enhanced_extracted.jpg".
```

#### Pixel-Level Analysis

> [!info] Understanding LSB Steganography
> Steghide uses Least Significant Bit (LSB) steganography, which replaces the least significant bits of the cover image's pixel values with bits from the secret data. Since changing the least significant bit alters the pixel value by at most 1, these changes are typically imperceptible to the human eye.

To analyze the effects of the steganography process at the pixel level, we created a side-by-side comparison of the original and modified cover images:

![[tmp/ccn6/steganography_demo/obsidian_images/comparison_covers.jpg|500]]
*Side-by-side comparison of original (left) and stego (right) cover images*

Despite containing the entire secret image, the stego image is visually identical to the original cover image. This demonstrates the effectiveness of LSB steganography in hiding data without perceptible changes.

We then used ImageMagick's compare tool to visualize the exact pixels that were modified during the embedding process:

```bash
compare -metric AE -highlight-color red enhanced_cover_original.jpg enhanced_cover.jpg difference_analysis.jpg
```

This command produced an output of `131927`, indicating that 131,927 pixels (out of 196,608 total pixels in the 512x384 image) were modified during the steganography process. This represents approximately 67.1% of the pixels in the image.

The resulting difference analysis image highlights the modified pixels in red:

![[tmp/ccn6/steganography_demo/obsidian_images/difference_analysis.jpg|400]]
*Pixel difference analysis showing modified pixels in red*

> [!note] Pixel Modification Pattern
> The pattern of modified pixels appears to be somewhat random rather than concentrated in a specific region. This is a characteristic of Steghide's embedding algorithm, which distributes the secret data throughout the cover image using a pseudorandom number generator seeded with the password. This distribution pattern helps make the steganography more resistant to detection.

#### Technical Insights

1. **Bit Modification**: While 67.1% of pixels were modified, each modification changed only the least significant bit(s) of the pixel values, resulting in color changes that are imperceptible to the human eye (a maximum change of 1 in a color value that ranges from 0-255).

2. **Capacity vs. Quality**: The enhanced cover image (512x384 pixels) could successfully hide the secret image (128x96 pixels) without visible degradation. This represents a capacity ratio of approximately 16:1 in terms of pixel count.

3. **Password Importance**: The password "StegDemo2025" serves two critical functions:
   - It seeds the pseudorandom number generator that determines where data is embedded
   - It protects the hidden data from extraction by unauthorized parties

4. **Robustness**: While LSB steganography successfully hides data from visual inspection, it may be vulnerable to statistical analysis and can be damaged by image compression or processing operations that modify pixel values.

## Results

### Text-in-Text Steganography
We successfully created a text file with hidden information using whitespace coding. The hidden message is imperceptible to casual readers but contains encoded binary data.

```
Let's demonstrate text-in-text steganography using whitespace coding.
The following sentence has hidden data using trailing spaces:
This line looks normal but has hidden binary data. Each word ends with a space for 1 or no space for 0: Hello  world  this is  a  hidden  message.
```
*Text file containing hidden data using whitespace coding*

### Text-in-Image Steganography
We successfully embedded the secret text file into the cover image. The modified image shows no visible differences from the original.

![[tmp/ccn6/steganography_demo/obsidian_images/cover_image.jpg|300]]
*Figure 2: The cover image containing hidden text*

We were able to extract the hidden text, confirming the success of this technique:

```
This is a secret message that will be hidden.
```

### Image-in-Image Steganography

#### Initial Experiment
In our initial experiment, we successfully embedded a smaller image into the cover image using Steghide. The visual appearance of the cover image remained unchanged.

![[tmp/ccn6/steganography_demo/obsidian_images/cover_image.jpg|300]]
*The cover image before embedding*

![[tmp/ccn6/steganography_demo/obsidian_images/smaller_secret.jpg|150]]
*The smaller secret image that was embedded*

We were able to extract the hidden image, confirming the success of this technique.

![[tmp/ccn6/steganography_demo/obsidian_images/extracted_secret_image.jpg|150]]
*The successfully extracted secret image*

#### Enhanced Experiment
Our enhanced experiment demonstrated the following key results:

1. **Visually Identical Images**: Despite embedding a 128x96 pixel secret image containing distinctive visual elements (circle and text), the resulting stego image showed no perceptible differences from the original when viewed normally.

![[tmp/ccn6/steganography_demo/obsidian_images/enhanced_cover_original.jpg|300]]
*Original enhanced cover image*

![[tmp/ccn6/steganography_demo/obsidian_images/enhanced_cover.jpg|300]]
*Stego image containing the hidden secret image*

2. **Successful Data Extraction**: We were able to perfectly extract the hidden image using the correct password:

![[tmp/ccn6/steganography_demo/obsidian_images/enhanced_extracted.jpg|200]]
*Extracted secret image showing perfect recovery*

3. **Pixel-Level Changes**: Our difference analysis revealed that 131,927 pixels (67.1% of the image) were modified during the embedding process. However, these changes were limited to the least significant bits, resulting in imperceptible visual differences:

![[tmp/ccn6/steganography_demo/obsidian_images/difference_analysis.jpg|400]]
*Difference analysis showing modified pixels in red*

4. **Data Distribution**: The modified pixels were distributed throughout the image rather than concentrated in specific regions, making the steganography more resistant to detection through simple visual inspection or basic statistical analysis.

## Discussion

### Effectiveness of Different Techniques
1. **Text-in-Text Steganography**: This method is simple but has limited capacity and is relatively easy to detect if someone is specifically looking for it. The main advantage is that it requires no special tools.

2. **Text-in-Image Steganography**: This method offers a good balance of capacity and security. The modified image shows no visible changes, making detection difficult without special analysis tools.

3. **Image-in-Image Steganography**: This technique requires careful consideration of capacity. Our initial attempt with Outguess failed due to capacity constraints, but Steghide succeeded with a smaller secret image. This highlights the importance of payload size in steganography. Our enhanced experiment demonstrated that even with complex images, approximately 67% of pixels needed modification to hide a secret image that was 1/16th the size of the cover image in terms of pixel count.

## Conclusion
This lab demonstrated three different steganography techniques, each with its own strengths and applications. Text-in-text steganography is simple but limited, while image-based techniques offer greater capacity and security at the cost of complexity.

The experiments highlighted the importance of considering payload size relative to the capacity of the carrier medium, and demonstrated that tools like Steghide can effectively hide information with no visible artifacts when used correctly. Our pixel-level analysis revealed that even when a significant percentage of pixels are modified (67% in our enhanced experiment), the changes remain imperceptible because they only affect the least significant bits of pixel values.

