# 🍌 bjoin.studio Network Architecture Setup Guide

This guide outlines the full setup of your studio network using the updated VLAN schema, bandwidth tiers, device roles, and routing policies. It’s optimized for deployment with OPNsense on a Protectli Vault.

---

## 🗺️ Definitive VLAN and IP Plan

This table serves as the single source of truth for VLANs, subnets, and IP addressing.

| VLAN ID | Zone         | Purpose                          | Bandwidth | Devices / Use Cases              | Subnet          | Gateway IP     | DHCP Range                  |
|:--------|:-------------|:---------------------------------|:----------|:---------------------------------|:----------------|:---------------|:----------------------------|
| **11**  | Production   | Production Wired (1Gb)           | 1 Gb      | Office workstations, admin       | `10.20.11.0/24` | `10.20.11.1`   | `10.20.11.100 – 200`        |
| **12**  | Production   | Production Wired (10Gb)          | 10 Gb     | Render nodes, file servers       | `10.20.12.0/24` | `10.20.12.1`   | `10.20.12.100 – 200`        |
| **13**  | Production   | Production Reserved              | 1 Gb      | Future production needs          | `10.20.13.0/24` | `10.20.13.1`   | Static only                 |
| **14**  | Production   | Production Wifi                  | WiFi      | Staff laptops, mobile devices    | `10.20.14.0/24` | `10.20.14.1`   | `10.20.14.100 – 200`        |
| **15**  | Production   | Production Monitoring            | 1 Gb      | Syslog, SNMP, NetFlow            | `10.20.15.0/24` | `10.20.15.1`   | `10.20.15.100 – 200`        |
| **21**  | Stage        | Stage Wired (1Gb)                | 1 Gb      | Cameras, lighting controllers    | `10.20.21.0/24` | `10.20.21.1`   | `10.20.21.100 – 200`        |
| **22**  | Stage        | Stage Wired (10Gb)               | 10 Gb     | Image servers, preview stations  | `10.20.22.0/24` | `10.20.22.1`   | `10.20.22.100 – 200`        |
| **23**  | Stage        | Stage Reserved                   | 1 Gb      | Future stage needs               | `10.20.23.0/24` | `10.20.23.1`   | Static only                 |
| **24**  | Stage        | Stage Wifi                       | WiFi      | Tablets, mobile control apps     | `10.20.24.0/24` | `10.20.24.1`   | `10.20.24.100 – 200`        |
| **25**  | Stage        | Stage Monitoring                 | 1 Gb      | Syslog, SNMP, NetFlow            | `10.20.25.0/24` | `10.20.25.1`   | `10.20.25.100 – 200`        |
| **31**  | Studio       | Studio Wired (1Gb)               | 1 Gb      | Editing bays, sound design       | `10.20.31.0/24` | `10.20.31.1`   | `10.20.31.100 – 200`        |
| **32**  | Studio       | Studio Wired (10Gb)              | 10 Gb     | Color grading, VFX workstations  | `10.20.32.0/24` | `10.20.32.1`   | `10.20.32.100 – 200`        |
| **33**  | Studio       | Studio Wired (100Gb)             | 100 Gb    | SAN/NAS systems, media servers   | `10.20.33.0/24` | `10.20.33.1`   | Static only                 |
| **34**  | Studio       | Studio Wifi                      | WiFi      | Creative team mobile devices     | `10.20.34.0/24` | `10.20.34.1`   | `10.20.34.100 – 200`        |
| **35**  | Studio       | Studio Monitoring                | 1 Gb      | Syslog, SNMP, NetFlow            | `10.20.35.0/24` | `10.20.35.1`   | `10.20.35.100 – 200`        |
| **41**  | Workshop     | Workshop Wired (1Gb)             | 1 Gb      | CAD stations, programming setups | `10.20.41.0/24` | `10.20.41.1`   | `10.20.41.100 – 200`        |
| **42**  | Workshop     | Workshop Reserved                | 1 Gb      | Future workshop needs            | `10.20.42.0/24` | `10.20.42.1`   | Static only                 |
| **43**  | Workshop     | Workshop Reserved                | 1 Gb      | Future workshop needs            | `10.20.43.0/24` | `10.20.43.1`   | Static only                 |
| **44**  | Workshop     | Workshop Wifi                    | WiFi      | Tool-connected devices           | `10.20.44.0/24` | `10.20.44.1`   | `10.20.44.100 – 200`        |
| **45**  | Workshop     | Workshop Monitoring              | 1 Gb      | Syslog, SNMP, NetFlow            | `10.20.45.0/24` | `10.20.45.1`   | `10.20.45.100 – 200`        |
| **51**  | Management   | Management Wired (1Gb)           | 1 Gb      | Switches, APs, firewalls         | `10.20.51.0/24` | `10.20.51.1`   | Static only                 |
| **52**  | Management   | Management Reserved              | 1 Gb      | Future management needs          | `10.20.52.0/24` | `10.20.52.1`   | Static only                 |
| **53**  | Management   | Management Reserved              | 1 Gb      | Future management needs          | `10.20.53.0/24` | `10.20.53.1`   | Static only                 |
| **54**  | Management   | Management Wifi                  | WiFi      | Admin mobile devices             | `10.20.54.0/24` | `10.20.54.1`   | `10.20.54.100 – 200`        |
| **55**  | Management   | Management Monitoring            | 1 Gb      | Syslog, SNMP, NetFlow            | `10.20.55.0/24` | `10.20.55.1`   | `10.20.55.100 – 200`        |
| **61**  | Guest        | Guest Wired (1Gb)                | 1 Gb      | Visitor laptops, phones          | `10.20.61.0/24` | `10.20.61.1`   | `10.20.61.100 – 200`        |
| **62**  | Guest        | Guest Reserved                   | 1 Gb      | Future guest needs               | `10.20.62.0/24` | `10.20.62.1`   | Static only                 |
| **63**  | Guest        | Guest Reserved                   | 1 Gb      | Future guest needs               | `10.20.63.0/24` | `10.20.63.1`   | Static only                 |
| **64**  | Guest        | Guest Wifi                       | WiFi      | Visitor laptops, phones          | `10.20.64.0/24` | `10.20.64.1`   | `10.20.64.100 – 200`        |
| **65**  | Guest        | Guest Monitoring                 | 1 Gb      | Syslog, SNMP, NetFlow            | `10.20.65.0/24` | `10.20.65.1`   | `10.20.65.100 – 200`        |

