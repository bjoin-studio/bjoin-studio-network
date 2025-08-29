# 🍌 bjoin.studio Network Architecture Setup Guide

This guide explains how our studio's computer network is set up. Think of it as the digital highway system for all our devices, from computers and cameras to specialized studio equipment. Our goal is to make sure everything runs smoothly, securely, and efficiently.

**How the Internet Connects:**
Imagine the internet as a vast, global highway. Our studio's connection to this highway comes through our Internet Service Provider (ISP) and enters our main network device, the "router on a stick." This isn't a literal stick, but a clever way we use a single physical connection to handle many different virtual network lanes (VLANs). It's like having one main road that branches off into many smaller, organized streets.

**The Firewall: Our Digital Gatekeeper:**
Right after the internet connection, we have our firewall. This is like a vigilant security guard at the entrance of our studio. Its job is to inspect all incoming and outgoing digital traffic. It only allows authorized traffic to pass, blocking anything suspicious or unwanted. This keeps our network safe from external threats and ensures our sensitive data stays private.

**VLANs: Keeping Everyone in Their Lanes:**
Inside our studio, we have different teams and types of equipment. For example, our production team needs access to specific high-performance storage, while our guest Wi-Fi needs to be completely separate for security. This is where VLANs (Virtual Local Area Networks) come in. Think of VLANs as dedicated, separate lanes on our digital highway. Each lane is for a specific group or type of device. This means:
*   The production team's devices stay in their lane, accessing only what they need.
*   Guest devices stay in their own isolated lane, preventing them from accessing our internal studio resources.
*   Our IT management tools have their own secure lane.

This organization prevents congestion, improves security by isolating different types of traffic, and ensures that everyone stays in their designated "lane" on the network.

This guide outlines the full setup of your studio network using the updated VLAN schema, bandwidth tiers, device roles, and routing policies. It’s optimized for deployment with OPNsense on a Protectli Vault.

---

## 🗺️ Definitive VLAN and IP Plan

This table serves as the single source of truth for VLANs, subnets, and IP addressing, and their corresponding FreeIPA groups.

