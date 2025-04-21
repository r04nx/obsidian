# Webserver Monitoring via Minikube, Prometheus & Grafana
# Lab Practical Report

## Student Details
- **Student Name:** Rohan Pawar
- **UID:** 2023201020
- **Batch:** C
- **Branch:** EXTC
- **Course:** Cloud Computing
- **Date:** April 18, 2025

---

## Aim
To set up a monitoring system for a web server using Minikube, Prometheus, and Grafana to track server performance metrics and visualize them in real-time.

---

## Introduction
In modern cloud environments, monitoring is a critical aspect of maintaining reliable and high-performing applications. This lab demonstrates how to implement a comprehensive monitoring solution for a web server using open-source tools in a Kubernetes environment:

- **Minikube**: A tool that runs a single-node Kubernetes cluster locally for development and testing
- **Prometheus**: An open-source systems monitoring and alerting toolkit
- **Grafana**: A multi-platform open-source analytics and interactive visualization web application

Together, these tools provide a powerful solution for monitoring web server performance, collecting metrics, and visualizing data through customizable dashboards.

---

## Software Requirements
1. Minikube (pre-installed on the VM)
2. kubectl CLI tool
3. Helm package manager
4. Prometheus
5. Grafana
6. NGINX web server (for demonstration)
7. Apache Benchmark (for load testing)

---

## Components and Their Purposes

### 1. Grafana
Grafana is a multi-platform open-source analytics and interactive visualization web application. It provides charts, graphs, and alerts when connected to supported data sources.

### 2. Prometheus
Prometheus is an open-source systems monitoring and alerting toolkit. It collects and stores metrics as time series data, with metadata stored as key-value pairs.

### 3. NGINX Demo Server
A simple NGINX-based web server used as a target application to monitor.

### 4. NGINX Exporter
The NGINX exporter extracts metrics from NGINX and exposes them in a format that Prometheus can scrape.

---

## Procedure

### 1. Setting Up the Environment

1. Started with a brand new VM with minikube pre-installed and connected via SSH
   ![[Pasted image 20250416003645.png]]

2. Verified the initial state of the Kubernetes cluster
   ![[Pasted image 20250416003715.png]]

3. Installed Helm package manager
   ```bash
   sudo snap install helm --classic
   ```
   ![[Pasted image 20250416004239.png]]

4. Added Prometheus and Grafana repositories to Helm
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   ```
   ![[Pasted image 20250416004640.png]]

### 2. Deploying NGINX Webserver

1. Created an NGINX deployment YAML file
   ![[Pasted image 20250416004842.png]]

2. The deployment file contents:
   ```yaml
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

3. Applied the deployment and verified its status
   ![[Pasted image 20250416005025.png]]

4. Set up port forwarding to access the NGINX server
   ```bash
   kubectl port-forward --address 0.0.0.0 service/nginx 8081:80
   ```
   ![[Pasted image 20250416010953.png]]
   ![[Pasted image 20250416011245.png]]

### 3. Setting Up Prometheus

1. Installed Prometheus using Helm
   ```bash
   helm install prometheus prometheus-community/prometheus
   ```
   ![[Pasted image 20250416011531.png]]

2. Created a ConfigMap for Prometheus configuration:
   ```yaml
   # prometheus-config.yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: prometheus-config
     namespace: monitoring
   data:
     prometheus.yml: |
       global:
         scrape_interval: 15s
         evaluation_interval: 15s
       
       scrape_configs:
         - job_name: 'prometheus'
           static_configs:
             - targets: ['localhost:9090']
         
         - job_name: 'nginx-exporter'
           static_configs:
             - targets: ['nginx-exporter:9113']
   ```

3. Created Prometheus Deployment and Service:
   ```yaml
   # prometheus-deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: prometheus
     namespace: monitoring
   spec:
     selector:
       matchLabels:
         app: prometheus
     template:
       metadata:
         labels:
           app: prometheus
       spec:
         containers:
         - name: prometheus
           image: prom/prometheus:v2.37.0
           ports:
           - containerPort: 9090
           volumeMounts:
           - name: config
             mountPath: /etc/prometheus
         volumes:
         - name: config
           configMap:
             name: prometheus-config
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: prometheus
     namespace: monitoring
   spec:
     selector:
       app: prometheus
     ports:
     - port: 9090
       targetPort: 9090
   ```

4. Added NGINX Exporter for metrics collection
   ```bash
   helm repo add nginx-stable https://helm.nginx.com/stable
   helm repo update
   ```

