# Key Network Concepts

This document explains some of the key concepts and architectural decisions behind the bjoin.studio network design.

## Key Architectural Decision: "Router-on-a-Stick"

A core principle of this network design is the use of a "Router-on-a-Stick" configuration. You might notice that even though the Protectli firewall has four ports, we are only using two: one for `WAN` (internet) and one for `LAN` (internal network). This is intentional and is a standard practice for building secure, scalable networks.

Here’s why we do it this way:

*   **Centralized Control:** By forcing all traffic between VLANs to go up the "stick" to the OPNsense firewall through a single port, we guarantee that every packet is inspected. This gives us a single, powerful point of control for all security policies.
*   **Specialized Roles:** It lets the switches do what they do best (handle high-speed VLAN traffic) and lets the firewall do what it does best (deep packet inspection, routing, and security).
*   **Flexibility:** We can add dozens of new VLANs in the future without ever needing to change the physical cabling on the firewall.

The spare ports on the firewall give us great options for the future, like a dedicated high-security DMZ or a redundant link to the core switch.

## A Note on Performance and Bottlenecks

It's fair to ask: "If we have a 100Gb/s switch, won't the 1Gb/s firewall be a bottleneck?" The answer is **no** for the most important traffic, and it highlights the power of this design. The key is understanding the two types of traffic on our network.

### 1. Traffic *Inside* a VLAN (East-West)
This is your high-speed lane. When a 100Gb/s editing workstation needs to pull a huge file from a 100Gb/s media server in the same VLAN, that traffic goes directly to the Cisco 100G switch and is handled there. It **never touches the firewall**. This is where the heavy lifting is done, at full speed.

### 2. Traffic *Between* VLANs (North-South)
When a device from one VLAN needs to talk to another (e.g., a 1G office workstation accessing a server), that traffic *must* go through the firewall to be inspected and routed. This traffic **is limited to the 1Gb/s speed of the firewall's port**.

This is an intentional trade-off. We are using the expensive, high-speed switch for the bulk data transfers *within* our performance-critical zones, while using the firewall to apply security and control to the lower-speed traffic that needs to cross between those zones.

### Upgrading Firewall Performance
If, in the future, the 1Gb/s speed for traffic *between* VLANs becomes a limitation, the solution is to upgrade the firewall hardware. To achieve true 10Gb/s firewalling, you would need a new machine with:

*   **10Gb Ports:** This raises the maximum physical speed of the connection to the network.
*   **A Powerful CPU:** This is the "engine" of the firewall. A faster CPU is critical for processing packets, inspecting traffic, and handling routing at high speeds.
*   **Sufficient RAM:** More memory is needed to handle the state table for a larger number of connections.
*   **Awareness of Services:** Performance-intensive services like Intrusion Detection (IDS/IPS) and VPNs will always require a more powerful CPU to maintain high throughput.

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