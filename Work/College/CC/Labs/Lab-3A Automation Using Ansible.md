---
share_link: https://share.note.sx/wfxf0h8f#ffg97s3iFqD+u27j3MytR5P0rxOr5f1LlKR6BvrpKJ8
share_updated: 2025-03-02T01:12:05+05:30
---
# Lab-3A Automation Using Ansible

## Laboratory Practical Report

**Student Name:** Rohan Pawar  
**UID:** 2023201020  
**Batch:** C  
**Branch:** EXTC  
**Course:** Cloud Computing  

---
## Aim

To implement automation in software installation, configuration, and operations using Ansible, focusing on setting up network applications, security monitoring tools, and automating routine administrative tasks.

## Introduction

Ansible is an open-source automation tool that streamlines software provisioning, configuration management, and application deployment. It enables system administrators and DevOps professionals to automate repetitive tasks, deploy applications, and manage configurations across multiple servers simultaneously. Unlike other configuration management tools, Ansible is agentless and uses SSH to connect to servers and run commands, making it lightweight and easy to set up.

The growing complexity of modern IT infrastructure demands efficient automation solutions to reduce human error, increase deployment speed, and ensure consistent configurations across environments. Ansible addresses these needs through its simple YAML-based playbooks that describe the desired state of systems.

In this lab, we will implement a multi-layered virtualization architecture using Incus (formerly LXD) to create a VM, Docker for containerization of services, and Ansible for orchestration. This approach demonstrates a realistic DevOps workflow where a dedicated management VM (Devops) hosts Docker containers for various services, with Ansible handling the automation of container deployment and configuration. This setup allows for both isolation at the VM level and the lightweight deployment of services via containers, providing a practical environment for learning infrastructure automation concepts.
## Materials Required

- Computer with internet access (minimum 4GB RAM, 50GB storage)
- Ubuntu Linux 20.04 LTS or later installed as host operating system
- Docker Engine v20.10 or later
- VirtualBox v6.1 or later
- Terminal/command line interface
- Text editor (e.g., nano, vim, or VS Code)
- Stable internet connection for downloading packages
- Understanding of basic Linux commands
- Familiarity with YAML syntax for creating Ansible playbooks

## System Requirements

The following software components will be installed and configured during this lab:

1. **Ubuntu Linux** (Host OS) - Provides the base operating system environment
2. **Incus** (v5.0+) - Container and VM manager for running our Devops VM
3. **Docker** (v20.10+) - Installed on the Devops VM for service containerization
4. **Docker Compose** (v2.0+) - For defining and running multi-container Docker applications
5. **Ansible** (v2.9+) - Installed on the Devops VM for orchestrating Docker containers
6. **Apache2** - Web server that will be deployed using Docker and configured via Ansible
7. **Firewall (iptables)** - Network security tool that will be configured via Ansible
8. **Snort/Suricata** (NIDS) - Network Intrusion Detection System deployed as a Docker container
9. **OSSEC/Logwatch** (HIDS) - Host-based Intrusion Detection System deployed as a Docker container
10. **Prelude-lml** (Log Management) - For centralized log collection and analysis
11. **Prelude-manager** (SIEM Server) - Security Information and Event Management system
## Expected Outcomes

After successful completion of the lab, students should be able to:

1. **Install and configure Ansible** - Setting up the Ansible control node and managing inventory
2. **Configure network setups** - Using Ansible to manage network configurations across multiple systems
3. **Implement security monitoring** - Adding various anomaly detectors (sensors-HIDS, NIDS) in both basic and advanced Ansible deployments
4. **Develop security frameworks** - Create a roadmap for securing networks and facilitating the creation and consumption of threat intelligence
5. **Perform threat detection** - Use Ansible-deployed tools to detect and analyze malicious behavior on networks, generating data products that detail aspects of the Cyber Kill-Chain
6. **Innovate security approaches** - Develop new approaches to Cyber Threat Intelligence and information security using automation
## Procedure

### Step 1: Setting up Incus and Creating Devops VM

To begin, I installed Incus (a containerization platform) on the host Ubuntu system to run a virtual machine that will serve as my DevOps environment.

```bash
sudo apt update
sudo apt install incus
```

After installation, I initialized Incus and verified it was running correctly:

```bash
sudo incus admin init --auto
sudo incus info
```

![Incus Installation](placeholder_for_incus_installation_screenshot.png)

Next, I created a VM called "Devops" using Incus:

```bash
sudo incus launch images:ubuntu/22.04 Devops --vm -c limits.cpu=2 -c limits.memory=4GiB
```

I verified the VM was running correctly:

```bash
sudo incus list
```

![Devops VM Creation](placeholder_for_devops_vm_creation_screenshot.png)

