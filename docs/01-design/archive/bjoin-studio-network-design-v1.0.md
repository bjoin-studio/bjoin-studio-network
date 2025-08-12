# 🔐 Studio Network Architecture: bjoin.studio

## 🔐 Environment Overview
### Environment	Description

Workshop	Low bandwidth, local only, no internet, limited servers, 1Gb switch only

Stage	Medium bandwidth, limited internet, 1Gb + 10Gb switches

Studio	High bandwidth, limited internet, many servers, 1Gb + 10Gb + 100Gb switches

Production	Medium bandwidth, medium internet, limited servers, 1Gb + 10Gb + WiFi

---

### 🛠️ Production VLAN (11-14)
- **Purpose**: Secure access to infrastructure devices.
- **Access Control**: Strict ACLs; only IT/admin users permitted.
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here.

| VLAN ID | Zone        | Purpose                          | Bandwidth | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|-----------|----------------------------------------------------------|
| **11**  | Production  | General wired traffic            | 1 Gb      | Office workstations, admin terminals                     |
|         |             |                                  |           |                                                          |
| **12**  | Production  | High-performance traffic         | 10 Gb     | Render nodes, file servers, production pipeline systems  |
|         |             |                                  |           |                                                          |
| **13**  | Production  | Reserved                         | —         | Future expansion (e.g., cloud gateway, AI processing)    |
|         |             |                                  |           |                                                          |
| **14**  | Production  | Wireless access                  | WiFi      | Staff laptops, mobile devices, general connectivity      |
|         |             |                                  |           |                                                          |

---

### 🛠️ Stage VLAN (21-24)
- **Purpose**: Secure access to infrastructure devices.
- **Access Control**: Strict ACLs; only IT/admin users permitted.
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here.

| VLAN ID | Zone        | Purpose                          | Bandwidth | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|-----------|----------------------------------------------------------|
| **21**  | Stage       | Tethered capture & control       | 1 Gb      | Cameras, lighting controllers, scene automation systems  |
|         |             |                                  |           |                                                          |
| **22**  | Stage       | High-speed image transfer        | 10 Gb     | Image servers, live preview/editing stations             |
|         |             |                                  |           |                                                          |
| **23**  | Stage       | Reserved                         | —         | Future tech (e.g., 8K streaming, AI rigs, robotics)      |
|         |             |                                  |           |                                                          |
| **24**  | Stage       | Wireless access                  | WiFi      | Tablets, mobile control apps, crew communication         |
|         |             |                                  |           |                                                          |

---

### 🛠️ Studio VLAN (31-34)
- **Purpose**: Secure access to infrastructure devices.
- **Access Control**: Strict ACLs; only IT/admin users permitted.
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here.

| VLAN ID | Zone        | Purpose                          | Bandwidth | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|-----------|----------------------------------------------------------|
| **31**  | Studio      | General creative workstations    | 1 Gb      | Editing bays, sound design terminals                     |
|         |             |                                  |           |                                                          |
| **32**  | Studio      | High-performance media editing   | 10 Gb     | Color grading, VFX workstations                          |
|         |             |                                  |           |                                                          |
| **33**  | Studio      | Ultra-high bandwidth media flow  | 100 Gb    | SAN/NAS systems, media servers, archival storage         |
|         |             |                                  |           |                                                          |
| **34**  | Studio      | Wireless access                  | WiFi      | Creative team mobile devices, wireless preview tools     |
|         |             |                                  |           |                                                          |

---

### 🛠️ Workshop VLAN (41-44)
- **Purpose**: Secure access to infrastructure devices.
- **Access Control**: Strict ACLs; only IT/admin users permitted.
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here.

| VLAN ID | Zone        | Purpose                          | Bandwidth | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|-----------|----------------------------------------------------------|
| **41**  | Workshop    | Engineering & prototyping        | 1 Gb      | CAD stations, microcontroller programming setups         |
|         |             |                                  |           |                                                          |
| **42**  | Workshop    | Reserved                         | —         | Future expansion (e.g., robotics, fabrication systems)   |
|         |             |                                  |           |                                                          |
| **43**  | Workshop    | Reserved                         | —         | Additional bandwidth tier or isolated subnet             |
|         |             |                                  |           |                                                          |
| **44**  | Workshop    | Wireless access                  | WiFi      | Tool-connected devices, mobile diagnostics               |
|         |             |                                  |           |                                                          |

---

### 🛠️ Management VLAN (51–53)
- **Purpose**: Secure access to infrastructure devices.
- **Access Control**: Strict ACLs; only IT/admin users permitted.
- **Monitoring**: SNMP, syslog, and telemetry traffic centralized here.

| VLAN ID | Zone        | Purpose                          | Bandwidth | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|-----------|----------------------------------------------------------|
| **51**  | Management  | Network device control           | 1 Gb      | Switches, APs, firewalls, monitoring systems             |
|         |             |                                  |           |                                                          |
| **52**  | Management  | Reserved                         | —         | Future expansion (e.g., out-of-band access)              |
|         |             |                                  |           |                                                          |
| **53**  | Management  | Monitoring & telemetry           | 1 Gb      | Syslog, SNMP, NetFlow, Prometheus, Grafana               |
|         |             |                                  |           |                                                          |

---

### 🌐 Guest WiFi VLAN (61–63)
- **Purpose**: Isolated internet access for visitors.
- **Security**: No access to internal resources; firewall enforced.
- **Optional Enhancements**: Captive portal, bandwidth throttling, usage analytics.

| VLAN ID | Zone        | Purpose                          | Bandwidth | Devices / Use Cases                                      |
|---------|-------------|----------------------------------|-----------|----------------------------------------------------------|
| **61**  | Guest WiFi  | Internet-only wireless access    | WiFi      | Visitor laptops, phones, tablets                         |
|         |             |                                  |           |                                                          |
| **62**  | Guest WiFi  | Reserved                         | —         | Optional captive portal, analytics, or VLAN isolation    |
|         |             |                                  |           |                                                          |
| **63**  | Guest WiFi  | Captive portal & analytics       | WiFi      | Visitor tracking, splash page, usage stats               |
|         |             |                                  |           |                                                          |

