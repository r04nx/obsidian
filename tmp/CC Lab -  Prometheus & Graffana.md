## Student Details
- **Name:** Rohan Prakash Pawar
- **UID:** 2023201020
- **Branch:** EXTC

---
Aim:
Objective:
Software Requirements:
Procedure Followed:

Firs i created a brand new Ubuntu Jammy VM via incus for the Lab practical, as shown in the following screenshot:
![[Pasted image 20250312092447.png]]

And then I SSHed in to the Devops VM as shown in the below image after setting up the ssh key pairs,
![[Pasted image 20250312092643.png]]
installed and verified docker as shown in the screenshot below
![[Pasted image 20250312092743.png]]
I created a directory for the lab practical called prometheus and in that i create the config file for the prometheus, to make promotheus to fetch the metrics from the endpoin we will be creating via node exporter (a docker image that exports the logs metrics, via http method on route /metrics, things like cpu, memory load etc), and the interval time, is set to be 1s
![[Pasted image 20250312093243.png]]
Now I in the following screenshot  I have started the nodeexporter docker instance and run docker ps, node exporter has successfully started
![[Pasted image 20250312094008.png]]
now when i do 
```bash
curl localhost:9100 
```
i am able to see tons of logs metrics, exported by the node exporter,
and with the help of the prometheus docker instance we'll store and query the log metrics efficiently
u can see the logs in the following screenshot
![[Pasted image 20250312094212.png]]
now with the following command and making use of the prometheus.yml configuration file we'll create a prometheus docker container which will fetch the logs metrics from the nodeexporter, 
```bash
 docker run --network host \
  -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml \
  --name prometheus \
  prom/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --web.listen-address=:9091
```
and the prometheus.yml is as following
```yaml
global:
  scrape_interval: 1s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets: ["localhost:9100"]
```
with the docker container i have started the promotheus container as shown in the following screenshot
![[Pasted image 20250312095727.png]]
let us navigate to the web browser and see if it is accessible 
we can see the nodeexporter successfully through web browser, successfully as shown in the screenshot below
![[Pasted image 20250312095051.png]]
Now I am able to see the Promotheus Web UI on the port 9091
![[Pasted image 20250312095809.png]]
Let us try running some queries to query the logs and get the insights
As we can see we are able to query and get the logs in below screenshot
with the query as follows
```promql
rate(node_cpu_seconds_total[5m])
```

![[Pasted image 20250312095927.png]]


