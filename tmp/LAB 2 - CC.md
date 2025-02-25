---
share_link: https://share.note.sx/6msh48im#vtej+Fh+8W4KPvH/cd6HCvk4gDym1WUNxw4x+o8FM9Q
share_updated: 2025-02-25T18:57:27+05:30
---
# Lab 1A: Creating and Running Virtual Machines on Hosted Hypervisors

## Student Details
- **Name:** Rohan Prakash Pawar
- **UID:** 2023201020
- **Branch:** EXTC

## Objective
To create and run virtual machines on hosted hypervisors such as KVM, VMware Workstation, and Oracle VirtualBox.

## Lab Outcomes
1. Install, configure and use hosted hypervisors
2. Deploy and manage virtual machines
3. Configure virtual machine settings
4. Evaluate the performance of virtual machines on hosted hypervisors

## System Requirements
- Host machine with sufficient resources (minimum 8GB RAM recommended)
- Installed hypervisors: Oracle VirtualBox
- ISO images of operating systems (CentOS/AlmaLinux and Ubuntu Server)
- At least 20GB free disk space for VMs

## Introduction
VMware and VirtualBox are powerful virtualization software that allow users to create and run multiple virtual machines on a single physical machine. This lab demonstrates the process of creating and configuring virtual machines using Oracle VirtualBox.

### Linux Distributions Overview

1. Ubuntu Arch

2. CentOS

3. Mint Linux

4. Arch Linux

5. Peppermint

6. Pop OS

A Linux distribution (distro) is an open source operating system that is packages with other components, such as an installation programs, management tools and additional software

ok let’s get started!

**How to create a Virtual Machine**

Creating a VMware is a very easy process.

I will be creating two VMware, one using CentOS and the other one with Ubuntu. I will first use the search bar to look for Oracle VM VirtualBox Manager and click on it

![](https://miro.medium.com/v2/resize:fit:764/1*oHwYWDfIM2ZqcUF-3QP-Eg.png)

The next step is to name it, which i choose to simply call it centOsvm .I will now go down to where it say type to choose the operating system that I want to install your virtual system. I selected Linux and Red Hat (64-Bit) for version.

![](https://miro.medium.com/v2/resize:fit:764/1*unV7mmdMd8wK153WlwpVgA.png)

Next steps

I will make sure that the base memory is a 2048 Mb and the Processors is at 1cpu then click next

![](https://miro.medium.com/v2/resize:fit:764/1*S8dAoUc7FESiFljytGBjEA.png)

![](https://miro.medium.com/v2/resize:fit:764/1*GLeKBOPmWWhBVaxAP9JB-Q.png)

I will then read over the summary and make sure everything is correct then click on finish.

And it should look like that now that I have completed all the steps

![](https://miro.medium.com/v2/resize:fit:764/1*MWwWlvyq_DjCy-Tf8G1j5Q.png)

I will now create one more with Ubuntu

![](https://miro.medium.com/v2/resize:fit:764/1*p8-jdOartRly73ksgLCnbQ.png)

the process is similar, I will follow the same steps as the previous one created. The only change that I will be changing the processor to 2 CPU. Go over the summary and click on finish and it should look like that.

![](https://miro.medium.com/v2/resize:fit:764/1*XtX2L2G5XWGjCPMlBaknHw.png)

Now I will install an operating system for the two VMware I created

For the first VMware, in order to install an operating system, I will first need to go on google and search for **_almalinux 9 iso._** I selected the second one, then select **_almaLinux-9.2-x89_64-boot.iso_** and download it. It will take a few minutes to download .

![](https://miro.medium.com/v2/resize:fit:764/1*SS9EwdlOtDci-i2ozqzn3A.png)

![](https://miro.medium.com/v2/resize:fit:764/1*T0NSTgG-m2K-GwuttcIYvg.png)

once it is completed, I will then follow these steps:

Open the Oracle VM VirtualBox Manager

Go on settings,

Go on storage,

Click on the disk symbol and click on the drop down

Click on “choose a disk file”. There I will see the iso file that I recently downloaded, I selected it then click on open

Go on network, click on Adapter 2, then **_Enable Network Adapter_**, and in the **“_Attached to_**_:_” section, select Bridged Adapter.

Once that is done, click on ok, the power on the Vm and that will start the installation.

![](https://miro.medium.com/v2/resize:fit:764/1*lBSfFU5Jl2-A8cYyKamEag.png)

The next step is to select the language then click continue

![](https://miro.medium.com/v2/resize:fit:764/1*Gg2uvNUk5378krIME8shfQ.png)

this window should appear next then click on installation destination

![](https://miro.medium.com/v2/resize:fit:764/1*nPkE26Cr6pFFVuDq09G95g.png)

click on the virtual hard disk of the VM, click on it and click on done

![](https://miro.medium.com/v2/resize:fit:764/1*6FQKMuUMWmDR8tRruZJR_A.png)

Wait for a moment and once more I will repeat the last two steps

click on Installation Destination, then select the hard disk and click on done

![](https://miro.medium.com/v2/resize:fit:764/1*A7X3PWsD8RBwbF37AgwCUA.png)

Once that is completed, I will then go to Network & Host Name.

There should be two network adapter for the VM. One is NAT and the second one is Bridge Adapter

Give it a host name and hit apply.

I will then go on the root password section and select a custom password, then begin the installation. The installation will take some time to install.

After the installation, I will need to go back to VirtualBox and stop the VM. Once its completed shutdown, I will go to settings- storage- click on the iso and remove disk from virtual drive to avoid the installation to start again.

After the VM is completed up, I will then start setup, give it name, password and I will be able to start using CentOS Stream

![](https://miro.medium.com/v2/resize:fit:764/1*BQamcge0T7NIjLvOpsYWMw.png)

Wow! what a long one. I hope you guys are still with it.

I will now install an operating system for the second VM. I will need to go on google and look ubuntu 22 server iso and select the one that says Jammy Jellyfish

![](https://miro.medium.com/v2/resize:fit:764/1*-Jg_es0170xD6ez_PG3C3g.png)

![](https://miro.medium.com/v2/resize:fit:764/1*8wnatb-Au8aNoiZ58wvZuQ.png)

## Conclusion
In this lab, we successfully demonstrated the creation and configuration of virtual machines using Oracle VirtualBox. We created two different virtual machines running CentOS/AlmaLinux and Ubuntu Server respectively. The process involved proper resource allocation, network configuration, and operating system installation. Through this practical exercise, we gained hands-on experience in virtual machine deployment and management, which is crucial for modern cloud computing and server administration.

## References
1. Oracle VirtualBox Documentation: https://www.virtualbox.org/wiki/Documentation
2. AlmaLinux Documentation: https://wiki.almalinux.org/
3. Ubuntu Server Documentation: https://ubuntu.com/server/docs