### 4. Setting Up Grafana

1. Created a dedicated monitoring namespace
   ```bash
   kubectl create namespace monitoring
   ```

2. Deployed Grafana in the monitoring namespace
   ```bash
   helm install my-grafana grafana/grafana --namespace monitoring
   ```
   ![[Pasted image 20250417235751.png]]
   ![[Pasted image 20250417235913.png]]

3. Verified Grafana deployment
   ```bash
   kubectl get all -n monitoring
   ```

   Output showed:
   ```
   NAME                              READY   STATUS    RESTARTS   AGE
   pod/my-grafana-7fdc4cc4b6-687wx   1/1     Running   0          12m

   NAME                 TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
   service/my-grafana   ClusterIP   10.109.188.197   <none>        80/TCP    12m

   NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/my-grafana   1/1     1            1           12m

   NAME                                    DESIRED   CURRENT   READY   AGE
   replicaset.apps/my-grafana-7fdc4cc4b6   1         1         1       12m
   ```

4. Set up port forwarding to access Grafana UI
   ```bash
   kubectl port-forward -n monitoring service/my-grafana 3000:80 &
   ```
   ![[Pasted image 20250418000506.png]]

5. Retrieved Grafana admin password
   ```bash
   kubectl get secret --namespace monitoring my-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
   ```

   This command returned the admin password: `23djtsN7EGZpQ1U16g4TGNR9rKVIRta5X5k127To`

6. Accessed Grafana through the browser
   ![[Pasted image 20250418000705.png]]

### 5. Setting Up NGINX Monitoring

1. Created NGINX Configuration with stub_status:
   ```yaml
   # nginx-config.yaml
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: nginx-config
     namespace: monitoring
   data:
     default.conf: |
       server {
         listen 80;
         
         location / {
           root /usr/share/nginx/html;
           index index.html index.htm;
         }
         
         location /stub_status {
           stub_status on;
           allow all;
         }
       }
   ```

2. Deployed NGINX Demo Server:
   ```yaml
   # nginx-hello-deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-hello
     namespace: monitoring
   spec:
     selector:
       matchLabels:
         app: nginx-hello
     template:
       metadata:
         labels:
           app: nginx-hello
       spec:
         containers:
         - name: nginx
           image: nginxdemos/hello:latest
           ports:
           - containerPort: 80
           volumeMounts:
           - name: nginx-config
             mountPath: /etc/nginx/conf.d
         volumes:
         - name: nginx-config
           configMap:
             name: nginx-config
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: nginx-hello
     namespace: monitoring
   spec:
     selector:
       app: nginx-hello
     ports:
     - port: 80
       targetPort: 80
   ```

3. Deployed NGINX Exporter:
   ```yaml
   # nginx-exporter-deployment.yaml
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: nginx-exporter
     namespace: monitoring
   spec:
     selector:
       matchLabels:
         app: nginx-exporter
     template:
       metadata:
         labels:
           app: nginx-exporter
       spec:
         containers:
         - name: nginx-exporter
           image: nginx/nginx-prometheus-exporter:0.10.0
           args:
           - -nginx.scrape-uri=http://nginx-hello:80/stub_status
           ports:
           - containerPort: 9113
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: nginx-exporter
     namespace: monitoring
   spec:
     selector:
       app: nginx-exporter
     ports:
     - port: 9113
       targetPort: 9113
   ```

4. Verified that all pods were running:
   ```bash
   kubectl get pods -n monitoring
   ```

   Output showed all pods running successfully:
   ```
   NAME                             READY   STATUS    RESTARTS   AGE
   my-grafana-7fdc4cc4b6-687wx      1/1     Running   0          18m
   nginx-exporter-cdff87b88-rcnw7   1/1     Running   0          2m37s
   nginx-hello-779699cdc9-5mxbj     1/1     Running   0          2m43s
   prometheus-5d6d4f7df4-57r9h      1/1     Running   0          2m55s
   ```

### 6. Configuring Prometheus and Grafana Integration

1. Confirmed all components were running properly
   ![[Pasted image 20250418001922.png]]

2. Added Prometheus as a data source in Grafana
   - In Grafana UI, navigated to Configuration > Data sources
   - Selected "Add data source" > "Prometheus"
   - Set URL to http://prometheus:9090
   ![[Pasted image 20250418003426.png]]
   - Saved and tested the connection
   ![[Pasted image 20250418003401.png]]

