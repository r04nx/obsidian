---
share_link: https://share.note.sx/n9dqq0pg#RtXBu74zUn6vb1QLjJBrr0kvM8WohOHKhcqnyei6JxQ
share_updated: 2025-03-04T00:03:46+05:30
---

# Laboratory Practical Report: Automation Using Ansible

**Student Name:** Rohan Pawar  
**UID:** 2023201020  
**Batch:** C  
**Branch:** EXTC  
**Course:** Cloud Computing  

---

## Aim
To understand and implement automation using Ansible by configuring multiple servers for different roles (web server, FTP server) and managing them through Ansible playbooks and roles.

## Software Requirements
- **Incus** (LXD successor) for container/VM management
- **Ubuntu** operating system (host and containers)
- **Ansible** (latest version)
- **Docker & Docker Compose** for simulating a multi-server environment
- **NGINX** web server
- **vsftpd** FTP server
- **Python 3** for Ansible modules
- **SSH** for connectivity between control node and managed nodes

## Introduction
Ansible is an open-source automation tool that simplifies complex IT tasks such as configuration management, application deployment, and orchestration. It uses a declarative language to describe system configurations and a push-based architecture to implement changes. Unlike other configuration management tools, Ansible is agentless and uses SSH for secure communications.

This lab demonstrates how to use Ansible to automate the deployment and configuration of multiple servers with different roles in a simulated enterprise environment. By implementing infrastructure as code, we can ensure consistent, repeatable deployments and reduce manual administration overhead.

## Procedure

### 1. Setup of the Virtual Environment in Incus
First, we created a virtual machine using Incus (successor to LXD) to serve as our Ansible control node.

The following screenshot shows the VM created via Incus for the Ansible tutorial:
![[Pasted image 20250303230040.png]]

### 2. Installing and Configuring Ansible
Next, we updated the system packages and installed Ansible using APT. The following screenshot shows the process of updating packages, installing Ansible, and verifying the installation by checking the Ansible version:

![[Pasted image 20250303230224.png]]

### 3. Creating the Ansible Project Structure
We created a dedicated directory structure to organize our Ansible project. This structure includes directories for playbooks, roles, inventory files, and templates.

The following screenshot shows the newly created directory for the Ansible tutorial and its initial structure:

![[Pasted image 20250303230348.png]]
ubuntu@devops:~/ansible-tutorial$ tree .
.
├── docker-compose.yml
├── inventory
│   └── hosts.yml
├── nginx-test-page.yml
├── playbooks
│   ├── check_internet.yml
│   ├── group_vars
│   │   └── ftpservers
│   │       └── ftp_credentials.yml
│   ├── install_ftp_server.yml
│   ├── security-fixed3.yml
│   ├── templates
│   │   └── vsftpd.conf.j2
│   └── undo_ftp.yml
├── roles
│   └── nginx
│       ├── files
│       │   └── favicon.ico
│       ├── handlers
│       │   └── main.yml
│       ├── tasks
│       │   └── main.yml
│       ├── templates
│       │   ├── test-index.html.j2
│       │   └── test-page.conf.j2
│       └── vars
│           └── main.yml
└── templates

13 directories, 17 files
![[Pasted image 20250303230519.png]]

Created the ssh key values pairs 
![[Pasted image 20250303230641.png]]
Docker Installed Verification
![[Pasted image 20250303230707.png]]
### 6. Creating a Simulated Environment with Docker Compose
We created a Docker Compose file to set up multiple Ubuntu-based containers that simulate a real-life IT infrastructure of an organization. The configuration includes:

- Static IP addresses for each container
- A dedicated Docker network called "Production"
- SSH key authentication by copying the public key to each container's authorized_keys file

The Docker Compose file is as follows:

