---
share_link: https://share.note.sx/e5gjucvj#i0O75yKbXMNDsgA/MUVv7VImIQ9mZ2Nr9pwKccCsNVQ
share_updated: 2025-05-14T00:56:51+05:30
---

# AWS Elastic Beanstalk (EB) Lab Report

> [!note] Student Details
> - **Name:** Rohan Prakash Pawar
>- **UID:** 2023201020
>- **Branch:** EXTC
>- **Date:** May 13, 2025

## 1. Objective

This lab aims to:
- Understand the core functionalities and features of AWS Elastic Beanstalk
- Deploy a Python Flask application to the AWS cloud using Elastic Beanstalk
- Explore the automated infrastructure provisioning capabilities of Elastic Beanstalk
- Analyze the configuration, deployment, and management aspects of Elastic Beanstalk
- Evaluate the cost-effectiveness and use cases for Elastic Beanstalk in cloud application hosting

## 2. Theoretical Background

### What is AWS Elastic Beanstalk?

AWS Elastic Beanstalk is a fully managed service that makes it easy to deploy, run, and scale applications in multiple languages using familiar application servers such as Apache, Nginx, and IIS. As a Platform as a Service (PaaS) offering, Elastic Beanstalk abstracts away the infrastructure details so developers can focus on writing code.

> [!tip] Key Elastic Beanstalk Characteristics
> - **Automated Infrastructure**: Automatically handles capacity provisioning, load balancing, scaling, and application health monitoring
> - **Developer Focus**: Allows developers to focus on writing code rather than managing infrastructure
> - **Platform Flexibility**: Supports various programming languages and application servers
> - **Full AWS Integration**: Easy integration with other AWS services like RDS, S3, and CloudWatch
> - **Customizable Environment**: Provides configuration options to tailor the underlying infrastructure

### Elastic Beanstalk Components

| Component | Description | Function |
|-----------|-------------|----------|
| Application | Logical collection of Elastic Beanstalk components | Organizes environments running different versions of your application |
| Application Version | Specific labeled iteration of deployable code | Allows tracking and deployment of different code versions |
| Environment | Collection of AWS resources running an application version | The actual runtime instance of your application |
| Environment Tier | Designates environment type (Web or Worker) | Determines how the application handles requests |
| Environment Configuration | Parameter settings that define environment behavior | Controls how resources behave and scale |

## 3. Requirements

To complete this lab, you will need:

- AWS account with sufficient permissions
- AWS CLI installed and configured
- EB CLI (Elastic Beanstalk Command Line Interface) installed
- Python 3.11 installed
- Git client for source code management
- A Flask application (our sample application from GitHub)

## 4. Procedure

### 4.1 Preparing the Flask Application

Our lab uses a Python Flask application as shown in the screenshot below:

![[Pasted image 20250513232704.png]]

When run locally, this is the output:

![[Pasted image 20250513232812.png]]

The project can be found at https://www.github.com/r04nx/loraid/webserver

The application has the following structure:
```
├── app.py
├── data.db
├── requirements.txt
├── setup_db.py
├── static
│   ├── script.js
│   └── style.css
├── templates
│   └── index.html
├── transmissions1.csv
├── transmissions.csv
└── transmissions_test_2.csv

3 directories, 10 files
```

### 4.2 Deploying with Elastic Beanstalk

First, verify that EB CLI is installed:

![[Pasted image 20250513233053.png]]

Initialize the Elastic Beanstalk application:
```bash
eb init -p python-3.11 loraid-connect
```

![[Pasted image 20250513233145.png]]

Create an Elastic Beanstalk environment:
```bash
eb create loraid-env 
```

![[Pasted image 20250513233426.png]]

> [!important]
> AWS Elastic Beanstalk requires the main application file to be named `application.py`. We renamed our `app.py` to `application.py` for compatibility.

### 4.3 Deployment and Testing

After deploying with `eb deploy`, the application was successfully deployed:

![[Pasted image 20250513235758.png]]

Checking the status with `eb status` shows the environment is ready:

![[Pasted image 20250513235643.png]] 

Opening the application with `eb open` displays the running application in the browser:

![[Pasted image 20250514000032.png]]

Testing the API with a curl request:

![[Pasted image 20250514000114.png]]

