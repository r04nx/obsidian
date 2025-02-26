---
share_link: https://share.note.sx/quwsbmk5#3JUjEOZDZ3dXuD5H4/GOF3xBBsRuphlhaxQvlHGgDFQ
share_updated: 2025-02-26T17:47:24+05:30
---
# Lab Practical Report - CCN

## Student Information
- **Name:** Rohan Prakash Pawar  
- **UID:** 2023201020  
- **Course:** CCN  
- **Branch:** EXTC - B2  
- **Lab:** 3  

---

## Table of Contents
1. [Aim](#aim)
2. [Objective](#objective)
3. [Theoretical Background](#theoretical-background)
4. [Program 1: IP Class Identification Using Numeric Input](#program-1-ip-class-identification-using-numeric-input)
5. [Program 2: IP Class Identification Using IP Address](#program-2-ip-class-identification-using-ip-address)
6. [Program 3: IP Class Information Retrieval](#program-3-ip-class-information-retrieval)
7. [Program 4: Private and Public IP Retrieval](#program-4-private-and-public-ip-retrieval)
8. [Program 5: Subnet Calculator](#program-5-subnet-calculator)
9. [Program Output](#program-output)
10. [Calculations](#calculations)
11. [Conclusion](#conclusion)

---

## Aim
To implement Python programs for identifying IP address classes, retrieving IP address information, and differentiating between private and public IP addresses.

## Objective
- Understand different IP address classes.
- Implement logic to classify IP addresses.
- Retrieve private and public IP addresses.
- Display class information for different IP ranges.

---

## Theoretical Background
IP addresses are classified into five different classes: A, B, C, D, and E. The classification is based on the first octet of the IP address.

### IP Address Classes
| Class | First Octet Range | Default Subnet Mask | Usage |
|-------|------------------|--------------------|--------|
| A     | 1 - 126         | 255.0.0.0         | Large Networks |
| B     | 128 - 191       | 255.255.0.0       | Medium Networks |
| C     | 192 - 223       | 255.255.255.0     | Small Networks |
| D     | 224 - 239       | N/A (Multicast)   | Multicasting |
| E     | 240 - 255       | N/A (Experimental)| Research |

---

## Program 1: IP Class Identification Using Numeric Input

### Code:
```python
number = int(input("Enter number: "))
if number == 1:
    print("Class A")
elif number == 10:
    print("Class B")
elif number == 110:
    print("Class C")
elif number == 1110:
    print("Class D")
elif number == 11110:
    print("Class E")
else:
    print("Invalid input")
```


---

## Program 2: IP Class Identification Using IP Address

### Code:
```python
ip_address = input("Please enter an IP address (like 192.168.1.1): ")
first_number = int(ip_address.split('.')[0])

if first_number >= 1 and first_number <= 126:
    print("This is a Class A IP address")
elif first_number >= 128 and first_number <= 191:
    print("This is a Class B IP address")
elif first_number >= 192 and first_number <= 223:
    print("This is a Class C IP address")
elif first_number >= 224 and first_number <= 239:
    print("This is a Class D IP address")
elif first_number >= 240 and first_number <= 255:
    print("This is a Class E IP address")
else:
    print("This is not a valid IP address")
```


---

## Program 3: IP Class Information Retrieval

### Code:
```python
ip_classes = {
    'A': {'range': '1.0.0.0 to 126.255.255.255', 'first_octet': '1-126', 'subnet_mask': '255.0.0.0', 'networks': '126', 'private_range': '10.0.0.0 to 10.255.255.255', 'network_bits': '8', 'host_bits': '24'},
    'B': {'range': '128.0.0.0 to 191.255.255.255', 'first_octet': '128-191', 'subnet_mask': '255.255.0.0', 'networks': '16,384', 'private_range': '172.16.0.0 to 172.31.255.255', 'network_bits': '16', 'host_bits': '16'},
    'C': {'range': '192.0.0.0 to 223.255.255.255', 'first_octet': '192-223', 'subnet_mask': '255.255.255.0', 'networks': '2,097,152', 'private_range': '192.168.0.0 to 192.168.255.255', 'network_bits': '24', 'host_bits': '8'},
    'D': {'range': '224.0.0.0 to 239.255.255.255', 'first_octet': '224-239', 'subnet_mask': 'N/A (Multicast)', 'networks': 'N/A', 'private_range': 'N/A', 'network_bits': 'N/A', 'host_bits': 'N/A'},
    'E': {'range': '240.0.0.0 to 255.255.255.255', 'first_octet': '240-255', 'subnet_mask': 'N/A (Experimental)', 'networks': 'N/A', 'private_range': 'N/A', 'network_bits': 'N/A', 'host_bits': 'N/A'}
}

ip_class = input("Enter IP class (A/B/C/D/E): ").upper()
if ip_class in ip_classes:
    info = ip_classes[ip_class]
    print(f"\nInformation for IP Class {ip_class}:")
    print("=" * 50)
    for key, value in info.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print("=" * 50)
else:
    print("Invalid input! Please enter A, B, C, D, or E.")
```


---

## Program 4: Private and Public IP Retrieval

### Code:
```python
import socket
import requests

def get_private_ip():
    return socket.gethostbyname(socket.gethostname())

def get_public_ip():
    try:
        return requests.get('https://api.ipify.org').text
    except requests.RequestException:
        return "Could not retrieve public IP"

print(f"Private IP: {get_private_ip()}")
print(f"Public IP: {get_public_ip()}")
```

---

## Program 5: Subnet Calculator

### Code:
```python
hosts = int(input("\U0001F5A5️ Enter the number of Hosts required? "))

```python
hosts = int(input("\U0001F5A5️ Enter the number of Hosts required? "))
    n += 1

subnet_mask = 32 - n
block_size = 2**n
subnet_mask_octets = [255, 255, 255, 256 - block_size] if subnet_mask >= 24 else [255, 255, 256 - block_size, 0]

print("Subnet Mask in Binary: " + ".".join([bin(octet)[2:].zfill(8) for octet in subnet_mask_octets]))

if block_size > hosts:
    print("🚨 Waste IP addresses (Kusriya): 🗑️ " + str(int(block_size) - int(hosts)))

print("\n🔢 Hosts per Subnet: " + str(block_size - 2))
print("🛡️ Subnet Mask: /" + str(subnet_mask) + " (" + ".".join(map(str, subnet_mask_octets)) + ")")

subnet_start = 0
while subnet_start < 256:
    print("\n🌍 Subnet: 192.168.1." + str(subnet_start) + "/" + str(subnet_mask))
    print("🔗 Network ID: 192.168.1." + str(subnet_start))
    print("📡 Usable Range: 192.168.1." + str(subnet_start + 1) + " - 192.168.1." + str(subnet_start + block_size - 2))
    print("📢 Broadcast ID: 192.168.1." + str(subnet_start + block_size - 1))
    subnet_start += block_size

```

---
## Program Output
### Program 1 Output
![[Pasted image 20250226173352.png]]

### Program 2 Output
![[Pasted image 20250226173412.png]]

### Program 3 Output
![[Pasted image 20250226173443.png]]

### Program 4 Output
![[Pasted image 20250226173506.png]]


### Program 5 Output
![[Pasted image 20250226174450.png]]

---
## Calculations
- The range of IP classes is determined based on the first octet value.
- Subnet mask determines the division between network and host portions.
- Public and private IP addresses help in network security and management.

---

## Conclusion
This lab covered the classification of IP addresses into different classes, retrieving IP details, and distinguishing between public and private IPs using Python programming.