```yaml
version: '3'

networks:
  production:
    name: production
    ipam:
      config:
        - subnet: 192.168.100.0/24

services:
  Webserver:
    image: ubuntu:latest
    container_name: Webserver
    hostname: Webserver
    restart: unless-stopped
    networks:
      production:
        ipv4_address: 192.168.100.10
    command: >
      bash -c "
        apt-get update && 
        apt-get install -y openssh-server python3 sudo && 
        mkdir -p /run/sshd && 
        mkdir -p /root/.ssh && 
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDvNUA8tkhRe58LD1YOjnSK4g20jmKHb07ETrXdOGr5C4xFPEOCayPRb7wP+Pl8/1ZvMnJFmcSR9aToKClfgJMtKgkZEZk+vK5TTCev2VQaTAFFH7ePq3gTKpMW4vSaKNrMn/... ubuntu@devops' > /root/.ssh/authorized_keys && 
        chmod 700 /root/.ssh && 
        chmod 600 /root/.ssh/authorized_keys && 
        sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && 
        sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && 
        /usr/sbin/sshd -D
      "

  FTP:
    image: ubuntu:latest
    container_name: FTP
    hostname: FTP
    restart: unless-stopped
    networks:
      production:
        ipv4_address: 192.168.100.20
    command: >
      bash -c "
        apt-get update && 
        apt-get install -y openssh-server python3 sudo && 
        mkdir -p /run/sshd && 
        mkdir -p /root/.ssh && 
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDvNUA8tkhRe58LD1YOjnSK4g20jmKHb07ETrXdOGr5C4xFPEOCayPRb7wP+Pl8/1ZvMnJFmcSR9aToKClfgJMtKgkZEZk+vK5TTCev2VQaTAFFH7ePq3gTKpMW4vSaKNrMn... ubuntu@devops' > /root/.ssh/authorized_keys && 
        chmod 700 /root/.ssh && 
        chmod 600 /root/.ssh/authorized_keys && 
        sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && 
        sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && 
        /usr/sbin/sshd -D
      "

  Monitoring:
    image: ubuntu:latest
    container_name: Monitoring
    hostname: Monitoring
    restart: unless-stopped
    networks:
      production:
        ipv4_address: 192.168.100.30
    command: >
      bash -c "
        apt-get update && 
        apt-get install -y openssh-server python3 sudo && 
        mkdir -p /run/sshd && 
        mkdir -p /root/.ssh && 
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDvNUA8tkhRe58LD1YOjnSK4g20jmKHb07ETrXdOGr5C4xFPEOCa... ubuntu@devops' > /root/.ssh/authorized_keys && 
        chmod 700 /root/.ssh && 
        chmod 600 /root/.ssh/authorized_keys && 
        sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && 
        sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && 
        /usr/sbin/sshd -D
      "

  FTP2:
    image: ubuntu:latest
    container_name: FTP2
    hostname: ftp2.devops.org
    restart: unless-stopped
    networks:
      production:
        ipv4_address: 192.168.100.50
    command: >
      bash -c "
        apt-get update && 
        apt-get install -y openssh-server python3 sudo && 
        mkdir -p /run/sshd && 
        mkdir -p /root/.ssh && 
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDvNUA8tkhRe58LD1YOjnSK4g20jmKHb07ETrXdOGr5C4xFPEOCa... ubuntu@devops' > /root/.ssh/authorized_keys && 
        chmod 700 /root/.ssh && 
        chmod 600 /root/.ssh/authorized_keys && 
        sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && 
        sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && 
        /usr/sbin/sshd -D
      "

  NetworkSecurity:
    image: ubuntu:latest
    container_name: NetworkSecurity
    hostname: NetworkSecurity
    restart: unless-stopped
    networks:
      production:
        ipv4_address: 192.168.100.40
    command: >
      bash -c "
        apt-get update && 
        apt-get install -y openssh-server python3 sudo && 
        mkdir -p /run/sshd && 
        mkdir -p /root/.ssh && 
        echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDvNUA8tkhRe58LD1YOjnSK4g20jmKHb07ETrXdOGr5C4xFPEOCayPRb7wP+Pl8/1ZvMnJFmcSR9aToKClfgJMtKgkZEZk+vK5TTCev2VQaTAFFH7ePq3gTKpMW4vSaKNrMn/... ubuntu@devops' > /root/.ssh/authorized_keys && 
        chmod 700 /root/.ssh && 
        chmod 600 /root/.ssh/authorized_keys && 
        sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config && 
        sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config && 
        /usr/sbin/sshd -D
      "

```
### 7. Starting the Docker Containers
We started the Ubuntu-based containers using the `docker-compose up -d` command:

![[Pasted image 20250303231129.png]]

We verified the running containers using the `docker ps -a` command:

![[Pasted image 20250303231230.png]]
![[Pasted image 20250303231435.png]]
### 8. Creating the Ansible Inventory
We created an inventory file (`inventory/hosts.yml`) to define the hosts and groups that Ansible will manage. The inventory also includes variables for SSH connection settings and host-specific configurations:

```yaml
webservers:
  hosts:
    webserver.devops.org:
      ansible_user: root
      ansible_host: 192.168.100.10
    web2.devops.org:
      ansible_user: root
      ansible_connection: local  # Mark as unreachable
      ansible_host_is_down: true  # Custom variable to indicate maintenance
      ansible_host: 10.10.50.141

  vars:
    ignore_unreachable: true  # Ignore unreachable hosts in this group

ftpservers:
  hosts:
    ftp.devops.org:
      ansible_user: root
      ansible_host: 192.168.100.20
    ftp2.devops.org:
      ansible_user: root
      ansible_host: 192.168.100.50
monitoring:
  hosts:
    monitoring.devops.org:
      ansible_user: root
      ansible_host: 192.168.100.30

security:
  hosts:
    networksecurity.devops.org:
      ansible_user: root
      ansible_host: 192.168.100.40

all:
  children:
    servers:
      children:
        webservers:
        ftpservers:
        monitoring:
        security:
  vars:
    ansible_ssh_private_key_file: ~/.ssh/id_rsa
    ansible_ssh_common_args: '-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null'
```
### 9. Testing Connectivity to Managed Hosts
After setting up the inventory, we tested connectivity to all hosts using the Ansible ping module to verify that they are accessible:

```bash
ubuntu@devops:~/ansible-tutorial$ ansible all -i inventory/hosts.yml -m ping
[WARNING]: Found variable using reserved name: ignore_unreachable
[WARNING]: Platform linux on host web2.devops.org is using the discovered Python interpreter at /usr/bin/python3.10, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
web2.devops.org | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.10"
    },
    "changed": false,
    "ping": "pong"
}
[WARNING]: Platform linux on host ftp2.devops.org is using the discovered Python interpreter at /usr/bin/python3.12, but future installation of another Python interpreter could
change the meaning of that path. See https://docs.ansible.com/ansible-core/2.17/reference_appendices/interpreter_discovery.html for more information.
ftp2.devops.org | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3.12"
    },
    "changed": false,
    "ping": "pong"
}

```

The output confirms successful connectivity to the hosts:

![[Pasted image 20250303231725.png]]

### 10. Creating the Nginx Role
We created a playbook with an Nginx role to install and configure the Nginx web server on the remote hosts under the "webservers" group:

![[Pasted image 20250303231924.png]]
### 11. Deploying Nginx with Ansible
We executed the playbook to deploy Nginx and configure the web server on all hosts in the "webservers" group:

![[Pasted image 20250303233335.png]]
![[Pasted image 20250303233331.png]]

The output/response of the Nginx setup shows successful deployment:

![[Pasted image 20250303233407.png]]

We verified the Nginx installation by accessing the web server through a browser:

![[Pasted image 20250304000014.png]]
![[Pasted image 20250304000021.png]]
### 12. Understanding the Nginx Role Structure

The Nginx role we created automates the deployment and configuration of web servers with the following components:

- **Tasks**: Install Nginx, create website directory, deploy content, configure server
- **Handlers**: Manage service restarts when configuration changes
- **Templates**: Configure server settings through templating
- **Variables**: Define customizable parameters for the web server

#### Nginx Test Page Playbook (nginx-test-page.yml)

This playbook deploys the Nginx web server with a test page:

- Installs and configures Nginx through the Nginx role
- Sets up a test page to verify the web server is functioning correctly

### 13. FTP Server Deployment with Ansible

We created a playbook to install and configure the vsftpd FTP server on hosts in the "ftpservers" group:

```yaml
# playbooks/install_ftp_server.yml
- name: Install and Configure FTP Server
  hosts: ftpservers
  become: yes
  vars:
    ftp_users:
      - username: ftpuser
        password: "FtpPass123"
        local_root: /var/ftp/ftpuser
        chroot: yes
        write_access: yes
      - username: readonly
        password: "FtpPass123"
        local_root: /var/ftp/readonly
        chroot: yes
        write_access: no
    ftp_banner: "Welcome to DevOps FTP Server"
    anonymous_enable: no
    local_enable: yes
    write_enable: yes
    chroot_local_user: yes
  tasks:
    - name: Install vsftpd
      apt:
        name: vsftpd
        state: present
        update_cache: yes
    
    - name: Backup original vsftpd.conf
      copy:
        src: /etc/vsftpd.conf
        dest: /etc/vsftpd.conf.bak
        remote_src: yes
        force: no
    
    - name: Configure vsftpd.conf
      template:
        src: templates/vsftpd.conf.j2
        dest: /etc/vsftpd.conf
        owner: root
        group: root
        mode: '0644'
      register: vsftpd_conf
    
    - name: Create FTP user directories
      file:
        path: "{{ item.local_root }}"
        state: directory
        mode: '0755'
      with_items: "{{ ftp_users }}"
      register: user_dirs
    
    - name: Create FTP users
      user:
        name: "{{ item.username }}"
        home: "{{ item.local_root }}"
        shell: /bin/bash
        state: present
      with_items: "{{ ftp_users }}"
    
    - name: Set user passwords
      shell: "echo '{{ item.username }}:{{ item.password }}' | chpasswd"
      with_items: "{{ ftp_users }}"
      no_log: true
    
    - name: Set correct permissions for FTP user directories
      file:
        path: "{{ item.local_root }}"
        state: directory
        mode: '0755'
        owner: "{{ item.username }}"
        group: "{{ item.username }}"
        recurse: yes
      with_items: "{{ ftp_users }}"
    
    - name: Create a user list file for vsftpd
      copy:
        content: |
          {% for user in ftp_users %}
          {{ user.username }}
          {% endfor %}
        dest: /etc/vsftpd.user_list
        owner: root
        group: root
        mode: '0644'
    
    - name: Create empty secure_chroot_dir
      file:
        path: /var/run/vsftpd/empty
        state: directory
        mode: '0755'
        owner: root
        group: root
    
    - name: Restart vsftpd service
      service:
        name: vsftpd
        state: restarted
        enabled: yes
    
    - name: Get process status
      shell: "ps aux | grep [v]sftpd"
      register: process_status
    
    - name: Display vsftpd process status
      debug:
        var: process_status.stdout_lines
```

