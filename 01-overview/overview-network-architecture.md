# Overview - Network Architecture (bjoin.studio)

## Table of Contents
1. [Introduction](#introduction)
2. [Core Networking Fabric](#core-networking-fabric)
3. [Ethernet Switch Capabilities](#ethernet-switch-capabilities)
4. [Identity, Policy and Auditing](#identity-policy-and-auditing)
5. [Appendix A: Configuration](#appendix-a-configuration)
6. [Appendix B: Troubleshooting](#appendix-b-troubleshooting)

## Introduction

This document provides a high level overview of the bjoin.studio intranet network architecture.

- **Core Networking Fabric**: [Ethernet](https://en.wikipedia.org/wiki/Ethernet)   
  (standardized, fast, reliable and scalable data transmission)

- **Identity, Policy and Auditing**: [FreeIPA](https://www.freeipa.org/)  
  (identity authentication, policy, and auditing)

- **Access Control, Routing and Perimeter Defense**: [OPNsense](https://www.opnsense.org)  
  (packet inspection and traffic management)

- **Security Layering**: [VLANs](https://en.wikipedia.org/wiki/VLAN)  
  (logical segmentation and network zone isolation)

   [Back to Table of Contents](#table-of-contents)

---

## Core Networking Fabric

The bjoin.studio fabric is comprised of Ethernet switches of varying speed and port density.

- **100 Gb Ethernet**:
   - **Core Switch:** [MikroTik CRS520-4XS-16XQ-RM](https://mikrotik.com/product/crs520_4xs_16xq_rm)  
   Layer 2 / Layer 3 Managed Ethernet Switch

   - **Core Switch:** [MikroTik CRS504-4XQ-IN](https://mikrotik.com/product/crs504_4xq_in)  
   Layer 2 / Layer 3 Managed Ethernet Switch

   - **Core Switch:** [Cisco NEXUS 9236c](https://www.cisco.com/c/en/us/products/switches/nexus-9236c-switch/index.html)  
   Layer 2 / Layer 3 Managed Ethernet Switch

- **10 Gb Ethernet**:
   - **Access Switch:** [Sodola KT-NOS SL-SWTGW2C8F](https://sodola-network.com/products/10g-sfp-switch-8-port-10g-sfp-unmanaged-switch-10g-ethernet-switch-with-2-port-10g-rj45-10g-fiber-switch-plug-play-fanless-metal-vlan-qos)  
   Layer 2 Managed Ethernet Switch

   - **Access Switch:** Bitengine SW08XM  
   Layer 2 Managed Ethernet Switch - 8x 10Gb

- **1Gb Ethernet**:

   - **Distribution Switch:** [TP-Link SG3428X](https://www.tp-link.com/us/business-networking/omada-sdn-switch/sg3428x/)  
   Layer 2 Managed Ethernet Switch

   - **Access Switch:** [Netgear GS108Ev4](https://www.netgear.com/business/wired/switches/plus/gs108e/)  
   Layer 2 Managed Ethernet Switch

   - **Unmanaged Switch:** [Netgear GS105](https://www.netgear.com/home/wired/switches/unmanaged/gs105/)  
   Unmanaged Ethernet Switch

   [Back to Table of Contents](#table-of-contents)

---
## Ethernet Switch Capabilities

- **Summary**

   | Switch Type              | Configurable | VLAN Support | Routing | Use Case                      |
   |--------------------------|--------------|--------------|---------|-------------------------------|
   | Layer 2/3 Managed        | ✅ Yes       | ✅ Yes       | ✅ Yes  | Enterprise-grade networks     |
   | Layer 2 Managed          | ✅ Yes       | ✅ Yes       | ❌ No   | Segmented LANs                |
   | Unmanaged                | ❌ No        | ❌ No        | ❌ No   | Small plug-and-play setups    |

---

- **Layer 2 / Layer 3 Managed Switch**
   - Combines Layer 2 switching **plus** Layer 3 routing.
   - Can route traffic between **different subnets or VLANs** using **IP addresses**.
   - Supports **inter-VLAN routing**, **ACLs**, **static/dynamic routing**, and more.
   - Ideal for **larger, complex networks** needing both switching and routing.

---

- **Layer 2 Managed Switch**
   - Operates at **Layer 2 (Data Link Layer)** of the OSI model.
   - Uses **MAC addresses** to forward Ethernet frames.
   - Supports **VLANs**, **port mirroring**, **QoS**, and **basic security**.
   - Great for **LAN segmentation** and **traffic control** within a single network.

---

- **Unmanaged Switch**
   - **Plug-and-play**: No configuration needed.
   - **Basic connectivity**: Just forwards traffic between devices.
   - **No control**: No VLANs, no security settings, no monitoring.
   - Best for **small, simple networks**.

   [Back to Table of Contents](#table-of-contents)

---

## Identity, Policy and Auditing

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

   [Back to Table of Contents](#table-of-contents)

---

---


## Definitive VLAN and IP Plan

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







- **100 Gb Ethernet**:
   - **Core Switch:** [MikroTik CRS520-4XS-16XQ-RM](https://mikrotik.com/product/crs520_4xs_16xq_rm)  
   Layer 2 / Layer 3 Managed Ethernet Switch - 16x 100Gb, 4x 25Gb, 2x 1Gb  
      - [Manual](https://help.mikrotik.com/docs/display/UM/CRS520-4XS-16XQ-RM)

   - **Core Switch:** [MikroTik CRS504-4XQ-IN](https://mikrotik.com/product/crs504_4xq_in)  
   Layer 2 / Layer 3 Managed Ethernet Switch - 4x 100Gb, 1x 1Gb
      - [Manual](https://help.mikrotik.com/docs/display/UM/CRS504-4XQ-IN)

   - **Core Switch:** [Cisco NEXUS 9236c](https://www.cisco.com/c/en/us/products/switches/nexus-9236c-switch/index.html)  
   Layer 2 / Layer 3 Managed Ethernet Switch - 36x 100Gb, 4x 1Gb
      - [Data Sheet](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-735989.html)

- **10 Gb Ethernet**:
   - **Access Switch:** [Sodola KT-NOS SL-SWTGW2C8F](https://sodola-network.com/products/10g-sfp-switch-8-port-10g-sfp-unmanaged-switch-10g-ethernet-switch-with-2-port-10g-rj45-10g-fiber-switch-plug-play-fanless-metal-vlan-qos)  
   Layer 2 Managed Ethernet Switch - 8x 10Gb
      - [Manual](https://sodola-network.com/pages/download)

   - **Access Switch:** Bitengine SW08XM  
   Layer 2 Managed Ethernet Switch - 8x 10Gb

- **1Gb Ethernet**:

   - **Distribution Switch:** [TP-Link SG3428X](https://www.tp-link.com/us/business-networking/omada-sdn-switch/sg3428x/)  
   Layer 2 Managed Ethernet Switch - 24x 1Gb, 4x 10Gb
      - [Data Sheet](https://static.tp-link.com/upload/product-overview/2021/202103/20210311/JetStream%20L2+%20Managed%20Switches%20Datasheet.pdf)
   - **Access Switch:** [Netgear GS108Ev4](https://www.netgear.com/business/wired/switches/plus/gs108e/)  
   Layer 2 Managed Ethernet Switch - 8x 1Gb
      - [Data Sheet](https://www.netgear.com/media/GS108Ev3_tcm148-69377.pdf)
   - **Unmanaged Switch:** [Netgear GS105](https://www.netgear.com/home/wired/switches/unmanaged/gs105/)  
   Unanaged Ethernet Switch - 5x 1Gb
      - [Data Sheet](https://www.netgear.com/media/GS105_108_116_DS_tcm148-69371.pdf)
