Institute: Bharatiya Vidya Bhavan's Sardar Patel Institute of Technology (SPIT)
Proeject: ASNA

Deployed the container Lab for the enterprise grade network
![[Pasted image 20250917150949.png]]

Tabular output of the container lab
![[Pasted image 20250917151051.png]]

following is the network topology
![[Pasted image 20250917153209.png]]

```md

📋 DETAILED LAYER BREAKDOWN:
=============================

🔵 CORE LAYER (Network Backbone):
  ├─ core-router     → 172.20.20.4  (Main routing + Quagga)
  ├─ core-firewall   → 172.20.20.12 (Security + iptables/ipset)
  └─ public-web      → 172.20.20.2  (DMZ/Public access)

🟢 DISTRIBUTION LAYER (Aggregation):
  ├─ dist-eng        → 172.20.20.11 (Engineering aggregation)
  ├─ dist-sales      → 172.20.20.13 (Sales aggregation)
  └─ dist-servers    → 172.20.20.3  (Server farm aggregation)

🟡 ACCESS LAYER (User Access):
  ├─ access-eng      → 172.20.20.6  (Engineering access switch)
  └─ access-sales    → 172.20.20.14 (Sales access switch)

💻 END DEVICES:
  Engineering Department:
  ├─ eng-gui         → 172.20.20.10 (Ubuntu Desktop + VNC :6080)
  └─ eng-dev         → 172.20.20.8  (Developer workstation)

  Sales Department:
  ├─ sales-gui       → 172.20.20.9  (Ubuntu Desktop + VNC :6081)
  └─ sales-mobile    → 172.20.20.7  (Mobile device)

🗄️ SERVER INFRASTRUCTURE:
  ├─ web-server      → 172.20.20.16 (Nginx - Enterprise Portal)
  ├─ db-server       → 172.20.20.15 (PostgreSQL + SQLite)
  └─ file-server     → 172.20.20.5  (Samba shares)
```

Summary for the monitoring stack
```
📊 Overall monitoring stack health check...
🔹 Prometheus targets summary:
     15 network-devices: up
      1 prometheus: up
      1 node-exporter: up
      1 cadvisor: up

🔹 Sample network metrics available:
18
Total 'up' metrics: 18

🔹 Network interface metrics available:
Network interface metrics: 59

🔹 Grafana health:
Grafana database status: ok

🎯 MONITORING SETUP COMPLETE!
✅ All 15 network devices are monitored
✅ Prometheus is scraping all targets successfully
✅ Grafana dashboards are available
✅ Real-time network monitoring is active

🔗 Access URLs:
   📈 Prometheus: http://localhost:9090
   📊 Grafana: http://localhost:3000 (admin/asna123)
   🖥️ cAdvisor: http://localhost:8081
```

Contianer lab Network Topology
![[Pasted image 20250917153520.png]]

the following is the graffana dashboard setup with the monitoring stack 
nodeexporter --> prometheus --> graffana
following are few Visulasations from the monitoring graffana dashboard

![[Pasted image 20250917153048.png]]
![[Pasted image 20250917153605.png]]
![[Pasted image 20250917153639.png]]
![[Pasted image 20250917153709.png]]
![[Pasted image 20250917153727.png]]

Now let us start working on the tiny  agent
following points to consider
what to detect and remediation sequence for the agent?
![[Pasted image 20250920204655.png]]

applied configuration drift via ansible in the eng container and this is the graffana dashboard
![[Pasted image 20250920204803.png]]![[Pasted image 20250920204842.png]]

Self Healing Agent
results logs
![[Pasted image 20250920205502.png]]

agent test results 
![[Pasted image 20250920220601.png]]

