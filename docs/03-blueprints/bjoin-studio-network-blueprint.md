# 🔐 Studio Network Architecture: `bjoin.studio`

## 🔐 Environment Overview

| Environment | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| **Workshop** | Low bandwidth, local only, no internet, limited servers, 1 Gb switch only   |
| **Stage**    | Medium bandwidth, limited internet, 1 Gb + 10 Gb switches                   |
| **Studio**   | High bandwidth, limited internet, many servers, 1 Gb + 10 Gb + 100 Gb switches |
| **Production** | Medium bandwidth, medium internet, limited servers, 1 Gb + 10 Gb + WiFi     |

---

## 🛠️ Production VLANs (11–14)

- **Access Control**: Role-based access via ACLs and firewall rules; segmented access for admins and production staff
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here
- **Security Notes**: Medium internet access; outbound traffic restricted by firewall policies

| VLAN ID | Zone        | Purpose                          | Bandwidth     | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|---------------|----------------------------------------------------------|
| **11**  | Production  | General wired traffic            | 1 Gb          | Office workstations, admin terminals                     |
| **12**  | Production  | High-performance traffic         | 10 Gb         | Render nodes, file servers, production pipeline systems  |
| **13**  | Production  | Reserved                         | —             | Future expansion (e.g., cloud gateway, AI processing)    |
| **14**  | Production  | Wireless access                  | WiFi          | Staff laptops, mobile devices, general connectivity      |

---

## 🛠️ Stage VLANs (21–24)

- **Access Control**: MAC filtering and port security; limited internet access for approved devices only
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here
- **Security Notes**: Image transfer systems isolated from control systems via ACLs

| VLAN ID | Zone        | Purpose                          | Bandwidth     | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|---------------|----------------------------------------------------------|
| **21**  | Stage       | Tethered capture & control       | 1 Gb          | Cameras, lighting controllers, scene automation systems  |
| **22**  | Stage       | High-speed image transfer        | 10 Gb         | Image servers, live preview/editing stations             |
| **23**  | Stage       | Reserved                         | —             | Future tech (e.g., 8K streaming, AI rigs, robotics)      |
| **24**  | Stage       | Wireless access                  | WiFi          | Tablets, mobile control apps, crew communication         |

---

## 🛠️ Studio VLANs (31–34)

- **Access Control**: Layer 2 segmentation; inter-VLAN routing restricted via firewalls
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here
- **Security Notes**: Creative systems isolated from management and guest networks; QoS applied for media flow

| VLAN ID | Zone        | Purpose                          | Bandwidth     | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|---------------|----------------------------------------------------------|
| **31**  | Studio      | General creative workstations    | 1 Gb          | Editing bays, sound design terminals                     |
| **32**  | Studio      | High-performance media editing   | 10 Gb         | Color grading, VFX workstations                          |
| **33**  | Studio      | Ultra-high bandwidth media flow  | 100 Gb        | SAN/NAS systems, media servers, archival storage         |
| **34**  | Studio      | Wireless access                  | WiFi          | Creative team mobile devices, wireless preview tools     |

---

## 🛠️ Workshop VLANs (41–44)

- **Access Control**: Routing restrictions enforce local-only access; no internet connectivity
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here
- **Security Notes**: Port security and static IPs recommended; VLANs isolated from external networks

| VLAN ID | Zone        | Purpose                          | Bandwidth     | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|---------------|----------------------------------------------------------|
| **41**  | Workshop    | Engineering & prototyping        | 1 Gb          | CAD stations, microcontroller programming setups         |
| **42**  | Workshop    | Reserved                         | —             | Future expansion (e.g., robotics, fabrication systems)   |
| **43**  | Workshop    | Reserved                         | —             | Additional bandwidth tier or isolated subnet             |
| **44**  | Workshop    | Wireless access                  | WiFi (local only) | Tool-connected devices, mobile diagnostics               |

---

## 🛠️ Management VLANs (51–53)

- **Access Control**: Strict ACLs, firewall zones, and NAC; only authenticated IT/admin devices permitted
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here
- **Security Notes**: Disable unused ports and discovery protocols; isolate from user VLANs

