---
share_link: https://share.note.sx/gz35qv2m#ffg97s3iFqD+u27j3MytR5P0rxOr5f1LlKR6BvrpKJ8
share_updated: 2025-04-18T23:57:10+05:30
---
# AWS Setup and Free Tier Exploration

## Laboratory Practical Report

**Student Name:** Rohan Pawar  
**UID:** 2023201020  
**Batch:** C  
**Branch:** EXTC  
**Course:** Cloud Computing  

---

## Aim

To set up an AWS account and explore the AWS Free Tier services to understand the fundamentals of cloud computing infrastructure.

## Introduction

Amazon Web Services (AWS) is one of the world's most comprehensive and broadly adopted cloud platforms, offering over 200 fully featured services from data centers globally. This practical lab focuses on creating an AWS account and exploring the Free Tier services, which allows new users to gain hands-on experience with various cloud services without incurring significant costs. 

Understanding cloud platforms like AWS is essential for modern computing professionals as organizations increasingly migrate their infrastructure to the cloud. The AWS Free Tier provides an excellent opportunity for learning cloud concepts, practicing deployment, and understanding the management of cloud resources.

## Materials Required

- Computer with internet access
- Web browser (Chrome, Firefox, or Edge recommended)
- Valid email address
- Mobile phone for verification
- Credit/debit card for account verification (no charges unless exceeding Free Tier limits)
- Personal identification information

## Procedure

### Step 1: Accessing the AWS Homepage

I navigated to AWS's official website (https://aws.amazon.com/) and clicked on the "Create an AWS Account" button located at the top right corner of the page.