---

## 🔐 VPN Zones

| VPN Type         | Subnet           | Access Scope                          |
|------------------|------------------|---------------------------------------|
| Remote Access VPN| 10.20.250.0/24   | VLANs 11, 21, 31 only                 |
| Site-to-Site VPN | 10.20.251.0/24   | All zones (bridged selectively)       |

---

## 🔄 Routing & Visibility Matrix

| Source VLAN | Destination VLANs | Access | Notes                                  |
|-------------|-------------------|--------|----------------------------------------|
| 33 (Studio 100Gb) | All VLANs     | ✅ Yes | Full visibility                        |
| 32 (Studio 10Gb)  | All VLANs     | ✅ Yes | Full visibility                        |
| 31 (Studio 1Gb)   | 32, 33        | ❌ No | Blocked unless explicitly allowed      |
| 41 (Workshop)     | Studio VLANs  | ❌ No | Isolated                               |
| 11–14 (Production)| Studio VLANs  | ❌ No | Blocked from initiating traffic        |
| VPN Clients       | VLANs 11, 21, 31 | ✅ Yes | Limited access to general work VLANs   |

---

## 🧱 Hardware Roles

| Device                  | Role                                | Notes                                                              |
|:------------------------|:------------------------------------|:-------------------------------------------------------------------|
| Protectli Vault         | OPNsense Firewall/Router            | The single point of control for all inter-VLAN routing and security. |
| Netgear R6220           | ISP Router                          | Provides the WAN connection; acts as the gateway to the internet.  |
| **Sodola 8-Port 10G**   | **Distribution Switch**             | The main switch connected to the firewall, distributes the VLAN trunk. |
| **BitEngine SW08XM**    | **Access/Aggregation Switch**       | Provides high-speed 10G RJ45 access for servers and workstations.  |
| Cisco Nexus 9236C       | 100G Core Switch                    | The high-performance backbone for the Studio Ultra VLAN.           |
| Netgear GS105           | Unmanaged Access Switch             | For simple, single-VLAN device connections.                        |
| **Mac Pro 6,1**         | **Proxmox VE Hypervisor**           | Hosts critical VMs like FreeIPA. Management in VLAN 51.            |
| Wireless APs/Controller | WiFi Access Points                  | Provides wireless access for various VLANs.                        |

---

## 🧠 Core Network Services

| Service        | Server Hostname(s)                     | VLAN | IP Address(es)                  | Purpose                                                      |
|:---------------|:---------------------------------------|:-----|:--------------------------------|:-------------------------------------------------------------|
| Identity & DNS | `ipa1.bjoin.studio`, `ipa2.bjoin.studio` | 51   | `10.20.51.10`, `10.20.51.11`    | Centralized user authentication (FreeIPA) and internal DNS.  |
| Virtualization | `pmx-01.bjoin.studio`                  | 51   | `10.20.51.20`                   | Proxmox VE host for running critical VMs.                    |

---

## 🛠️ OPNsense Setup Guide

This section guides you through installing and configuring OPNsense on your Protectli Vault to manage VLANs, routing, DHCP, firewall rules, and VPN access.

### 🔹 6.1 Installation & Initial Access

