---
share_link: https://share.note.sx/5jvus5yt#CsPin3nZ2mbGs2U1KIiPUy14FckfxyyTsAOzDJ7S/YA
share_updated: 2025-03-08T17:01:42+05:30
---
## Laboratory Practical Report: Setting Up and Exploring Kubernetes with Minikube

**Student Name:** Rohan Pawar  
**UID:** 2023201020  
**Batch:** C  
**Branch:** EXTC  
**Course:** Cloud Computing  

---

### Aim:
The aim of this laboratory practical is to set up a local Kubernetes environment using Minikube, deploy containerized applications, and explore fundamental Kubernetes concepts such as pod deployment, scaling, load balancing, and self-healing capabilities. This hands-on experience will provide practical understanding of container orchestration in a controlled environment.

### Software Requirements:
- **Operating System**: Ubuntu 22.04 LTS or other Linux distribution
- **Minikube**: Version 1.35.0 or later (Tool for running Kubernetes locally)
- **Docker**: Version 27.4.1 or later (Container runtime)
- **kubectl**: Version 1.32.0 (Kubernetes command-line tool)
- **Web Browser**: For accessing the Minikube dashboard and deployed web applications
- **Internet Connection**: For downloading necessary images and packages
- **Minimum Hardware**: 2 CPU cores, 2GB RAM, 20GB free disk space

### Procedure Followed:
#### 1. Installing Minikube

First, we need to download and install Minikube, which allows us to run Kubernetes locally:

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

Output:
```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  119M  100  119M    0     0  5639k      0  0:00:21  0:00:21 --:--:-- 6130k
```

![[Pasted image 20250304001426.png]]

#### 2. Verifying Minikube Installation

After installation, we verified that Minikube was correctly installed by checking the version:

```bash
minikube version
```

![[Pasted image 20250304001602.png]]

#### 3. Verifying Docker Installation

Since we'll be using Docker as the container runtime for Minikube, we need to ensure it's properly installed:

```bash
docker --version
```

![[Pasted image 20250304001646.png]]
#### 4. Starting Minikube with Docker as the Driver

Next, we started Minikube using Docker as the driver. This creates a Kubernetes cluster inside Docker containers:

```bash
minikube start --driver=docker
```

Output:
```
😄  minikube v1.35.0 on Ubuntu 22.04 (kvm/amd64)
✨  Using the docker driver based on existing profile
👍  Starting "minikube" primary control-plane node in "minikube" cluster
🚜  Pulling base image v0.0.46 ...
🤷  docker "minikube" container is missing, will recreate.
🔥  Creating docker container (CPUs=2, Memory=2200MB) ...
🐳  Preparing Kubernetes v1.32.0 on Docker 27.4.1 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔗  Configuring bridge CNI (Container Networking Interface) ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass

❗  /usr/bin/kubectl is version 1.29.14, which may have incompatibilities with Kubernetes 1.32.0.
    ▪ Want kubectl v1.32.0? Try 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

![[Pasted image 20250304003314.png]]

This process allocates resources (2 CPUs and 2200MB memory) to the Minikube virtual machine and sets up Kubernetes v1.32.0 with Docker as the container runtime. The warning about kubectl version differences is normal and offers a solution to use the matching kubectl version through Minikube.
#### 5. Running Basic kubectl Commands

We ran some basic kubectl commands to verify our Kubernetes setup:

```bash
kubectl get nodes
kubectl cluster-info
```

![[Pasted image 20250304003431.png]]

#### 6. Starting the Minikube Dashboard

Minikube includes a built-in dashboard for visualizing and managing Kubernetes resources. We started it with:

```bash
minikube dashboard
```

![[Pasted image 20250304003949.png]]

![[Pasted image 20250304004000.png]]

The dashboard provides a graphical interface to manage all Kubernetes resources, monitor health, and troubleshoot issues in the cluster.

#### 7. Deploying a Test Application

To verify that everything is working correctly, we deployed the hello-minikube sample application:

```bash
kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.10
kubectl expose deployment hello-minikube --type=NodePort --port=8080
```

![[Pasted image 20250304004046.png]]
#### 8. Creating a Simple Pod

To understand the most basic Kubernetes object, we created a temporary pod:

```bash
kubectl run tmp-pod --image=nginx --restart=Never
```

![[Pasted image 20250305104026.png]]

We then verified that the pod was successfully created:

```bash
kubectl get pods
```

![[Pasted image 20250305104159.png]]

This simple pod runs a single container with the nginx web server image. Unlike deployments, this pod won't be automatically recreated if it fails or is deleted.
#### 9. Deploying OWASP Juice Shop Application

Next, we deployed a more complex web application - the OWASP Juice Shop, which is a deliberately vulnerable web application for security training.

First, we created a deployment YAML file for the Juice Shop:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: juiceshop-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: juiceshop
  template:
    metadata:
      labels:
        app: juiceshop
    spec:
      containers:
      - name: juiceshop
        image: bkimminich/juice-shop
        ports:
        - containerPort: 3000
```