The output of running the FTP server playbook showed successful installation and configuration of vsftpd on the designated servers.

### 14. FTP Server Installation Results

We executed the FTP server playbook and verified the successful installation:

![[Pasted image 20250304000046.png]]
![[Pasted image 20250304000057.png]]
Verifying the FTP server installation by connecting to the FTP server and creating a new directory, which worked fine,  
![](https://share.note.sx/files/06/06yuarp2taczwzycfj9a.png)

Verifying on the another remote host  
![](https://share.note.sx/files/l8/l8sozd777nlf8ret07nf.png)


Automates the setup of vsftpd FTP servers:

- Installs the vsftpd package
- Creates FTP user accounts based on defined variables
- Sets up user directories with appropriate permissions
- Configures the server using a template
- Ensures the service is running and enabled
  
### 15. Internet Connectivity Testing
We created another playbook for testing the internet connectivity of the containers:

```yaml
# playbooks/check_internet.yml
- name: Check internet connectivity from web servers
  hosts: all
  tasks:
    - name: Check internet access
      uri:
        url: https://www.google.com
        method: GET
        return_content: no
      register: result
      ignore_errors: yes

    - name: Display connectivity status
      debug:
        msg: "Internet is reachable"  
      when: result.status == 200

    - name: Display failure message
      debug:
        msg: "No internet access!"  
      when: result.failed is defined and result.failed
```

Running the above playbook
![[Pasted image 20250303234939.png]]
![[Pasted image 20250303235004.png]]
The above playbook ran successfully, confirming internet connectivity in all the containers.

### 16. Summary of Playbooks and Roles

#### Internet Connectivity Check (check_internet.yml)

This playbook verifies internet connectivity on managed hosts:

- Tests connectivity to external resources
- Reports success or failure for each host
- Provides detailed output for troubleshooting

> Note: All of the Ansible setup files, YAML configurations, templates, etc. can be found on GitHub at: https://github.com/r04nx/ansible-tutorial 

## Observation

Through this lab, we observed several key aspects of Ansible automation:

1. **Centralized Management**: Ansible provided a centralized way to manage multiple servers from a single control node, streamlining administration tasks.

2. **Idempotency**: Running the same playbook multiple times produced consistent results, with Ansible only making changes when needed.

3. **Scalability**: The same playbooks could be applied to one server or many servers without modification, demonstrating Ansible's scalability.

4. **Parallelization**: Ansible executed tasks in parallel across multiple hosts, significantly reducing deployment time compared to manual methods.

5. **Templating Capabilities**: Using Jinja2 templates allowed for dynamic configuration generation based on variables, enabling customization while maintaining consistency.

6. **Role-Based Organization**: Structuring code into roles (like the Nginx role) promoted reusability and modularity, making maintenance easier.

7. **Error Handling**: Ansible provided clear feedback when errors occurred, making troubleshooting more straightforward than with manual deployments.

## Conclusion

This lab demonstrated the power and efficiency of Ansible as an automation tool for IT infrastructure management. By leveraging Ansible's declarative approach and agentless architecture, we were able to:

1. **Increase Efficiency**: Tasks that would have taken hours to perform manually across multiple servers were completed in minutes through automation.

2. **Improve Consistency**: Every server was configured identically according to our specifications, eliminating configuration drift and human error.

3. **Enable Infrastructure as Code**: By representing our infrastructure configuration as code, we created a documented, version-controllable, and repeatable system setup process.

4. **Simplify Complex Deployments**: Ansible's playbook structure made it easy to break down complex deployment processes into manageable, logical steps.

5. **Reduce Administrative Overhead**: Once configured, the same playbooks can be reused for future deployments, reducing the ongoing maintenance burden.

Ansible proves to be an invaluable tool for modern DevOps practices, enabling organizations to automate routine tasks, standardize environments, and focus more on innovation rather than maintenance. The skills learned in this lab provide a foundation for implementing automation in real-world enterprise environments, ultimately leading to more reliable, consistent, and efficiently managed infrastructure.

# https://github.com/r04nx/ansible-tutorial 