#### 🧰 Requirements
- Protectli Vault (or compatible x86 hardware)
- USB stick (at least 4GB)
- Monitor + keyboard (for initial setup)
- Internet access via Netgear R6220

#### 🧾 Installation Steps
1. **Download OPNsense ISO**
   - Visit [OPNsense Downloads](https://opnsense.org/download/)
   - Select: `AMD64`, `VGA`, latest stable release

2. **Create Bootable USB**
   - Use [Rufus](https://rufus.ie/) or BalenaEtcher
   - Write the ISO to your USB stick

3. **Install OPNsense**
   - Plug USB into Protectli Vault
   - Connect monitor and keyboard
   - Boot from USB and follow installer prompts
   - Choose ZFS (recommended for reliability)
   - Assign interfaces:
     - WAN → Connect to Netgear LAN port
     - LAN → Connect to internal switch (e.g., GS105)

4. **Access Web GUI**
   - Connect a laptop to LAN port
   - Navigate to `https://192.168.1.1`
   - Default credentials: `admin / opnsense`
   - Change password immediately

### 🔹 6.2 LAN IP & Interface Setup

#### 🧭 Set LAN IP
- Navigate to: `Interfaces > LAN`
- Change IP to match your first VLAN gateway (e.g., Production VLAN 11)
  - IP: `10.20.11.1`
  - Subnet: `255.255.255.0`
- Save and apply changes

#### 🔌 Interface Naming Convention
Use clear names for each VLAN interface:
- `LAN_Prod_1Gb` for VLAN 11
- `LAN_Studio_10Gb` for VLAN 32
- `LAN_Stage_WiFi` for VLAN 24
- etc.

### 🔹 6.3 VLAN Tagging & Interface Assignment

#### 🧬 Create VLANs
For each VLAN:
1. Go to `Interfaces > Other Types > VLAN`
2. Click `+ Add`
3. Set:
   - Parent Interface: LAN NIC (e.g., `igb0`)
   - VLAN Tag: e.g., `11`
   - Description: e.g., `Production 1Gb`
4. Save

Repeat for all VLANs defined in the 'Definitive VLAN and IP Plan' table at the beginning of this document.

#### 🔗 Assign VLAN Interfaces
1. Go to `Interfaces > Assignments`
2. Click `+` to add each VLAN
3. Enable each interface
4. Set static IP (e.g., `10.20.11.1/24`)
5. Rename interface for clarity

### 🔹 6.4 DHCP Configuration

For each VLAN:
1. Go to `Services > DHCPv4`
2. Select the VLAN interface (e.g., `LAN_Prod_1Gb`)
3. Enable DHCP server
4. Set:
   - Range: `10.20.11.100 – 10.20.11.200`
   - DNS: `10.20.51.10` (internal DNS) or `8.8.8.8`
   - Lease Time: `24h` or shorter for testing

Repeat for all VLANs that require DHCP.

### 🔹 6.5 Firewall Rules

#### 🔥 Default Policy
OPNsense blocks all inter-VLAN traffic by default. You must explicitly allow or deny traffic.

#### 🧱 Create Rules Per VLAN
1. Go to `Firewall > Rules`
2. Select VLAN interface (e.g., `LAN_Studio_10Gb`)
3. Add rules:
   - Allow traffic to specific VLANs (e.g., allow VLAN 32 to access VLAN 11)
   - Block traffic from VLAN 41 (Workshop) to VLAN 33 (Studio 100Gb)
   - Allow DNS, DHCP, and internal services

#### 🧠 Example Rule: Block Workshop → Studio
- Interface: `LAN_Workshop_1Gb`
- Action: `Block`
- Source: `Workshop subnet (10.20.41.0/24)`
- Destination: `Studio VLANs (10.20.31.0/24, 10.20.32.0/24, 10.20.33.0/24)`
- Protocol: `Any`

### 🔐 6.6 VPN Configuration

#### 🧳 Remote Access VPN (WireGuard or OpenVPN)
1. Install plugin: `System > Firmware > Plugins`
2. Configure VPN server:
   - Subnet: `10.20.250.0/24`
   - Assign interface: `VPN_Remote`
   - Set firewall rules to allow access to VLANs 11, 21, 31 only

#### 🔗 Site-to-Site VPN
1. Use IPSec or WireGuard
2. Subnet: `10.20.251.0/24`
3. Configure peer tunnel
4. Add firewall rules to bridge VLANs selectively

### 🧠 6.7 Best Practices

- **Static IPs**: Reserve `.2 – .50` for switches, servers, APs
- **DNS**: Use internal DNS (e.g., `dnsmasq`) for `bjoin.studio` resolution
- **Monitoring**: Enable NetFlow or Insight for traffic analytics
- **Backups**: Export config regularly via `System > Configuration > Backups`
