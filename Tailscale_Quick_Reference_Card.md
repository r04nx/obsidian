# Tailscale Quick Reference Card - Advantech IoT

## Emergency Recovery (After Power Outage)

```bash
# 1. Connect via local network
ssh root@10.0.0.1
# (Empty password - just press Enter)

# 2. Restore WAN connectivity
killall udhcpc 2>/dev/null
udhcpc -i eth1 -x hostname:ecu1051-455071 -b -t 10 -n &
sleep 10

# 3. Test internet
ping -c 3 8.8.8.8

# 4. Start Tailscale
/home/sysuser/tailscale_autostart.sh

# 5. Verify connection (wait 15 seconds)
/usr/local/bin/tailscale --socket=/var/run/tailscale/tailscaled.sock status
```

## Essential Commands

| Task | Command |
|------|---------|
| **Check Status** | `/usr/local/bin/tailscale --socket=/var/run/tailscale/tailscaled.sock status` |
| **Get IP** | `/usr/local/bin/tailscale --socket=/var/run/tailscale/tailscaled.sock ip` |
| **Start Daemon** | `/usr/local/bin/tailscaled --state=/home/tailscale.state --socket=/var/run/tailscale/tailscaled.sock --tun=tailscale0 &` |
| **Stop Daemon** | `killall tailscaled` |
| **Check Network** | `ifconfig && ip route show` |
| **Test Internet** | `ping -c 3 8.8.8.8` |

## Network Configuration

- **eth0 (LAN)**: 10.0.0.1/24
- **eth1 (WAN)**: 10.10.57.3/24 (DHCP)
- **Tailscale**: 100.77.175.49

## Access Methods

- **Local SSH**: `ssh root@10.0.0.1`
- **Tailscale SSH**: `ssh root@100.77.175.49`
- **Web Dashboard**: `https://100.77.175.49`

## Troubleshooting Checklist

1. ✅ Is eth1 connected and has IP?
2. ✅ Can ping 8.8.8.8?
3. ✅ Is tailscaled daemon running?
4. ✅ Does tailscale0 interface exist?
5. ✅ Can reach other Tailscale devices?

## Auto-Start Location

**Script**: `/home/sysuser/tailscale_autostart.sh`
**Log**: `/home/tailscale_startup.log`

## Device Information

- **Model**: Advantech ECU-1051
- **Hostname**: ecu1051-455071
- **Tailscale Version**: 1.76.1
- **Access**: Root with empty password
