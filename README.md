# Network Architecture Documentation

This repository serves as a centralized location for all documentation related to the network architecture, design, and operation of bjoin.studio.

## Overview

The goal of this repository is to maintain a living record of our network infrastructure. This includes high-level designs, standards, operational procedures, security policies, and more.

## Key Architectural Decision: "Router-on-a-Stick"

A core principle of this network design is the use of a "Router-on-a-Stick" configuration. You might notice that even though the Protectli firewall has four ports, we are only using two: one for `WAN` (internet) and one for `LAN` (internal network). This is intentional and is a standard practice for building secure, scalable networks.

Here’s why we do it this way:

*   **Centralized Control:** By forcing all traffic between VLANs to go up the "stick" to the OPNsense firewall through a single port, we guarantee that every packet is inspected. This gives us a single, powerful point of control for all security policies.
*   **Specialized Roles:** It lets the switches do what they do best (handle high-speed VLAN traffic) and lets the firewall do what it does best (deep packet inspection, routing, and security).
*   **Flexibility:** We can add dozens of new VLANs in the future without ever needing to change the physical cabling on the firewall.

The spare ports on the firewall give us great options for the future, like a dedicated high-security DMZ or a redundant link to the core switch.

## What is a DMZ (Demilitarized Zone)?

The concept of a DMZ can seem a bit confusing, but it's a simple and very powerful security tool. Think of your network like a secure office building.

*   Your **Internal LAN** (VLANs 11, 32, etc.) is the secure main office where all your trusted employees and sensitive documents are. You don't want random people from the street wandering in.
*   The **Internet** is the public street outside.
*   A **DMZ** is like the **lobby** of your building.

Visitors from the street (the internet) are allowed into the lobby (the DMZ) to talk to a receptionist or drop off a package (e.g., access your public web server). However, the lobby is separated from the main office by locked, secure doors (the firewall). A visitor in the lobby can't get into the main office.

In network terms, a DMZ is a small, isolated network that sits between the internet and your trusted internal LAN. It's where you place any services that need to be accessible from the internet.

The firewall rules are simple and strict:
*   The **Internet** can talk to servers in the **DMZ**.
*   The **Internet** can **NOT** talk to your **Internal LAN**.
*   The **DMZ** can **NOT** talk to your **Internal LAN**. This is the most important rule. If a server in your DMZ is compromised, the attacker is still trapped in the lobby and can't access your secure internal network.

One of the spare ports on the Protectli firewall is the perfect tool to create a dedicated, physical DMZ if you ever decide to host a public-facing service.

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

## Table of Contents

### Project Files
*   [README.md](README.md)
*   [GEMINI.md](GEMINI.md)

### Scripts
*   [mac_pro_6_1_IOMMU_config.sh](src/mac_pro_6_1_IOMMU_config.sh) - A utility script to enable IOMMU on the Proxmox host, which is necessary for PCI(e) passthrough (e.g., giving a VM direct access to a GPU).

### Design
*   [bjoin-studio-network-design.md](docs/design/bjoin-studio-network-design.md)

### Standards
*   [host-naming-conventions.md](docs/standards/host-naming-conventions.md)

### Operational
*   **diagrams/**
    *   [data-flow-diagrams.md](docs/operational/diagrams/data-flow-diagrams.md)
    *   [logical-diagram.md](docs/operational/diagrams/logical-diagram.md)
    *   [physical-cabling-guide.md](docs/operational/diagrams/physical-cabling-guide.md)
    *   [physical-diagram.md](docs/operational/diagrams/physical-diagram.md)
*   **ipam/**
    *   [ip-address-management.md](docs/operational/ipam/ip-address-management.md)
*   **runbooks/**
    *   [firewall-firmware-updates.md](docs/operational/runbooks/firewall-firmware-updates.md)
    *   [opnsense-initial-setup-guide.md](docs/operational/runbooks/opnsense-initial-setup-guide.md)
    *   [opnsense-vlan-config-1x-production.md](docs/operational/runbooks/opnsense-vlan-config-1x-production.md)
    *   [opnsense-vlan-config-2x-stage.md](docs/operational/runbooks/opnsense-vlan-config-2x-stage.md)
    *   [opnsense-vlan-config-3x-studio.md](docs/operational/runbooks/opnsense-vlan-config-3x-studio.md)
    *   [opnsense-vlan-config-4x-workshop.md](docs/operational/runbooks/opnsense-vlan-config-4x-workshop.md)
    *   [opnsense-vlan-config-5x.md](docs/operational/runbooks/opnsense-vlan-config-5x.md)
    *   [opnsense-vlan-config-6x-guest.md](docs/operational/runbooks/opnsense-vlan-config-6x-guest.md)
    *   [proxmox-host-setup-guide.md](docs/operational/runbooks/proxmox-host-setup-guide.md)
    *   [server-onboarding.md](docs/operational/runbooks/server-onboarding.md)

### Security
*   **plans/**
    *   [incident-response-plan.md](docs/security/plans/incident-response-plan.md)
    *   [vulnerability-management-plan.md](docs/security/plans/vulnerability-management-plan.md)
*   **policies/**
    *   [acceptable-use-policy.md](docs/security/policies/acceptable-use-policy.md)
    *   [firewall-rule-policy.md](docs/security/policies/firewall-rule-policy.md)
    *   [vpn-access-policy.md](docs/security/policies/vpn-access-policy.md)

### Lifecycle
*   [asset-management.md](docs/lifecycle/asset-management.md)
*   [change-management-log.md](docs/lifecycle/change-management-log.md)
*   [roadmap.md](docs/lifecycle/roadmap.md)

### Disaster Recovery
*   [backup-and-recovery-plan.md](docs/disaster-recovery/backup-and-recovery-plan.md)
*   [disaster-recovery-plan.md](docs/disaster-recovery/disaster-recovery-plan.md)

### Insights
*   [repository-insights.md](docs/insights/repository-insights.md)

## Contributing

Contributions to this documentation are welcome and encouraged. Please place new documents in the appropriate directory and follow the existing naming conventions.