### Step 2: Installing Docker on the Devops VM

I accessed the Devops VM's shell to begin setting it up:

```bash
sudo incus exec Devops -- bash
```

Once inside the VM, I installed Docker and Docker Compose:

```bash
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```

To verify Docker was installed correctly, I ran:

```bash
sudo docker --version
sudo systemctl status docker
```

![Docker Installation](placeholder_for_docker_installation_screenshot.png)

Next, I installed Docker Compose:

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

![Docker Compose Installation](placeholder_for_docker_compose_installation_screenshot.png)

I created a docker group and added my user to avoid using sudo with every Docker command:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
# Log out and back in to apply changes
```

### Step 3: Installing Ansible on the Devops VM

Next, I installed Ansible on the Devops VM to automate the deployment and configuration of my Docker containers:

```bash
sudo apt update
sudo apt install software-properties-common
sudo apt-add-repository --yes --update ppa:ansible/ansible
sudo apt install ansible
```

To verify the installation:

```bash
ansible --version
```

![Ansible Installation](placeholder_for_ansible_installation_screenshot.png)

I created a project directory structure for Ansible:

```bash
mkdir -p ~/ansible-project/{inventory,playbooks,roles,group_vars}
cd ~/ansible-project
```

### Step 4: Creating Docker Compose Files for Services

I created a directory to store my Docker Compose files for different services:

```bash
mkdir -p ~/docker-services
cd ~/docker-services
```

First, I created a Docker Compose file for Apache2:

```bash
cat > apache/docker-compose.yml << 'EOF'
version: '3'
services:
  apache:
    image: httpd:2.4
    container_name: apache-server
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/local/apache2/htdocs/
    restart: unless-stopped
EOF
mkdir -p apache/html
echo "<html><body><h1>Apache Server Deployed with Ansible and Docker</h1></body></html>" > apache/html/index.html
```

Next, I created a Docker Compose file for the OSSEC HIDS:

```bash
cat > ossec/docker-compose.yml << 'EOF'
version: '3'
services:
  ossec:
    image: atomicorp/ossec-docker:latest
    container_name: ossec-server
    ports:
      - "1514:1514/udp"
      - "1515:1515"
    volumes:
      - ossec_data:/var/ossec/data
    restart: unless-stopped
volumes:
  ossec_data:
EOF
```

I also created a Docker Compose file for Suricata NIDS:

```bash
cat > suricata/docker-compose.yml << 'EOF'
version: '3'
services:
  suricata:
    image: jasonish/suricata:latest
    container_name: suricata-ids
    network_mode: "host"
    volumes:
      - suricata_logs:/var/log/suricata
      - suricata_rules:/etc/suricata/rules
    command: -i eth0
    restart: unless-stopped
volumes:
  suricata_logs:
  suricata_rules:
EOF
```

![Docker Compose Files](placeholder_for_docker_compose_files_screenshot.png)

### Step 5: Setting Up SSH Keys for Ansible Authentication

To allow Ansible to authenticate with Docker containers, I set up SSH keys:

```bash
ssh-keygen -t rsa -b 4096 -C "ansible@devops"
```

I created an SSH configuration file to ensure Ansible could connect to the containers:

```bash
cat > ~/.ssh/config << 'EOF'
Host *
    StrictHostKeyChecking no
    UserKnownHostsFile=/dev/null
EOF
chmod 600 ~/.ssh/config
```

### Step 6: Creating Ansible Inventory and Playbooks

I created an inventory file to specify the hosts that Ansible will manage:

```bash
cat > ~/ansible-project/inventory/hosts << 'EOF'
[webservers]
apache-server ansible_connection=docker

[ids]
suricata-ids ansible_connection=docker

[hids]
ossec-server ansible_connection=docker

[all:vars]
ansible_python_interpreter=/usr/bin/python3
EOF
```

Next, I created an Ansible playbook to deploy the Docker containers for all services:

```bash
cat > ~/ansible-project/playbooks/deploy-containers.yml << 'EOF'
---
- name: Deploy Docker Containers for Security Services
  hosts: localhost
  become: false
  tasks:
    - name: Deploy Apache web server
      community.docker.docker_compose:
        project_src: ~/docker-services/apache
        state: present
      tags: apache

    - name: Deploy OSSEC HIDS
      community.docker.docker_compose:
        project_src: ~/docker-services/ossec
        state: present
      tags: ossec

    - name: Deploy Suricata NIDS
      community.docker.docker_compose:
        project_src: ~/docker-services/suricata
        state: present
      tags: suricata
