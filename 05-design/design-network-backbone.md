# Network Backbone Design

This document outlines the design and role of the core network backbone for bjoin.studio, focusing on its high-speed fabric and Layer 2/Layer 3 capabilities.

## 1. Core Network Fabric

The bjoin.studio network backbone is built upon high-speed Ethernet switches, primarily utilizing 100 Gigabit Ethernet for its core. This fabric is designed for standardized, fast, reliable, and scalable data transmission across the entire network.

### Key Backbone Devices:

*   **Core Switch (Primary):** MikroTik CRS520-4XS-16XQ-RM (Layer 2 / Layer 3 Managed Ethernet Switch)
    *   This switch serves as the network's primary core switch, providing high-speed inter-VLAN routing and aggregation for all network traffic. It handles all Layer 2 switching and Layer 3 routing functions for the internal network.

*   **Core Switches (Secondary/Redundant/Specialized):**
    *   MikroTik CRS504-4XQ-IN (Layer 2 / Layer 3 Managed Ethernet Switch)
    *   Cisco NEXUS 9236c (Layer 2 / Layer 3 Managed Ethernet Switch)
    *   These devices provide additional 100GbE capacity and can serve as secondary core switches, specialized routing platforms, or for specific high-bandwidth applications.

## 2. Backbone Capabilities: Layer 2 and Layer 3 Routing

The core backbone switches are Layer 2/Layer 3 managed devices, meaning they combine both switching and routing functionalities.

*   **Layer 2 Switching:** Uses MAC addresses to forward Ethernet frames within the same VLAN at high speeds.
*   **Layer 3 Routing:** Utilizes IP addresses to route traffic between different subnets or VLANs. The core switch supports inter-VLAN routing, Access Control Lists (ACLs), and static/dynamic routing protocols.

This dual capability is crucial for managing complex network traffic, ensuring efficient communication between different network segments (VLANs) at wire speed.

## 3. Backbone Role in Network Plan

The network backbone, centered around the MikroTik CRS520-4XS-16XQ-RM, plays a critical role in the overall network plan:

*   **Inter-VLAN Routing:** It is responsible for all inter-VLAN routing, facilitating high-speed communication between all defined network segments (Production, Stage, Studio, Workshop, Management, Guest).
*   **Default Gateway:** The core switch's VLAN interfaces serve as the default gateways for each respective VLAN.
*   **Traffic Aggregation:** All network traffic from access switches and end devices aggregates at the core switch before being routed to its destination or to the perimeter firewall (OPNsense) for internet access.
*   **Scalability:** The 100GbE capacity of the core switches provides a robust foundation for future network expansion and increased bandwidth demands.
