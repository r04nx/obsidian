---
title: "Lab 4A: Kubernetes using Minikube"
date: 2025-02-11
professor: Dr. D. Ambawade
course: Cloud Computing
share_link: https://share.note.sx/ph3xey8u#n4QRqkZBNFTGOKU/0u/brFnm83RUViL9XeEQNsHL39U
share_updated: 2025-02-11T20:47:34+05:30
---

# Lab 4A: Kubernetes using Minikube

> [!info] Table of Contents
> - [[#Course Information]]
> - [[#Objective]]
> - [[#Learning Outcomes]]
> - [[#System Requirements]]
> - [[#Introduction to Minikube]]
> - [[#Part I: Minikube Installation and Setup]]
> - [[#Part II: Run Nginx on Kubernetes Using Minikube]]
> - [[#Conclusion]]
> - [[#References]]

## Course Information
- **Professor**: Prof. Dr. D. Ambawade
- **Course**: Cloud Computing


## Objective
> [!abstract] Learning Goals
> - Learn basic Kubernetes commands for resource inspection
> - Understand the process of making deployed applications accessible both internally and externally through service exposure
> - Learn to deploy servers like NGINX on Kubernetes pods using YAML for effective resource management

## Learning Outcomes
After successful completion of the lab, students should be able to:

1. 🔄 Gain proficiency in Kubernetes concepts such as pods, services, and deployments
2. 💻 Acquire practical experience with Minikube, kubectl, and YAML file handling
3. 🛠️ Develop skills in creating, managing, and exposing deployments and services within a Kubernetes cluster
4. 🌐 Access applications deployed in a Kubernetes cluster using various methods
5. 🔍 Confidently troubleshoot and solve issues within Kubernetes environments

## System Requirements
> [!important] Prerequisites
> 1. A computer running a Unix-based operating system (e.g., Ubuntu Linux, macOS)
> 2. Minikube for running applications with kubernetes(k8s)
> 3. Superuser (root) privileges or sudo access
> 4. Internet connectivity for downloading VirtualBox VM (Ubuntu 22.04)

## Introduction to Minikube
> [!tip] Getting Started
> Watch the introductory videos on Minikube and Kubernetes available on YouTube to understand the basics of Minikube and its capabilities. See references [1][2][3][4] for detailed videos.








## Part I: Minikube Installation and Setup

### Installation
1. Visit the [Minikube website](https://minikube.sigs.k8s.io/docs/start/) and follow the installation instructions

> [!note] Installing on Linux x86-64
> Run the following commands to install the latest minikube stable release:
> ```bash
> curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
> sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
> ```

### Basic Operations

#### Starting the Cluster
```bash
# From a terminal with administrator access (but not as root)
minikube start
```

#### Interacting with Your Cluster
```bash
# If kubectl is already installed
kubectl get po -A

# Using minikube's kubectl
minikube kubectl -- get po -A

# Create a helpful alias
alias kubectl="minikube kubectl --"
```

#### Deploying Sample Applications
```bash
# Create a deployment and expose it
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
kubectl expose deployment hello-minikube --type=NodePort --port=8080

# Check the service status
kubectl get services hello-minikube

# Access the service
minikube service hello-minikube

# Alternative: Port forwarding
kubectl port-forward service/hello-minikube 7080:8080
```

#### Cluster Management Commands
> [!tip] Common Management Tasks
> ```bash
> # Pause/Unpause cluster
> minikube pause
> minikube unpause
> 
> # Stop cluster
> minikube stop
> 
> # Configure memory
> minikube config set memory 9001
> 
> # List addons
> minikube addons list
> 
> # Create additional cluster
> minikube start -p aged --kubernetes-version=v1.16.1
> 
> # Delete all clusters
> minikube delete --all
> ```

## Part II: Run Nginx on Kubernetes Using Minikube

> [!info] Reference Tutorial
> This section is based on the tutorial available at [Medium - How to Run Nginx on Kubernetes Using Minikube](https://medium.com/cloud-native-daily/how-to-run-nginx-on-kubernetes-using-minikube-df3319b80511)

### Setting Up the Environment
```bash
mkdir my_directory
cd my_directory
```

### Creating Configuration Files

#### Service Configuration
Create `service.yaml` with the following content:
```yaml
apiVersion: v1
kind: Service
metadata:
name: nginx-service
labels:
    env: sandbox
spec:
type: LoadBalancer
ports:
- port: 80
selector:
    env: sandbox
```

#### Deployment Configuration
Create `deployment.yaml` with the following content:
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
name: nginx-deployment
labels:
    env: sandbox
spec:
replicas: 3
selector:
    matchLabels:
    env: sandbox
template:
    metadata:
    labels:
        env: sandbox
    spec:
    containers:
    - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

### Deploying to Kubernetes
> [!note] Deployment Steps
> ```bash
> # Start Minikube
> minikube start
> 
> # Create Kubernetes resources
> kubectl create -f service.yaml
> kubectl create -f deployment.yaml
> 
> # Check pod status
> kubectl get pods
> 
> # Access the service
> minikube service nginx-service
> ```
> The browser should open showing the Nginx welcome page.

### Cleanup
```bash
# Remove all resources
minikube delete --all
```



## Conclusion
> [!warning] Student Task
> Write a two-paragraph conclusion describing your learning experience and key takeaways from this lab.

## References
1. [Minikube Documentation](https://minikube.sigs.k8s.io/docs/start/)
2. [Medium Article: Running Nginx on Kubernetes Using Minikube](https://medium.com/cloud-native-daily/how-to-run-nginx-on-kubernetes-using-minikube-df3319b80511)
3. [YouTube Tutorial 1](https://youtu.be/s_o8dwzRlu4)
4. [YouTube Tutorial 2](https://youtu.be/E2pP1MOfo3g)

## Command History
> [!example] Commands Used in This Lab
> ```bash
> sudo apt update
> curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
> sudo install minikube-linux-amd64 /usr/local/bin/minikube
> minikube start






List of commands on my setup: history command
        sudo apt update
   21  curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
   22  sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
   28  minikube start
   29  sudo chmod 777 /var/run/docker.sock 
   30  minikube start
   31  kubectl get po -A
   32  docker ps
   33  docker ps -a
   34  docker ps -aq
   35  docker ps -a
   36  minikube kubectl -- get po -A
   37  docker ps -a
   38  alias kubectl="minikube kubectl --"
   39  minikube dashboard
   40  sudo minikube dashboard
   41  sudo minikube start
   42  minikube dashboard
   43  kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0
   44  kubectl expose deployment hello-minikube --type=NodePort --port=8080
   45  kubectl get services hello-minikube
   46  minikube service hello-minikube
   47  kubectl port-forward service/hello-minikube 7080:8080
   48  ifconfig 
   49  kubectl port-forward service/hello-minikube 7080:8080
   50  minikube kubectl -- get pods
   51  mkdir my_directory
   52  cd my_directory/
   53  nano service.yaml
   54  nano deployment.yaml
   55  kubectl create -f service.yaml
   56  kubectl create -f deployment.yaml
   57  Kubectl get pods
   58  kubectl get pods
   59  minikube service nginx-service
   60  kubectl get pods
   61  docker ps -a

