# Network Routing Design

This document outlines the routing design for the bjoin.studio network, detailing the roles of key devices in facilitating traffic flow within and outside the network.

## 1. Introduction to Network Routing

Network routing is critical for enabling communication between different network segments (VLANs) and between the internal network and the internet. The bjoin.studio network employs a consolidated routing model designed for high performance, simplified management, and robust security.

## 2. Centralized Layer 2 and Layer 3 Routing

The core of the bjoin.studio network's routing infrastructure is the **MikroTik CRS520-4XS-16XQ-RM**. This powerful Layer 2/Layer 3 managed switch handles all primary switching and routing responsibilities for the internal network.

*   **Consolidated Control:** All VLANs are defined on the MikroTik, and all inter-VLAN routing is performed directly on its high-speed backplane. This approach eliminates previous bottlenecks and simplifies traffic flow by centralizing Layer 3 control.
*   **Default Gateway:** The MikroTik CRS520-4XS-16XQ-RM serves as the default gateway for each VLAN. Devices within each VLAN are configured to point to the MikroTik's VLAN interface IP address as their gateway.

## 3. Inter-VLAN Routing (East-West Traffic)

Internal traffic between different VLANs (East-West traffic) is routed directly by the MikroTik CRS520-4XS-16XQ-RM.

*   **High-Speed Performance:** When a device in one VLAN needs to communicate with a device in another VLAN, the traffic is routed at wire speed by the MikroTik. This ensures maximum performance for internal data transfers, as the perimeter firewall (OPNsense) is not involved in this path.
*   **Example:** A workstation in the `Production` VLAN (VLAN 10) accessing a file server in the `Studio` VLAN (VLAN 30) will have its traffic routed directly by the MikroTik switch.

## 4. Firewall's Role in Routing (North-South Traffic)

While the MikroTik handles internal routing, the virtualized OPNsense instance (`opnsense-vm`) on the HP Z620 workstation serves as the dedicated security gateway for all external (North-South) traffic.

*   **Perimeter Security:** All traffic destined for the internet, or originating from the internet and destined for the internal network, is directed to the OPNsense VM.
*   **Firewall-on-a-Stick Configuration:** The OPNsense VM is configured as a "firewall-on-a-stick." The MikroTik's routing table directs all internet-bound traffic to the OPNsense VM's IP address as the next hop.
*   **Security Policy Enforcement:** OPNsense performs stateful inspection, Network Address Translation (NAT), and applies security policies before forwarding traffic to the WAN.
*   **Example:** A user on a `Production` VLAN workstation browsing a public website will have their traffic routed by the MikroTik to the OPNsense VM, which then processes and forwards it to the internet.

## 5. Routing Protocols

*   **Static Routes:** For simpler network configurations, static routes can be implemented to define specific network paths.
*   **Dynamic Routing:** For more complex or larger environments, dynamic routing protocols (e.g., OSPF - Open Shortest Path First) can be considered to automatically exchange routing information between network devices, improving fault tolerance and scalability.

## 6. Traffic Flow Scenarios

This section illustrates common data flow paths within the bjoin.studio network, demonstrating the routing principles in action.

### Scenario 1: High-Speed Storage Access (Intra-VLAN or MikroTik Routed)

This scenario shows a workstation accessing the QNAP NAS. If both devices are in the same VLAN, traffic is switched at Layer 2. If they are in different VLANs routed by the MikroTik, traffic is routed at Layer 3 by the MikroTik.

*   **Data Path:** Traffic flows directly from the workstation to the MikroTik CRS520-4XS-16XQ-RM, which handles high-speed Layer 2 switching or Layer 3 routing, and then sends the traffic directly to the NAS. The OPNsense firewall is not involved in this data path.

### Scenario 2: Internet Access from a Workstation

This scenario shows a user on a workstation accessing the internet.

*   **Data Path:** Traffic flows from the workstation to its access switch (e.g., Netgear GS108Ev4), then to the MikroTik CRS520-4XS-16XQ-RM. The MikroTik routes the internet-bound traffic to the OPNsense VM. The OPNsense firewall then performs NAT and sends the traffic to the internet.

### Scenario 3: Proxmox Host Management

This scenario shows an administrator accessing the Proxmox host's web interface.

*   **Data Path:** The administrator's traffic goes from their workstation to its access switch, then to the MikroTik CRS520-4XS-16XQ-RM. The MikroTik routes the traffic from the admin's VLAN to the Management VLAN (VLAN 51) where the Proxmox host resides. The OPNsense firewall is not involved in this internal management traffic unless specific firewall rules are configured on the MikroTik to direct it there.

## 7. High-Level Topology

The bjoin.studio network is segmented into multiple VLANs, all of which are routed through the central MikroTik CRS520-4XS-16XQ-RM core switch. The OPNsense firewall acts as the secure gateway for internet traffic.

*   **Collapsed Core Design:** The network utilizes a collapsed core design, where the MikroTik CRS520-4XS-16XQ-RM serves as both the core and distribution layer.
*   **VLAN Segmentation:** Traffic is logically separated into distinct VLANs for different purposes (e.g., Production, Stage, Studio, Workshop, Management, Guest).
*   **Traffic Flow Policies:** By default, all inter-VLAN traffic is blocked by the firewall. Rules must be explicitly created to allow traffic to flow between VLANs.

## 8. Inter-VLAN Routing and Purpose

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