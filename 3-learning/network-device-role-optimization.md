# Network Device Role Optimization and Hybrid Routing Strategy

This document outlines the strategic roles of key network devices within the bjoin.studio network, focusing on how their unique capabilities are leveraged to achieve both performance and security goals. It details a hybrid routing approach that optimizes traffic flow while maintaining necessary security controls.

## 1. Key Takeaways

*   **We use three main types of devices:** A secure firewall, a high-speed core switch, and a flexible distribution switch.
*   **The firewall inspects all traffic** going to the internet and between most internal network zones.
*   **The high-speed core switch handles traffic** between our performance-critical zones to make it faster.
*   **The distribution switch acts as the central hub**, connecting the firewall, the core switch, and our access switches.
*   **This 'hybrid' approach gives us both security and performance.**

---

## 2. OPNsense (Protectli Vault) Role: The Secure Gateway

The OPNsense firewall, running on the Protectli Vault, serves as the primary security enforcement point and the gateway to the Internet. It operates primarily in a "Router-on-a-Stick" configuration for most inter-VLAN traffic.

*   **What is "Router-on-a-Stick"?** This is a method of routing traffic between VLANs by sending it up a single physical link (the "stick") to a router or firewall. The firewall then inspects the traffic and routes it back down the same link to the destination VLAN. This centralizes security and control.

*   **Primary Functions:**
    *   **Internet Gateway:** All traffic to and from the Internet passes through OPNsense for NAT, firewalling, and security inspection.
    *   **Centralized Security Policy:** OPNsense is the single point of control for all firewall rules, Intrusion Detection/Prevention (IDS/IPS), and traffic shaping.
    *   **Inter-VLAN Routing (Default):** OPNsense handles routing between most VLANs. This ensures that all inter-VLAN traffic is inspected by the firewall.
    *   **DHCP and DNS:** Provides DHCP services for various VLANs and acts as the primary DNS resolver (forwarding to FreeIPA for internal domains).
    *   **VPN Termination:** Handles remote access and site-to-site VPN connections.

*   **Performance Consideration:** The 1Gbps LAN port on the Protectli Vault can become a bottleneck for high-bandwidth inter-VLAN traffic if all routing is performed by OPNsense. This is where the Cisco Nexus 9236C plays a complementary role.

---

## 3. Sodola KT-NOS SL-SWTGW2C8F Role: The Distribution Hub

The Sodola 10Gb switch is the central distribution hub of the network. It connects the firewall to the core switch and the access switches, and provides high-speed 10GbE access for key devices.

*   **Primary Functions:**
    *   **Firewall Uplink:** Connects to the OPNsense firewall and receives the main VLAN trunk.
    *   **Core Switch Uplink:** Connects to the Cisco Nexus 9236c core switch, providing a high-speed path for traffic to and from the core.
    *   **Access Switch Uplink:** Connects to the Netgear GS108Ev4 access switch, extending the VLANs to the edge of the network.
    *   **10GbE Access:** Provides 10GbE access for key servers and devices, such as the Proxmox host.

---

## 4. Cisco Nexus 9236C Role: The High-Speed Inter-VLAN Router

The Cisco Nexus 9236C is a powerful Layer 3 switch designed for high-performance data center and campus environments. It is leveraged to offload high-bandwidth inter-VLAN routing from the OPNsense firewall.

*   **Primary Functions:**
    *   **High-Speed Layer 2 Switching:** Provides wire-speed switching within VLANs.
    *   **High-Speed Layer 3 Switching (Inter-VLAN Routing):** For designated trusted, high-bandwidth VLANs, the Nexus switch acts as the default gateway and performs routing directly between these VLANs using Switched Virtual Interfaces (SVIs). This traffic stays on the switch's high-speed backplane.
    *   **Core Network Connectivity:** Serves as a central distribution point for high-speed servers and storage.

---

## 5. The Hybrid Routing Approach

The bjoin.studio network employs a hybrid routing strategy to balance security and performance.

### Routing Policy Table

| VLAN Zone      | Routed By           | Notes                                                                 |
|:---------------|:--------------------|:----------------------------------------------------------------------|
| Internet Bound | OPNsense Firewall   | All traffic to and from the internet is inspected by the firewall.      |
| Guest (6x)     | OPNsense Firewall   | Isolated from all internal networks and routed directly to the internet.|
| Management (5x)| OPNsense Firewall   | Strictly controlled access to critical infrastructure.                 |
| Workshop (4x)  | OPNsense Firewall   | Isolated from other internal networks.                                |
| Production (1x)| OPNsense Firewall   | General purpose workstations and servers.                             |
| Stage (2x)     | OPNsense Firewall   | Production equipment with limited access to other zones.              |
| Studio (3x)    | Cisco Nexus 9236c   | High-speed routing for performance-critical media and rendering traffic.|

### Hybrid Routing Data Flow Diagram