The data is successfully submitted via the API and reflected in the frontend:

![[Pasted image 20250514000158.png]]

### 4.4 Examining the Elastic Beanstalk Configuration

To investigate the configuration of our deployed application environment, we run:
```bash
eb config
```

![[Pasted image 20250514004729.png]]

## 5. Observations

From our deployment and configuration analysis, we observed:

1. **Automated Provisioning**: Elastic Beanstalk automatically provisioned all necessary resources, including EC2 instances, load balancers, and security groups.

2. **Simplified Deployment**: The `eb deploy` command handled packaging, uploading, and deployment of the application, eliminating manual steps.

3. **Environment Health Monitoring**: Elastic Beanstalk continuously monitors the health of the application and reports status (green/yellow/red).

4. **Configuration Management**: The platform handled configuration details such as port mappings, process management, and dependency installation.

5. **Integration with AWS Services**: The environment seamlessly integrated with other AWS services like CloudWatch for logging and monitoring.

## 6. Use Cases of AWS Elastic Beanstalk

AWS Elastic Beanstalk is ideal for a variety of scenarios:

1. **Web Applications**: Perfect for hosting web applications and APIs built with frameworks like Flask, Django, Spring Boot, or Express.js.

2. **Microservices Architecture**: Simplifies deployment and management of individual microservices in a larger system.

3. **Startups and MVPs**: Enables rapid deployment of minimum viable products with minimal infrastructure knowledge.

4. **Development and Test Environments**: Quick provisioning of development, testing, and staging environments with identical configurations.

5. **Small to Medium Business Applications**: Cost-effective hosting solution for business applications without dedicated DevOps resources.

6. **Education and Training**: Ideal platform for learning cloud deployment without the complexity of manual infrastructure setup.

## 7. Benefits of AWS Elastic Beanstalk

> [!success] Key Benefits
> - **Developer Productivity**: Reduces time spent on infrastructure management
> - **No Additional Charges**: Pay only for the underlying AWS resources
> - **Platform Variety**: Supports multiple programming languages and frameworks
> - **Application Versioning**: Easy deployment and rollback between different application versions
> - **Environment Cloning**: Quick duplication of environments for testing or scaling
> - **Customization Options**: Flexible configuration to meet specific application requirements
> - **Managed Platform Updates**: Simplified patching and updates of the platform components

## 8. Financial Aspects

### Cost Components of Elastic Beanstalk

1. **Compute Resources**: EC2 instances used to run your application
2. **Load Balancing**: Elastic Load Balancing charges if enabled
3. **Storage**: S3 storage for application versions and logs
4. **Data Transfer**: Network data transfer in and out of the application
5. **Database**: Optional RDS instances if your application uses a database

### Sample Monthly Cost Estimation

| Resource | Configuration | Monthly Cost (US East) |
|----------|---------------|------------------------|
| EC2 Instances | 1 t3.small instance | ~$15.50 |
| Load Balancer | Application Load Balancer | ~$16.20 |
| S3 Storage | 5 GB for versions and logs | ~$0.12 |
| CloudWatch | Basic monitoring | ~$0.00 (Free Tier) |
| Data Transfer | 100 GB outbound | ~$9.00 |

> [!tip] Cost Optimization
> - Use the right instance type for your workload
> - Configure auto-scaling to adjust capacity based on demand
> - Implement environment time-based scaling for non-production environments
> - Consider reserved instances for production environments
> - Delete unused application versions and environments

## 9. Conclusion

AWS Elastic Beanstalk provides a powerful yet simple platform for deploying and scaling web applications in the AWS cloud. Our lab demonstrated how quickly a Flask application can be deployed without having to manually manage the underlying infrastructure.

Key takeaways:
- Elastic Beanstalk abstracts away infrastructure complexities so developers can focus on code
- The service integrates with key AWS services while managing their configuration
- Application deployment and scaling become straightforward operations
- Environment management tools provide visibility and control over application health

For teams looking to reduce operational overhead while maintaining control over their applications, AWS Elastic Beanstalk offers an excellent balance between convenience and flexibility.

---

> [!quote] 
> "AWS Elastic Beanstalk is like having a DevOps engineer built into your deployment pipeline - it handles the infrastructure details so you can focus on building great applications."