| VLAN ID | Zone        | Purpose                          | Bandwidth     | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|---------------|----------------------------------------------------------|
| **51**  | Management  | Network device control           | 1 Gb          | Switches, APs, firewalls, monitoring systems             |
| **52**  | Management  | Reserved                         | —             | Future expansion (e.g., out-of-band access)              |
| **53**  | Management  | Monitoring & telemetry           | 1 Gb          | Syslog, SNMP, NetFlow, Prometheus, Grafana               |

---

## 🌐 Guest WiFi VLANs (61–63)

- **Access Control**: Captive portal authentication; firewall isolation from internal networks
- **Monitoring**: Optional usage analytics and bandwidth tracking
- **Security Notes**: VLAN isolation and DHCP snooping prevent lateral movement

| VLAN ID | Zone        | Purpose                          | Bandwidth     | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|---------------|----------------------------------------------------------|
| **61**  | Guest WiFi  | Internet-only wireless access    | WiFi          | Visitor laptops, phones, tablets                         |
| **62**  | Guest WiFi  | Reserved                         | —             | Optional captive portal, analytics, or VLAN isolation    |
| **63**  | Guest WiFi  | Captive portal & analytics       | WiFi          | Visitor tracking, splash page, usage stats               |

---

You're building a seriously well-architected network—this documentation is already impressive. To make it even more cohesive, I’ve integrated your VLAN-to-subnet mapping, switch roles, and OPNSense strategy into a unified markdown document. I also refined formatting and added clarity where needed.

---

# 🧠 Studio Network Architecture: `bjoin.studio`

## 🔐 Environment Overview

| Environment | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| **Workshop** | Low bandwidth, local only, no internet, limited servers, 1 Gb switch only   |
| **Stage**    | Medium bandwidth, limited internet, 1 Gb + 10 Gb switches                   |
| **Studio**   | High bandwidth, limited internet, many servers, 1 Gb + 10 Gb + 100 Gb switches |
| **Production** | Medium bandwidth, medium internet, limited servers, 1 Gb + 10 Gb + WiFi     |

---

## 🧩 Network Goals

- **VLAN Segmentation**: Isolate zones (Production, Stage, Studio, Workshop, Management, Guest)
- **Firewall Enforcement**: All inter-VLAN traffic routed through OPNSense
- **Bandwidth Optimization**: Use 10G/100G switches for high-throughput zones
- **Layer 3 Routing**: Centralized on OPNSense (static routes or OSPF)
- **Management Access**: Dedicated VLAN for infrastructure control

---

## 🔧 Hardware Inventory

| Device                  | Ports         | Role                          | Notes                          |
|-------------------------|---------------|-------------------------------|--------------------------------|
| **Netgear 6220**        | 4x RJ45 (1G)  | WAN uplink                    | Unmanaged, silent              |
| **Protectli FW4B**      | 4x RJ45 (1G)  | Core router/firewall          | OPNSense 25.7                  |
| **Cisco Nexus 9236C**   | 36x QSFP28    | Studio backbone               | 100G, Layer 3, data center     |
| **Sodola 8-Port 10G**   | 8x SFP+       | Stage backbone                | Web managed, fanless           |
| **BitEngine SW08XM**    | 8x RJ45 (10G) | Core switch                   | Web managed, 160Gbps           |
| **Netgear GS108Ev4**    | 8x RJ45 (1G)  | Access switch                 | Managed, silent                |
| **Netgear GS105**       | 5x RJ45 (1G)  | Legacy access                 | Unmanaged, silent              |

---

## 🧵 VLAN Trunking Strategy

- **Protectli LAN → BitEngine SW08XM**: Primary VLAN trunk
- **BitEngine → Sodola 10G**: Trunk uplink for Stage
- **BitEngine → Cisco Nexus**: Trunk for Studio 100G VLANs
- **BitEngine → GS108Ev4**: Trunk for 1G access zones
- **GS108Ev4 → GS105 / 6220**: Access ports only (no VLAN tagging)

---

## 🛠️ VLAN Deployment Summary

