#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import math

def create_budget_pie():
    """Create budget distribution pie chart"""
    width, height = 800, 600
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
    
    # Title
    draw.text((400, 30), "Budget Distribution (₹4,00,00,000)", fill=(0, 51, 102), font=title_font, anchor="mm")
    
    # Budget data
    categories = [
        ("Infrastructure & Hardware", 46.25, (0, 102, 204)),
        ("Personnel (36 months)", 27.00, (51, 153, 102)),
        ("Software & Licensing", 11.25, (255, 153, 0)),
        ("Office & Facilities", 6.25, (204, 0, 0)),
        ("Training & Certifications", 3.75, (153, 51, 255)),
        ("Contingency & Misc", 5.50, (255, 204, 0))
    ]
    
    # Draw pie chart
    center_x, center_y = 350, 300
    radius = 150
    start_angle = 0
    
    for label, percentage, color in categories:
        angle = percentage * 3.6  # Convert percentage to degrees
        end_angle = start_angle + angle
        draw.pieslice([(center_x-radius, center_y-radius), (center_x+radius, center_y+radius)], 
                     start_angle, end_angle, fill=color, outline='white', width=2)
        start_angle = end_angle
    
    # Draw legend
    legend_y = 150
    for label, percentage, color in categories:
        draw.rectangle([(550, legend_y), (580, legend_y+20)], fill=color)
        draw.text((590, legend_y+10), f"{label}: {percentage}%", fill='black', font=label_font, anchor="lm")
        legend_y += 35
    
    img.save('diagram-budget.png', 'PNG', quality=95)
    print("Created: diagram-budget.png")

def create_timeline():
    """Create implementation timeline"""
    width, height = 1000, 500
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
    
    # Title
    draw.text((500, 30), "36-Month Implementation Timeline", fill=(0, 51, 102), font=title_font, anchor="mm")
    
    # Timeline phases
    phases = [
        ("Planning", 0, 4, (51, 153, 255)),
        ("Infrastructure", 3, 9, (51, 204, 102)),
        ("Equipment", 5, 12, (255, 153, 51)),
        ("Launch", 10, 15, (204, 51, 153)),
        ("Operations", 14, 36, (153, 51, 204))
    ]
    
    # Draw timeline bar
    timeline_y = 150
    month_width = 25
    start_x = 100
    
    # Draw months scale
    for i in range(0, 37, 6):
        x = start_x + i * month_width
        draw.line([(x, timeline_y-10), (x, timeline_y+150)], fill=(200, 200, 200), width=1)
        draw.text((x, timeline_y-20), f"M{i}", fill='black', font=label_font, anchor="mm")
    
    # Draw phases
    bar_y = timeline_y
    for label, start, end, color in phases:
        x1 = start_x + start * month_width
        x2 = start_x + end * month_width
        draw.rectangle([(x1, bar_y), (x2, bar_y+40)], fill=color, outline='black', width=2)
        draw.text(((x1+x2)/2, bar_y+20), label, fill='white', font=label_font, anchor="mm")
        bar_y += 50
    
    # Add milestones
    milestones = [(4, "Vendors"), (9, "Infra"), (12, "Pilot"), (15, "Launch"), (36, "CoE")]
    for month, label in milestones:
        x = start_x + month * month_width
        draw.ellipse([(x-8, timeline_y+200-8), (x+8, timeline_y+200+8)], fill=(255, 215, 0), outline='black', width=2)
        draw.text((x, timeline_y+220), label, fill='black', font=label_font, anchor="mm")
    
    img.save('diagram-timeline.png', 'PNG', quality=95)
    print("Created: diagram-timeline.png")

