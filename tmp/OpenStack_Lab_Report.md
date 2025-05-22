---
share_link: https://share.note.sx/4c6fud6k#zWxogME5DRPD2j96LqkomDIxy6kc1MapCOCXPfzdVn8
share_updated: 2025-05-13T20:56:39+05:30
---
# OpenStack Installation and VM Creation Lab Report

## Student Details
- **Name:** Rohan Prakash Pawar
- **UID:** 2023201020
- **Branch:** EXTC
- **Date:** May 13, 2025

## Objectives
- Setup and configure OpenStack using DevStack
- Access the OpenStack dashboard
- Import a cloud image
- Create a virtual machine instance

## Requirements
- Virtual Machine environment
- Internet connection
- Ubuntu OS
- DevStack repository access
- Sufficient system resources to run OpenStack

## Procedure

### 1. Setting up DevStack

1. Clone the DevStack repository
   
   ![[Pasted image 20250507010154.png]]

2. Navigate to the DevStack directory and configure the local.conf file
   
   ![[Pasted image 20250507010317.png]]

3. Set the required parameters in local.conf:
   ```
   ADMIN_PASSWORD=secret
   DATABASE_PASSWORD=SADMIN_PASSWORD
   RABBIT_PASSWORD=SADMIN_PASSWORD
   SERVICE_PASSWORD=S$ADMIN_PASSWORD
   HOST_IP=10.0.2.15
   ```
   
   ![[Pasted image 20250507010424.png]]

4. Execute the stack.sh script to start the installation
   
   ![[Pasted image 20250507010650.png]]

### 2. Accessing the OpenStack Dashboard

1. After successful installation (approximately 20 minutes), the dashboard URL is provided
   
   ![[Pasted image 20250507010844.png]]

2. Open the URL in a web browser to access the authentication page
   
   ![[Pasted image 20250507011003.png]]

3. Login to access the OpenStack dashboard
   
   ![[Pasted image 20250507011053.png]]

### 3. Exploring OpenStack Resources

1. View the instances section to manage virtual machines
   
   ![[Pasted image 20250507011141.png]]

2. Examine the default network topology created by OpenStack
   
   ![[Pasted image 20250507011219.png]]

### 4. Creating a Virtual Machine

1. Download an Ubuntu cloud image using wget
   
   ![[Pasted image 20250507011423.png]]

2. Import the downloaded image into OpenStack with the name 'demo'
   
   ![[Pasted image 20250507011623.png]]

3. Create a new instance by clicking 'Launch Instance'
   
   ![[Pasted image 20250507011810.png]]

4. Fill in the necessary information and proceed to the next step
   
   ![[Pasted image 20250507011904.png]]

5. Select the boot source and configure the volume size
   
   ![[Pasted image 20250507011946.png]]

6. Choose an appropriate instance type (flavor) such as m1.nano, m1.micro, or m1.tiny
   
   ![[Pasted image 20250507012019.png]]

## Observations

1. The DevStack installation process took approximately 20 minutes to complete.
2. After successful installation, the OpenStack dashboard was accessible through the web browser.
3. The default network topology was automatically created by OpenStack.
4. Ubuntu cloud image was successfully imported into OpenStack.
5. The instance creation process involved multiple steps: providing instance details, selecting boot source, configuring storage, and choosing instance type.

## Conclusion

In this lab, I successfully set up OpenStack using DevStack on a virtual machine. The installation process was straightforward, following the standard procedures. After configuration, I was able to access the OpenStack dashboard and explore various features like instance management and network topology.

I successfully imported an Ubuntu cloud image and initiated the process of creating a virtual machine from this image. This lab demonstrates the capability of OpenStack as a cloud platform for managing virtual infrastructure resources. The knowledge gained from this lab will be useful for future cloud computing projects and understanding Infrastructure as a Service (IaaS) platforms.

The OpenStack dashboard provides an intuitive interface for managing cloud resources, making it accessible for users without extensive command-line knowledge. Overall, this lab provided practical experience in cloud infrastructure setup and management using OpenStack.
