# Lab 1: Linux User Management and Basic Commands

## Introduction
This lab exercise focuses on essential Linux system administration tasks, including user management and basic system commands. Through hands-on practice, you'll learn how to create users, manage sudo privileges, and execute common system commands to gather system information.

## Objectives
- Create and configure a new Linux user account
- Grant and manage sudo privileges
- Execute and understand basic Linux system commands
- Document and verify system information

## Prerequisites
- Access to a Linux system with root or sudo privileges
- Basic familiarity with command-line interface
- Text editor (such as nano or vim)

## Steps

### 1. User Creation
#### Creating a New User
```bash
sudo adduser newuser
```
![[user_creation.png]]
*Screenshot: User creation process*

#### Verifying User Creation
```bash
grep newuser /etc/passwd
```
![[user_verification.png]]
*Screenshot: Verification of user creation*

### 2. Managing Sudo Access
#### Granting Sudo Privileges
```bash
sudo usermod -aG sudo newuser
```
![[sudo_access.png]]
*Screenshot: Adding user to sudo group*

#### Verifying Sudo Access
```bash
sudo -l -U newuser
```
![[sudo_verification.png]]
*Screenshot: Verification of sudo privileges*

### 3. System Commands
#### System Information
```bash
# CPU Information
lscpu

# Network Interface Information
ifconfig

# Memory Information
free -h

# Disk Usage
df -h
```
![[system_info.png]]
*Screenshot: System information output*

#### Process Information
```bash
# Current Running Processes
ps aux

# System Resource Usage
top
```
![[process_info.png]]
*Screenshot: Process information output*

## Conclusion
In this lab, we successfully:
- Created a new user account
- Configured sudo access for the new user
- Executed and documented various system commands
- Verified system information and user privileges

The skills learned in this lab provide a foundation for basic Linux system administration and user management tasks.

