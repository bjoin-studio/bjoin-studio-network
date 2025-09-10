# Network Plan

## 1. Objective
This document outlines the comprehensive plan for designing, implementing, and maintaining the bjoin.studio network infrastructure. The primary goal is to establish a robust, secure, scalable, and highly available network that supports all project services and operations.

## 2. Physical Layout
- **Rack Layout:** Detailed plan for equipment placement within network racks, including power and cooling considerations.
- **Cabling:** Structured cabling plan, specifying cable types (e.g., Cat6a, Fiber Optic), lengths, and routing paths.
- **Device Placement:** Strategic positioning of network devices (routers, switches, firewalls, servers) for optimal performance, accessibility, and redundancy.
    - **Core Switch:** The MikroTik CRS520-4XS-16XQ-RM will serve as the network's core switch, providing high-speed inter-VLAN routing and aggregation for all network traffic.
    - **Access Switches:** All other switches in the network will function as access layer switches, connecting end-user devices and servers to the core switch. Connections between access switches and the core switch will utilize appropriate high-bandwidth uplinks (e.g., 10GbE or 40GbE fiber).
    - *Consideration:* Document specific hardware models (e.g., Cisco Nexus 9236C, Netgear GS108Ev4) and their physical connections.

## 3. IP Addressing
- **Subnetting:** Detailed subnetting scheme for all network segments, including production, staging, studio, workshop, management, and guest networks.
- **IP Allocation:** Strategy for IP address assignment (static, DHCP, DHCP reservations) for servers, network devices, and client machines.
    - *Reference:* Refer to `6-configuration/ip-address-management.md` for the detailed IPAM.

## 4. VLANs
- **VLAN IDs:** Define specific VLAN IDs for each network segment (e.g., Production, Staging, Studio, Workshop, Management, Guest) to logically separate traffic.
- **VLAN Assignments:** Clearly map VLANs to specific switch ports, SSIDs, and network interfaces on servers and virtual machines.
    - *Reference:* Refer to `8-deployment/opnsense-vlan-config-*.md` for detailed VLAN configurations.

## 5. Routing
- **Inter-VLAN Routing:** The core switch (MikroTik CRS520-4XS-16XQ-RM) will handle inter-VLAN routing to facilitate communication between different network segments.
- **Default Gateway:** Define default gateway addresses for each VLAN, pointing to the core switch's VLAN interface.
- **Static Routes/Dynamic Routing:** Implement static routes for specific network paths or consider dynamic routing protocols (e.g., OSPF) for more complex environments.

## 6. Security
- **Firewall Rules:** Implement robust firewall rules on the network perimeter (e.g., OPNsense firewall) and internal network segments to control traffic flow and prevent unauthorized access.
    - *Reference:* Refer to `6-configuration/cfg/opnsense/opnsense-firewall-rules.md` for detailed firewall rule policies.
- **Access Control:** Implement access control lists (ACLs) on switches and routers to restrict access to sensitive network resources.
- **Intrusion Detection/Prevention (IDS/IPS):** Evaluate and implement IDS/IPS solutions for real-time threat detection and prevention.
- **Network Segmentation:** Utilize VLANs and firewall rules to enforce strict network segmentation, limiting the blast radius of security incidents.

## 7. Services
- **DNS:** Implement a robust DNS resolution strategy, potentially using FreeIPA for internal DNS and external DNS servers for internet resolution.
    - *Reference:* Refer to `03-research/understanding-dns-freeipa.md` for FreeIPA DNS integration.
- **DHCP:** Configure DHCP services for automatic IP address assignment to client devices within each VLAN.
- **NTP:** Ensure all network devices and servers synchronize their time with reliable NTP sources for accurate logging and troubleshooting.
- **Monitoring:** Implement a comprehensive network monitoring solution (e.g., LibreNMS, Prometheus) to track network performance, device health, and identify potential issues.
    - *Reference:* Refer to `8-deployment/network-monitoring-setup.md` for monitoring setup details.

## 8. High-Level Design/Architecture Overview
- **Topology:** A brief description of the network topology (e.g., a collapsed core design with a single core switch and multiple access switches).
- **Key Components:** Overview of major network components (firewall, core switch, access switches, servers, wireless access points).
- **Data Flow:** High-level understanding of how data flows within the network and to/from external networks.
    - *Reference:* Refer to `5-physical-layout/logical-diagram.md` and `5-physical-layout/data-flow-diagrams.md` for visual representations.

## 9. Requirements
- **Functional Requirements:**
    - **Connectivity:** Provide reliable network connectivity for all devices and users.
    - **Performance:** Support required bandwidth and low latency for critical applications.
    - **Scalability:** Ability to easily expand the network to accommodate future growth in devices and users.
    - **Availability:** Ensure high uptime for critical network services and infrastructure.
- **Non-Functional Requirements:**
    - **Security:** Protect network resources from unauthorized access and cyber threats.
    - **Manageability:** Ease of configuration, monitoring, and troubleshooting.
    - **Cost-Effectiveness:** Optimize for cost while meeting performance and security requirements.
    - **Compliance:** Adherence to relevant industry standards and regulations.

## 10. Assumptions and Constraints
- **Assumptions:**
    - Availability of required hardware and software.
    - Stable power and environmental conditions in network closets/racks.
    - Existing ISP connectivity is reliable and meets bandwidth needs.
- **Constraints:**
    - Budget limitations for hardware and software.
    - Physical space limitations in network closets.
    - Existing infrastructure (e.g., cabling) may impose limitations.
    - Personnel availability and skill sets for implementation and management.

## 11. Naming Conventions
- Adherence to established host naming conventions for all network devices, servers, and virtual machines.
    - *Reference:* Refer to `12-appendix/host-naming-conventions.md` for detailed guidelines.

## 12. Backup and Recovery
- **Configuration Backup:** Implement automated backups of network device configurations (routers, switches, firewalls) to a secure, off-site location.
- **Disaster Recovery Plan:** Develop and regularly test a disaster recovery plan for critical network infrastructure to ensure business continuity.
    - *Reference:* Refer to `9-maintenance/backup-and-recovery-plan.md` and `9-maintenance/disaster-recovery-plan.md`.

## 13. Testing Plan
- **Pre-Deployment Testing:** Conduct thorough testing of network configurations in a lab environment before deployment to production.
- **Post-Deployment Verification:** Verify network functionality, performance, and security after deployment through a series of tests (e.g., connectivity, throughput, security scans).
    - *Reference:* Refer to `8-deployment/vlan-testing-procedure.md`.

## 14. Phased Implementation
- Outline a phased approach for network implementation, breaking down the project into manageable stages to minimize disruption and facilitate troubleshooting.
    - *Example Phases:*
        1.  Core Network Setup (Firewall, Core Switch)
        2.  VLAN and IP Addressing Configuration
        3.  Access Switch Deployment)
        4.  Service Integration (DNS, DHCP, Monitoring)
        5.  Client Onboarding

## 15. Future Considerations and Scalability
- **Growth Planning:** Plan for future network expansion, including additional devices, users, and bandwidth requirements.
- **Technology Refresh:** Periodically review and update network hardware and software to leverage new technologies and improve performance/security.
- **Emerging Technologies:** Stay informed about emerging networking technologies (e.g., SDN, intent-based networking) and evaluate their potential benefits.