3. Imported an NGINX dashboard
   - In Grafana UI, clicked "+" > "Import"
   - Entered dashboard ID 12708 (popular NGINX Prometheus dashboard)
   ![[Pasted image 20250418002430.png]]
   - Selected the Prometheus data source and completed the import
   ![[Pasted image 20250418002556.png]]

### 7. Testing the Monitoring Setup

1. Generated test load to the NGINX server using Apache Benchmark tool
   ```bash
   ab -n 500 -c 10 http://localhost:8081/
   ```
   ![[Pasted image 20250418003128.png]]

2. Observed the metrics in Grafana dashboard
   ![[Pasted image 20250418003231.png]]

---

## Observations

1. The Minikube environment successfully hosted all components (NGINX, Prometheus, and Grafana) in a local Kubernetes cluster.

2. Prometheus was able to scrape metrics from the NGINX server and store them in its time-series database.

3. Grafana successfully connected to Prometheus as a data source and displayed the metrics in pre-built dashboards.

4. When load was applied to the NGINX server using Apache Benchmark, the dashboard showed real-time changes in metrics including:
   - Increase in connection count
   - Spike in request rate
   - Changes in response time
   - Distribution of HTTP response codes

5. The monitoring setup provided valuable insights into the web server's performance under load.

6. Helm simplified the deployment process for both Prometheus and Grafana, demonstrating the power of package managers in Kubernetes.

7. The NGINX exporter successfully extracted metrics from the NGINX server and exposed them in a format that Prometheus could scrape.

---

## Results

The lab successfully achieved the following:

1. Established a functioning Kubernetes environment using Minikube

2. Deployed an NGINX web server with a sample application

3. Set up Prometheus for metrics collection from the web server

4. Configured Grafana to visualize the metrics collected by Prometheus

5. Created a complete monitoring pipeline from data collection to visualization

6. Demonstrated the system's capability to detect and display changes in web server performance during load testing

7. Implemented a practical monitoring solution that could be extended to production environments

8. Successfully configured and integrated the NGINX exporter to collect NGINX-specific metrics

---

## Conclusion

This lab demonstrated the implementation of a comprehensive monitoring solution for web servers using Minikube, Prometheus, and Grafana. The integration of these tools creates a powerful system for tracking performance metrics and gaining insights into server behavior.

The monitoring setup successfully detected and visualized changes in server performance during load testing, proving its effectiveness in real-time monitoring scenarios. This approach to monitoring is valuable for:

1. Identifying performance bottlenecks
2. Tracking system resource utilization
3. Establishing baselines for normal operation
4. Detecting anomalies that might indicate problems
5. Supporting capacity planning decisions

In cloud environments, such monitoring is essential for maintaining high availability and optimal performance. The skills acquired in this lab provide a foundation for implementing more complex monitoring solutions in production environments.

The combination of Kubernetes, Prometheus, and Grafana represents a modern approach to infrastructure monitoring that is both powerful and flexible, allowing for customization to meet specific monitoring requirements.

From this lab, we can extend our monitoring capabilities by:
- Creating custom dashboards in Grafana
- Adding more exporters for other applications
- Configuring alerting for important metrics
- Scaling the monitoring infrastructure as needed

---

## Summary of Files and Commands

### Files Created

1. prometheus-config.yaml - Prometheus configuration
2. prometheus-deployment.yaml - Prometheus deployment and service
3. nginx-config.yaml - NGINX configuration with stub_status enabled
4. nginx-hello-deployment.yaml - NGINX demo server deployment and service
5. nginx-exporter-deployment.yaml - NGINX exporter deployment and service

### Commands Used

1. `kubectl get all -n monitoring` - Check existing resources
2. `kubectl apply -f prometheus-config.yaml` - Apply Prometheus configuration
3. `kubectl apply -f prometheus-deployment.yaml` - Deploy Prometheus
4. `kubectl apply -f nginx-config.yaml` - Apply NGINX configuration
5. `kubectl apply -f nginx-hello-deployment.yaml` - Deploy NGINX
'EOF'
'
6. `kubectl apply -f nginx-exporter-deployment.yaml` - Deploy NGINX exporter
7. `kubectl get pods -n monitoring` - Verify pod status
8. `kubectl port-forward -n monitoring service/my-grafana 3000:80` - Access Grafana
9. `kubectl get secret -n monitoring my-grafana -o jsonpath="{.data.admin-password}" | base64 --decode` - Get Grafana password
10. `ab -n 500 -c 10 http://localhost:8081/` - Generate test load with Apache Benchmark

---

**Note:** All commands and configurations in this lab were performed within a controlled Minikube environment and do not affect external systems.
