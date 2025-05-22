---
share_link: https://share.note.sx/37x3rhs6#p2+oQaLN3aEqUwj+b+rJ0OjqYagwGFWhUx4aXpyH/ug
share_updated: 2025-05-22T16:37:56+05:30
---
# AWS Site-to-Site VPN Lab 7

> [!note] Student Details
> - **Name:** Rohan Prakash Pawar
> - **UID:** 2023201020
> - **Branch:** EXTC
> - **Date:** May 13, 2025

## Objective/AIM

> [!abstract] Objective
> To establish a Site-to-Site VPN connection between an on-premises application and a database hosted in AWS cloud using AWS Client VPN service, demonstrating secure communication between distributed components of an application.

## Requirements

> [!info] Requirements
> - AWS Account with appropriate permissions
> - Wireguard for client VPN setup
> - AWS Client VPN service
> - EC2 instance for hosting the database
> - Flask-based web application (Notu)
> - PostgreSQL database
> - Basic understanding of networking concepts (VPC, subnets, routing)

## Procedure

### 1. Setup Overview

For this lab, we will use:  
- Wireguard for setting up a Client VPN  
- AWS Client VPN fully managed VPN service provided by AWS  
- Our use case: On-premises application (Notu) will connect to the PostgreSQL database on AWS cloud via Client VPN

### 2. Application Overview

To simulate the on-premises application, we will use Notu - a note-taking app developed in Python Flask which will connect to a PostgreSQL database running in AWS cloud on EC2. We will establish a VPN connection between these microservices.

The following are some screenshots of the application:
![[Pasted image 20250522161728.png]]

And this is the database running:
![[Pasted image 20250522161849.png]]

### 3. VPC Setup

First, let's check if there are any available VPCs in our AWS account.
There are none as shown in the following screenshot when running the command:
```bash
aws ec2 describe-vpcs
```
![[Pasted image 20250519040920.png]]

Now creating a VPC with the following command:
![[Pasted image 20250519041303.png]]

Creating a subnet in the availability zone ap-south-1a:
![[Pasted image 20250519041354.png]]

Creating an Internet Gateway:
![[Pasted image 20250519041425.png]]

Attaching the internet gateway to the newly created VPC:
![[Pasted image 20250519041512.png]]

Checking the default routing table for this setup:
![[Pasted image 20250519041601.png]]

Creating a route to the internet gateway:
![[Pasted image 20250519041733.png]]

Ensuring the subnet is associated with our routing table:
![[Pasted image 20250519041848.png]]

### 4. Security Group Configuration

Creating a Security Group for the VPN:
![[Pasted image 20250519041932.png]]

Configuring rules for the security group to allow ingress traffic:
![[Pasted image 20250519042028.png]]

Creating the security group for the VPN endpoints:
![[Pasted image 20250519042336.png]]

Configuring this security group to allow only SSH (port 22) traffic:
![[Pasted image 20250519042611.png]]

### 5. EC2 Instance Setup

Modifying the subnet to assign public IPs on launch:
![[Pasted image 20250519042715.png]]

Creating an EC2 instance with Amazon Linux AMI, using existing key pairs in the subnet and VPC we created previously, and associating it with the security group:
![[Pasted image 20250519042802.png]]

Verifying the instance creation with describe-instances command:
![[Pasted image 20250519042930.png]]

> [!success] Progress Summary
> At this point, we have successfully completed the following steps:
> 1. Created a VPC with CIDR block 10.0.0.0/16
> 2. Created a subnet with CIDR 10.0.1.0/24 in the ap-south-1a availability zone
> 3. Created and attached an Internet Gateway to the VPC
> 4. Updated the route table to allow internet access
> 5. Created security groups for the instance
> 6. Generated an SSH key pair (saved as my-vpc-key.pem in your current directory)
7. Launched an Amazon Linux 2 t2.micro instance in the subnet

> [!example] EC2 Instance Details
> - Instance ID: i-02c4ca057df492d7c
> - Public IP: 13.126.132.2
> - Private IP: 10.0.1.28
> 
> SSH Connection Command:
> ```bash
> ssh -i my-vpc-key.pem ec2-user@13.126.132.2
> ```

### 6. VPN Certificate Generation

Cloning the repository for generating certificates and keys required for the client VPN setup in AWS:
![[Pasted image 20250519045555.png]]

Running the following commands to generate certificates:  
![[Pasted image 20250519045628.png]]
![[Pasted image 20250519045657.png]]

![[Pasted image 20250519045723.png]]

Responding with 'yes' where necessary during certificate generation:
![[Pasted image 20250519045759.png]]

Creating a directory to store all credential-related files:

Copying all important files to that directory:
![[Pasted image 20250519045915.png]]

Running the final configuration command:
![[Pasted image 20250519045938.png]]

### 7. VPN Connection Establishment

After this setup, we enabled the VPN connection in the operating system and connected with the VPC in AWS availability zone. This allowed us to have access to the private network of the AWS environment.

### 8. Application Deployment

Cloning the application codebase from GitHub:

```bash
git clone https://github.com/r04nx/notu.git
cd notu
```

Creating a virtual environment and activating it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Installing the dependencies:

```bash
pip install -r requirements.txt
```

Setting up the PostgreSQL database:
- Creating a new PostgreSQL database named `notu_db`
- Updating the `.env` file with database credentials

Initializing the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

Creating an admin user (optional):
```bash
python create_admin.py
```

### 9. Application Configuration

Creating a `.env` file from the provided example:
```bash
cp .env.example app/.env
```

Editing the `.env` file with specific configuration:
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=your_secret_key_here
DATABASE_URL=postgresql://username:password@localhost:5432/notu_db
UNSPLASH_ACCESS_KEY=your_unsplash_access_key_here
TINYMCE_API_KEY=your_tinymce_api_key_here
```

> [!tip] Configuration Notes
> - Replace `your_secret_key_here` with a secure random string
> - Update the database URL with your PostgreSQL credentials
> - (Optional) Add your Unsplash API key to enable dynamic background images
- (Optional) Add your TinyMCE API key for enhanced editor features

### 10. VPN Connection Testing

Configuring the database connection to use the local private IP of the VM running locally, making the application connect to the local database via VPN:
Editing the `.env` file with nano and using the same address and port which was used for the local setup:
![[Pasted image 20250522162526.png]]

## Observation

> [!important] Key Observations
> - The application successfully connected to the database over the VPN connection
> - Network latency was minimal and did not affect application performance
> - Security groups effectively controlled traffic flow between the application and database
> - The VPN connection remained stable throughout the testing period

As shown in the screenshot below, the application is working without failure because it is able to communicate with the local database server which is on the on-premises server via the VPN connection:
![[Pasted image 20250522162854.png]]

## Conclusion

> [!success] Conclusion
> In this lab, we successfully established a Site-to-Site VPN connection between an on-premises application and a cloud-hosted database using AWS Client VPN service. The key accomplishments include:
> 
> 1. Successfully created and configured a VPC with proper networking components (subnets, internet gateway, routing tables)
> 2. Implemented appropriate security groups to control traffic flow
> 3. Generated and configured VPN certificates for secure communication
> 4. Deployed the application and configured it to connect to the database over VPN
> 5. Verified the secure connection by testing the application functionality
> 
> This lab demonstrates how AWS VPN services can be used to securely connect distributed application components across different network environments, enabling hybrid cloud architectures while maintaining security and performance.