---

Would you like help drafting a topology diagram or writing up a deployment guide for this network?


---

Would you like help drafting VLAN-to-subnet mappings or switch port assignments next?
+--------------------------+
| Netgear 6220             |
| 4x RJ45 (1G)             |
| Unmanaged, Silent        |
+--------------------------+
| Protectli FW4B-0-8-120   |
| 4x RJ45 (1G)             |      
| OPNSense 25.7.           |
+--------------------------+
| Cisco Nexus 9236C        |
| 36x QSFP28 (100G)        |
| Layer 3, Data Center     |
+--------------------------+
| Sodola 8-Port 10G        |
| 8x SFP+ (10G)            |
| Web Managed, Fanless     |
+--------------------------+
| BitEngine SW08XM         |
| 8x RJ45 (10G)            |      
| Web Managed, 160Gbps     |      
+--------------------------+
| Netgear GS108Ev4         |
| 8x RJ45 (1G)             |
| Managed, Silent          |
+--------------------------+
| Netgear ProSafe GS105    |
| 5x RJ45 (1G)             |
| Unmanaged, Silent        |
+--------------------------+

This is a fantastic setup to build a robust, segmented, and high-performance network. You’ve got a mix of high-speed switches, a capable firewall, and a clear goal: isolate and control traffic across VLANs with proper routing, security, and bandwidth allocation.

Let’s walk through a network topology and connection strategy that leverages your equipment for optimal VLAN design, firewall enforcement, and future scalability.

🧠 High-Level Network Goals
VLAN Segmentation: Isolate zones (Production, Stage, Studio, Workshop, Management, Guest).

Firewall Enforcement: All inter-VLAN traffic passes through OPNSense for policy control.

Bandwidth Optimization: Use 10G/100G switches for high-throughput zones (Studio, Stage).

Layer 3 Routing: Centralized on OPNSense, with static routes or OSPF if needed.

Management Access: Dedicated VLAN for switch/AP/firewall control.

🧩 Recommended Topology
🔐 Firewall Core (Protectli FW4B)
WAN: Connected to Netgear 6220 (DHCP from Charter modem).

LAN (Port 1): Trunk to BitEngine SW08XM (10G switch) — carries all VLANs.

OPT1 (Port 2): Optional DMZ or isolated subnet (e.g., Guest WiFi).

OPT2 (Port 3): Optional out-of-band management or future expansion.

🧵 VLAN Trunking Strategy
Trunk from Protectli LAN → BitEngine SW08XM: Primary VLAN trunk.

BitEngine SW08XM → Sodola 10G SFP+: Trunk uplink for high-speed zones.

BitEngine SW08XM → Netgear GS108Ev4: Trunk or access ports for 1G zones.

BitEngine SW08XM → Cisco Nexus 9236C: Trunk for Studio 100G VLANs.

GS108Ev4 → GS105 / 6220: Access ports only (no VLAN trunking).

🔧 VLAN Deployment Strategy
VLAN ID	Zone	Switches Used	Notes
11–14	Production	GS108Ev4, GS105	1G access ports only
21–24	Stage	Sodola 10G, GS108Ev4	10G trunk to Sodola, 1G access for control
31–34	Studio	Cisco Nexus 9236C	100G trunk, routed via Protectli
41–44	Workshop	GS108Ev4, BitEngine	1G/10G mixed access
51–52	Management	GS108Ev4, BitEngine	Isolated VLAN for switch/firewall access
61–62	Guest WiFi	OPT1 or GS108Ev4	Routed through firewall, internet-only
🔐 OPNSense Configuration
Interfaces: Assign VLANs to LAN interface (via VLAN tagging).

DHCP: Serve IPs per VLAN (or relay if needed).

Firewall Rules:

Block inter-VLAN traffic by default.

Allow specific flows (e.g., Studio → Stage for media ingest).

NAT Guest VLAN to WAN with no LAN access.

Routing: Static or dynamic (OSPF) depending on complexity.

🛠️ Switch Configuration Summary
Switch	Role	VLAN Mode	Notes
Netgear 6220	WAN uplink	Unmanaged	DHCP to Protectli WAN
Protectli FW4B	Core router/firewall	VLAN trunking	All VLANs routed and filtered here
Cisco Nexus 9236C	Studio backbone	VLAN trunking	100G VLANs only
Sodola 10G SFP+	Stage backbone	VLAN trunking	10G VLANs, uplink to BitEngine
BitEngine SW08XM	Core switch	VLAN trunking	Central VLAN distribution
Netgear GS108Ev4	Access switch	VLAN trunking	1G VLANs, management ports
Netgear GS105	Legacy access	Untagged only	Use for simple devices
🧭 Next Steps
Define VLAN-to-subnet mappings (e.g., VLAN 11 → 192.168.11.0/24).

Configure VLAN interfaces on OPNSense.

Set up trunk ports and access ports on managed switches.

Apply firewall rules and DHCP scopes.

Would you like help drafting the VLAN-to-subnet map or OPNSense interface assignments next?

🧭 Part 1: VLAN-to-Subnet Mapping
This mapping ensures each VLAN has its own IP space, making routing and firewall rules easier to manage.

Great preference—and yes, using a **Class A private address space like `10.101.x.x`** is absolutely valid and often preferred in enterprise environments. It gives you **massive flexibility** for subnetting and future growth.

And no, it will **not negatively affect intra-VLAN traffic** at all. VLANs operate at Layer 2 (Ethernet), and IP addressing is Layer 3. As long as each VLAN has its own subnet and gateway, traffic within a VLAN will flow normally. Inter-VLAN traffic will still be routed through OPNSense, just as before.

---

## ✅ Updated VLAN-to-Subnet Mapping (Class A: `10.101.x.x/24`)

