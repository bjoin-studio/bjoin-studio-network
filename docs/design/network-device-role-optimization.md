# Network Device Role Optimization and Hybrid Routing Strategy

This document outlines the strategic roles of key network devices within the bjoin.studio network, focusing on how their unique capabilities are leveraged to achieve both performance and security goals. It details a hybrid routing approach that optimizes traffic flow while maintaining necessary security controls.

## 1. Introduction

The bjoin.studio network design prioritizes both high-performance data transfer within specific zones and robust security for inter-zone and internet-bound traffic. This is achieved by strategically assigning roles to network devices, allowing each to excel at its primary function. This document explains how the OPNsense firewall and the Cisco Nexus 9236C switch work in concert to create a hybrid routing environment.

## 2. OPNsense (Protectli Vault) Role: The Secure Gateway

The OPNsense firewall, running on the Protectli Vault, serves as the primary security enforcement point and the gateway to the Internet. It operates primarily in a "Router-on-a-Stick" configuration for most inter-VLAN traffic.

*   **Primary Functions:**
    *   **Internet Gateway:** All traffic to and from the Internet passes through OPNsense for NAT, firewalling, and security inspection.
    *   **Centralized Security Policy:** OPNsense is the single point of control for all firewall rules, Intrusion Detection/Prevention (IDS/IPS), and traffic shaping.
    *   **Inter-VLAN Routing (Default):** OPNsense handles routing between VLANs. This ensures that all inter-VLAN traffic is inspected by the firewall.
    *   **DHCP and DNS:** Provides DHCP services for various VLANs and acts as the primary DNS resolver (forwarding to FreeIPA for internal domains).
    *   **VPN Termination:** Handles remote access and site-to-site VPN connections.

*   **Performance Consideration:** The 1Gbps LAN port on the Protectli Vault can become a bottleneck for high-bandwidth inter-VLAN traffic if all routing is performed by OPNsense. This is where the Cisco Nexus 9236C plays a complementary role.

## 3. Cisco Nexus 9236C Role: The High-Speed Inter-VLAN Router

The Cisco Nexus 9236C is a powerful Layer 3 switch designed for high-performance data center and campus environments. It is leveraged to offload high-bandwidth inter-VLAN routing from the OPNsense firewall.

*   **Primary Functions:**
    *   **High-Speed Layer 2 Switching:** Provides wire-speed switching within VLANs.
    *   **High-Speed Layer 3 Switching (Inter-VLAN Routing):** For designated trusted, high-bandwidth VLANs, the Nexus switch acts as the default gateway and performs routing directly between these VLANs using Switched Virtual Interfaces (SVIs). This traffic stays on the switch's high-speed backplane.
    *   **Core Network Connectivity:** Serves as a central distribution point for network segments, including uplinks to other switches and critical servers.

## 4. The Hybrid Routing Approach

The bjoin.studio network employs a hybrid routing strategy to balance security and performance:

*   **OPNsense as the "Security Router":**
    *   All traffic destined for the **Internet** is routed via OPNsense.
    *   Traffic between **less trusted VLANs** (e.g., Guest to Production) is routed via OPNsense to ensure full firewall inspection.
    *   Traffic to/from the **Management VLAN (VLAN 51)** is typically routed via OPNsense to maintain strict control over critical infrastructure access.

*   **Cisco Nexus 9236C as the "Performance Router":**
    *   **High-bandwidth, trusted inter-VLAN traffic** (e.g., between Studio Wired 10Gb/100Gb VLANs, or Production 10Gb VLANs) is routed directly by the Nexus switch. This traffic bypasses the OPNsense firewall's 1Gb LAN port, allowing it to flow at the Nexus's much higher speeds.
    *   The Nexus switch maintains a default route pointing to OPNsense for all traffic not explicitly routed by the switch.

### Security Considerations of the Hybrid Approach

It is critical to understand the security implications of Layer 3 switching on the Nexus:

*   **Firewall Bypass:** Traffic routed directly by the Cisco Nexus 9236C **does NOT pass through the OPNsense firewall**. This means any firewall rules, IDS/IPS, or traffic shaping configured on OPNsense for those specific inter-VLAN flows will be bypassed.
*   **Policy Enforcement:** Security policies for traffic routed by the Nexus must be enforced at the source/destination hosts (e.g., host-based firewalls) or by carefully designed Access Control Lists (ACLs) on the Nexus itself.
*   **Trust Zones:** This hybrid model relies on clearly defined trust zones. High-trust, high-bandwidth zones can leverage the Nexus for speed, while lower-trust or internet-facing zones rely on OPNsense for deep inspection.

## 5. Other Devices in the Optimized Design

*   **Netgear GS108Ev4:** Functions as an access layer switch, providing port-level VLAN assignment for end devices. Its configuration is manual via web GUI.
*   **QNAP NAS:** Connects to multiple VLANs (e.g., 31, 32, 33) via a single trunk port on an upstream switch, allowing high-speed access from various studio zones. FreeIPA provides centralized authentication for NAS shares.
*   **Proxmox VE Host (`pmx-01`):** Connects to the network via a trunk port, allowing VMs to be placed in various VLANs.

## 6. Long-Term Improvements

As the network evolves, the following improvements could be considered:

*   **Dedicated 10Gb/25Gb/40Gb/100Gb Firewall:** Upgrading the OPNsense hardware to support higher-speed interfaces would eliminate the 1Gb bottleneck entirely, allowing all inter-VLAN traffic to be inspected by the firewall at higher speeds. This would simplify the routing design by potentially moving all inter-VLAN routing back to the firewall.
*   **Ansible Automation for Cisco Nexus:** Develop comprehensive Ansible playbooks for the Cisco Nexus 9236C to automate VLAN creation, SVI configuration, port assignments, and routing policies. This would ensure configuration consistency and enable rapid deployment.
*   **Network Monitoring Integration:** Implement robust monitoring solutions (e.g., Prometheus, Grafana, ELK stack) to gain deep insights into traffic patterns, device health, and security events across all VLANs.
*   **Centralized Log Management:** Consolidate logs from all network devices, servers, and security appliances into a central log management system for easier troubleshooting and security auditing.
*   **Advanced Security Features:** Explore features like Network Access Control (NAC), micro-segmentation, and more advanced IDS/IPS capabilities as the network grows.
*   **Redundancy and High Availability:** Implement redundant links, devices, and power supplies for critical network components to ensure continuous operation.
