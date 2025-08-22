# Logical Network Diagram

This document describes the logical topology of the bjoin.studio network, including VLANs, IP subnets, routing paths, and traffic flow policies.

## High-Level Topology

The network is segmented into multiple VLANs, all of which are routed through the central OPNsense firewall and the Cisco Nexus core switch in a hybrid routing model.

```
                               +--------------------+ +--------------------+
                               |      Internet      | |   Proxmox Host     |
                               +---------+----------+ | (pmx-01.bjoin.studio)|
                                         |            +---------+----------+
                                         | WAN                  | Management (VLAN 51)
                               +---------+----------+            |
                               |  OPNsense Firewall |            |
                               | (Protectli FW4B)   |            |
                               | Gateway: 10.20.x.1 +------------+
                               +---------+----------+
                                         | LAN (VLAN Trunk)
                                         |
+----------------------------------------+---------------------------------------+
|                                                                               |
|                                  Core Switching                               |
|                      (Sodola, Cisco - L2/L3, BitEngine)                         |
|                                                                               |
+--+-------------+--------------+----------------+---------------+-------------+--+
   |             |              |                |               |             |
   | VLAN 1x     | VLAN 2x      | VLAN 3x        | VLAN 4x       | VLAN 5x/6x  |
   | Production  | Stage        | Studio         | Workshop      | Mgmt/Guest  |
   +-------------+--------------+----------------+---------------+-------------+

```

---

## VLAN Routing and Purpose

By default, all inter-VLAN traffic is **blocked** by the firewall. Rules must be explicitly created to allow traffic to flow between VLANs. The Cisco Nexus switch handles high-speed routing between trusted VLANs.

### Production VLANs (11, 12, 14)
*   **Purpose:** For general office work, administrative tasks, and high-performance rendering.
*   **Routing:** Has filtered access to the internet. Blocked from initiating traffic to the Studio, Stage, or Workshop VLANs to protect those environments.

### Stage VLANs (21, 22, 24)
*   **Purpose:** For devices used during production shoots, such as cameras, lighting, and control systems.
*   **Routing:** Has very limited, filtered internet access. Can send data *to* the Studio VLANs (e.g., for media ingest) but cannot initiate connections to other zones.

### Studio VLANs (31, 32, 33, 34)
*   **Purpose:** The core creative environment for editing, color grading, and VFX.
*   **Routing:** Has limited, filtered internet access. The high-performance VLANs (32, 33) have broad visibility to other zones to pull media, but the general workstation VLAN (31) is more restricted.

### Workshop VLANs (41, 44)
*   **Purpose:** For engineering, prototyping, and fabrication.
*   **Routing:** This zone is **isolated** and has **no internet access**. It cannot initiate connections to any other VLANs.

### Management VLANs (51, 52, 53)
*   **Purpose:** For secure access to network hardware and monitoring.
*   **Routing:** This is a highly privileged zone. Access *to* this VLAN is heavily restricted by firewall rules, only allowing connections from designated admin workstations.

### Guest VLAN (61)
*   **Purpose:** For providing internet access to visitors.
*   **Routing:** This zone is completely isolated from all internal VLANs. It can only access the internet.