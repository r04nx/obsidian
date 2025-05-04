
![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfmrx-hwpOl-VrrjC96x--RBfrvf59z-usWwPEq-IsZp4qAGNdvNWnqzXB-Oswlmll194SNcTflllAZIiBU0LbOULq9mKED01j72bAoZbTGV6CQLqwTe-G0DgeCUjUMJ5omfXADpGIUYAfLeiuoTg?key=7Sa9LJ9gxRSLMiay9Z4soqJ8)
## Lab Practical 05: Basic Network Configuration in Cisco Packet Tracer

>[!info] Student Information
>- **Name:**: Rohan Prakash Pawar
>- **UID:** 2023201020
>- **Experiment No:** 05

## Aim
Basic Network Configuration in Cisco Packet Tracer

## Theory
>[!note] 
>Cisco Packet Tracer is a powerful network simulation tool developed by Cisco Systems that allows users to design, configure, and troubleshoot virtual networks. It is widely used in academic environments and professional training to simulate complex networking scenarios without the need for physical hardware.
>
>Packet Tracer supports a wide range of Cisco devices and protocols, enabling users to practice routing, switching, IP addressing, subnetting, VLAN configuration, wireless networking, and more. The platform provides a visual interface where users can drag and drop devices, connect them, and configure their settings through CLI (Command Line Interface) or GUI.

---

## 🌐 PART A: Basic Network Setup

>[!tip] Objective
>- Setup a small network with PCs, a switch, and a router
>- Assign IP addresses to devices
>- Test network connectivity using the ping command

### Required Components
| Device | Count | Purpose |
| ------ | ----- | ------- |
| PC | 2 | End devices for testing connectivity |
| Switch | 1 | Connecting devices at Layer 2 |
| Router | 1 | Providing Layer 3 connectivity |
| Ethernet cables | 3 | Physical connections |

### Procedure

- [ ] **1. Open Cisco Packet Tracer**
  - Launch the software and create a new project

- [ ] **2. Add Network Devices**
  - Drag and drop two PCs from the "End Devices" section
  - Drag and drop one Switch from the "Switches" section
  - Drag and drop one Router from the "Routers" section

- [ ] **3. Connect Devices Using Cables**
  - Use Copper Straight-Through cables to connect:
    - PC0 to Switch (FastEthernet0)
    - PC1 to Switch (FastEthernet1)
    - Switch to Router (GigabitEthernet0/0)

- [ ] **4. Assign IP Addresses to PCs**
  >[!example] PC0 Configuration
  >- IP Address: 192.168.1.2
  >- Subnet Mask: 255.255.255.0
  >- Default Gateway: 192.168.1.1
  
  >[!example] PC1 Configuration
  >- IP Address: 192.168.1.3
  >- Subnet Mask: 255.255.255.0
  >- Default Gateway: 192.168.1.1

- [ ] **5. Configure the Router**
  ```cisco
  enable
  configure terminal
  interface GigabitEthernet0/0
  ip address 192.168.1.1 255.255.255.0
  no shutdown
  exit
  end
  write
  ```

- [ ] **6. Test Connectivity**
  - Open PC0 > Desktop > Command Prompt
  - Type: `ping 192.168.1.3`
  - If successful, the connection is working

### Connection Diagram
![[Pasted image 20250504151417.png]]

### Router Configuration Output
![[Pasted image 20250504151455.png]]
![[Pasted image 20250504151536.png]]
![[Pasted image 20250504151553.png]]

---

## 🌐 PART B: Connecting Networks with Static Routes

>[!tip] Objective
>- Establish connectivity between two networks using static routes

### Required Components
| Device | Count | Purpose |
| ------ | ----- | ------- |
| Router | 2 | Providing routing between networks |
| Switch | 2 | Connecting devices within each network |
| PC | 4 | End devices for testing connectivity |
| Ethernet & Serial Cable | Several | Connecting devices |

### Procedure

- [ ] **1. Configure Network Setup**
  - Connect devices according to the connection diagram

- [ ] **2. Configure Routers**
  - Set up IP addresses and routing tables on both routers
  - Configure static routes to enable cross-network communication

- [ ] **3. Test Connectivity**
  - Ping from PC0 to PC1
  - If successful, routing is working correctly

### Connection Diagram
![[Pasted image 20250504151742.png]]

>[!example] Network Topology
>```mermaid
>graph TD
>    PC0[PC0] --> SW1[Switch1]
>    PC1[PC1] --> SW1
>    SW1 --> R1[Router1]
>    R1 <--> R2[Router2]
>    R2 --> SW2[Switch2]
>    SW2 --> PC2[PC2]
>    SW2 --> PC3[PC3]
>```

### Router Configuration Output
![[Pasted image 20250504151641.png]]
![[Pasted image 20250504151709.png]]
![[Pasted image 20250504151801.png]]

---

## 🌐 PART C: DHCP Configuration

>[!tip] Objective
>- Setup DHCP to dynamically assign IPs

### Required Components
| Device | Count | Purpose |
| ------ | ----- | ------- |
| Router | 1 | Acting as DHCP server |
| Switch | 1 | Connecting network devices |
| PC | 3 | Clients receiving DHCP addresses |

### Procedure

- [ ] **1. Configure Router as a DHCP Server**
  - Set up DHCP pool with appropriate network settings

- [ ] **2. Set PCs to Obtain IP Dynamically**
  - Go to PC0, PC1, PC2 > Desktop > IP Configuration
  - Select DHCP option

- [ ] **3. Test Connectivity**
  - Run `ipconfig /all` on PCs to check assigned IPs
  - Verify connectivity between devices

### Connection Diagram
![[Pasted image 20250504151844.png]]

### DHCP Configuration Output
![[Pasted image 20250504151825.png]]

![[Pasted image 20250504151908.png]]
![[Pasted image 20250504151924.png]]

---

## 🎓 Conclusion
>[!success] Summary
>In this experiment, we successfully configured a basic computer network using Cisco Packet Tracer. Key tasks included assigning IP addresses to PCs and routers, configuring switches, verifying connectivity through the ping command, and ensuring proper communication across devices.
>
>This exercise helped reinforce fundamental networking concepts such as IP addressing, subnetting, and default gateway configuration. It also provided hands-on experience with Cisco networking devices, which is essential for understanding how real-world networks operate.
>
>Overall, the lab demonstrated how correct configuration ensures efficient data transmission within a network.

## 📊 Results and Analysis
| Test               | Result                  |
| ------------------ | ----------------------- |
| PC0 to PC1 Ping    | Successful              |
| PC0 to Router Ping | Successful              |
| DHCP IP Assignment | IPs in configured range |

