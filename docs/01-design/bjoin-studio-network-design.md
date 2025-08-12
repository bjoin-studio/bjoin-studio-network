# 🍌 bjoin.studio Network Architecture Setup Guide

This guide outlines the full setup of your studio network using the updated VLAN schema, bandwidth tiers, device roles, and routing policies. It’s optimized for deployment with OPNsense on a Protectli Vault.

---

## 🗺️ Definitive VLAN and IP Plan

This table serves as the single source of truth for VLANs, subnets, and IP addressing.

| VLAN ID | Zone         | Purpose                          | Bandwidth | Devices / Use Cases              | Subnet          | Gateway IP     | DHCP Range                  |
|:--------|:-------------|:---------------------------------|:----------|:---------------------------------|:----------------|:---------------|:----------------------------|
| **11**  | Production   | General wired traffic            | 1 Gb      | Office workstations, admin       | `10.20.11.0/24` | `10.20.11.1`   | `10.20.11.100 – 200`        |
| **12**  | Production   | High-performance traffic         | 10 Gb     | Render nodes, file servers       | `10.20.12.0/24` | `10.20.12.1`   | `10.20.12.100 – 200`        |
| **14**  | Production   | Wireless access                  | WiFi      | Staff laptops, mobile devices    | `10.20.14.0/24` | `10.20.14.1`   | `10.20.14.100 – 200`        |
| **21**  | Stage        | Tethered capture & control       | 1 Gb      | Cameras, lighting controllers    | `10.20.21.0/24` | `10.20.21.1`   | `10.20.21.100 – 200`        |
| **22**  | Stage        | High-speed image transfer        | 10 Gb     | Image servers, preview stations  | `10.20.22.0/24` | `10.20.22.1`   | `10.20.22.100 – 200`        |
| **24**  | Stage        | Wireless access                  | WiFi      | Tablets, mobile control apps     | `10.20.24.0/24` | `10.20.24.1`   | `10.20.24.100 – 200`        |
| **31**  | Studio       | General creative workstations    | 1 Gb      | Editing bays, sound design       | `10.20.31.0/24` | `10.20.31.1`   | `10.20.31.100 – 200`        |
| **32**  | Studio       | High-performance media editing   | 10 Gb     | Color grading, VFX workstations  | `10.20.32.0/24` | `10.20.32.1`   | `10.20.32.100 – 200`        |
| **33**  | Studio       | Ultra-high bandwidth media flow  | 100 Gb    | SAN/NAS systems, media servers   | `10.20.33.0/24` | `10.20.33.1`   | Static only                 |
| **34**  | Studio       | Wireless access                  | WiFi      | Creative team mobile devices     | `10.20.34.0/24` | `10.20.34.1`   | `10.20.34.100 – 200`        |
| **41**  | Workshop     | Engineering & prototyping        | 1 Gb      | CAD stations, programming setups | `10.20.41.0/24` | `10.20.41.1`   | `10.20.41.100 – 200`        |
| **44**  | Workshop     | Wireless access                  | WiFi      | Tool-connected devices           | `10.20.44.0/24` | `10.20.44.1`   | `10.20.44.100 – 200`        |
| **51**  | Management   | Network device control           | 1 Gb      | Switches, APs, firewalls         | `10.20.51.0/24` | `10.20.51.1`   | Static only                 |
| **61**  | Guest WiFi   | Internet-only wireless access    | WiFi      | Visitor laptops, phones          | `10.20.61.0/24` | `10.20.61.1`   | `10.20.61.100 – 200`        |

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

| Device                  | Role                                |
|-------------------------|-------------------------------------|
| Protectli Vault         | OPNsense firewall/router            |
| Netgear R6220           | ISP router, NAT, DHCP for WAN       |
| Cisco Nexus 9236C       | Core switch (100Gb backbone)        |
| Sodola 8-Port 10G       | Aggregation switch (SFP+)           |
| BitEngine SW08XM        | High-speed LAN switch (RJ45 10G)    |
| Netgear GS105           | Basic unmanaged switch (RJ45 1G)    |
| WiFi Controller         | VLAN-aware SSID provisioning        |

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

Repeat for all VLANs (11–34, 41, 44, 51, 61).

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