| VLAN ID | Zone        | Subnet              | Gateway IP         | Notes                                      |
|---------|-------------|---------------------|---------------------|--------------------------------------------|
| **11**  | Production  | 10.101.11.0/24      | 10.101.11.1         | General wired workstations                 |
| **12**  | Production  | 10.101.12.0/24      | 10.101.12.1         | High-performance systems                   |
| **13**  | Production  | 10.101.13.0/24      | 10.101.13.1         | Reserved                                   |
| **14**  | Production  | 10.101.14.0/24      | 10.101.14.1         | WiFi access                                |
| **21**  | Stage       | 10.101.21.0/24      | 10.101.21.1         | Tethered cameras, lighting                 |
| **22**  | Stage       | 10.101.22.0/24      | 10.101.22.1         | Image servers, preview stations            |
| **23**  | Stage       | 10.101.23.0/24      | 10.101.23.1         | Reserved                                   |
| **24**  | Stage       | 10.101.24.0/24      | 10.101.24.1         | WiFi access                                |
| **31**  | Studio      | 10.101.31.0/24      | 10.101.31.1         | Editing bays, creative workstations        |
| **32**  | Studio      | 10.101.32.0/24      | 10.101.32.1         | High-performance editing                   |
| **33**  | Studio      | 10.101.33.0/24      | 10.101.33.1         | 100G media servers                         |
| **34**  | Studio      | 10.101.34.0/24      | 10.101.34.1         | WiFi access                                |
| **41**  | Workshop    | 10.101.41.0/24      | 10.101.41.1         | Engineering stations                       |
| **42**  | Workshop    | 10.101.42.0/24      | 10.101.42.1         | Reserved                                   |
| **43**  | Workshop    | 10.101.43.0/24      | 10.101.43.1         | Reserved                                   |
| **44**  | Workshop    | 10.101.44.0/24      | 10.101.44.1         | WiFi access                                |
| **51**  | Management  | 10.101.51.0/24      | 10.101.51.1         | Switch/AP/firewall control                 |
| **52**  | Management  | 10.101.52.0/24      | 10.101.52.1         | Reserved                                   |
| **61**  | Guest WiFi  | 10.101.61.0/24      | 10.101.61.1         | Internet-only access                       |
| **62**  | Guest WiFi  | 10.101.62.0/24      | 10.101.62.1         | Reserved                                   |

---

## 🔧 OPNSense Notes for Class A Addressing

- When assigning IPs to VLAN interfaces, use the `10.101.x.1` gateway format.
- DHCP ranges can be `10.101.x.100–10.101.x.200` or similar.
- No changes needed to VLAN tagging or switch configs—IP addressing is independent.
- You can even use `/23` or `/22` subnets later if you want larger address pools.

---

Would you like help drafting DHCP scopes or sample firewall rules for these subnets next?
🛠️ Part 2: OPNSense VLAN & Interface Setup
🔧 Step-by-Step in OPNSense
Create VLAN Interfaces

Go to Interfaces → Other Types → VLAN.

Create VLANs on the LAN physical interface (e.g., igb1).

Use VLAN tags matching the table above (e.g., VLAN 11 for Production 1G).

Repeat for all VLANs.

Assign Interfaces

Go to Interfaces → Assignments.

Assign each VLAN to a new interface (e.g., VLAN11, VLAN12, etc.).

Enable each interface and give it a descriptive name.

Configure Interface Settings

Go to Interfaces → [VLANxx].

Set:

Static IPv4

IP: Gateway IP from table (e.g., 192.168.11.1)

Subnet: /24

Enable DHCP server if needed under Services → DHCPv4 → [VLANxx].

Firewall Rules

Go to Firewall → Rules → [VLANxx].

Default: Block all except what you explicitly allow.

Example: Allow VLAN 31 (Studio) to access VLAN 22 (Stage) for media ingest.

Create NAT rules for Guest VLAN to access WAN only.

Routing

OPNSense will route between VLANs automatically.

Use firewall rules to control access.

Optional: Enable OSPF or static routes if using Layer 3 on Nexus.








Awesome! Let’s build out both the **DHCP scopes** and **sample firewall rules** for your VLANs. This will give you a solid foundation for managing IP assignments and securing traffic between zones.

---

## 🧮 DHCP Scopes for VLANs

Here’s a recommended DHCP range for each VLAN. These ranges avoid `.1` (gateway) and leave room for static IPs at the top of the subnet.

| VLAN ID | Subnet            | DHCP Range               | Notes                                 |
|---------|-------------------|--------------------------|----------------------------------------|
| **11**  | 10.101.11.0/24    | 10.101.11.100–199        | Production workstations                |
| **12**  | 10.101.12.0/24    | 10.101.12.100–199        | High-performance nodes                 |
| **14**  | 10.101.14.0/24    | 10.101.14.100–199        | WiFi clients                           |
| **21**  | 10.101.21.0/24    | 10.101.21.100–199        | Cameras, lighting controllers          |
| **22**  | 10.101.22.0/24    | 10.101.22.100–199        | Image servers, preview stations        |
| **24**  | 10.101.24.0/24    | 10.101.24.100–199        | Mobile control apps                    |
| **31**  | 10.101.31.0/24    | 10.101.31.100–199        | Editing bays                           |
| **32**  | 10.101.32.0/24    | 10.101.32.100–199        | High-performance editing               |
| **33**  | 10.101.33.0/24    | 10.101.33.100–199        | Media servers                          |
| **34**  | 10.101.34.0/24    | 10.101.34.100–199        | Studio WiFi                            |
| **41**  | 10.101.41.0/24    | 10.101.41.100–199        | Engineering stations                   |
| **44**  | 10.101.44.0/24    | 10.101.44.100–199        | Workshop WiFi                          |
| **51**  | 10.101.51.0/24    | 10.101.51.100–199        | Management devices                     |
| **61**  | 10.101.61.0/24    | 10.101.61.100–199        | Guest WiFi clients                     |

