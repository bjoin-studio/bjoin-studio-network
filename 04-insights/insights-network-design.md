# Evolving the Network: From "Router-on-a-Stick" to Hybrid Routing

This document explains the key concepts and architectural decisions behind the bjoin.studio network design, highlighting its evolution from a simple "Router-on-a-Stick" model to a more sophisticated **hybrid routing** strategy. This new approach is designed to balance security with the high-performance demands of a media production environment.

## The Core Challenge: Overcoming the 1Gbps Bottleneck

The initial network design relied on a Protectli firewall with 1Gbps ports. While excellent for security, it created a performance bottleneck. All traffic between different VLANs (e.g., a video editor accessing a file on a server in another VLAN) was forced through this 1Gbps link.

This was an intentional trade-off, prioritizing security and inspection for all cross-VLAN traffic. However, as the need for high-speed access to large media files grew, this bottleneck became a significant limitation.

## The Solution: A Hybrid Routing Strategy

To address this, the network was upgraded to a **hybrid routing** model. This approach combines the strengths of two different types of devices:

1.  **A High-Performance 10Gbps Virtualized Firewall:** The primary routing and security functions are now handled by a powerful OPNsense firewall running as a virtual machine on an HP Z620 workstation. This VM has a dedicated **10Gbps Solarflare network card**, eliminating the 1Gbps bottleneck for inter-VLAN traffic that requires inspection.

2.  **A High-Speed Layer 3 Core Switch:** For specific, trusted, high-bandwidth VLANs (like the `Studio` zone), routing is offloaded to the **MikroTik CRS520-4XS-16XQ-RM core switch**. This allows traffic between these performance-critical zones to be routed at the switch's full backplane speed (up to 100Gbps), bypassing the firewall entirely.

### How Hybrid Routing Works

This model provides the best of both worlds:

*   **Performance-Critical Traffic (East-West):** When a 100Gb/s editing workstation needs to pull a huge file from a 100Gb/s media server in another trusted, high-speed VLAN, that traffic is routed directly by the MikroTik core switch. It **never touches the firewall**, ensuring maximum speed.

*   **Security-Sensitive Traffic (North-South):** When a device from one VLAN needs to talk to a less-trusted VLAN, or to the internet, that traffic *must* go through the 10Gbps OPNsense firewall to be inspected and routed.

This is an intentional, strategic design. We use the expensive, high-speed switch for bulk data transfers within our performance-critical zones, while using the powerful virtualized firewall to apply security and control to all other traffic.

## VLAN Tagging Standard: 802.1Q

When configuring VLANs, you will see references to different tagging standards. For this entire network, we will be using the **802.1Q** standard.

*   **802.1Q** is the universal standard for creating VLANs on an internal network. It's like putting colored labels on your internal office mail to send it to the right department. All of your equipment (OPNsense, switches) uses this standard.

*   You may also see an option for **802.1ad (QinQ)**. This is a specialized standard for service providers to "stack" customer VLANs inside their own. It's like FedEx putting your entire box of labeled mail inside a larger FedEx box. We are the office, not FedEx, so we will not use this.

**In short: For all VLAN configuration, 802.1Q is the correct and only standard you need to use.**

## What is a DMZ (Demilitarized Zone)?

The concept of a DMZ can seem a bit confusing, but it's a simple and very powerful security tool. Think of your network like a secure office building.

*   Your **Internal LAN** (e.g., Production Wired VLAN 11, Studio Wired VLAN 32) is the secure main office where all your trusted employees and sensitive documents are. You don't want random people from the street wandering in.
*   The **Internet** is the public street outside.
*   A **DMZ** is like the **lobby** of your building.

Visitors from the street (the internet) are allowed into the lobby (the DMZ) to talk to a receptionist or drop off a package (e.g., access your public web server). However, the lobby is separated from the main office by locked, secure doors (the firewall). A visitor in the lobby can't get into the main office.

In network terms, a DMZ is a small, isolated network that sits between the internet and your trusted internal LAN. It's where you place any services that need to be accessible from the internet.

The firewall rules are simple and strict:
*   The **Internet** can talk to servers in the **DMZ**.
*   The **Internet** can **NOT** talk to your **Internal LAN**.
*   The **DMZ** can **NOT** talk to your **Internal LAN**. This is the most important rule. If a server in your DMZ is compromised, the attacker is still trapped in the lobby and can't access your secure internal network.

One of the spare ports on the Protectli firewall is the perfect tool to create a dedicated, physical DMZ if you ever decide to host a public-facing service.

## Enabling Seamless Cross-VLAN Access with FreeIPA

Your network design is indeed on target for building a FreeIPA environment that allows users to seamlessly cross VLANs and access resources in a controlled and secure manner. This is achieved through the powerful combination of:

*   **VLANs for Isolation:** Your VLAN segmentation provides a fundamental layer of security by isolating different network segments. This is a strength, not a limitation.
*   **FreeIPA for Centralized Control:** FreeIPA acts as the central authority for authentication and authorization across all these isolated VLANs. It provides a single identity for users and machines.
*   **The Firewall for Mediation:** Your OPNsense firewall is the critical component that mediates controlled communication between VLANs. It enforces the rules that allow specific traffic (e.g., FreeIPA authentication requests) to pass between segments.

This architecture ensures that users can access resources across VLANs using their single FreeIPA identity, while maintaining granular control over what they can access and from where. For example, a lead flame artist who is also a system administrator can be granted broad access through FreeIPA group memberships and `sudo` rules, allowing them to manage storage, networks, servers, and production systems from any authorized workstation, regardless of its VLAN.

## A Note on FreeIPA Network Traffic

FreeIPA traffic is generally not heavy. A 1Gbps connection is more than sufficient for the FreeIPA server. Here's a breakdown of why:

*   **Lightweight Traffic:** FreeIPA traffic mostly consists of small, quick transactions like DNS lookups, Kerberos authentication tickets, and LDAP queries. These are very small packets and don't consume much bandwidth.
*   **Not a File Server:** You won't be transferring large files to or from the FreeIPA server. It's purely for authentication and identity management.
*   **The Real Bottleneck:** If you were to experience performance issues with FreeIPA, the bottleneck would almost certainly be the CPU or the disk I/O on the Proxmox host, not the network connection.

### When Could it Spike?

The only time you might see a spike in FreeIPA traffic is during a "login storm" – for example, if everyone in the studio logs in at exactly the same time on a Monday morning. Even in this worst-case scenario, the traffic is highly unlikely to saturate a 1Gbps link.
