🍌 Studio Network Architecture: bjoin.studio
🧭 Environment Overview
Environment	Description
Workshop	Low bandwidth, local only, no internet, limited servers, 1Gb switch only
Stage	Medium bandwidth, limited internet, 1Gb + 10Gb switches
Studio	High bandwidth, limited internet, many servers, 1Gb + 10Gb + 100Gb switches
Production	Medium bandwidth, medium internet, limited servers, 1Gb + 10Gb + WiFi
🌐 VLAN and Subnet Assignments
VLAN ID	Environment	Bandwidth Tier	Subnet Range	Notes
10	Workshop	1Gb	10.10.101.0/24	Isolated, no internet
20	Stage	1Gb	10.10.201.0/24	Basic devices
21	Stage	10Gb	10.10.210.0/24	High-performance gear
30	Studio	1Gb	10.10.301.0/24	Legacy or low-bandwidth gear
31	Studio	10Gb	10.10.310.0/24	Mid-tier servers/devices
32	Studio	100Gb	10.10.310.0/24	Core infrastructure
40	Production	1Gb	10.10.401.0/24	General devices
41	Production	10Gb	10.10.410.0/24	High-performance gear
42	Production	WiFi	10.10.18.0/24	Wireless clients
🔐 VPN Zones
VPN Type	Subnet Range	Access Scope
Remote Access VPN	10.20.250.0/24	Studio 1Gb + Production 1Gb only
Site-to-Site VPN	10.20.251.0/24	Inter-environment bridging
🔄 Routing & Visibility Rules
Source VLAN	Destination VLAN	Access Allowed	Notes
32 (Studio 100Gb)	All VLANs	✅ Yes	Full visibility
31 (Studio 10Gb)	All VLANs	✅ Yes	Full visibility
30 (Studio 1Gb)	31, 32	❌ No	Blocked unless explicitly allowed
10 (Workshop)	31, 32	❌ No	Isolated
40–42 (Production)	31, 32	❌ No	Blocked from initiating traffic
VPN Clients	VLAN 30, 40	✅ Yes	Limited access to Studio/Production 1Gb
🧱 Hardware Notes
Component	Role
Router / L3 Switch	VLAN routing, ACL enforcement
Managed Switches	VLAN tagging, QoS
Firewall	Stateful inspection, traffic shaping
WiFi Controller	VLAN-aware SSIDs
📌 Expansion Ideas
Reserve 10.20.11.0/24 to 10.20.15.0/24 for future Studio growth
Add VLAN 50+ for management interfaces or out-of-band control
Use internal DNS (e.g., dnsmasq) for banana.studio domain resolution










Absolutely! Here's a single Markdown document that outlines your studio network architecture using structured tables. It includes:

Environment overview

VLAN and subnet assignments

Bandwidth tiers

Routing and visibility rules

VPN zones

You can copy this into any Markdown editor or documentation system and expand on it as your network evolves.

🍌 Studio Network Architecture: banana.studio

🧭 Environment Overview

Workshop: [1Gb] Local only, no internet
Stage:    [1Gb/10Gb] Limited internet
Studio:   [1Gb/10Gb/100Gb] Limited internet
Production: [1Gb/10Gb/WiFi] Medium internet

🌐 VLAN and Subnet Assignments

VLAN 10: Workshop [1Gb] 10.20.0.0/24
VLAN 20: Stage [1Gb] 10.20.4.0/24
VLAN 21: Stage [10Gb] 10.20.5.0/24
VLAN 30: Studio [1Gb] 10.20.8.0/24
VLAN 31: Studio [10Gb] 10.20.9.0/24
VLAN 32: Studio [100Gb] 10.20.10.0/24
VLAN 40: Production [1Gb] 10.20.16.0/24
VLAN 41: Production [10Gb] 10.20.17.0/24
VLAN 42: Production [WiFi] 10.20.18.0/24

🔐 VPN Zones

Remote Access VPN: 10.20.250.0/24
Site-to-Site VPN: 10.20.251.0/24

🔄 Routing & Visibility Rules