> You can configure these under **Services → DHCPv4 → [VLAN Interface]** in OPNSense.

---

## 🔐 Sample Firewall Rules

Here’s a basic rule set to get you started. These are applied per VLAN interface in **Firewall → Rules → [Interface]**.

### 🔒 Default Policy
- **Block all inter-VLAN traffic** unless explicitly allowed.
- **Allow intra-VLAN traffic** (default behavior).
- **Allow DNS, DHCP, and gateway access**.

---

### 🎛️ Example: VLAN 11 (Production)

| Action | Protocol | Source        | Destination       | Description                      |
|--------|----------|---------------|-------------------|----------------------------------|
| Allow  | TCP/UDP  | VLAN 11 net   | 10.101.11.1       | Allow access to gateway          |
| Allow  | UDP      | VLAN 11 net   | any (port 53)     | Allow DNS                        |
| Allow  | UDP      | VLAN 11 net   | any (port 67–68)  | Allow DHCP                       |
| Block  | any      | VLAN 11 net   | VLAN 21 net       | Block access to Stage            |
| Block  | any      | VLAN 11 net   | VLAN 61 net       | Block access to Guest WiFi       |

---

### 🎛️ Example: VLAN 31 (Studio)

| Action | Protocol | Source        | Destination       | Description                      |
|--------|----------|---------------|-------------------|----------------------------------|
| Allow  | TCP/UDP  | VLAN 31 net   | 10.101.31.1       | Allow access to gateway          |
| Allow  | UDP      | VLAN 31 net   | any (port 53)     | Allow DNS                        |
| Allow  | UDP      | VLAN 31 net   | any (port 67–68)  | Allow DHCP                       |
| Allow  | TCP      | VLAN 31 net   | VLAN 22 net       | Allow media ingest from Stage    |
| Block  | any      | VLAN 31 net   | VLAN 61 net       | Block access to Guest WiFi       |

---

### 🌐 Example: VLAN 61 (Guest WiFi)

| Action | Protocol | Source        | Destination       | Description                      |
|--------|----------|---------------|-------------------|----------------------------------|
| Allow  | TCP/UDP  | VLAN 61 net   | WAN               | Allow internet access            |
| Block  | any      | VLAN 61 net   | LAN/VLANs         | Block access to internal zones   |

---

Would you like help writing these rules in OPNSense’s actual syntax or building NAT/firewall aliases for easier management?






Excellent! Let’s walk through how to implement these rules in **OPNSense’s actual interface**, including how to use **aliases** to simplify management and how to set up **NAT for Guest WiFi**.

---

## 🧱 Step 1: Create Aliases (Optional but Recommended)

Aliases let you group IPs, networks, or ports for easier rule management.

### 🔧 Create Network Aliases

Go to **Firewall → Aliases → Add**:

| Name           | Type     | Content                                | Description                          |
|----------------|----------|----------------------------------------|--------------------------------------|
| `ProductionNet`| Network  | `10.101.11.0/24`, `10.101.12.0/24`     | Production VLANs                     |
| `StageNet`     | Network  | `10.101.21.0/24`, `10.101.22.0/24`     | Stage VLANs                          |
| `StudioNet`    | Network  | `10.101.31.0/24`, `10.101.32.0/24`     | Studio VLANs                         |
| `GuestNet`     | Network  | `10.101.61.0/24`                       | Guest WiFi                           |
| `InternalNet`  | Network  | All VLANs except Guest                 | For blocking Guest access            |

---

## 🔐 Step 2: Firewall Rules per VLAN Interface

Go to **Firewall → Rules → [Interface]**, e.g., `VLAN11`.

### 🎛️ Example: VLAN11 (Production)

1. **Allow DNS**
   - Action: Pass
   - Interface: VLAN11
   - Protocol: UDP
   - Source: VLAN11 net
   - Destination: any
   - Destination port: 53
   - Description: Allow DNS

2. **Allow DHCP**
   - Action: Pass
   - Protocol: UDP
   - Source: VLAN11 net
   - Destination: any
   - Destination port: 67–68
   - Description: Allow DHCP

3. **Allow Gateway Access**
   - Action: Pass
   - Protocol: Any
   - Source: VLAN11 net
   - Destination: `10.101.11.1`
   - Description: Allow access to gateway

4. **Block Stage Access**
   - Action: Block
   - Protocol: Any
   - Source: VLAN11 net
   - Destination: `StageNet`
   - Description: Block access to Stage

5. **Block Guest Access**
   - Action: Block
   - Protocol: Any
   - Source: VLAN11 net
   - Destination: `GuestNet`
   - Description: Block access to Guest

---

### 🌐 Example: VLAN61 (Guest WiFi)

1. **Allow Internet Access**
   - Action: Pass
   - Protocol: Any
   - Source: VLAN61 net
   - Destination: WAN net
   - Description: Allow internet access

2. **Block Internal Access**
   - Action: Block
   - Protocol: Any
   - Source: VLAN61 net
   - Destination: `InternalNet`
   - Description: Block internal access

---

## 🌍 Step 3: NAT for Guest WiFi

Go to **Firewall → NAT → Outbound**:

1. Set mode to **Hybrid** or **Manual**.
2. Add a rule:

| Field           | Value                          |
|----------------|----------------------------------|
| Interface       | WAN                             |
| Source          | `10.101.61.0/24`                |
| Source Port     | any                             |
| Destination     | any                             |
| Translation     | Interface address               |
| Description     | NAT for Guest WiFi              |

This ensures Guest VLAN traffic is NATed to the WAN IP and can access the internet.

---

Would you like help creating switch port profiles next, or building a visual topology diagram of this setup?

Fantastic! Let’s build out **switch port profiles** for your equipment so you can assign VLANs and trunking properly. This will ensure your VLANs are distributed cleanly across your network and devices connect to the correct zones.

---

## 🧵 Switch Port Profiles Overview