| VLAN ID | Zone         | Purpose                          | Primary FreeIPA Group | Devices / Use Cases              | Subnet          | Gateway IP     | DHCP Range                  |
|:--------|:-------------|:---------------------------------|:----------------------|:---------------------------------|:----------------|:---------------|:----------------------------|
| **11**  | Production   | Business-critical services       | `grp-production`      | Producer, admin staff, finance systems, CRM, secure document storage | `10.20.11.0/24` | `10.20.11.1`   | `10.20.11.100 – 200`        |
| **12**  | Production   | High-performance production      | `grp-production`      | Render nodes, file servers       | `10.20.12.0/24` | `10.20.12.1`   | `10.20.12.100 – 200`        |
| **13**  | Production   | Production Reserved              | `grp-production`      | Future production needs          | `10.20.13.0/24` | `10.20.13.1`   | Static only                 |
| **14**  | Production   | Production Wifi                  | `grp-production`      | Staff laptops, mobile devices    | `10.20.14.0/24` | `10.20.14.1`   | `10.20.14.100 – 200`        |
| **15**  | Production   | Production Monitoring            | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.15.0/24` | `10.20.15.1`   | `10.20.15.100 – 200`        |
| **21**  | Stage        | Physical photography stage       | `grp-stage`           | Robotic rigs, lighting arrays, product movers, control systems, IoT interfaces | `10.20.21.0/24` | `10.20.21.1`   | `10.20.21.100 – 200`        |
| **22**  | Stage        | High-performance stage           | `grp-stage`           | Image servers, preview stations  | `10.20.22.0/24` | `10.20.22.1`   | `10.20.22.100 – 200`        |
| **23**  | Stage        | Stage Reserved                   | `grp-stage`           | Future stage needs               | `10.20.23.0/24` | `10.20.23.1`   | Static only                 |
| **24**  | Stage        | Stage Wifi                       | `grp-stage`           | Tablets, mobile control apps     | `10.20.24.0/24` | `10.20.24.1`   | `10.20.24.100 – 200`        |
| **25**  | Stage        | Stage Monitoring                 | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.25.0/24` | `10.20.25.1`   | `10.20.25.100 – 200`        |
| **31**  | Studio       | Digital photography processing   | `grp-studio`          | Director, editors, retouchers, editing suites, color grading tools | `10.20.31.0/24` | `10.20.31.1`   | `10.20.31.100 – 200`        |
| **32**  | Studio       | High-performance studio          | `grp-studio`          | Color grading, VFX workstations  | `10.20.32.0/24` | `10.20.32.1`   | `10.20.32.100 – 200`        |
| **33**  | Studio       | Ultra-high-performance studio    | `grp-studio`          | SAN/NAS systems, media servers   | `10.20.33.0/24` | `10.20.33.1`   | Static only                 |
| **34**  | Studio       | Studio Wifi                      | `grp-studio`          | Creative team mobile devices     | `10.20.34.0/24` | `10.20.34.1`   | `10.20.34.100 – 200`        |
| **35**  | Studio       | Studio Monitoring                | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.35.0/24` | `10.20.35.1`   | `10.20.35.100 – 200`        |
| **41**  | Workshop     | Fabrication and prototyping      | `grp-workshop`        | Makers, engineers, technicians, CAD stations, equipment controllers | `10.20.41.0/24` | `10.20.41.1`   | `10.20.41.100 – 200`        |
| **42**  | Workshop     | Workshop Reserved                | `grp-workshop`        | Future workshop needs            | `10.20.42.0/24` | `10.20.42.1`   | Static only                 |
| **43**  | Workshop     | Workshop Reserved                | `grp-workshop`        | Future workshop needs            | `10.20.43.0/24` | `10.20.43.1`   | Static only                 |
| **44**  | Workshop     | Workshop Wifi                    | `grp-workshop`        | Tool-connected devices           | `10.20.44.0/24` | `10.20.44.1`   | `10.20.44.100 – 200`        |
| **45**  | Workshop     | Workshop Monitoring              | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.45.0/24` | `10.20.45.1`   | `10.20.45.100 – 200`        |
| **51**  | Management   | IT infrastructure and oversight  | `grp-management`      | IT manager, C-level staff, FreeIPA admin tools, audit logs, network monitoring | `10.20.51.0/24` | `10.20.51.1`   | Static only                 |
| **52**  | Management   | Management Reserved              | `grp-management`      | Future management needs          | `10.20.52.0/24` | `10.20.52.1`   | Static only                 |
| **53**  | Management   | Management Reserved              | `grp-management`      | Future management needs          | `10.20.53.0/24` | `10.20.53.1`   | Static only                 |
| **54**  | Management   | Management Wifi                  | `grp-management`      | Admin mobile devices             | `10.20.54.0/24` | `10.20.54.1`   | `10.20.54.100 – 200`        |
| **55**  | Management   | Management Monitoring            | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.55.0/24` | `10.20.55.1`   | `10.20.55.100 – 200`        |
| **61**  | Guest        | Visitor access                   | `grp-guest`           | Clients, freelancers, visitors, isolated VLAN, no internal resource access | `10.20.61.0/24` | `10.20.61.1`   | `10.20.61.100 – 200`        |
| **62**  | Guest        | Guest Reserved                   | `grp-guest`           | Future guest needs               | `10.20.62.0/24` | `10.20.62.1`   | Static only                 |
| **63**  | Guest        | Guest Reserved                   | `grp-guest`           | Future guest needs               | `10.20.63.0/24` | `10.20.63.1`   | Static only                 |
| **64**  | Guest        | Guest Wifi                       | `grp-guest`           | Visitor laptops, phones          | `10.20.64.0/24` | `10.20.64.1`   | `10.20.64.100 – 200`        |
| **65**  | Guest        | Guest Monitoring                 | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.65.0/24` | `10.20.65.1`   | `10.20.65.100 – 200`        |