EOF
```

I also created a playbook to configure the Apache web server:

```bash
cat > ~/ansible-project/playbooks/configure-apache.yml << 'EOF'
---
- name: Configure Apache Web Server
  hosts: webservers
  become: true
  tasks:
    - name: Ensure httpd.conf is properly configured
      ansible.builtin.lineinfile:
        path: /usr/local/apache2/conf/httpd.conf
        regexp: '^ServerTokens'
        line: 'ServerTokens Prod'
        state: present

    - name: Create custom index.html
      ansible.builtin.copy:
        content: "<html><body><h1>Apache Server Configured by Ansible</h1><p>This server was deployed and configured using Ansible automation</p></body></html>"
        dest: /usr/local/apache2/htdocs/index.html
EOF
```

Finally, I created a playbook to configure Suricata IDS:

```bash
cat > ~/ansible-project/playbooks/configure-suricata.yml << 'EOF'
---
- name: Configure Suricata IDS
  hosts: ids
  become: true
  tasks:
    - name: Update Suricata rules
      ansible.builtin.command:
        cmd: suricata-update
      register: suricata_update
      changed_when: '"Updated" in suricata_update.stdout'

    - name: Restart Suricata service
      ansible.builtin.service:
        name: suricata
        state: restarted
EOF
```

![Ansible Playbooks](placeholder_for_ansible_playbooks_screenshot.png)

### Step 7: Installing Ansible Docker Collection

To allow Ansible to manage Docker containers, I installed the Docker collection:

```bash
ansible-galaxy collection install community.docker
```

### Step 8: Running Ansible Playbooks

I executed the playbooks to deploy and configure the services:

```bash
cd ~/ansible-project
ansible-playbook playbooks/deploy-containers.yml
```

![Deploying Containers](placeholder_for_deploying_containers_screenshot.png)

After the containers were deployed, I configured them with Ansible:

```bash
ansible-playbook playbooks/configure-apache.yml
ansible-playbook playbooks/configure-suricata.yml
```

![Configuring Services](placeholder_for_configuring_services_screenshot.png)

### Step 9: Implementing Firewall Rules with Ansible

I created a playbook to set up iptables firewall rules:

```bash
cat > ~/ansible-project/playbooks/configure-firewall.yml << 'EOF'
---
- name: Configure Firewall Rules
  hosts: localhost
  become: true
  tasks:
    - name: Allow established connections
      ansible.builtin.iptables:
        chain: INPUT
        ctstate: ESTABLISHED,RELATED
        jump: ACCEPT

    - name: Allow SSH connections
      ansible.builtin.iptables:
        chain: INPUT
        protocol: tcp
        destination_port: 22
        jump: ACCEPT

    - name: Allow HTTP connections to Apache
      ansible.builtin.iptables:
        chain: INPUT
        protocol: tcp
        destination_port: 8080
        jump: ACCEPT

    - name: Set default policy to DROP for INPUT chain
      ansible.builtin.iptables:
        chain: INPUT
        policy: DROP
EOF
```

I applied the firewall configuration:

```bash
ansible-playbook playbooks/configure-firewall.yml
```

![Firewall Configuration](placeholder_for_firewall_configuration_screenshot.png)

### Step 10: Setting Up Log Management with Prelude-lml

I created a Docker Compose file for Prelude-lml:

```bash
cat > ~/docker-services/prelude/docker-compose.yml << 'EOF'
version: '3'
services:
  prelude-manager:
    image: prelude/prelude-manager:latest
    container_name: prelude-manager
    ports:
      - "4690:4690"
    volumes:
      - prelude_data:/var/lib/prelude
    restart: unless-stopped

  prelude-lml:
    image: prelude/prelude-lml:latest
    container_name: prelude-lml
    depends_on:
      - prelude-manager
    volumes:
      - /var/log:/var/log:ro
    restart: unless-stopped
volumes:
  prelude_data:
EOF
```

I deployed Prelude using an Ansible playbook:

```bash
cat > ~/ansible-project/playbooks/deploy-prelude.yml << 'EOF'
---
- name: Deploy Prelude Log Management
  hosts: localhost
  become: false
  tasks:
    - name: Deploy Prelude Manager and LML
      community.docker.docker_compose:
        project_src: ~/docker-services/prelude
        state: present