```
+---------------------------+
|   Internet                |
+-------------+-------------+
              |
+-------------+-------------+
| OPNsense Firewall (Router-on-a-Stick) |
+-------------+-------------+
              | (Trunk Link)
+-------------+-------------+
| Sodola KT-NOS (L2 Switch)   |
+-------------+-------------+
              | (Trunk Link)
+-------------+-------------+
| Cisco Nexus 9236C (L3 Switch) |
+--+----------+----------+--+
   |          |          |
   | (VLAN 32)|          | (VLAN 61)
   |          |          |
+--+-----+  +--+-----+  +--+-----+
| VFX WS |  | SAN    |  | Guest  |
+--------+  +--------+  +--------+
 (VLAN 32)  (VLAN 33)  (VLAN 61)

```

*   **Scenario 1 (Performance Routing):** `VFX WS` in VLAN 32 sends a large file to the `SAN` in VLAN 33. The traffic is routed directly by the **Cisco Nexus 9236C** at high speed.
*   **Scenario 2 (Security Routing):** `Guest` device in VLAN 61 tries to access the internet. The traffic goes up the trunk to the **Cisco Nexus 9236C**, which then forwards it to the **Sodola switch**, and then to the **OPNsense Firewall**. The firewall inspects the traffic and sends it to the internet.

### Security Considerations of the Hybrid Approach

It is critical to understand the security implications of Layer 3 switching on the Nexus:

*   **Firewall Bypass:** Traffic routed directly by the Cisco Nexus 9236C **does NOT pass through the OPNsense firewall**. This means any firewall rules, IDS/IPS, or traffic shaping configured on OPNsense for those specific inter-VLAN flows will be bypassed.
*   **Policy Enforcement:** Security policies for traffic routed by the Nexus must be enforced at the source/destination hosts (e.g., host-based firewalls) or by carefully designed Access Control Lists (ACLs) on the Nexus itself. For example, you can use VLAN ACLs (VACLs) to filter traffic between the high-speed VLANs.
*   **Trust Zones:** This hybrid model relies on clearly defined trust zones. High-trust, high-bandwidth zones can leverage the Nexus for speed, while lower-trust or internet-facing zones rely on OPNsense for deep inspection.

---

## 6. Other Devices in the Optimized Design

*   **BitEngine SW08XM:** Functions as an access layer switch, providing 1GbE access for end devices.
*   **Netgear GS108Ev4:** Functions as an access layer switch, providing port-level VLAN assignment for end devices. Its configuration is manual via web GUI.
*   **Netgear GS105:** An unmanaged access switch for simple, single-VLAN device connections.
*   **QNAP TS-h1290FX:** A high-performance NAS connected to the core switch via a 100GbE LAG, providing high-speed storage access to multiple VLANs.
*   **Proxmox VE Host (`pmx-01`):** Hosts critical VMs like FreeIPA. It is connected to the network via a dedicated access port on the distribution switch for management, and can have other network interfaces for VM traffic.

---

## 7. Design Decisions and Alternatives

### Why not connect the firewall directly to the Cisco Nexus switch?

Connecting the 1GbE firewall directly to a 100GbE port on the Cisco Nexus switch was considered, but this approach was not chosen for the following reasons:

*   **Wasted Port:** It would be a significant waste of a high-value 100GbE port on the core switch.
*   **Adapter Complexity:** It would require chaining multiple adapters (QSFP28 to SFP+, then SFP+ to RJ45), which can be unreliable.
*   **Purpose-Built Roles:** The current design allows each device to perform its intended role: the Sodola switch acts as a flexible distribution hub, and the Cisco Nexus switch focuses on high-speed core switching and routing.

---

## 8. Long-Term Improvements

As the network evolves, the following improvements could be considered:

*   **Dedicated 10Gb/25Gb/40Gb/100Gb Firewall:** Upgrading the OPNsense hardware to support higher-speed interfaces would eliminate the 1Gb bottleneck entirely, allowing all inter-VLAN traffic to be inspected by the firewall at higher speeds. This would simplify the routing design by potentially moving all inter-VLAN routing back to the firewall.
*   **Ansible Automation:** Develop comprehensive Ansible playbooks for the Cisco Nexus 9236C and other managed switches to automate configuration and ensure consistency.
*   **Network Access Control (NAC):** Implement a NAC solution like PacketFence or Cisco ISE to enhance security by authenticating and authorizing devices as they connect to the network.
*   **Network Monitoring Integration:** Implement robust monitoring solutions (e.g., Prometheus, Grafana, ELK stack) to gain deep insights into traffic patterns, device health, and security events across all VLANs.
*   **Centralized Log Management:** Consolidate logs from all network devices, servers, and security appliances into a central log management system for easier troubleshooting and security auditing.
*   **Redundancy and High Availability:** Implement redundant links, devices, and power supplies for critical network components to ensure continuous operation.