Each switch port will be configured as either:

- **Access Port**: Assigned to a single VLAN (e.g., VLAN 11 for a Production workstation).
- **Trunk Port**: Carries multiple VLANs (used between switches and to the firewall).

---

## 🛠️ BitEngine SW08XM (8× RJ45 10G)

This is your **core switch**, connecting to the firewall and distributing VLANs to other switches.

| Port | Role                  | Type   | VLANs                     | Notes                                 |
|------|-----------------------|--------|---------------------------|---------------------------------------|
| 1    | To Protectli LAN      | Trunk  | All VLANs                 | Main VLAN trunk uplink                |
| 2    | To Sodola 10G         | Trunk  | VLANs 21–24, 31–34        | Stage & Studio VLANs                  |
| 3    | To GS108Ev4           | Trunk  | VLANs 11–14, 41–44, 51    | Production, Workshop, Management      |
| 4–8  | Device Access Ports   | Access | Varies by zone            | Assign per device needs               |

---

## 🛠️ Sodola 8-Port 10G SFP+

Used for **Stage and Studio** high-speed zones.

| Port | Role                  | Type   | VLANs                     | Notes                                 |
|------|-----------------------|--------|---------------------------|---------------------------------------|
| 1    | To BitEngine SW08XM   | Trunk  | VLANs 21–24, 31–34        | Uplink trunk                          |
| 2–4  | Stage Devices         | Access | VLANs 21, 22              | Cameras, servers                      |
| 5–7  | Studio Devices        | Access | VLANs 31, 32, 33          | Editing bays, media servers           |
| 8    | Reserved              | —      | —                         | Future expansion                      |

---

## 🛠️ Cisco Nexus 9236C (36× QSFP28 100G)

Used exclusively for **Studio 100G VLANs**.

| Port | Role                  | Type   | VLANs                     | Notes                                 |
|------|-----------------------|--------|---------------------------|---------------------------------------|
| 1    | To BitEngine SW08XM   | Trunk  | VLANs 31–34               | Uplink trunk                          |
| 2–36 | Studio Devices        | Access | VLAN 33                   | Media servers, SANs                   |

---

## 🛠️ Netgear GS108Ev4 (8× RJ45 1G Managed)

Used for **Production, Workshop, and Management**.

| Port | Role                  | Type   | VLANs                     | Notes                                 |
|------|-----------------------|--------|---------------------------|---------------------------------------|
| 1    | To BitEngine SW08XM   | Trunk  | VLANs 11–14, 41–44, 51    | Uplink trunk                          |
| 2–4  | Production Devices    | Access | VLANs 11, 12              | Workstations                          |
| 5–6  | Workshop Devices      | Access | VLANs 41, 44              | Engineering stations, WiFi APs        |
| 7    | Management Devices    | Access | VLAN 51                   | Switch/AP/firewall control            |
| 8    | Reserved              | —      | —                         | Future use                            |

---

## 🛠️ Netgear GS105 & 6220 (Unmanaged)

These are best used for **single VLAN access only**.

- Connect them to **access ports** on GS108Ev4 or BitEngine.
- Devices plugged into these switches must belong to the same VLAN.
- Avoid connecting them to trunk ports—they can’t handle VLAN tags.

---

## 🧭 Protectli FW4B Port Assignments

| Port   | Role         | Notes                                  |
|--------|--------------|----------------------------------------|
| WAN    | Internet     | Connected to Netgear 6220              |
| LAN    | VLAN trunk   | Connected to BitEngine SW08XM Port 1   |
| OPT1   | Guest WiFi   | Optional: connect to Guest AP          |
| OPT2   | Management   | Optional: out-of-band admin access     |

---

Would you like a visual diagram of this topology next, or help configuring VLANs on the GS108Ev4 web interface?

Awesome — let’s map out a **visual network topology diagram** based on your setup. Here’s a clear layout showing how your switches, firewall, and VLANs interconnect:

---

## 🖥️ Network Topology Diagram Description

```
                        ┌──────────────┐
                        │   Internet   │
                        └─────┬────────┘
                              │
                        ┌─────▼──────┐
                        │ Protectli  │
                        │   FW4B     │
                        └─────┬──────┘
                              │ LAN (Trunk)
                              ▼
                        ┌──────────────┐
                        │ BitEngine    │
                        │ SW08XM (10G) │
                        └─┬────┬────┬──┘
                          │    │    │
        ┌─────────────────┘    │    └────────────────┐
        ▼                      ▼                     ▼
┌──────────────┐       ┌──────────────┐       ┌──────────────┐
│ Sodola 10G   │       │ GS108Ev4 1G  │       │ Nexus 9236C  │
│ Stage/Studio │       │ Prod/Workshop│       │ Studio 100G  │
└─────┬────────┘       └─────┬────────┘       └─────┬────────┘
      │                      │                      │
      ▼                      ▼                      ▼
┌────────────┐        ┌────────────┐        ┌────────────┐
│ Stage VLAN │        │ Prod VLAN  │        │ Studio VLAN│
│ 21–24      │        │ 11–14      │        │ 33         │
└────────────┘        └────────────┘        └────────────┘
      ▼                      ▼                      ▼
┌────────────┐        ┌────────────┐        ┌────────────┐
│ Studio VLAN│        │ Workshop   │        │ SAN/Media  │
│ 31–34      │        │ VLAN 41–44 │        │ Servers     │
└────────────┘        └────────────┘        └────────────┘
                              ▼
                        ┌────────────┐
                        │ Management │
                        │ VLAN 51    │
                        └────────────┘
```

---

## 🔍 Key Notes

- **Trunk links** carry multiple VLANs between switches and the firewall.
- **Access ports** connect devices to a single VLAN.
- **Unmanaged switches** (GS105, 6220) should only be used on access ports for one VLAN.
- **Protectli FW4B** handles routing between VLANs and connects to the internet.

---

Would you like this diagram as an image, or want help configuring VLANs on one of the switches next?