Studio 100Gb (VLAN 32): Full visibility to all VLANs
Studio 10Gb (VLAN 31): Full visibility to all VLANs
Studio 1Gb (VLAN 30): Blocked to VLAN 31, 32 unless allowed
Workshop (VLAN 10): Isolated from VLAN 31, 32
Production (VLAN 40-42): Blocked from initiating traffic to VLAN 31, 32
VPN Clients: Limited access to Studio/Production 1Gb

🧱 Hardware Notes

Router / L3 Switch: VLAN routing, ACL enforcement
Managed Switches: VLAN tagging, QoS
Firewall: Stateful inspection, traffic shaping
WiFi Controller: VLAN-aware SSIDs

📌 Expansion Ideas

Reserve 10.20.11.0/24 to 10.20.15.0/24 for future Studio growth
Add VLAN 50+ for management interfaces or out-of-band control
Use internal DNS (e.g., dnsmasq) for banana.studio domain resolution

Would you like me to turn this into a visual diagram next, or help you write config snippets for your router or switches?


+------------------+       +------------------+       +------------------+       +------------------+
|   Workshop       |       |     Stage        |       |     Studio       |       |   Production     |
| VLAN 10          |       | VLANs 20, 21     |       | VLANs 30, 31, 32 |       | VLANs 40, 41, 42 |
| Subnet:          |       | Subnets:         |       | Subnets:         |       | Subnets:         |
| 10.20.0.0/24     |       | 10.20.4.0/24     |       | 10.20.8.0/24     |       | 10.20.16.0/24    |
|                  |       | 10.20.5.0/24     |       | 10.20.9.0/24     |       | 10.20.17.0/24    |
|                  |       |                  |       | 10.20.10.0/24    |       | 10.20.18.0/24    |
+------------------+       +------------------+       +------------------+       +------------------+

        ↘                     ↘                     ↘                     ↘
         ↘                     ↘                     ↘                     ↘
        +----------------------+----------------------+----------------------+
        |        Router / L3 Switch (VLAN Routing + ACLs)                   |
        +----------------------+----------------------+----------------------+
                          ↘                          ↘
                           ↘                          ↘
            +----------------------+      +----------------------+
            |   VPN Zone           |      |   Internal DNS       |
            | 10.20.250.0/24       |      | banana.studio        |
            +----------------------+      +----------------------+




+--------------------------+      +--------------------------+
| Cisco Nexus 9236C       |      | Sodola 8-Port 10G        |
| 36x QSFP28 (100G)       |      | 8x SFP+ (10G)             |
| Layer 3, Data Center    |      | Web Managed, Fanless     |
| Ideal for core routing  |      | Great for homelab/edge   |
+--------------------------+      +--------------------------+

         ↘                                ↘
          ↘                                ↘

+--------------------------+      +--------------------------+
| BitEngine SW08XM         |      | Netgear ProSafe GS105    |
| 8x RJ45 (10G)            |      | 5x RJ45 (1G)              |
| Web Managed, 160Gbps     |      | Unmanaged, Silent        |
| Ideal for high-speed LAN|      | Good for small segments  |
+--------------------------+      +--------------------------+

🔍 Use Case Summary
Switch Model	Role in Network	Port Type	Management	Ideal For
Cisco Nexus 9236C	Core/Spine Switch	QSFP28 (100G)	Layer 3	Data center, backbone routing
Sodola 8-Port 10G	Aggregation/Edge	SFP+ (10G)	Web	Homelab, small enterprise
BitEngine SW08XM	High-Speed LAN	RJ45 (10G)	Web	NAS, 10G desktop, streaming
Netgear ProSafe GS105	Basic Connectivity	RJ45 (1G)	Unmanaged	Small office, low traffic


You're thinking in the right direction—layering your switches from basic to enterprise-grade is a smart way to build out a test environment. Let’s walk through how to set up your test router and how to assign IP and DHCP settings based on your topology.
🛠️ Suggested Network Topology
[Router]
   ↓
[Netgear GS105] — basic unmanaged switch
   ↓
[BitEngine SW08XM] — 10G RJ45 switch
   ↓