def create_org_chart():
    """Create organizational hierarchy"""
    width, height = 900, 700
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
        bold_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        bold_font = ImageFont.load_default()
    
    # Title
    draw.text((450, 30), "Organizational Structure", fill=(0, 51, 102), font=title_font, anchor="mm")
    
    # Director box
    draw.rectangle([(325, 80), (575, 140)], fill=(255, 102, 102), outline='black', width=2)
    draw.text((450, 95), "Lab Director", fill='white', font=bold_font, anchor="mm")
    draw.text((450, 115), "Dr. D.D. Ambawade", fill='white', font=label_font, anchor="mm")
    
    # Level 2 boxes
    level2_positions = [
        (150, 200, "Sr. Research\nAssociate 1", (102, 178, 255)),
        (350, 200, "Sr. Research\nAssociate 2", (102, 178, 255)),
        (550, 200, "System\nAdministrator", (102, 204, 153)),
        (750, 200, "Admin\nAssistant", (255, 178, 102))
    ]
    
    for x, y, label, color in level2_positions:
        draw.rectangle([(x-75, y), (x+75, y+60)], fill=color, outline='black', width=2)
        draw.text((x, y+30), label, fill='white', font=label_font, anchor="mm", align='center')
        # Connection line from director
        draw.line([(450, 140), (x, y)], fill='black', width=2)
    
    # Level 3 boxes (technicians)
    tech_positions = [
        (150, 320, "Lab Tech 1\nNetwork"), 
        (350, 320, "Lab Tech 2\nAI/IoT")
    ]
    
    for i, (x, y, label) in enumerate(tech_positions):
        draw.rectangle([(x-60, y), (x+60, y+50)], fill=(255, 229, 153), outline='black', width=2)
        draw.text((x, y+25), label, fill='black', font=label_font, anchor="mm", align='center')
        # Connection line from associate
        parent_x = 150 if i == 0 else 350
        draw.line([(parent_x, 260), (x, y)], fill='black', width=2)
    
    img.save('diagram-orgchart.png', 'PNG', quality=95)
    print("Created: diagram-orgchart.png")

def create_lab_layout():
    """Create lab layout diagram"""
    width, height = 1000, 800
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    
    try:
        title_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
        label_font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 12)
    except:
        title_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
    
    # Title
    draw.text((500, 30), "Lab Layout (3,500 sq.ft)", fill=(0, 51, 102), font=title_font, anchor="mm")
    
    # Border
    draw.rectangle([(50, 70), (950, 750)], outline=(0, 51, 102), width=3)
    
    # Labs (simplified grid layout)
    labs = [
        (70, 90, 280, 240, "Network Security\n500 sq.ft\n20 students", (102, 153, 255)),
        (300, 90, 510, 240, "Penetration Testing\n500 sq.ft\n15 students", (255, 153, 102)),
        (530, 90, 720, 240, "Digital Forensics\n400 sq.ft\n12 students", (153, 204, 102)),
        (740, 90, 930, 240, "AI/ML Security\n400 sq.ft\n15 students", (255, 102, 178)),
        (70, 260, 280, 410, "IoT Security\n350 sq.ft\n12 students", (204, 153, 255)),
        (300, 260, 510, 410, "CPS/ICS Security\n450 sq.ft\n10 students", (255, 204, 102)),
        (530, 260, 720, 410, "Malware Analysis\n300 sq.ft\n8 students", (153, 255, 204)),
        (740, 260, 930, 410, "Server & SOC\n600 sq.ft\n8 analysts", (255, 178, 102)),
        (70, 430, 370, 550, "Conference Room\n250 sq.ft\n30 people", (204, 204, 255)),
        (390, 430, 620, 550, "Office Space\n200 sq.ft\n6 staff", (255, 229, 153)),
        (640, 430, 930, 550, "Storage & Utility\n150 sq.ft", (220, 220, 220))
    ]
    
    for x1, y1, x2, y2, label, color in labs:
        draw.rectangle([(x1, y1), (x2, y2)], fill=color, outline='black', width=2)
        draw.text(((x1+x2)/2, (y1+y2)/2), label, fill='black', font=label_font, anchor="mm", align='center')
    
    # Entry
    draw.rectangle([(420, 730), (580, 750)], fill=(102, 255, 102), outline='black', width=2)
    draw.text((500, 740), "ENTRY", fill='black', font=label_font, anchor="mm")
    
    img.save('diagram-lablayout.png', 'PNG', quality=95)
    print("Created: diagram-lablayout.png")

# Create all diagrams
create_budget_pie()
create_timeline()
create_org_chart()
create_lab_layout()

print("\nAll diagrams created successfully!")