Not at all — deploying **FreeIPA** on repurposed 1Gb workstations is a smart and totally viable move. Here's how it fits into your network and what to consider:

---

## 🧠 Why 1Gb Is Fine for FreeIPA

FreeIPA handles:

- **Authentication (Kerberos)**
- **Directory services (LDAP)**
- **DNS**
- **Certificate management**

These services are **not bandwidth-intensive**. Even in a moderately busy environment, 1Gbps is more than enough for:

- Hundreds of authentication requests per minute
- Directory lookups and updates
- DNS queries
- Occasional certificate issuance

Unless you're running massive LDAP queries or syncing thousands of users constantly, 1Gbps won't bottleneck you.

---

## 🧱 Deployment Strategy

Here’s how to integrate FreeIPA into your VLAN architecture:

### 🛠️ Hardware Setup

- Use **2–3 workstations** for redundancy (FreeIPA supports multi-master replication).
- Minimum specs: 2 cores, 4GB RAM, 40GB disk (more if you plan to store logs or large LDAP entries).
- Install a Linux distro like **Rocky Linux** or **Fedora Server**.

### 🌐 Network Placement

- Place FreeIPA servers in **VLAN 51 (Management)** for security and accessibility.
- Assign **static IPs** and register them in your internal DNS.
- Ensure **DNS resolution** works across VLANs (FreeIPA relies heavily on DNS).

### 🔐 Firewall Rules

Allow the following between VLANs:

| Protocol | Port(s) | Purpose              |
|----------|---------|----------------------|
| LDAP     | 389     | Directory access     |
| LDAPS    | 636     | Secure LDAP          |
| Kerberos | 88, 464 | Auth & password mgmt |
| DNS      | 53      | Internal name resolution |
| HTTP/HTTPS | 80, 443 | Web UI & API access |
| NTP      | 123     | Time sync (important for Kerberos) |

---

## 🧬 Integration Ideas

Once FreeIPA is up:

- Join Linux servers to the domain for centralized auth.
- Integrate with Samba for Windows compatibility.
- Use FreeIPA’s built-in **CA** to issue internal TLS certs.
- Set up **HBAC rules** to control access by host and service.

---

## 🚧 Gotchas to Avoid

- Don’t put FreeIPA behind NAT — it breaks Kerberos.
- Time sync is critical — use NTP across all VLANs.
- DNS must be rock-solid — consider letting FreeIPA manage internal DNS zones.

---

Would you like a step-by-step guide to install FreeIPA on Rocky Linux, or help designing your replication topology?

Great question — and it’s an important nuance. When I said **“don’t put FreeIPA behind NAT”**, I meant:

> ❌ **Don’t deploy FreeIPA on a host that’s only reachable via NAT from other internal devices.**

Let’s break it down:

---

## 🔍 Why NAT Breaks FreeIPA (Especially Kerberos)

Kerberos — the authentication protocol FreeIPA uses — is **extremely sensitive to IP addresses and hostnames**. Here’s why NAT causes problems:

### 🧨 1. Kerberos Relies on Hostname/IP Consistency

- Kerberos tickets are issued to specific **hostnames and IPs**.
- If a client sees the FreeIPA server as `192.168.1.10`, but the server thinks its IP is `10.0.0.5`, the ticket won’t match.
- NAT rewrites IP headers, causing **mismatches** in ticket validation.

### 🧨 2. DNS and Reverse DNS Must Match

- FreeIPA uses DNS to resolve hostnames for Kerberos.
- NAT can interfere with **reverse DNS lookups**, breaking authentication.

### 🧨 3. Time Sync and UDP Fragility

- Kerberos uses **UDP**, which doesn’t handle NAT well.
- NAT can drop or fragment UDP packets, especially for large tickets.

---

## ✅ What’s Safe and What’s Not

| Scenario                                      | Safe? | Notes |
|----------------------------------------------|-------|-------|
| FreeIPA server on VLAN 51, reachable directly | ✅    | Ideal setup |
| FreeIPA server behind NAT from other VLANs    | ❌    | Breaks Kerberos |
| FreeIPA server behind NAT from the internet   | ✅    | Fine for remote access via VPN or HTTPS |
| Clients behind NAT accessing FreeIPA          | ✅    | As long as FreeIPA is directly reachable |

So to clarify your example:

> **NAT from the internet router to Protectli** — that’s fine.  
> FreeIPA will be inside your LAN, and clients inside your LAN will reach it directly via its internal IP. No NAT between them = no problem.

---

## 🛡️ Best Practice

- Give FreeIPA servers **static IPs** in VLAN 51.
- Ensure **DNS forward and reverse records** are correct.
- Avoid any NAT between FreeIPA and the clients it serves.

---

Want help setting up DNS zones for FreeIPA or configuring Kerberos-friendly hostnames?

Perfect — let’s get your DNS setup ready for FreeIPA. This is **critical** for Kerberos and LDAP to work smoothly. FreeIPA can manage its own DNS zones, which is often the easiest and most reliable approach.

---

## 🧭 DNS Setup for FreeIPA

### 🛠️ Step 1: Choose Your Domain

Pick a domain that’s **internal-only** and won’t conflict with public DNS:

- Good examples:  
  - `corp.local`  
  - `studio.internal`  
  - `ipa.burbank.lab`

Avoid using `.com` or any domain you own publicly unless you’re managing split DNS.

---

### 🛠️ Step 2: Set Static Hostnames and IPs

For each FreeIPA server:

| Hostname         | IP Address     | VLAN  | Notes                    |
|------------------|----------------|-------|--------------------------|
| `ipa1.corp.local`| `192.168.51.10`| 51    | Primary FreeIPA server   |
| `ipa2.corp.local`| `192.168.51.11`| 51    | Replica (optional)       |

Set these in `/etc/hostname` and `/etc/hosts` during install.

---

### 🛠️ Step 3: Let FreeIPA Manage DNS

