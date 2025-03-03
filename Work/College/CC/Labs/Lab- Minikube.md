Installed Minikube:
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && sudo install minikube-linux-amd64 /usr/local/bin/minikube
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  119M  100  119M    0     0  5639k      0  0:00:21  0:00:21 --:--:-- 6130k
![[Pasted image 20250304001426.png]]
Verified the Minikube Installation
![[Pasted image 20250304001602.png]]
verifying Docker installed
![[Pasted image 20250304001646.png]]

Setting the docker as the Driver for the minikube
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
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by defaul
![[Pasted image 20250304003314.png]]

to be ocred:
![[Pasted image 20250304003431.png]]

Started the Minikube Dashboard via
![[Pasted image 20250304003949.png]]

![[Pasted image 20250304004000.png]]

Started this application
![[Pasted image 20250304004046.png]]