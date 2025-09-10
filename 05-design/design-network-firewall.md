# Network Firewall Design

This document outlines the firewall design for the bjoin.studio network, detailing the role of OPNsense as the dedicated security gateway and best practices for firewall rule management.

## 1. Introduction to Network Firewalling

The firewall is a critical component of the bjoin.studio network's security posture. Its primary role is to control and inspect all traffic entering and leaving the internal network, enforcing security policies, and protecting sensitive resources from unauthorized access and threats.

## 2. OPNsense as the Dedicated Security Gateway

The virtualized **OPNsense instance** (`opnsense-vm`) running on the HP Z620 workstation serves as the dedicated security gateway for the entire network.

*   **Primary Role:** OPNsense is the single point of egress and ingress for all external (North-South) network traffic. It acts as the network's perimeter defense, ensuring that all traffic leaving or entering the internal network is inspected and adheres to defined security policies.
*   **Firewall-on-a-Stick Configuration:** The OPNsense VM is integrated into the network using a "firewall-on-a-stick" configuration. The MikroTik CRS520-4XS-16XQ-RM (the internal VLAN gateway) directs all internet-bound traffic to the OPNsense VM's IP address as the next hop. OPNsense then performs stateful inspection, Network Address Translation (NAT), and applies security rules before forwarding the traffic to the ISP modem.
*   **Decommissioned Hardware:** The Protectli Vault appliance is no longer the primary firewall in this design, its role has been superseded by the more powerful virtualized OPNsense instance.

## 3. Firewall Rule Best Practices

Effective firewall management relies on adhering to established best practices:

*   **Default Deny:** Always start with a default-deny rule on all interfaces. This ensures that only traffic that is explicitly allowed is permitted, minimizing the attack surface.
*   **Be Specific:** Create granular rules for the traffic you want to allow. Avoid using "any" for source, destination, or port whenever possible to limit potential exposure.
*   **Use Aliases:** Utilize aliases for IP addresses, ports, and networks. This makes rules much easier to read, manage, and update, especially in complex configurations.
*   **Documentation:** Add clear and concise descriptions to every firewall rule. Document its purpose, the reason for its existence, and any relevant ticket numbers or policy references.
*   **Order Matters:** Firewalls process rules from top to bottom. The first rule that matches a packet is the one that is applied. Place more specific rules before more general (e.g., `allow all`) rules to ensure intended policy enforcement.

## 4. Demilitarized Zone (DMZ) Concept

The DMZ is a crucial security concept implemented via firewalling. It is a small, isolated network segment that sits between the internet and your trusted internal LAN.

*   **Purpose:** The DMZ acts as a buffer zone for services that need to be accessible from the internet (e.g., public web servers, VPN endpoints).
*   **Security Principle:** The DMZ is strictly separated from the internal LAN by firewall rules. The internet can access services in the DMZ, but it cannot directly access the internal LAN. Crucially, services within the DMZ cannot directly initiate connections to the internal LAN. This design ensures that if a service in the DMZ is compromised, the attacker is contained within the DMZ and cannot easily access sensitive internal resources.

## 5. Firewall's Role in Traffic Flow

*   **External (North-South) Traffic:** All traffic destined for the internet (or originating from it) is routed by the MikroTik to the OPNsense VM. OPNsense acts as the internet gateway, applying security policies before forwarding.
*   **Internal (East-West) Traffic:** Traffic between different VLANs is routed directly by the MikroTik CRS520-4XS-16XQ-RM. OPNsense is **not** involved in this path, ensuring high performance for internal communications.