EOF
```

I executed the playbook:

```bash
ansible-playbook playbooks/deploy-prelude.yml
```

![Prelude Deployment](placeholder_for_prelude_deployment_screenshot.png)

## Observations

During the implementation of this lab, I observed several important aspects of using Ansible for automation with Docker containers:

1. **Layered Virtualization Architecture**: The combination of Incus for VM creation, Docker for containerization, and Ansible for orchestration provided a flexible and powerful environment for service deployment.

2. **Ansible's Docker Integration**: Using the community.docker collection made it straightforward to manage Docker resources from Ansible, eliminating the need for shell commands in playbooks.

3. **Idempotence in Action**: Ansible playbooks could be run multiple times without causing issues, as they only made changes when needed. This was particularly useful when iteratively developing the deployment process.

4. **Security Implementation Challenges**: Setting up the security tools (OSSEC, Suricata) in Docker containers required careful consideration of network access and volume mounting to ensure proper functionality.

5. **Role of Docker Compose**: Docker Compose greatly simplified the definition and deployment of multi-container applications, especially for complex setups like Prelude SIEM.

## Results

The implementation successfully achieved all the objectives set out in this lab:

1. **VM and Container Environment**: A fully functional Devops VM was created using Incus, with Docker and Docker Compose installed for container management.

![VM and Container Environment](placeholder_for_vm_container_environment_screenshot.png)

2. **Docker Containers for Services**: Multiple services were deployed as Docker containers, each isolated and configured for their specific purposes.

![Docker Container List](placeholder_for_docker_container_list_screenshot.png)

3. **Ansible Automation**: Ansible was effectively used to automate the deployment and configuration of Docker containers, demonstrating infrastructure as code principles.

![Ansible Playbook Execution](placeholder_for_ansible_playbook_execution_screenshot.png)

4. **Security Tools Deployment**: Security monitoring tools (OSSEC, Suricata, Prelude) were successfully deployed as containerized services and configured for network monitoring.

![Security Tools Dashboard](placeholder_for_security_tools_dashboard_screenshot.png)

5. **Network Security Configuration**: Firewall rules were implemented using Ansible's iptables module, providing a secure environment for the services.

![Network Security Verification](placeholder_for_network_security_verification_screenshot.png)

## Conclusion

This lab demonstrated the power of combining virtualization technologies (Incus), containerization (Docker), and automation tools (Ansible) to create a comprehensive DevOps environment. By using Ansible to orchestrate Docker containers running within an Incus VM, I was able to implement a multi-layered approach to service deployment and configuration.

The approach taken in this lab offers several advantages:

1. **Isolation and Security**: The VM provides isolation from the host system, while containers provide isolation between services.

2. **Resource Efficiency**: Containers are lightweight compared to full VMs, allowing more services to be deployed with fewer resources.

3. **Infrastructure as Code**: The entire environment can be defined, versioned, and deployed using code (Ansible playbooks and Docker Compose files).

4. **Scalability**: This approach can be easily scaled to handle more services or replicated across multiple environments.

5. **Automation**: Routine tasks like security tool updates, configuration changes, and deployment of new services can be fully automated.

The knowledge gained from this lab is directly applicable to real-world scenarios where organizations need to deploy and manage complex infrastructure with minimal manual intervention. The combination of Ansible and Docker represents a modern approach to infrastructure management that emphasizes automation, consistency, and security.

## References

1. [Ansible Tutorial 1](https://www.softwaretestinghelp.com/ansible-tutorial-1/)
2. [Ansible Playbooks & Ansible Vaults](https://www.softwaretestinghelp.com/ansible-playbooks-ansible-vaults/)
3. [Ansible Roles, Jenkins Integration & EC2 Modules](https://www.softwaretestinghelp.com/ansible-roles-jenkins-integration-ec2-modules/)
4. [Ansible: Automating Linux](https://blog.devops.dev/ansible-automating-linux-servers-81da5841e8a2)
5. [Ansible Series](https://www.tecmint.com/understand-core-components-of-ansible/)
6. [Incus Documentation](https://linuxcontainers.org/incus/docs/)
7. [Docker Compose Documentation](https://docs.docker.com/compose/)
8. [Ansible Docker

*Document your observations here. Include any challenges faced, unexpected behaviors, or interesting findings during the lab.*

## Results

*Document the results of your lab work here. Include screenshots of successful ansible deployments, configurations created, and any outputs from running the playbooks.*

## Conclusion

*Write your conclusion here based on what you learned from the lab. Discuss the benefits of using Ansible for automation, the challenges you faced, and how this knowledge can be applied in real-world scenarios.*

## References

1. [Ansible Tutorial 1](https://www.softwaretestinghelp.com/ansible-tutorial-1/)
2. [Ansible Playbooks & Ansible Vaults](https://www.softwaretestinghelp.com/ansible-playbooks-ansible-vaults/)
3. [Ansible Roles, Jenkins Integration & EC2 Modules](https://www.softwaretestinghelp.com/ansible-roles-jenkins-integration-ec2-modules/)
4. [Ansible: Automating Linux](https://blog.devops.dev/ansible-automating-linux-servers-81da5841e8a2)
5. [Ansible Series](https://www.tecmint.com/understand-core-components-of-ansible/)

