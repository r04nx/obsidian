
Spun up brand new VM, equipped with minikube setup preinstalled and sshed in to it as shown in the following screenshot
![[Pasted image 20250416003645.png]]
No resources when i do, kubectl get pods
![[Pasted image 20250416003715.png]]

I have successfully installed helm with the following command
sudo snap install helm --classic
![[Pasted image 20250416004239.png]]

Now i have added the repositry for graffana and prometheus via following command
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

as shown in the following screenshot
![[Pasted image 20250416004640.png]]

Now i have created a nginx deployment yml file as shown in the following screenshot 
![[Pasted image 20250416004842.png]]

the file contents are as follows
```yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginxdemos/hello
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  selector:
    app: nginx
  ports:
  - port: 80
    targetPort: 80
    protocol: TCP
```
now appliied the deployment via the command as shown in the following screenshot and after running 
kubectl get all it shows me provisioning and then in ready state
![[Pasted image 20250416005025.png]]

Now using the following command i have port forwarded to my host vm as shown in the following screenshot and the output is visible
```bash 
kubectl port-forward --address 0.0.0.0 service/nginx 8081:80
Forwarding from 0.0.0.0:8081 -> 80
Handling connection for 8081
```

![[Pasted image 20250416010953.png]]
![[Pasted image 20250416011245.png]]

Install prometheus via the following
```bash
helm install prometheus prometheus-community/prometheus
```
and it shows this output as shown in the following screenshot
![[Pasted image 20250416011531.png]]
### Add NGINX Exporter 
```bash
helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update
```



