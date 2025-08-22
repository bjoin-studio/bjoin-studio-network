# Logical Network Diagram

This document describes the logical topology of the bjoin.studio network, including VLANs, IP subnets, routing paths, and traffic flow policies.

## High-Level Topology

The network is segmented into multiple VLANs, all of which are routed through the central OPNsense firewall and the Cisco Nexus core switch in a hybrid routing model.

```
                               +--------------------+
                               |      Internet      |
                               +---------+----------+
                                         |
                                         | WAN
                               +---------+----------+
                               |  OPNsense Firewall |
                               | (Secure Gateway)   |
                               +---------+----------+
                                         | LAN (VLAN Trunk)
                               +---------+----------+
                               | Sodola Switch      |
                               | (Distribution Hub) |
                               +---------+----------+
                                         |
+----------------------------------------+---------------------------------------+
|                                        |                                       |
|      Cisco Nexus Switch                |      Access Switches (BitEngine, Netgear) |
|      (L3 Core)                         |      (L2 Access)                      |
|                                        |                                       |
+--+-------------+--------------+--------+--------+---------------+-------------+--+
   |             |              |                 |               |             |
   | VLAN 3x     | VLAN 1x/2x   | VLAN 4x         | VLAN 5x       | VLAN 6x     |
   | (Studio)    | (Prod/Stage) | (Workshop)      | (Management)  | (Guest)     |
   +-------------+--------------+-----------------+---------------+-------------+

```

---

## VLAN Routing and Purpose

By default, all inter-VLAN traffic is **blocked** by the firewall. Rules must be explicitly created to allow traffic to flow between VLANs. The Cisco Nexus switch handles high-speed routing between trusted VLANs.

### Production VLANs (11-15)
*   **Purpose:** For business-critical services, such as contracts, billing, and client records, as well as high-performance rendering.
*   **Routing:** Routed by OPNsense. Has filtered access to the internet. Blocked from initiating traffic to the Studio, Stage, or Workshop VLANs to protect those environments.

### Stage VLANs (21-25)
*   **Purpose:** For devices used during production shoots, such as cameras, lighting, and control systems.
*   **Routing:** Routed by OPNsense. Has very limited, filtered internet access. Can send data *to* the Studio VLANs (e.g., for media ingest) but cannot initiate connections to other zones.

### Studio VLANs (31-35)
*   **Purpose:** The core creative environment for editing, color grading, and VFX.
*   **Routing:** Routed by the Cisco Nexus switch for high-speed performance. Has limited, filtered internet access via OPNsense.

### Workshop VLANs (41-45)
*   **Purpose:** For engineering, prototyping, and fabrication.
*   **Routing:** Routed by OPNsense. This zone is **isolated** and has **no internet access**. It cannot initiate connections to any other VLANs.

### Management VLANs (51-55)
*   **Purpose:** For secure access to network hardware and monitoring.
*   **Routing:** Routed by OPNsense. This is a highly privileged zone. Access *to* this VLAN is heavily restricted by firewall rules, only allowing connections from designated admin workstations.

### Guest VLANs (61-65)
*   **Purpose:** For providing internet access to visitors.
*   **Routing:** Routed by OPNsense. This zone is completely isolated from all internal VLANs. It can only access the internet.

---

## Link Aggregation Groups (LAGs)

LAGs are used to bundle multiple physical links into a single logical link. This provides increased bandwidth and redundancy.

*   **Sodola to Cisco:** A 4-port LAG connects the Sodola distribution switch to the Cisco core switch, providing a 40Gbps connection.
*   **Cisco to QNAP:** A 2-port LAG connects the Cisco core switch to the QNAP NAS, providing a 200Gbps connection.