---

## 🔐 Identity and Access Management

This section outlines the FreeIPA group structure and design. This design is intended to be modular, scalable, and intuitive, mirroring the physical and operational layout of the studio.

### Group Naming Convention

To ensure consistency and clarity, the following naming convention will be used for FreeIPA groups:

*   **`grp-<domain>`:** For primary, domain-specific groups (e.g., `grp-studio`).
*   **`role-<function>`:** For role-based groups that can be nested within domain groups (e.g., `role-creative`, `role-technical`).

### Core Domain Groups

This table defines the primary FreeIPA groups, aligned with the network's VLANs and operational domains.

| **Group Name**     | **Domain Purpose**                                                                 | **Typical Members**              | **Access Scope**                                                                 | **Nesting Suggestion** |
|:-------------------|:-----------------------------------------------------------------------------------|:---------------------------------|:---------------------------------------------------------------------------------|:-----------------------|
| `grp-production`   | Business-critical services: contracts, billing, client records                     | Producer, admin staff            | Finance systems, CRM, secure document storage                                   | `role-executive`       |
| `grp-stage`        | Physical photography stage: robotic rigs, lighting arrays, product movers          | Technical crew, automation staff | Control systems, IoT interfaces, robotics dashboards                            | `role-technical`       |
| `grp-studio`       | Digital photography processing: NAS storage, graphics workstations                 | Director, editors, retouchers    | File servers, editing suites, color grading tools                               | `role-creative`        |
| `grp-workshop`     | Fabrication and prototyping: metal/plastic/woodworking, 3D printers, heavy tools   | Makers, engineers, technicians   | CAD stations, equipment controllers, safety monitoring systems                  | `role-technical`       |
| `grp-management`   | IT infrastructure and executive oversight: auditing, system control                | IT manager, C-level staff         | FreeIPA admin tools, audit logs, network monitoring, privileged access systems  | `role-executive`       |
| `grp-guest`        | Visitor access: passwordless Wi-Fi, limited internet                               | Clients, freelancers, visitors   | Isolated VLAN, no internal resource access, captive portal if needed            | -                      |

### Role-Based Groups (Nested Groups)

Nested groups can be used to create a more granular and flexible access control model. For example, you could create the following role-based groups and nest them within the appropriate domain groups:

*   **`role-creative`:** For users who need access to creative tools and resources (e.g., editors, retouchers).
*   **`role-technical`:** For users who need access to technical systems and equipment (e.g., engineers, technicians).
*   **`role-executive`:** For users who need high-level access to business-critical systems and data (e.g., producers, C-level staff).

### Implementation Details

#### Host-Based Access Control (HBAC)

HBAC rules are used to control which users and groups can access which hosts and services. For example, you could create an HBAC rule that only allows members of the `grp-management` group to SSH into the Proxmox host.

**Example HBAC Rule:**

*   **Rule Name:** `allow_management_ssh_to_proxmox`
*   **Who:** `grp-management`
*   **Accessing:** `pmx-01.bjoin.studio`
*   **Via Service:** `sshd`

#### Sudo Rules

Sudo rules are used to grant elevated privileges to specific users and groups. For example, you could create a sudo rule that allows members of the `grp-management` group to run any command as root on any host.

**Example Sudo Rule:**

*   **Rule Name:** `allow_management_all_commands`
*   **Who:** `grp-management`
*   **Run Command:** `ALL`
*   **As User:** `root`

#### Automount

Automount can be used to automatically mount users' home directories from a central file server (e.g., the QNAP NAS) when they log in to a workstation. This provides a consistent user experience and simplifies home directory management.

---

## 🧱 Hardware Roles & Physical Connectivity

This section outlines the roles of key hardware and how they are physically connected.

