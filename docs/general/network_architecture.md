
# Network Architecture for bjoin.studio

This document outlines the proposed network architecture designed to support the internal structure of **bjoin.studio**, the digital backbone of **Bjoin Films Photography Studio**.

## Purpose

The goal of this architecture is to establish a secure, scalable, and efficient internal network that supports the studio's creative workflows, data management, and collaborative operations. The system will serve as the foundation for digital asset storage, editing pipelines, client communications, and administrative tools.

## Overview

The architecture will encompass:

- Centralized storage for high-resolution photography and video assets
- Secure access controls for internal and external collaborators
- Scalable cloud integration for remote editing and backup
- Redundant systems to ensure uptime and data integrity
- Workflow automation for asset tagging, archiving, and delivery

## Next Steps

Further sections will detail:

- Physical and cloud infrastructure
- User roles and access levels
- Software stack and integrations
- Security protocols
- Maintenance and scalability plans


# 🌐 Router IP & DHCP Settings by VLAN

| VLAN | Environment   | Subnet           | Router IP     | DHCP Range                  |
|------|----------------|------------------|---------------|-----------------------------|
| 10   | Workshop       | 10.20.10.0/24    | 10.20.10.1    | 10.20.10.100 – 10.20.10.200 |
| 20   | Stage 1Gb      | 10.20.20.0/24    | 10.20.20.1    | 10.20.20.100 – 10.20.20.200 |
| 21   | Stage 10Gb     | 10.20.21.0/24    | 10.20.21.1    | 10.20.21.100 – 10.20.21.200 |
| 30   | Studio 1Gb     | 10.20.30.0/24    | 10.20.30.1    | 10.20.30.100 – 10.20.30.200 |
| 31   | Studio 10Gb    | 10.20.31.0/24    | 10.20.31.1    | 10.20.31.100 – 10.20.31.200 |
| 32   | Studio 100Gb   | 10.20.32.0/24    | 10.20.32.1    | 10.20.32.100 – 10.20.32.200 |
| 40   | Prod 1Gb       | 10.20.40.0/24    | 10.20.40.1    | 10.20.40.100 – 10.20.40.200 |
| 41   | Prod 10Gb      | 10.20.41.0/24    | 10.20.41.1    | 10.20.41.100 – 10.20.41.200 |
| 42   | Prod WiFi      | 10.20.42.0/24    | 10.20.42.1    | 10.20.42.100 – 10.20.42.200 |
| VPN  | Remote VPN     | 10.20.250.0/24   | 10.20.250.1   | 10.20.250.100 – 10.20.250.200 |
| VPN  | Site VPN       | 10.20.251.0/24   | 10.20.251.1   | 10.20.251.100 – 10.20.251.200 |

---

# 🔧 Additional Router Config Tips

- Enable VLAN tagging on router interfaces if using trunk ports
- Set up DHCP relay if your router doesn’t serve DHCP directly
- Use ACLs or firewall rules to enforce visibility restrictions  
  _(e.g., block VLAN 10 from accessing VLAN 32)_
- DNS: Point clients to internal DNS (e.g., `10.20.250.10`) or external fallback (`8.8.8.8`)


# Network Architecture for bjoin.studio

This document outlines the internal network architecture for **bjoin.studio**, the digital infrastructure supporting **Bjoin Films Photography Studio**. The design prioritizes performance, segmentation, and scalability across multiple creative departments.

---

## Current ISP & Gateway

- **ISP**: Charter Spectrum (ADSL)
- **Primary Gateway**: Netgear 6220 (temporary substitute for real internet)
- **Router NAT Range**: `192.168.1.0/24`
- **Protectli FW4B-0-8-120** running **OPNsense 25.7** is used for VLAN, routing, and firewall management.

---

## Protectli Port Assignments

| Port  | Role        | Notes                                                                 |
|-------|-------------|-----------------------------------------------------------------------|
| WAN   | Internet    | Connected to Netgear 6220, receives `192.168.1.254/24` via DHCP       |
| LAN   | Core VLAN   | Currently set to `10.20.0.1/24` (likely default or placeholder subnet)|
| OPT1  | Unused      | Reserved for future VLAN trunking or DMZ                              |
| OPT2  | Unused      | Reserved for high-speed uplink or isolated services                   |

---

## VLAN Design

The network is segmented by department and bandwidth requirements. Each VLAN has its own subnet, router IP, and DHCP range.

| VLAN | Environment     | Subnet           | Router IP     | DHCP Range                  |
|------|------------------|------------------|---------------|-----------------------------|
| 10   | Workshop         | 10.20.10.0/24    | 10.20.10.1    | 10.20.10.100 – 10.20.10.200 |
| 20   | Stage 1Gb        | 10.20.20.0/24    | 10.20.20.1    | 10.20.20.100 – 10.20.20.200 |
| 21   | Stage 10Gb       | 10.20.21.0/24    | 10.20.21.1    | 10.20.21.100 – 10.20.21.200 |
| 30   | Studio 1Gb       | 10.20.30.0/24    | 10.20.30.1    | 10.20.30.100 – 10.20.30.200 |
| 31   | Studio 10Gb      | 10.20.31.0/24    | 10.20.31.1    | 10.20.31.100 – 10.20.31.200 |
| 32   | Studio 100Gb     | 10.20.32.0/24    | 10.20.32.1    | 10.20.32.100 – 10.20.32.200 |
| 40   | Production 1Gb   | 10.20.40.0/24    | 10.20.40.1    | 10.20.40.100 – 10.20.40.200 |
| 41   | Production 10Gb  | 10.20.41.0/24    | 10.20.41.1    | 10.20.41.100 – 10.20.41.200 |
| 42   | Production WiFi  | 10.20.42.0/24    | 10.20.42.1    | 10.20.42.100 – 10.20.42.200 |
| 250  | Remote VPN       | 10.20.250.0/24   | 10.20.250.1   | 10.20.250.100 – 10.20.250.200 |
| 251  | Site-to-Site VPN | 10.20.251.0/24   | 10.20.251.1   | 10.20.251.100 – 10.20.251.200 |

---

## Recommendations & Improvements

### 🔧 VLAN Optimization
- **Collapse bandwidth tiers** where possible. For example, Stage and Studio could share VLANs with QoS rules if physical separation isn't critical.
- **Use VLAN tagging** across switches to reduce port usage and improve scalability.

### 🔐 Security Enhancements
- **Isolate VLANs** with strict firewall rules in OPNsense.
- **Enable IDS/IPS** on OPNsense for Studio and Production VLANs.
- **Use VLAN 999** or similar as a "black hole" for unused ports.

### 📡 WiFi Strategy
- Deploy **dedicated access points** per environment with VLAN tagging.
- Use **WPA3** and **RADIUS authentication** for Studio and Production WiFi.

### 📈 Performance Planning
- Use **LACP (Link Aggregation)** on OPT ports for trunking to core switches.
- Consider **10Gb/100Gb switches** with SFP+ or QSFP28 uplinks for Studio and Production.

### 🧠 Management & Monitoring
- Deploy **NetFlow or sFlow** for traffic analysis.
- Use **Zabbix, Prometheus, or LibreNMS** for network health monitoring.

---

## Next Steps

- Finalize VLAN assignments and firewall rules in OPNsense
- Configure OPT1/OPT2 for trunking or uplinks
- Deploy managed switches with VLAN support
- Set up WiFi access points with VLAN tagging
- Document physical topology and cable maps

