#!/bin/bash

# Function to convert mermaid code to PNG using Kroki
convert_kroki() {
    local mermaid_code="$1"
    local output_file="$2"
    
    echo "Converting: $output_file"
    
    # Use Kroki API with mermaid
    curl -X POST "https://kroki.io/mermaid/png" \
         -H "Content-Type: text/plain" \
         --data-raw "$mermaid_code" \
         -o "$output_file" 2>/dev/null
    
    if [ -f "$output_file" ] && [ -s "$output_file" ]; then
        echo "  ✓ Success: $output_file ($(ls -lh $output_file | awk '{print $5}'))"
    else
        echo "  ✗ Failed: $output_file"
    fi
}

echo "==========================================="
echo "Converting Mermaid Diagrams using Kroki.io"
echo "==========================================="
echo ""

# 1. Budget Distribution Pie Chart
convert_kroki 'pie title Budget Distribution (Rs 4 Crores)
    "Infrastructure & Hardware 46%" : 46.25
    "Personnel 27%" : 27.00
    "Software 11%" : 11.25
    "Office 6%" : 6.25
    "Training 4%" : 3.75
    "Contingency 6%" : 5.50' \
    "kroki-budget-pie.png"

# 2. Implementation Timeline Gantt Chart
convert_kroki 'gantt
    title 36-Month Implementation Timeline
    dateFormat YYYY-MM
    section Phase 1 Setup
    Planning & Design           :2026-06, 2M
    Tender & Vendor Selection   :2026-08, 2M
    section Phase 2 Infrastructure
    Civil Work                  :2026-08, 4M
    Power & HVAC               :2026-09, 3M
    Network Cabling            :2026-10, 2M
    section Phase 3 Equipment
    Hardware Batch 1           :2026-10, 3M
    Software Licensing         :2026-11, 2M
    Equipment Testing          :2027-01, 2M
    section Phase 4 Operations
    Pilot Testing              :2027-03, 2M
    Soft Launch                :2027-05, 3M
    Full Operations            :2027-08, 22M' \
    "kroki-timeline-gantt.png"

# 3. Personnel Budget Distribution
convert_kroki 'pie title Personnel Budget (Rs 1.08 Crores)
    "Lab Director 25%" : 25
    "Research Associate 1 27%" : 27
    "Research Associate 2 22%" : 22
    "System Admin 20%" : 20
    "Lab Tech 1 13%" : 13
    "Lab Tech 2 9%" : 9
    "Admin Assistant 12%" : 12' \
    "kroki-personnel-pie.png"

# 4. Organizational Hierarchy
convert_kroki 'graph TD
    A[Lab Director<br/>Dr. D.D. Ambawade<br/>Rs 27L]
    B[Sr. Research Associate 1<br/>Network & Pentesting<br/>Rs 28.8L]
    C[Sr. Research Associate 2<br/>AI/ML & IoT Security<br/>Rs 24L]
    D[System Administrator<br/>Infrastructure<br/>Rs 21.6L]
    E[Admin Assistant<br/>Operations<br/>Rs 12.6L]
    F[Lab Technician 1<br/>Network Labs<br/>Rs 14.4L]
    G[Lab Technician 2<br/>AI/IoT Labs<br/>Rs 9.6L]
    H[Student Assistants<br/>Part-time]
    
    A --> B
    A --> C
    A --> D
    A --> E
    B --> F
    C --> G
    D --> H
    
    style A fill:#ff6b6b,stroke:#c92a2a,color:#fff
    style B fill:#4ecdc4,stroke:#0a8080
    style C fill:#4ecdc4,stroke:#0a8080
    style D fill:#95e1d3,stroke:#38ada9
    style E fill:#95e1d3,stroke:#38ada9
    style F fill:#ffeaa7,stroke:#fdcb6e
    style G fill:#ffeaa7,stroke:#fdcb6e
    style H fill:#dfe6e9,stroke:#b2bec3' \
    "kroki-org-chart.png"