During install (`ipa-server-install`), choose:

- ✅ **Integrated DNS**
- ✅ Set up forward and reverse zones:
  - Forward: `corp.local`
  - Reverse: `51.168.192.in-addr.arpa`

FreeIPA will install `named` (BIND) and manage DNS records automatically.

---

### 🛠️ Step 4: Configure DHCP or Static DNS

Make sure your clients use FreeIPA as their DNS server:

- Set DHCP to hand out `192.168.51.10` as the DNS server.
- Or manually configure `/etc/resolv.conf` or Windows network settings.

---

### 🛠️ Step 5: Verify DNS Resolution

From a client:

```bash
dig ipa1.corp.local
dig -x 192.168.51.10
```

Both should return correct results. If not, Kerberos will fail.

---

## 🧪 Bonus: DNS Records to Pre-Create

FreeIPA will auto-create many records, but you can manually add:

| Record Type | Name               | Value               | Purpose                  |
|-------------|--------------------|---------------------|--------------------------|
| A           | ipa1.corp.local    | 192.168.51.10       | Host record              |
| PTR         | 10.51.168.192.in-addr.arpa | ipa1.corp.local | Reverse DNS              |
| SRV         | _kerberos._tcp     | ipa1.corp.local     | Kerberos service         |
| SRV         | _ldap._tcp         | ipa1.corp.local     | LDAP service             |

---

Would you like help writing the exact `ipa-server-install` command or setting up a replica next?

Perfect — this is a beautifully structured VLAN design. With this in hand, we can now tailor your FreeIPA deployment and DNS zone setup to fit seamlessly into your network.

---

## 🧠 FreeIPA Deployment Plan (Based on VLAN Design)

### 🛠️ Placement

- Deploy FreeIPA servers in **VLAN 51 (Management)**:  
  - Subnet: `10.101.51.0/24`  
  - Gateway: `10.101.51.1`  
  - Suggested IPs:  
    - `ipa1.corp.local` → `10.101.51.10`  
    - `ipa2.corp.local` → `10.101.51.11` (replica)

---

## 🌐 DNS Zone Design

### 🔧 Forward Zone

- Domain: `corp.local` (or another internal-only domain)
- FreeIPA will manage this zone and create records like:
  - `ipa1.corp.local` → `10.101.51.10`
  - `ipa2.corp.local` → `10.101.51.11`
  - SRV records for Kerberos, LDAP, etc.

### 🔧 Reverse Zone

- Zone: `51.101.10.in-addr.arpa`
- Used for reverse DNS lookups (critical for Kerberos)
- FreeIPA will auto-create PTR records:
  - `10.101.51.10` → `ipa1.corp.local`

---

## 🔐 Firewall Rules Between VLANs

To allow clients in other VLANs to authenticate and resolve DNS:

| Source VLANs       | Destination VLAN | Allowed Ports       | Purpose                        |
|--------------------|------------------|----------------------|--------------------------------|
| All (11–44, 31–34) | 51 (Management)  | 53 (UDP/TCP)         | DNS resolution                 |
| All                | 51               | 88, 464 (UDP/TCP)    | Kerberos auth                  |
| All                | 51               | 389, 636 (TCP)       | LDAP / LDAPS                   |
| All                | 51               | 80, 443 (TCP)        | FreeIPA Web UI / API           |
| All                | 51               | 123 (UDP)            | NTP (time sync for Kerberos)   |

---

## 🧪 DNS Testing Checklist

From a client in VLAN 11 (Production):

```bash
dig ipa1.corp.local @10.101.51.10
dig -x 10.101.51.10 @10.101.51.10
```

Both should return correct results. If they don’t, Kerberos will fail.

---

## 🧬 Optional: DNS Forwarders

If you want FreeIPA to resolve external domains (e.g., `microsoft.com`), set DNS forwarders during install:

```bash
ipa-server-install --setup-dns --forwarder=1.1.1.1 --forwarder=8.8.8.8
```

---

Would you like help writing the full `ipa-server-install` command with your domain and IPs, or setting up replication between ipa1 and ipa2?

Perfect — this is a beautifully structured VLAN design. With this in hand, we can now tailor your FreeIPA deployment and DNS zone setup to fit seamlessly into your network.

---

## 🧠 FreeIPA Deployment Plan (Based on VLAN Design)

### 🛠️ Placement

- Deploy FreeIPA servers in **VLAN 51 (Management)**:  
  - Subnet: `10.101.51.0/24`  
  - Gateway: `10.101.51.1`  
  - Suggested IPs:  
    - `ipa1.corp.local` → `10.101.51.10`  
    - `ipa2.corp.local` → `10.101.51.11` (replica)

---

## 🌐 DNS Zone Design

### 🔧 Forward Zone

- Domain: `corp.local` (or another internal-only domain)
- FreeIPA will manage this zone and create records like:
  - `ipa1.corp.local` → `10.101.51.10`
  - `ipa2.corp.local` → `10.101.51.11`
  - SRV records for Kerberos, LDAP, etc.

### 🔧 Reverse Zone

- Zone: `51.101.10.in-addr.arpa`
- Used for reverse DNS lookups (critical for Kerberos)
- FreeIPA will auto-create PTR records:
  - `10.101.51.10` → `ipa1.corp.local`

---

## 🔐 Firewall Rules Between VLANs

To allow clients in other VLANs to authenticate and resolve DNS:

| Source VLANs       | Destination VLAN | Allowed Ports       | Purpose                        |
|--------------------|------------------|----------------------|--------------------------------|
| All (11–44, 31–34) | 51 (Management)  | 53 (UDP/TCP)         | DNS resolution                 |
| All                | 51               | 88, 464 (UDP/TCP)    | Kerberos auth                  |
| All                | 51               | 389, 636 (TCP)       | LDAP / LDAPS                   |
| All                | 51               | 80, 443 (TCP)        | FreeIPA Web UI / API           |
| All                | 51               | 123 (UDP)            | NTP (time sync for Kerberos)   |