![](https://miro.medium.com/v2/resize:fit:764/0*FCM2mZstYilqUMmo)

### Step 2: Creating the AWS Account

I filled in the required information, including my email address, password, and AWS account name, then clicked "Continue" to proceed with the account creation process.

![](https://miro.medium.com/v2/resize:fit:764/1*1S7TUxYryiHwqcOUY7cdog.png)

### Step 3: Providing Contact Information

I entered my contact information as required and agreed to the AWS Customer Agreement. Then I clicked on "Create Account and Continue" to proceed to the next step.

![](https://miro.medium.com/v2/resize:fit:764/1*ERt-JNgEST2DhiDi4uVB5g.png)

![](https://miro.medium.com/v2/resize:fit:564/1*j_crNKTPRtBoSh4-Vd1nAQ.png)

![](https://miro.medium.com/v2/resize:fit:764/1*inehB9aqfP8-p0PcrGsArw.png)

![](https://miro.medium.com/v2/resize:fit:600/1*J15no7kGhDwnQ0fueOZZUg.png)

### Step 4: Adding Payment Information

I entered my credit card details for verification purposes. AWS requires this to verify identity and prevent misuse of the Free Tier. As informed, no charges would be applied unless services beyond the Free Tier limits are used.

![](https://miro.medium.com/v2/resize:fit:454/0*NhtIrKsRyK6GxxtO.png)

### Step 5: Completing Phone Verification

I entered my phone number to receive a verification code. Once I received the code, I input it into the field provided and clicked on "Verify code and continue" to proceed.

![](https://miro.medium.com/v2/resize:fit:600/0*9tqVKREzM0az-2YQ.png)

### Step 6: Selecting a Support Plan

I selected the free "Basic" support plan which is sufficient for experimenting with the Free Tier services.

![](https://miro.medium.com/v2/resize:fit:635/0*2SJshSyi5hpU0xHZ.png)

### Step 7: Accessing the AWS Management Console

After completing all the required steps, I successfully created my AWS account. I was then able to sign in to the AWS Management Console to begin exploring the Free Tier services.

![](https://miro.medium.com/v2/resize:fit:764/0*PbY-H6kDgTHiKNF-.png)

### Step 8: EC2 Instance Creation and SSH Access

After accessing the AWS Management Console, I proceeded to launch and connect to an EC2 instance to gain hands-on experience with cloud computing resources.

#### Navigating to EC2 Service

I navigated to the EC2 service by clicking on "Services" in the top navigation bar and selecting "EC2" under the Compute category. This took me to the EC2 Dashboard where I could manage virtual servers in the cloud.

![[Pasted image 20250302010217.png]]

#### Launching an EC2 Instance

I clicked on the "Launch Instance" button to begin the process of creating a new virtual server. This opened the instance creation wizard with various configuration options.

![[Pasted image 20250302010239.png]]


#### Selecting an Amazon Machine Image (AMI)

From the available options, I selected "Ubuntu Server 22.04 LTS (HVM)" as my operating system, which is a popular Linux distribution that offers good stability and support.

![[Pasted image 20250302010422.png]]



#### Choosing Instance Type

I selected the t2.micro instance type, which is eligible for the AWS Free Tier. This instance type provides 1 vCPU and 1 GiB of memory, sufficient for basic testing and learning purposes.

![[Pasted image 20250302010355.png]]

#### Configuring Instance Details

I kept the default settings for the instance details, which included:
- Number of instances: 1
- Network: Default VPC
- Subnet: Default subnet
- Auto-assign Public IP: Enable


#### Configuring Security Group

I created a new security group with the following rules:
- SSH (port 22): Source set to "My IP" to allow secure shell access only from my current IP address
- HTTP (port 80): Source set to "Anywhere" to allow web traffic if needed

This configuration ensured that my instance would be accessible via SSH while maintaining basic security practices.

![[Pasted image 20250302010707.png]]

#### Creating and Downloading Key Pair

I created a new key pair named "ubuntu-key" and downloaded the .pem file to my local computer. I understood that this key pair is essential for secure SSH access to the instance and should be kept in a safe location.
![[Pasted image 20250302010647.png]]

#### Launching the Instance

After reviewing all configurations, I clicked "Launch" to create the EC2 instance. I waited for approximately 2 minutes while AWS provisioned the virtual server.

![[Pasted image 20250302010514.png]]

![[Pasted image 20250302010736.png]]
#### Connecting to the Instance via SSH

Once the instance was running, I prepared to connect to it using SSH:

1. I changed the permissions of my key pair file to make it secure:
```bash
chmod 400 ubuntu-key.pem
```

![[Pasted image 20250302010829.png]]
1. I connected to the instance using the SSH command 


2. I confirmed the connection when prompted and successfully accessed the Ubuntu server command line.

![[Pasted image 20250302010905.png]]


## Observations

During the AWS account setup process, I observed the following:

1. **Security Measures**: AWS implements multiple security measures including email verification, phone verification, and payment information verification to ensure the authenticity of users.

2. **User-Friendly Interface**: The account creation process was straightforward with clear instructions at each step.

3. **Free Tier Information**: AWS prominently displays information about the Free Tier limits to ensure users are aware of the available resources.

4. **Service Organization**: The AWS Management Console organizes services by categories, making it easier to navigate through the vast array of available services.

5. **AWS Free Tier Limits** that I noted include:
   - 750 hours of Amazon EC2 Cloud computing capability per month
   - 5 GB of standard storage on Amazon S3
   - 750 hours of Amazon RDS database usage monthly (for SQL Server, MariaDB, PostgreSQL, and MySQL)
   - 5 GB of Amazon EFS storage
   - 30 GB of General Purpose (SSD) or Magnetic Elastic Block Storage from Amazon Elastic Store

## Results

After successfully setting up my AWS account, I explored several key services available within the Free Tier:

1. **Amazon EC2**: I examined the virtual server options, understanding how to launch instances that can be used for computing in the cloud.

2. **Amazon S3**: I explored the storage service, learning how data can be stored and retrieved from anywhere at any time.

3. **AWS Lambda**: I investigated serverless computing options, understanding how code can be run without provisioning or managing servers.

Through this exploration, I gained practical knowledge of the AWS environment and understood how these services can be leveraged for various cloud computing applications.

## Conclusion

This lab practical provided valuable hands-on experience with AWS account setup and exploration of Free Tier services. By successfully creating an AWS account and navigating through the Management Console, I have gained fundamental knowledge about cloud service providers and their offerings.

The AWS Free Tier serves as an excellent platform for learning cloud computing concepts without financial commitment. Understanding these services is crucial for developing skills in cloud architecture, deployment, and management – all essential competencies in today's technology landscape.

The practical knowledge gained through this lab will be fundamental in understanding more complex cloud computing concepts as the course progresses. It will serve as the foundation for future labs involving actual deployment and management of cloud resources.

This practical reinforced the theoretical concepts of cloud service models (IaaS, PaaS, SaaS) discussed in lectures, providing a tangible demonstration of how these services are implemented in real-world cloud environments.
