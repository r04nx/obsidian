---
marp: true
theme: default
paginate: true
backgroundColor: white
---

# AWS Cloud Training 2025
## Banking & Financial Services Edition
![width:300px](aws_logo.png)

Dr. Dayanand Ambawade
March 19-20, 2025

---

# Training Overview

- **Duration**: 2 Days
- **Focus**: Banking Sector Implementation
- **Approach**: Hands-on Learning
- **Modules**: 7 Comprehensive Sections

---

# Day 1 Schedule | March 19, 2025

| Time | Module |
|------|--------|
| 9:30 - 11:00 | AWS Basics |
| 11:15 - 1:15 | AWS EC2 |
| 2:15 - 4:15 | AWS VPC |
| 4:30 - 6:30 | Amazon S3 |

---

# Day 2 Schedule | March 20, 2025

| Time | Module |
|------|--------|
| 9:30 - 11:00 | Cost Management |
| 11:15 - 1:15 | AWS DevOps Part-1 |
| 2:15 - 5:30 | AWS DevOps Part-2 |

---

# Module 3.1: AWS Basics

![bg right:40% 80%](aws_services.png)

- AWS Account Management
- Resource Groups
- IP Management
- AWS KMS

---

# AWS Account Structure

```mermaid
graph TD
    A[Root Account] --> B[IAM Users]
    A --> C[Organizations]
    C --> D[Resource Groups]
    B --> E[Permissions]
    E --> F[Policies]
```

---

# IP Management in AWS

- CIDR Notation
- Public vs Private IPs
- Elastic IP Configuration
- IP Range Planning

![bg right:40% 80%](networking.png)

---

# Module 3.2: EC2 Implementation

![bg right:40% 80%](ec2_types.png)

- Instance Types
- AMI Selection
- Storage Options
- Auto Scaling

---

# EC2 Architecture

```mermaid
graph LR
    A[Load Balancer] --> B[EC2 Instance 1]
    A --> C[EC2 Instance 2]
    B --> D[EBS Volume]
    C --> E[EBS Volume]
```

---

# Module 3.3: VPC Design

![bg right:40% 80%](vpc_diagram.png)

- VPC Components
- Subnet Planning
- Security Groups
- Network ACLs

---

# VPC Security Layers

```mermaid
graph TD
    A[Internet Gateway] --> B[NACL]
    B --> C[Security Group]
    C --> D[EC2 Instance]
```

---

# Module 3.4: S3 Storage

![bg right:40% 80%](s3_classes.png)

- Storage Classes
- Bucket Policies
- Encryption Options
- Lifecycle Rules

---

# S3 Storage Classes

```mermaid
graph TD
    A[S3 Standard] --> B[S3 IA]
    A --> C[S3 One Zone]
    A --> D[Glacier]
    D --> E[Deep Archive]
```

---

# Module 4.1: Cost Management

![bg right:40% 80%](cost_management.png)

- Budgets
- Cost Explorer
- CloudWatch
- Alerts

---

# Cost Optimization

```mermaid
graph TD
    A[Cost Management] --> B[Budgets]
    A --> C[Alerts]
    A --> D[Reports]
    D --> E[Analysis]
```

---

# Module 4.2: ECR & Containers

![bg right:40% 80%](container_workflow.png)

- Container Basics
- ECR Setup
- Image Management
- Security

---

# Container Workflow

```mermaid
graph LR
    A[Development] --> B[Build]
    B --> C[Push to ECR]
    C --> D[Deploy]
    D --> E[Monitor]
```

---

# Module 4.3: CI/CD Pipeline

![bg right:40% 80%](cicd_pipeline.png)

- CodeCommit
- CodeBuild
- CodeDeploy
- CodePipeline

---

# CI/CD Architecture

```mermaid
graph LR
    A[Source] --> B[Build]
    B --> C[Test]
    C --> D[Deploy]
    D --> E[Monitor]
```

---

# Hands-on Labs Overview

1. AWS Console Navigation
2. Resource Group Creation
3. EC2 Management
4. VPC Setup
5. S3 Configuration
6. Cost Management
7. Container Registry
8. Pipeline Setup

---

# Best Practices & Guidelines

- 🔒 Security First
- 💰 Cost Optimization
- 🔄 Automation
- 📊 Monitoring
- 🔍 Compliance

---

# Thank You!

## Contact Information
- Email: instructor@example.com
- AWS Training Portal: aws.training
- Support: Available 24/7

![bg right:40% 80%](thank_you.png)

