---
share_link: https://share.note.sx/14ejtvfv#83HJHDETCB0eBET+e2cxhiNDhdkmM5K59iaILPciKr4
share_updated: 2025-09-19T20:50:36+05:30
---
# Tailscale Installation SOP - Advantech Industrial IoT Gateway

## Document Information
- **Version**: 1.0
- **Date**: 2025-09-19
- **Device**: Advantech ECU-1051 (ARM-based Industrial IoT Gateway)
- **OS**: Linux with Busybox (Embedded)
- **Tailscale Version**: 1.76.1

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Network Configuration](#network-configuration)
3. [Tailscale Installation](#tailscale-installation)
4. [Initial Setup & Authentication](#initial-setup--authentication)
5. [Auto-Start Configuration](#auto-start-configuration)
6. [Verification & Testing](#verification--testing)
7. [Troubleshooting](#troubleshooting)
8. [Maintenance](#maintenance)

## Prerequisites
```bash
wget  https://pkgs.tailscale.com/stable/tailscale_1.76.1_arm.tgz -o tailscale_arm.tgz
sshpass -p '' scp tailscale_arm.tgz root@10.0.0.1:/home/
sshpass -p '' ssh root@10.0.0.1 "ls -la /usr/ && mkdir -p /usr/local/bin"
sshpass -p '' ssh root@10.0.0.1 "cd /usr/local/bin && tar -xzf /home/tailscale_arm.tgz --strip-components=1 tailscale_1.76.1_arm/tailscale tailscale_1.76.1_arm/tailscaled && ls -la"


sshpass -p '' ssh root@10.0.0.1 "chmod +x /usr/local/bin/tailscale* && /usr/local/bin/tailscale version"

sshpass -p '' ssh root@10.0.0.1 "rm /home/tailscale_arm.tgz && mkdir -p /var/lib/tailscale && mkdir -p /etc/default"

sshpass -p '' ssh root@10.0.0.1 "timeout 10 /usr/local/bin/tailscaled --state=/var/lib/tailscale/tailscaled.state --socket=/var/lib/tailscale/tailscaled.sock --tun=userspace-networking"


```

### Hardware Requirements
- Advantech Industrial IoT Gateway (ECU-1051 or similar)
- Two Ethernet interfaces (eth0 for LAN, eth1 for WAN)
- Internet connectivity via WAN interface
- Minimum 100MB free storage

### Access Requirements
- SSH access to the IoT gateway
- Root credentials (default: empty password)
- Tailscale account with auth key
- Network access from management device

### Tools Required
- SSH client (OpenSSH)
- `sshpass` utility for automated SSH connections
- `curl` or web browser for testing

## Network Configuration

### 1. Initial Network Assessment

```bash
# Connect to IoT Gateway
ssh root@<GATEWAY_IP>
# Note: Default password is empty (just press Enter)

# Check current network configuration
ifconfig
ip addr show
ip route show
```

### 2. Configure WAN Interface (eth1)

The IoT gateway requires proper internet connectivity via eth1 for Tailscale to function.

```bash
# Check current eth1 status
ifconfig eth1

# If eth1 doesn't have IP, restart DHCP client
killall -9 udhcpc 2>/dev/null
udhcpc -i eth1 -x hostname:ecu1051-455071 -b -t 10 -n &
sleep 8

# Verify internet connectivity
ping -c 3 8.8.8.8

# Check routing table
ip route show
```

**Expected Output:**
```
default via 10.10.57.1 dev eth1 metric 5
10.0.0.0/24 dev eth0 proto kernel scope link src 10.0.0.1
10.10.57.0/24 dev eth1 proto kernel scope link src 10.10.57.3
```

### 3. Configure LAN Interface (eth0)

```bash
# eth0 should be configured for local network
# Default configuration: 10.0.0.1/24
ifconfig eth0
```

## Tailscale Installation

### 1. Check Existing Installation

```bash
# Check if Tailscale is already installed
which tailscale
which tailscaled
ls -la /usr/local/bin/tail*
```

### 2. Installation Process

**Note**: Tailscale was pre-installed on this device. For manual installation:

```bash
# Download Tailscale for ARM Linux (if needed)
# This step is typically not required as it's pre-installed

# Verify installation
/usr/local/bin/tailscale version
/usr/local/bin/tailscaled --version
```

**Expected Output:**
```
1.76.1
  tailscale commit: 24929f6b611127cdc40d45ef40d75c6afc1fcc4c
  other commit: 5e54dcf15265cb83e84e617a5a7e0c1b013c61c7
  go version: go1.23.1
```

## Initial Setup & Authentication

### 1. Prepare Environment

```bash
# Create necessary directories
mkdir -p /var/run/tailscale
mkdir -p /home/root/.cache/Tailscale

# Check available storage
df -h
# Ensure sufficient space in /home partition
```

### 2. Start Tailscale Daemon

```bash
# Start tailscaled with proper configuration
/usr/local/bin/tailscaled \
    --state=/home/tailscale.state \
    --socket=/var/run/tailscale/tailscaled.sock \
    --tun=tailscale0 \
    --cleanup &

# Wait for daemon to initialize
sleep 5

# Verify daemon is running
ps aux | grep tailscaled | grep -v grep
```

### 3. Authenticate with Auth Key

```bash
# Use your Tailscale auth key for authentication
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    up \
    --auth-key=tskey-auth-<YOUR_AUTH_KEY> \
    --accept-routes \
    --accept-dns=false

# Wait for authentication to complete
sleep 10
```

### 4. Verify Connection

```bash
# Check Tailscale status
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    status

# Get assigned Tailscale IP
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    ip
```

**Expected Output:**
```
100.77.175.49   ecu1051-455071       your-email@domain   linux   -
100.77.175.49
fd7a:115c:a1e0::8532:af31
```

## Auto-Start Configuration

### 1. Create Startup Script

```bash
# Create auto-start script
cat > /home/sysuser/tailscale_autostart.sh << 'SCRIPT_EOF'
#!/bin/sh
# Tailscale Auto-Start Script
echo "Starting Tailscale auto-start at $(date)" >> /home/tailscale_startup.log

# Wait for network to be available
sleep 15

# Kill any existing tailscaled processes
killall tailscaled 2>/dev/null || true
sleep 2

# Ensure directories exist
mkdir -p /var/run/tailscale

# Start tailscaled daemon
/usr/local/bin/tailscaled \
    --state=/home/tailscale.state \
    --socket=/var/run/tailscale/tailscaled.sock \
    --tun=tailscale0 &

echo "Tailscale daemon started at $(date)" >> /home/tailscale_startup.log
SCRIPT_EOF

# Make script executable
chmod +x /home/sysuser/tailscale_autostart.sh
```

### 2. Manual Startup (After Reboot)

Since the embedded system has a read-only `/etc` directory, auto-start must be manually configured:

```bash
# After each reboot, run:
/home/sysuser/tailscale_autostart.sh

# Or add to any existing startup scripts in /home/sysuser/
```

## Verification & Testing

### 1. Network Interface Verification

```bash
# Check all network interfaces
ifconfig

# Verify tailscale0 interface
ifconfig tailscale0
```

**Expected tailscale0 output:**
```
tailscale0 Link encap:UNSPEC  HWaddr 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  
          inet addr:100.77.175.49  P-t-P:100.77.175.49  Mask:255.255.255.255
          inet6 addr: fd7a:115c:a1e0::8532:af31/128 Scope:Global
          UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1280  Metric:1
```

### 2. Connectivity Testing

```bash
# Test connectivity to other Tailscale devices
# Replace IP with actual device from your network
ping -c 3 100.93.34.45

# Test DNS resolution (with explicit DNS server)
nslookup google.com 8.8.8.8
```

### 3. Web Dashboard Access

The device runs a web dashboard on HTTPS port 443:

```bash
# Test local dashboard access
curl -s -k -I https://127.0.0.1/

# From external device, test via Tailscale IP:
curl -s -k -I https://100.77.175.49/
```

**Access URLs:**
- **Local Network**: `https://10.0.0.1`
- **Internet**: `https://10.10.57.3` (if accessible)
- **Tailscale**: `https://100.77.175.49` ✅ **Recommended**

### 4. SSH Access Testing

```bash
# From another Tailscale device:
ssh root@100.77.175.49
# Password: (empty - just press Enter)
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Tailscale Daemon Won't Start

**Symptoms:**
- `tailscaled` process not found
- Connection refused errors

**Solutions:**
```bash
# Check for conflicting processes
ps aux | grep tailscale
killall tailscaled 2>/dev/null

# Check storage space
df -h
# If /tmp is full, use /home for state:
rm -f /tmp/tailscale.state*

# Restart with verbose logging
/usr/local/bin/tailscaled \
    --state=/home/tailscale.state \
    --socket=/var/run/tailscale/tailscaled.sock \
    --tun=tailscale0 \
    --verbose=2 &
```

#### 2. No Internet Connectivity

**Symptoms:**
- DNS resolution failures
- Cannot reach Tailscale servers

**Solutions:**
```bash
# Check network interfaces
ip addr show
ip route show

# Restart DHCP client on WAN interface
killall udhcpc 2>/dev/null
udhcpc -i eth1 -x hostname:ecu1051-455071 -b -t 10 -n &
sleep 10

# Test connectivity
ping -c 3 8.8.8.8
nslookup google.com 8.8.8.8
```

#### 3. Authentication Failures

**Symptoms:**
- "Not logged in" status
- Auth key errors

**Solutions:**
```bash
# Check current status
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    status

# Re-authenticate with fresh auth key
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    up \
    --auth-key=tskey-auth-<NEW_AUTH_KEY> \
    --accept-routes \
    --accept-dns=false
```

#### 4. Network Interface Issues

**Symptoms:**
- tailscale0 interface not created
- IP assignment problems

**Solutions:**
```bash
# Check kernel modules
lsmod | grep tun

# Manually create TUN interface if needed
modprobe tun 2>/dev/null || echo "TUN module not available"

# Restart daemon with cleanup
killall tailscaled 2>/dev/null
sleep 3
/usr/local/bin/tailscaled \
    --state=/home/tailscale.state \
    --socket=/var/run/tailscale/tailscaled.sock \
    --tun=tailscale0 \
    --cleanup &
```

#### 5. After Power Outage Recovery

**Symptoms:**
- Tailscale not running after reboot
- Network configuration lost

**Complete Recovery Process:**
```bash
# 1. Check network status
ifconfig
ip route show

# 2. Restore WAN connectivity
killall udhcpc 2>/dev/null
udhcpc -i eth1 -x hostname:ecu1051-455071 -b -t 10 -n &
sleep 10

# 3. Test internet
ping -c 3 8.8.8.8

# 4. Start Tailscale
/home/sysuser/tailscale_autostart.sh

# 5. Verify connection
sleep 15
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    status
```

### Debug Commands

```bash
# Check system logs
dmesg | tail -20

# Monitor network changes
ip monitor

# Check process status
ps aux | grep -E "(tailscale|dhcp|network)"

# Test connectivity step by step
ping -c 1 127.0.0.1          # Loopback
ping -c 1 10.0.0.1           # Local interface
ping -c 1 10.10.57.1         # Gateway
ping -c 1 8.8.8.8            # Internet
ping -c 1 100.77.175.49      # Tailscale (self)
```

## Maintenance

### Regular Health Checks

```bash
# Weekly status check
/usr/local/bin/tailscale \
    --socket=/var/run/tailscale/tailscaled.sock \
    status

# Check daemon uptime
ps aux | grep tailscaled

# Verify network connectivity
ping -c 3 8.8.8.8
```

### Log Management

```bash
# Check startup logs
cat /home/tailscale_startup.log

# Monitor real-time logs (limited on embedded system)
dmesg | grep tailscale
```

### Performance Monitoring

```bash
# Check network statistics
cat /proc/net/dev

# Monitor memory usage
free -m

# Check disk space
df -h
```

## Quick Reference Commands

### Essential Operations

| Operation      | Command                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Start Daemon   | `/usr/local/bin/tailscaled --state=/home/tailscale.state --socket=/var/run/tailscale/tailscaled.sock --tun=tailscale0 &` |
| Check Status   | `/usr/local/bin/tailscale --socket=/var/run/tailscale/tailscaled.sock status`                                            |
| Get IP Address | `/usr/local/bin/tailscale --socket=/var/run/tailscale/tailscaled.sock ip`                                                |
| Stop Daemon    | `killall tailscaled`                                                                                                     |
| Restart DHCP   | `killall udhcpc; udhcpc -i eth1 -x hostname:ecu1051-455071 -b &`                                                         |
| Test Internet  | `ping -c 3 8.8.8.8`                                                                                                      |

---

**Note**: This document is based on the successful installation and configuration of Tailscale on an Advantech ECU-1051 Industrial IoT Gateway. Commands and procedures may vary slightly for different Advantech models.