### Hardware Roles
| Device                  | Role                                | Notes                                                              |
|:------------------------|:------------------------------------|:-------------------------------------------------------------------|
| Protectli Vault         | OPNsense Firewall/Router            | The single point of control for all inter-VLAN routing and security. |
| ISP Modem               | Internet Gateway                    | Provides the WAN connection.                                       |
| Sodola KT-NOS SL-SWTGW2C8F | Distribution Switch                 | The main switch connected to the firewall, distributes the VLAN trunk. |
| Cisco Nexus 9236C       | 100G Core Switch                    | The high-performance backbone for the Studio Ultra VLAN.           |
| BitEngine SW08XM        | Access Switch                       | Provides high-speed 10G RJ45 access for servers and workstations.  |
| Netgear GS108Ev4        | Access Switch                       | Provides 1G access for end devices.                                |
| Netgear GS105           | Unmanaged Access Switch             | For simple, single-VLAN device connections.                        |
| QNAP TS-h1290FX         | High-Performance NAS                | Provides high-speed storage access to multiple VLANs.              |
| Mac Pro 6,1             | Proxmox VE Hypervisor               | Hosts critical VMs like FreeIPA. Management in VLAN 51.            |

### Physical Connectivity
*   **ISP Modem** connects to **Protectli FW4B (WAN)** via a 3D CAT6e RJ45 cable.
*   **Protectli FW4B (LAN)** connects to **Sodola KT-NOS (Port 8)** via an RJ45 cable and an SFP+ to 1G RJ45 transceiver.
*   **Sodola KT-NOS (Ports 1-4 LAG)** connects to **Cisco Nexus 9236c (Port 1)** via a 40Gb to 100Gb trunk.
*   **Sodola KT-NOS (Port 5)** connects to **Mac Pro 6,1 (1GbE Port)** via an RJ45 cable (Access Port for VLAN 51).
*   **Sodola KT-NOS (Port 7)** connects to **Netgear GS108Ev4 (Port 8)** via an SFP+ transceiver and an RJ45 cable (Trunk Port).
*   **Netgear GS108Ev4 (Port 5)** connects to **Netgear GS105 (Port 5)** via an RJ45 cable (Access Port for VLAN 51).
*   **Cisco Nexus 9236c (Ports 3-4 LAG)** connects to **QNAP TS-h1290FX (Ports 1-2 LAG)**.

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

*   **A Note on Interfaces:** During the OPNsense installation, it is critical to correctly identify and assign the network interfaces. The `WAN` interface should be connected to your ISP modem, and the `LAN` interface should be connected to your internal network (the Sodola switch).

#### 🧰 Requirements
- Protectli Vault (or compatible x86 hardware)
- USB stick (at least 4GB)
- Monitor + keyboard (for initial setup)
- Internet access via ISP Modem

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
   - Assign interfaces correctly (WAN and LAN).

4. **Access Web GUI**
   - Connect a laptop to LAN port
   - Navigate to `https://192.168.1.1`
   - Default credentials: `admin / opnsense`
   - Change password immediately

### 🔹 6.2 Firewall Rule Best Practices

*   **Default Deny:** Start with a default deny rule on all interfaces. This ensures that only traffic that is explicitly allowed is permitted.
*   **Be Specific:** Create specific rules for the traffic you want to allow. Avoid using "any" for source, destination, or port whenever possible.
*   **Use Aliases:** Use aliases for IP addresses, ports, and networks. This makes rules easier to read and manage.
*   **Documentation:** Add clear and concise descriptions to every firewall rule to explain its purpose.
*   **Order Matters:** The firewall processes rules from top to bottom. The first rule that matches the traffic is applied. Place more specific rules before more general rules.

---

## 🚀 Next Steps

1.  **Configure Switches:** Configure the Sodola, Cisco, and Netgear switches with the appropriate VLANs, trunks, and access ports.
2.  **Configure OPNsense:** Perform the initial setup of OPNsense, including creating VLANs, configuring DHCP, and setting up firewall rules.
3.  **Deploy FreeIPA:** Set up the FreeIPA server on the Proxmox host.
4.  **Test Connectivity:** Thoroughly test connectivity between all VLANs and to the internet.