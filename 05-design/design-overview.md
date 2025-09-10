# Network Design Overview

This document provides a high-level overview of the bjoin.studio network design. It serves as a central entry point and a table of contents for the more detailed design documents, each focusing on a specific aspect of the network architecture.

## Design Principles

The bjoin.studio network is designed with the following core principles:

*   **Consolidated Control:** Centralizing Layer 2 and Layer 3 functions on high-performance devices for simplified management and maximized throughput.
*   **Performance Optimization:** Ensuring high-speed data transfer for internal communications by leveraging dedicated hardware and optimized routing paths.
*   **Robust Security:** Implementing layered security measures, including network segmentation, dedicated firewalls, and strict access controls.
*   **Scalability:** Building a foundation that can easily expand to accommodate future growth in devices, users, and bandwidth requirements.

## Detailed Design Documents

For in-depth information on specific components and aspects of the network, please refer to the following documents:

*   **Network Backbone Design:** Details the high-speed core network fabric and the capabilities of Layer 2/Layer 3 switches.
    *   [design-network-backbone.md](design-network-backbone.md)

*   **Network VLAN Design:** Outlines the Virtual Local Area Network (VLAN) design, including segmentation, tagging standards, and the definitive VLAN and IP addressing plan.
    *   [design-network-vlans.md](design-network-vlans.md)

*   **Network Routing Design:** Explains the routing infrastructure, the roles of the core switch and firewall in traffic flow, and routing protocols.
    *   [design-network-routing.md](design-network-routing.md)

*   **Network Gateway Design:** Describes the design and roles of internal VLAN gateways and the external internet gateway.
    *   [design-network-gateway.md](design-network-gateway.md)

*   **Network Firewall Design:** Details the firewall architecture, OPNsense's role as the dedicated security gateway, firewall rule best practices, and the DMZ concept.
    *   [design-network-firewall.md](design-network-firewall.md)