---

## 🧪 DNS Testing Checklist

From a client in VLAN 11 (Production):

```bash
dig ipa1.corp.local @10.101.51.10
dig -x 10.101.51.10 @10.101.51.10
```

Both should return correct results. If they don’t, Kerberos will fail.

---

## 🧬 Optional: DNS Forwarders

If you want FreeIPA to resolve external domains (e.g., `microsoft.com`), set DNS forwarders during install:

```bash
ipa-server-install --setup-dns --forwarder=1.1.1.1 --forwarder=8.8.8.8
```

---

Would you like help writing the full `ipa-server-install` command with your domain and IPs, or setting up replication between ipa1 and ipa2?

Perfect — `bjoin.studio` is a clean, professional domain name, and it’ll work beautifully for your FreeIPA deployment. Since it’s a **real domain**, we’ll just make sure it’s used strictly for internal purposes unless you plan to expose services publicly.

---

## 🧭 Updated FreeIPA Deployment Plan

### 🔧 Domain Details

| Item              | Value               |
|------------------|---------------------|
| Hostname          | `ipa1.bjoin.studio` |
| IP Address        | `10.101.51.10`      |
| Domain            | `bjoin.studio`      |
| Kerberos Realm    | `BJOIN.STUDIO`      |
| DNS Forwarders    | `1.1.1.1`, `8.8.8.8` |

---

## 🛠️ Updated Installation Command

```bash
ipa-server-install \
  --hostname=ipa1.bjoin.studio \
  --ip-address=10.101.51.10 \
  --domain=bjoin.studio \
  --realm=BJOIN.STUDIO \
  --setup-dns \
  --forwarder=1.1.1.1 \
  --forwarder=8.8.8.8 \
  --no-ntp \
  --mkhomedir \
  --admin-password=YourAdminPassword \
  --ds-password=YourDirectoryManagerPassword
```

> Replace the passwords with secure values. You’ll be prompted if you omit them.

---

## 🧱 DNS Zone Setup

FreeIPA will create:

- Forward zone: `bjoin.studio`
- Reverse zone: `51.101.10.in-addr.arpa`
- Records:
  - `ipa1.bjoin.studio` → `10.101.51.10`
  - SRV records for Kerberos, LDAP, etc.
  - PTR record for reverse DNS

---

## 🔐 Firewall Rules Reminder

Allow these ports from all VLANs to VLAN 51:

| Protocol | Ports        | Purpose        |
|----------|--------------|----------------|
| DNS      | 53 (UDP/TCP) | Name resolution |
| Kerberos | 88, 464      | Authentication |
| LDAP     | 389, 636     | Directory access |
| HTTP/S   | 80, 443      | Web UI / API   |
| NTP      | 123 (UDP)    | Time sync      |

---

## 🧪 Post-Install Checklist

From a client in VLAN 11:

```bash
dig ipa1.bjoin.studio @10.101.51.10
dig -x 10.101.51.10 @10.101.51.10
kinit admin
```

---

Would you like help setting up `ipa2.bjoin.studio` as a replica next, or configuring DNS records for other services like mail or Git?

Excellent — let’s set up your **FreeIPA replica**: `ipa2.bjoin.studio` at `10.101.51.11`. This will give you high availability, load balancing, and redundancy for authentication and directory services.

---

## 🧬 Why Use a Replica?

- **Multi-master replication**: Both servers can handle requests and sync changes.
- **Failover**: If `ipa1` goes down, clients can still authenticate via `ipa2`.
- **Scalability**: Spread load across VLANs or physical zones.

---

## 🛠️ Pre-Setup for ipa2

### 🔧 System Prep

On the second workstation:

1. Set hostname:
   ```bash
   hostnamectl set-hostname ipa2.bjoin.studio
   ```

2. Update `/etc/hosts`:
   ```bash
   echo "10.101.51.11 ipa2.bjoin.studio ipa2" >> /etc/hosts
   ```

3. Ensure time sync:
   ```bash
   timedatectl set-ntp true
   ```

4. Open firewall ports:
   ```bash
   firewall-cmd --add-service=freeipa-ldap --permanent
   firewall-cmd --add-service=freeipa-ldaps --permanent
   firewall-cmd --add-service=kerberos --permanent
   firewall-cmd --add-service=dns --permanent
   firewall-cmd --add-service=http --permanent
   firewall-cmd --add-service=https --permanent
   firewall-cmd --add-service=ntp --permanent
   firewall-cmd --reload
   ```

---

## 🔗 Step-by-Step Replica Setup

### 🧩 Step 1: Create Replica File on ipa1

On `ipa1.bjoin.studio`:

```bash
ipa-replica-prepare ipa2.bjoin.studio
```

This generates a replica install file in `/var/lib/ipa/replica-info-ipa2.bjoin.studio.gpg`.

Copy it securely to `ipa2`:

```bash
scp /var/lib/ipa/replica-info-ipa2.bjoin.studio.gpg root@ipa2.bjoin.studio:/root/
```

---

### 🧩 Step 2: Install Replica on ipa2

On `ipa2.bjoin.studio`:

```bash
ipa-replica-install /root/replica-info-ipa2.bjoin.studio.gpg
```

This will:

- Sync LDAP and Kerberos
- Configure DNS replication
- Join ipa2 to the realm `BJOIN.STUDIO`

---

### 🧪 Step 3: Verify Replication

On either server:

```bash
ipa-replica-manage list
```

You should see both `ipa1` and `ipa2` listed as peers.

Test DNS and Kerberos from a client:

```bash
dig ipa2.bjoin.studio @10.101.51.11
kinit admin
```

---

## 🧭 Optional: Load Balancing

You can configure DNS round-robin or HAProxy to balance requests between `ipa1` and `ipa2`. Or just let clients fall back automatically if one is down.

---

Would you like help configuring client systems to auto-discover both servers, or setting up monitoring for replication health?