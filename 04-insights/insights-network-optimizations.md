# Network Architecture: A Consolidated High-Performance Model

This document outlines the current, optimized network architecture for bjoin.studio. The design has been consolidated to centralize routing and switching functions on a high-performance core device, simplifying management and maximizing throughput.

## 1. Core Principle: Centralized Layer 2 and Layer 3

The network now operates on a centralized model where a single device, the **MikroTik CRS520-4XS-16XQ-RM**, handles all primary Layer 2 (switching) and Layer 3 (routing) responsibilities.

*   **What this means:** All VLANs are defined on the MikroTik, and all inter-VLAN routing is performed directly on its high-speed backplane. This eliminates previous bottlenecks and simplifies traffic flow. The Sodola switch is no longer a distribution hub and now functions as a simple access-layer switch.

## 2. The Firewall: A Dedicated Security Gateway

With the MikroTik handling all internal routing, the role of the firewall has become more specialized and secure.

*   **Device:** A virtualized OPNsense instance (`opnsense-vm`) running on the **HP Z620 workstation**. This VM is equipped with a 10Gbps network interface.
*   **Primary Role:** It acts as a dedicated **Security Gateway** for all North-South traffic (traffic going to and from the internet).
*   **Configuration:** It is configured as a "firewall-on-a-stick." All internet-bound traffic from the MikroTik is directed to the OPNsense VM for stateful inspection, NAT, and security policy enforcement before being sent to the WAN.
*   **Decommissioned Hardware:** The Protectli Vault appliance is no longer the primary firewall in this design.

## 3. Traffic Flow Examples

### Internal Traffic (East-West)

*   **Scenario:** A workstation in the `Production` VLAN (VLAN 10) needs to access a file server in the `Studio` VLAN (VLAN 30).
*   **Data Path:**
    1.  Traffic leaves the workstation and hits the MikroTik switch.
    2.  The MikroTik, as the gateway for both VLANs, routes the traffic internally from VLAN 10 to VLAN 30 at wire speed.
    3.  The traffic is forwarded to the file server.
*   **Key Insight:** The OPNsense firewall is **not** involved in this communication path, ensuring maximum performance for internal data transfers.

### External Traffic (North-South)

*   **Scenario:** A user on a `Production` VLAN workstation browses a public website.
*   **Data Path:**
    1.  Traffic leaves the workstation and hits the MikroTik switch.
    2.  The MikroTik's routing table directs the internet-bound traffic to the OPNsense VM's IP address as the next hop.
    3.  The OPNsense firewall inspects the packet, applies security rules, performs NAT (Network Address Translation), and forwards it out through its WAN interface to the internet.
*   **Key Insight:** All external traffic is forced through the firewall, providing a robust security perimeter.

## 4. Benefits of the New Architecture

*   **Simplified Management:** All L2 and L3 configuration is centralized on a single device (MikroTik), reducing complexity.
*   **Maximized Performance:** Internal traffic is routed at the full speed of the core switch, removing the firewall as a bottleneck.
*   **Enhanced Security:** The firewall is now a dedicated security gateway, focused exclusively on protecting the network perimeter without the burden of internal routing.
*   **Scalability:** The powerful MikroTik core provides ample capacity for future growth in terms of both ports and routing performance.