[Sodola 8-Port 10G] — 10G SFP+ switch
   ↓
[Cisco Nexus 9236C] — core L3 switch
This setup lets you:
Use the Netgear for basic devices or initial uplink
Use BitEngine for high-speed copper connections (e.g., desktops, NAS)
Use Sodola for fiber/SFP+ aggregation
Use Cisco Nexus for VLAN routing, ACLs, and backbone traffic
🌐 Router Setup
🔹 IP Addressing
Let’s assume you’re testing in the Workshop VLAN (VLAN 10), which uses:
Subnet: 10.20.0.0/24
Gateway: 10.20.0.1
So your router should be:
LAN IP: 10.20.0.1
Subnet Mask: 255.255.255.0
DHCP Range: 10.20.0.100 – 10.20.0.200 (or adjust as needed)
🔹 DHCP Settings
Start IP: 10.20.0.100
End IP: 10.20.0.200
Lease Time: 24 hours (or shorter for testing)
DNS Server: You can use 10.20.250.10 if you have an internal DNS, or fallback to 8.8.8.8 (Google DNS)
🧠 Pro Tips
Router Placement: If your router supports VLAN tagging and routing, you could eventually move it closer to the Cisco Nexus for more control.
Static IPs: Reserve static IPs for switches and servers outside the DHCP range (e.g., 10.20.0.2 – 10.20.0.50)
Testing: Start with ping tests between devices on the Netgear and BitEngine to confirm connectivity before layering in VLANs and ACLs.
Want help generating a config snippet for your router or a visual of this topology? I can whip that up next.











🧠 Router Setup Strategy
Your router will act as the default gateway for each VLAN. That means:
It needs a virtual interface (SVI) or sub-interface for each VLAN
Each interface gets the .1 IP in its subnet
DHCP ranges should avoid .1 (gateway) and leave room for static IPs
# 🌐 Router IP & DHCP Settings by VLAN

| VLAN | Environment     | Subnet           | Router IP     | DHCP Range                    |
|------|-----------------|------------------|---------------|-------------------------------|
| 10   | Workshop        | 10.20.10.0/24    | 10.20.10.1    | 10.20.10.100 – 10.20.10.200   |
| 20   | Stage 1Gb       | 10.20.20.0/24    | 10.20.20.1    | 10.20.20.100 – 10.20.20.200   |
| 21   | Stage 10Gb      | 10.20.21.0/24    | 10.20.21.1    | 10.20.21.100 – 10.20.21.200   |
| 30   | Studio 1Gb      | 10.20.30.0/24    | 10.20.30.1    | 10.20.30.100 – 10.20.30.200   |
| 31   | Studio 10Gb     | 10.20.31.0/24    | 10.20.31.1    | 10.20.31.100 – 10.20.31.200   |
| 32   | Studio 100Gb    | 10.20.32.0/24    | 10.20.32.1    | 10.20.32.100 – 10.20.32.200   |
| 40   | Prod 1Gb        | 10.20.40.0/24    | 10.20.40.1    | 10.20.40.100 – 10.20.40.200   |
| 42   | Prod WiFi       | 10.20.42.0/24    | 10.20.42.1    | 10.20.42.100 – 10.20.42.200   |
| 41   | Prod 10Gb       | 10.20.41.0/24    | 10.20.41.1    | 10.20.41.100 – 10.20.41.200   |
| VPN  | Remote VPN      | 10.20.250.0/24   | 10.20.250.1   | 10.20.250.100 – 10.20.250.200 |
| VPN  | Site VPN        | 10.20.251.0/24   | 10.20.251.1   | 10.20.251.100 – 10.20.251.200 |

---

# 🔧 Additional Router Config Tips

- Enable VLAN tagging on router interfaces if using trunk ports
- Set up DHCP relay if your router doesn’t serve DHCP directly
- Use ACLs or firewall rules to enforce visibility restrictions  
  _(e.g., block VLAN 10 from accessing VLAN 32)_
- DNS: Point clients to internal DNS (e.g., `10.20.250.10`) or external fallback (`8.8.8.8`)



