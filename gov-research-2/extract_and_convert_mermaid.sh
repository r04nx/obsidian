#!/bin/bash

# Function to convert mermaid code to image URL
convert_mermaid() {
    local mermaid_code="$1"
    local output_file="$2"
    
    # Encode to base64
    local encoded=$(echo -n "$mermaid_code" | base64 -w 0)
    
    # Download image from mermaid.ink
    echo "Downloading: $output_file"
    curl -s "https://mermaid.ink/img/$encoded" -o "$output_file"
    
    if [ -f "$output_file" ] && [ -s "$output_file" ]; then
        echo "  Success: $output_file ($(ls -lh $output_file | awk '{print $5}'))"
    else
        echo "  Failed: $output_file"
    fi
}

# Extract and convert pie chart from Executive Summary
cat > /tmp/mermaid1.txt << 'EOF'
pie title Budget Distribution by Category
    "Infrastructure & Hardware" : 46.25
    "Personnel (36 months)" : 27.00
    "Software & Licensing" : 11.25
    "Office & Facilities" : 6.25
    "Training & Certifications" : 3.75
    "Contingency & Misc" : 5.50
EOF
convert_mermaid "$(cat /tmp/mermaid1.txt)" "mermaid-budget-pie.png"

# Extract Gantt chart from Timeline
cat > /tmp/mermaid2.txt << 'EOF'
gantt
    title Cyber Security Lab Implementation Timeline
    dateFormat YYYY-MM
    section Phase 1 Setup
    Infrastructure Planning & Procurement    :2026-06, 4M
    Lab Construction & Installation          :2026-10, 3M
    section Phase 2 Deployment
    Equipment Installation & Testing         :2027-01, 2M
    Software Configuration & Integration     :2027-03, 2M
    section Phase 3 Operations
    Personnel Recruitment & Training         :2027-05, 2M
    Pilot Operations & Testing               :2027-07, 2M
    section Phase 4 Production
    Full Operations & Research Activities    :2027-09, 21M
EOF
convert_mermaid "$(cat /tmp/mermaid2.txt)" "mermaid-timeline-gantt.png"

# Personnel Budget Distribution
cat > /tmp/mermaid3.txt << 'EOF'
pie title Personnel Budget Distribution (36 months)
    "Lab Director" : 27
    "Research Associate 1" : 28.8
    "Research Associate 2" : 24
    "System Administrator" : 21.6
    "Lab Technician 1" : 14.4
    "Lab Technician 2" : 9.6
    "Admin Assistant" : 12.6
EOF
convert_mermaid "$(cat /tmp/mermaid3.txt)" "mermaid-personnel-pie.png"

# Organizational Chart
cat > /tmp/mermaid4.txt << 'EOF'
graph TD
    A[Lab Director<br/>Dr. D.D. Ambawade] --> B[Sr. Research Associate 1<br/>Network Security]
    A --> C[Sr. Research Associate 2<br/>AI/ML & IoT Security]
    A --> D[System Administrator<br/>Infrastructure]
    A --> E[Admin Assistant<br/>Operations]
    B --> F[Lab Technician 1<br/>Network Labs]
    C --> G[Lab Technician 2<br/>AI/IoT Labs]
    D --> H[Student Assistants<br/>Part-time]
EOF
convert_mermaid "$(cat /tmp/mermaid4.txt)" "mermaid-org-chart.png"

# Research Areas Mindmap
cat > /tmp/mermaid5.txt << 'EOF'
mindmap
  root((Cyber Security Research))
    AI/ML Security
      Adversarial ML
      Model Security
      Privacy-Preserving ML
    IoT Security
      Firmware Analysis
      Hardware Security
      Protocol Vulnerabilities
    Network Security
      Zero Trust
      5G/6G Security
      APT Detection
    CPS & ICS
      SCADA Security
      Smart Grids
      Industrial Protocols
    Blockchain
      Smart Contracts
      DeFi Security
      Crypto Forensics
    Cloud Security
      Container Security
      Serverless
      Multi-cloud
    Digital Forensics
      Mobile Forensics
      Cloud Forensics
      Memory Analysis
EOF
convert_mermaid "$(cat /tmp/mermaid5.txt)" "mermaid-research-mindmap.png"

# Hardware Budget Pie
cat > /tmp/mermaid6.txt << 'EOF'
pie title Hardware Budget Distribution
    "Workstations (40.5%)" : 75
    "Network Infrastructure (18.9%)" : 35
    "Server Infrastructure (16.2%)" : 30
    "GPU Cluster (8.1%)" : 15
    "CPS Lab Equipment (5.4%)" : 10
    "Digital Forensics (4.3%)" : 8
    "IoT Lab (2.7%)" : 5
    "Vulnerable Machines (1.6%)" : 3
    "Displays (2.2%)" : 4
EOF
convert_mermaid "$(cat /tmp/mermaid6.txt)" "mermaid-hardware-pie.png"

# Lab Capacity Breakdown
cat > /tmp/mermaid7.txt << 'EOF'
graph TB
    A[Total Capacity:<br/>120+ Concurrent Users]
    A --> B[Network Security Lab<br/>20 students]
    A --> C[Penetration Testing<br/>15 students]
    A --> D[Digital Forensics<br/>12 students]
    A --> E[AI/ML Security<br/>15 students]
    A --> F[IoT Security<br/>12 students]
    A --> G[CPS/ICS Security<br/>10 students]
    A --> H[Malware Analysis<br/>8 students]
    A --> I[SOC Training<br/>8 analysts]
EOF
convert_mermaid "$(cat /tmp/mermaid7.txt)" "mermaid-lab-capacity.png"

echo ""
echo "All mermaid diagrams converted!"
echo "Generated files:"
ls -lh mermaid-*.png 2>/dev/null | awk '{print "  " $9 " - " $5}'