# 5. Research Focus Areas Mindmap
convert_kroki 'mindmap
  root((Cyber Security<br/>Research))
    AI/ML Security
      Adversarial ML
      Model Security
      Privacy ML
      Threat Detection
    IoT Security
      Firmware Analysis
      Hardware Security
      Protocol Vulnerabilities
      Smart Devices
    Network Security
      Zero Trust
      5G/6G Security
      APT Detection
      SDN/NFV
    CPS & ICS
      SCADA Security
      Smart Grids
      Industrial Protocols
      OT Security
    Blockchain
      Smart Contracts
      DeFi Security
      Crypto Forensics
      Consensus
    Cloud Security
      Container Security
      Serverless
      Multi-cloud
      DevSecOps
    Digital Forensics
      Mobile Forensics
      Cloud Forensics
      Memory Analysis
      Anti-Forensics' \
    "kroki-research-mindmap.png"

# 6. Hardware Budget Pie Chart
convert_kroki 'pie title Hardware Budget (Rs 1.85 Crores)
    "Workstations 41%" : 75
    "Network Infra 19%" : 35
    "Server Infra 16%" : 30
    "GPU Cluster 8%" : 15
    "CPS Lab 5%" : 10
    "Forensics 4%" : 8
    "IoT Lab 3%" : 5
    "Vulnerable 2%" : 3
    "Displays 2%" : 4' \
    "kroki-hardware-pie.png"

# 7. Lab Capacity Flowchart
convert_kroki 'graph TB
    A[Total Lab Capacity<br/>120+ Concurrent Users]
    A --> B[Network Security Lab<br/>20 students<br/>500 sq.ft]
    A --> C[Penetration Testing<br/>15 students<br/>500 sq.ft]
    A --> D[Digital Forensics<br/>12 students<br/>400 sq.ft]
    A --> E[AI/ML Security<br/>15 students<br/>400 sq.ft]
    A --> F[IoT Security<br/>12 students<br/>350 sq.ft]
    A --> G[CPS/ICS Security<br/>10 students<br/>450 sq.ft]
    A --> H[Malware Analysis<br/>8 students<br/>300 sq.ft]
    A --> I[SOC Training<br/>8 analysts<br/>600 sq.ft]
    
    style A fill:#ff6b6b,color:#fff
    style B fill:#51cf66
    style C fill:#51cf66
    style D fill:#51cf66
    style E fill:#4ecdc4
    style F fill:#4ecdc4
    style G fill:#ffd43b
    style H fill:#ffd43b
    style I fill:#748ffc' \
    "kroki-lab-capacity.png"

# 8. Impact Metrics Graph
convert_kroki 'graph LR
    A[3-Year Impact]
    A --> B[1500+ Students Trained]
    A --> C[50+ Research Papers]
    A --> D[100+ Industry Partnerships]
    A --> E[500+ Certifications]
    A --> F[Rs 2 Cr+ External Funding]
    A --> G[3+ Patents Filed]
    
    style A fill:#ff6b6b,color:#fff
    style B fill:#51cf66
    style C fill:#4ecdc4
    style D fill:#ffd43b
    style E fill:#ff8787
    style F fill:#a29bfe
    style G fill:#fab1a0' \
    "kroki-impact-metrics.png"

# 9. Year-wise Budget Flow
convert_kroki 'graph TD
    A[Total Budget<br/>Rs 4 Crores<br/>36 Months]
    A --> B[Year 1<br/>Rs 2.04 Crores]
    A --> C[Year 2<br/>Rs 96 Lakhs]
    A --> D[Year 3<br/>Rs 1 Crore]
    
    B --> B1[Infrastructure Rs 1.4Cr]
    B --> B2[Personnel Rs 36L]
    B --> B3[Software Rs 20L]
    B --> B4[Other Rs 8L]
    
    C --> C1[Infrastructure Rs 25L]
    C --> C2[Personnel Rs 36L]
    C --> C3[Software Rs 15L]
    C --> C4[Other Rs 20L]
    
    D --> D1[Infrastructure Rs 20L]
    D --> D2[Personnel Rs 36L]
    D --> D3[Software Rs 10L]
    D --> D4[Other Rs 34L]
    
    style A fill:#ff6b6b,color:#fff
    style B fill:#51cf66
    style C fill:#4ecdc4
    style D fill:#ffd43b' \
    "kroki-yearwise-budget.png"

echo ""
echo "==========================================="
echo "Conversion Complete!"
echo "==========================================="
echo ""
echo "Generated Kroki diagrams:"
ls -lh kroki-*.png 2>/dev/null | awk '{print "  " $9 " - " $5}'
echo ""
echo "Total diagrams: $(ls kroki-*.png 2>/dev/null | wc -l)"