🔹 Software
OPNsense Installer ISO
Rufus or similar tool to create bootable USB
🚀 Step-by-Step Setup Guide
1. Download & Prepare Installer
Go to OPNsense Downloads
Choose AMD64 architecture, VGA image (unless using serial console)
Use Rufus to write the ISO to your USB stick
2. Install OPNsense on the Vault
Plug in USB, monitor, and keyboard
Boot into USB and follow the installer prompts
Choose ZFS or UFS file system (ZFS recommended for reliability)
Assign interfaces:
WAN → connected to your upstream router (Netgear or modem)
LAN → connected to your internal switch (Netgear GS105 or others)
3. Initial Configuration
Access OPNsense via browser: https://192.168.1.1
Default credentials: admin / opnsense
Change password immediately
Set LAN IP to match your VLAN 10 gateway: 10.20.0.1
🌐 VLAN Setup
Example: Create VLAN 10 (Workshop)
Go to Interfaces > Other Types > VLAN
Add VLAN:
Parent Interface: LAN NIC
VLAN Tag: 10
Description: Workshop
Go to Interfaces > Assignments
Add new VLAN interface
Enable it and set static IP: 10.20.0.1/24
Repeat for VLANs 20–42 as needed.
🧩 DHCP Setup
Go to Services > DHCPv4
Select VLAN 10 interface
Enable DHCP server
Set range: 10.20.0.100 – 10.20.0.200
Repeat for each VLAN.
🔐 Firewall Rules
Go to Firewall > Rules
Select each VLAN interface
Add rules to allow or block traffic based on your visibility matrix
Example: Block VLAN 10 from accessing VLAN 32
🛡️ VPN Setup (Optional for Later)
Use WireGuard or OpenVPN plugin
Assign VPN subnet: 10.20.250.0/24
Create firewall rules to restrict access to Studio/Production 1Gb only
Would you like help generating the exact VLAN and firewall rule config for your studio layout? I can build a tailored config plan for OPNsense.


🧭 Your Setup Goals
Netgear R6220 acts like your ISP router:
Provides DHCP in 192.168.1.0/24
Does NAT and WiFi
Protectli Vault (OPNsense) connects via WAN port to Netgear LAN
Gets IP from Netgear (e.g., 192.168.1.100)
Governs internal VLANs, VPNs, and studio traffic
OPNsense LAN side uses your custom subnet (e.g., 10.20.0.0/24)
Serves DHCP to studio devices
Routes between VLANs
Hosts VPNs
🔌 Physical Connections
[Production Cable Modem]
      ↓
[Netgear R6220] — 192.168.1.1
      ↓
[Protectli Vault WAN port] ← gets IP like 192.168.1.100
      ↓
[Protectli Vault LAN port] → connects to studio switches
      ↓
[Studio Devices] — get IPs like 10.20.0.x
⚙️ IP & DHCP Configuration
🔹 Netgear R6220
LAN IP: 192.168.1.1
DHCP Range: 192.168.1.100 – 192.168.1.200
WAN Port: Connected to cable modem
LAN Port: Connected to Protectli WAN
🔹 Protectli Vault (OPNsense)
WAN IP: Receives 192.168.1.x from Netgear
LAN IP: Set to 10.20.0.1
DHCP Range: 10.20.0.100 – 10.20.0.200
VPN Subnet: 10.20.250.0/24 (for remote access)
🔐 VPN & VLAN Strategy
OPNsense governs internal VLANs (e.g., Workshop, Stage, Studio, Production)
VPN clients connect to OPNsense and get IPs in 10.20.250.0/24
OPNsense routes traffic between VLANs based on your visibility rules
Netgear just provides internet access to OPNsense via WAN
🧠 Why This Works
You’re emulating your ISP router with the Netgear R6220
OPNsense becomes your internal network controller
You avoid double NAT issues because OPNsense is behind Netgear, and you’re not exposing it externally yet
Would you like help setting up OPNsense interfaces and VPN configuration next? I can walk you through assigning VLANs and building firewall rules.



