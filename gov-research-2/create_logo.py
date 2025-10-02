#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import math

# Create a professional logo
width, height = 800, 400
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# Background gradient effect (simulate with rectangles)
for i in range(height):
    shade = int(255 - (i / height) * 40)
    draw.rectangle([(0, i), (width, i+1)], fill=(shade, shade, 255))

# Draw shield shape
shield_points = [
    (400, 80),   # top center
    (500, 100),  # top right
    (500, 250),  # middle right
    (400, 320),  # bottom center
    (300, 250),  # middle left
    (300, 100),  # top left
]
draw.polygon(shield_points, fill=(0, 51, 102), outline=(218, 165, 32))

# Add text
try:
    title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    subtitle_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    small_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    small_font = ImageFont.load_default()

# Draw SHIELD text
draw.text((400, 160), "SHIELD", fill=(255, 215, 0), font=title_font, anchor="mm")
draw.text((400, 200), "Security Lab", fill=(255, 255, 255), font=subtitle_font, anchor="mm")

# Draw full name at bottom
draw.text((400, 360), "Securing Hardware & Infrastructure through Education, Labs & Defense", 
          fill=(0, 51, 102), font=small_font, anchor="mm")

img.save('shield-logo.png', 'PNG', quality=95)
print("Logo created: shield-logo.png")
