# Network VLAN Design

This document details the Virtual Local Area Network (VLAN) design for the bjoin.studio network, outlining its purpose, standards, and the definitive VLAN and IP addressing plan.

## 1. Introduction to VLANs

VLANs are a fundamental component of the bjoin.studio network architecture, providing logical segmentation of the network. This segmentation enhances security, improves performance by reducing broadcast domains, and simplifies network management. By isolating different types of traffic and user groups into distinct VLANs, we can apply granular security policies and optimize resource allocation.

## 2. VLAN Tagging Standard: 802.1Q

For all VLAN configurations within this network, the **802.1Q** standard is used.

*   **802.1Q** is the universal standard for creating VLANs on an internal network. It functions by adding a small tag to Ethernet frames, indicating which VLAN the frame belongs to. This allows a single physical network infrastructure (switches, cables) to carry traffic for multiple logical networks. All network equipment (switches, firewalls, servers) in the bjoin.studio network is configured to utilize this standard.

*   **802.1ad (QinQ)**, a specialized standard for service providers, is not used in this internal network design.

## 3. Definitive VLAN, IP, and Group Plan

This table serves as the single source of truth for VLAN IDs, their associated network zones, purposes, IP addressing schemes, and corresponding FreeIPA groups.

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

## 4. Demilitarized Zone (DMZ) Concept

A DMZ is a small, isolated network segment that sits between the internet and your trusted internal LAN. It acts as a buffer zone for services that need to be accessible from the internet (e.g., public web servers).

*   **Security Principle:** The DMZ is separated from the internal LAN by firewall rules that strictly control traffic flow. The internet can access the DMZ, but the internet cannot directly access the internal LAN, and crucially, the DMZ cannot directly initiate connections to the internal LAN. This design ensures that if a service in the DMZ is compromised, the attacker is contained within the DMZ and cannot easily access sensitive internal resources.

## 5. VLANs and Identity Management (FreeIPA)

VLAN segmentation works hand-in-hand with FreeIPA to provide robust access control and seamless cross-VLAN access for users.

*   **VLANs for Isolation:** VLANs provide the fundamental layer of network security by isolating different network segments.
*   **FreeIPA for Centralized Control:** FreeIPA acts as the central authority for authentication and authorization across all these isolated VLANs, providing a single identity for users and machines.
*   **Firewall for Mediation:** The OPNsense firewall mediates controlled communication between VLANs, enforcing rules that allow specific traffic (e.g., FreeIPA authentication requests) to pass between segments.

## 6. VLAN Routing and Purpose

By default, all inter-VLAN traffic is **blocked** by the firewall. Rules must be explicitly created to allow traffic to flow between VLANs. The MikroTik CRS520-4XS-16XQ-RM handles high-speed routing between trusted VLANs.

### Production VLANs (11-15)
*   **Purpose:** For business-critical services, such as contracts, billing, and client records, as well as high-performance rendering.
*   **Routing:** Routed by OPNsense. Has filtered access to the internet. Blocked from initiating traffic to the Studio, Stage, or Workshop VLANs to protect those environments.

### Stage VLANs (21-25)
*   **Purpose:** For devices used during production shoots, such as cameras, lighting, and control systems.
*   **Routing:** Routed by OPNsense. Has very limited, filtered internet access. Can send data *to* the Studio VLANs (e.g., for media ingest) but cannot initiate connections to other zones.

### Studio VLANs (31-35)
*   **Purpose:** The core creative environment for editing, color grading, and VFX.
*   **Routing:** Routed by the MikroTik CRS520-4XS-16XQ-RM for high-speed performance. Has limited, filtered internet access via OPNsense.

### Workshop VLANs (41-45)
*   **Purpose:** For engineering, prototyping, and fabrication.
*   **Routing:** Routed by OPNsense. This zone is **isolated** and has **no internet access**. It cannot initiate connections to any other VLANs.

### Management VLANs (51-55)
*   **Purpose:** For secure access to network hardware and monitoring.
*   **Routing:** Routed by OPNsense. This is a highly privileged zone. Access *to* this VLAN is heavily restricted by firewall rules, only allowing connections from designated admin workstations.

### Guest VLANs (61-65)
*   **Purpose:** For providing internet access to visitors.
*   **Routing:** Routed by OPNsense. This zone is completely isolated from all internal VLANs. It can only access the internet.