![[Pasted image 20250305104315.png]]

We applied this configuration to create the deployment:

```bash
kubectl apply -f juiceshop-deployment.yaml
```

After running the command, we checked the status of our pods:

```bash
kubectl get pods
```

![[Pasted image 20250308162452.png]]

After a few moments, we checked again to see the running status:

```bash
kubectl get pods
```

![[Pasted image 20250308162520.png]]

While the pods were running, we still couldn't access the web application because it wasn't exposed outside the cluster. To make it accessible, we needed to create a Service.

We created a service YAML file to expose the application:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: juiceshop-service
spec:
  selector:
    app: juiceshop
  ports:
  - port: 3000
    targetPort: 3000
    nodePort: 30635
  type: NodePort
```

![[Pasted image 20250308162631.png]]

We applied this service configuration:

```bash
kubectl apply -f juiceshop-service.yaml
```

Then we checked our services to confirm it was created:

```bash
kubectl get services
```

![[Pasted image 20250308162917.png]]

The service was successfully created and mapped to the internal IP 10.101.89.47 and port 30635. However, to access it from our browser, we needed the external IP of the Minikube node.

to get the ip of the node, we run minikube ip as shown in the below screenshot
![[Pasted image 20250308162948.png]]

Now let me navigate to the web browser and see if im able to access the web application from the node ip address and the port specified and exposed ![[Pasted image 20250308163210.png]]
as you can see in the above screencap, we are able to access the web application from the ip and port, 

let us test the main advantage of the kubernetes, now let us explicitly specify that i want 10 contianers instance running of the same web application
that we can do by editing the deployment directly and it will reflect the changes in the realtime, 
shown in the following screencap
![[Pasted image 20250308163426.png]]

as we can see, there are total 10 pods running and few are being created, and this is how the load is balanced among the contianers, instances

let us now test the  self healing feature of the kubernetes, let us sabotage or intentionally crash the one of the instance and see the kubernetes behaviour
as shown in the below screeenshot, i have deleted one of the pods for juice shop web app, and then we run get pods, we can see, the new pod is taking birth again, and is in container creating state
self healing in action 
![[Pasted image 20250308164545.png]]
with the following i can assign the resources to the deployment pods# Update deployment with resource limits and requests
kubectl set resources deployment juiceshop-deployment --limits=cpu=200m,memory=256Mi --requests=cpu=100m,memory=128Mi

With the following i am able to scale up and scale down the pods
```bash
kubectl scale deployment juiceshop-deployment --replicas=15
```


### Observation

During this Minikube lab, the following key observations were made:

* **Deployment and Management**: Kubernetes efficiently managed both simple and complex application deployments using declarative YAML configurations, automating the container lifecycle process with minimal user intervention.

* **Scaling and Self-Healing**: The platform demonstrated impressive capabilities for both horizontal scaling (from 3 to 15 replicas without disruption) and automatic recovery from failures. When pods were deliberately deleted, Kubernetes immediately created replacements to maintain the desired state.

* **Resource Control**: Fine-grained CPU and memory management was achieved through simple kubectl commands, allowing efficient resource utilization even on modest hardware.

* **Monitoring and Networking**: The Minikube dashboard provided intuitive visualization of cluster status, while the service abstraction successfully exposed applications externally and managed internal service discovery seamlessly.

### Conclusion

This Minikube laboratory exercise provided a valuable hands-on introduction to Kubernetes and container orchestration. Through practical experimentation, we gained insights into Kubernetes operations and benefits for modern application deployment.

**Key learnings:**

* **Kubernetes Fundamentals**: We successfully demonstrated core concepts (pods, deployments, services, scaling) in a controlled environment using Minikube, without the complexity of cloud deployment.

* **Container Orchestration Benefits**:
   - **Scalability**: Simple commands for scaling applications to handle varying workloads
   - **Reliability**: Automatic recovery from failures through self-healing mechanisms
   - **Consistency**: Declarative configurations ensuring consistent application behavior
   - **Resource Efficiency**: Fine-grained control over computing resources

* **Real-World Relevance**: The techniques learned apply directly to microservices architecture, CI/CD pipelines, high-availability applications, and containerized development environments.

Minikube has proven invaluable for learning Kubernetes in a safe, local environment. Even with modest hardware resources, we were able to implement enterprise-grade reliability features, demonstrating how container orchestration can bring cloud-native practices to any development environment.