| VLAN ID | Zone        | Switches Used         | Notes                                           |
|---------|-------------|-----------------------|-------------------------------------------------|
| 11–14   | Production  | GS108Ev4, GS105       | 1G access ports only                            |
| 21–24   | Stage       | Sodola 10G, GS108Ev4  | 10G trunk to Sodola, 1G access for control      |
| 31–34   | Studio      | Cisco Nexus 9236C     | 100G trunk, routed via Protectli                |
| 41–44   | Workshop    | GS108Ev4, BitEngine   | 1G/10G mixed access                             |
| 51–53   | Management  | GS108Ev4, BitEngine   | Isolated VLAN for switch/firewall access        |
| 61–63   | Guest WiFi  | OPT1 or GS108Ev4      | Routed through firewall, internet-only          |

---

## 🌐 VLAN-to-Subnet Mapping (`10.101.x.x/24`)

| VLAN ID | Zone        | Subnet              | Gateway IP         | Purpose                                      |
|---------|-------------|---------------------|---------------------|----------------------------------------------|
| **11**  | Production  | 10.101.11.0/24      | 10.101.11.1         | General wired workstations                   |
| **12**  | Production  | 10.101.12.0/24      | 10.101.12.1         | High-performance systems                     |
| **13**  | Production  | 10.101.13.0/24      | 10.101.13.1         | Reserved                                     |
| **14**  | Production  | 10.101.14.0/24      | 10.101.14.1         | WiFi access                                  |
| **21**  | Stage       | 10.101.21.0/24      | 10.101.21.1         | Tethered cameras, lighting                   |
| **22**  | Stage       | 10.101.22.0/24      | 10.101.22.1         | Image servers, preview stations              |
| **23**  | Stage       | 10.101.23.0/24      | 10.101.23.1         | Reserved                                     |
| **24**  | Stage       | 10.101.24.0/24      | 10.101.24.1         | WiFi access                                  |
| **31**  | Studio      | 10.101.31.0/24      | 10.101.31.1         | Editing bays, creative workstations          |
| **32**  | Studio      | 10.101.32.0/24      | 10.101.32.1         | High-performance editing                     |
| **33**  | Studio      | 10.101.33.0/24      | 10.101.33.1         | 100G media servers                           |
| **34**  | Studio      | 10.101.34.0/24      | 10.101.34.1         | WiFi access                                  |
| **41**  | Workshop    | 10.101.41.0/24      | 10.101.41.1         | Engineering stations                         |
| **42**  | Workshop    | 10.101.42.0/24      | 10.101.42.1         | Reserved                                     |
| **43**  | Workshop    | 10.101.43.0/24      | 10.101.43.1         | Reserved                                     |
| **44**  | Workshop    | 10.101.44.0/24      | 10.101.44.1         | WiFi access                                  |
| **51**  | Management  | 10.101.51.0/24      | 10.101.51.1         | Switch/AP/firewall control                   |
| **52**  | Management  | 10.101.52.0/24      | 10.101.52.1         | Reserved                                     |
| **53**  | Management  | 10.101.53.0/24      | 10.101.53.1         | Monitoring & telemetry                       |
| **61**  | Guest WiFi  | 10.101.61.0/24      | 10.101.61.1         | Internet-only access                         |
| **62**  | Guest WiFi  | 10.101.62.0/24      | 10.101.62.1         | Reserved                                     |
| **63**  | Guest WiFi  | 10.101.63.0/24      | 10.101.63.1         | Captive portal & analytics                   |

---

## 🔐 OPNSense Configuration

- **Interfaces**: Assign VLANs to LAN interface via tagging
- **DHCP**: Serve IPs per VLAN (e.g., `10.101.x.100–200`)
- **Firewall Rules**:
  - Block inter-VLAN traffic by default
  - Allow specific flows (e.g., Studio → Stage for ingest)
  - NAT Guest VLAN to WAN; deny LAN access
- **Routing**: Static or OSPF depending on complexity

---

Would you like help generating switch port maps, OPNSense interface assignments, or a visual diagram next? I can also help you write config snippets for your managed switches.