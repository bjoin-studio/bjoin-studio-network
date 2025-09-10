# Network Gateway Design

This document outlines the design and roles of the network gateways within the bjoin.studio infrastructure, distinguishing between internal VLAN gateways and the external internet gateway.

## 1. Introduction to Network Gateways

Network gateways are essential devices that enable communication between different network segments and between the internal network and external networks like the internet. In the bjoin.studio network, gateways are strategically placed to ensure efficient traffic flow, robust security, and clear network segmentation.

## 2. Internal VLAN Gateways

The **MikroTik CRS520-4XS-16XQ-RM** serves as the default gateway for all internal VLANs. This powerful Layer 2/Layer 3 managed switch is responsible for routing traffic between the various segmented networks within the studio.

*   **Role:** For every defined VLAN, the MikroTik CRS520-4XS-16XQ-RM holds the gateway IP address (typically the `.1` address of the subnet). All devices within a specific VLAN are configured to use this IP address as their default gateway to reach other VLANs or the internet.
*   **Inter-VLAN Routing:** By centralizing the gateway function on the MikroTik, inter-VLAN routing occurs at wire speed on the switch's high-performance backplane, ensuring minimal latency for internal communications.

### Definitive VLAN Gateway IP Plan

The following table, extracted from the Definitive VLAN, IP, and Group Plan, highlights the gateway IP address for each VLAN:

| VLAN ID | Zone         | Subnet          | Gateway IP     |
|:--------|:-------------|:----------------|:---------------|
| **11**  | Production   | `10.20.11.0/24` | `10.20.11.1`   |
| **12**  | Production   | `10.20.12.0/24` | `10.20.12.1`   |
| **13**  | Production   | `10.20.13.0/24` | `10.20.13.1`   |
| **14**  | Production   | `10.20.14.0/24` | `10.20.14.1`   |
| **15**  | Production   | `10.20.15.0/24` | `10.20.15.1`   |
| **21**  | Stage        | `10.20.21.0/24` | `10.20.21.1`   |
| **22**  | Stage        | `10.20.22.0/24` | `10.20.22.1`   |
| **23**  | Stage        | `10.20.23.0/24` | `10.20.23.1`   |
| **24**  | Stage        | `10.20.24.0/24` | `10.20.24.1`   |
| **25**  | Stage        | `10.20.25.0/24` | `10.20.25.1`   |
| **31**  | Studio       | `10.20.31.0/24` | `10.20.31.1`   |
| **32**  | Studio       | `10.20.32.0/24` | `10.20.32.1`   |
| **33**  | Studio       | `10.20.33.0/24` | `10.20.33.1`   |
| **34**  | Studio       | `10.20.34.0/24` | `10.20.34.1`   |
| **35**  | Studio       | `10.20.35.0/24` | `10.20.35.1`   |
| **41**  | Workshop     | `10.20.41.0/24` | `10.20.41.1`   |
| **42**  | Workshop     | `10.20.42.0/24` | `10.20.42.1`   |
| **43**  | Workshop     | `10.20.43.0/24` | `10.20.43.1`   |
| **44**  | Workshop     | `10.20.44.0/24` | `10.20.44.1`   |
| **45**  | Workshop     | `10.20.45.0/24` | `10.20.45.1`   |
| **51**  | Management   | `10.20.51.0/24` | `10.20.51.1`   |
| **52**  | Management   | `10.20.52.0/24` | `10.20.52.1`   |
| **53**  | Management   | `10.20.53.0/24` | `10.20.53.1`   |
| **54**  | Management   | `10.20.54.0/24` | `10.20.54.1`   |
| **55**  | Management   | `10.20.55.0/24` | `10.20.55.1`   |
| **61**  | Guest        | `10.20.61.0/24` | `10.20.61.1`   |
| **62**  | Guest        | `10.20.62.0/24` | `10.20.62.1`   |
| **63**  | Guest        | `10.20.63.0/24` | `10.20.63.1`   |
| **64**  | Guest        | `10.20.64.0/24` | `10.20.64.1`   |
| **65**  | Guest        | `10.20.65.0/24` | `10.20.65.1`   |

## 3. External Internet Gateway

The virtualized **OPNsense instance** (`opnsense-vm`) running on the HP Z620 workstation functions as the dedicated security gateway for all external (North-South) network traffic.

*   **Role:** OPNsense is the single point of egress and ingress for all internet-bound traffic. It acts as the network's perimeter defense, ensuring that all traffic leaving or entering the internal network is inspected and adheres to security policies.
*   **Firewall-on-a-Stick Configuration:** The MikroTik CRS520-4XS-16XQ-RM directs all internet-bound traffic to the OPNsense VM's IP address as the next hop. OPNsense then performs stateful inspection, Network Address Translation (NAT), and applies security rules before forwarding the traffic to the ISP modem.
*   **DMZ Concept:** OPNsense also provides the capability to establish a Demilitarized Zone (DMZ), an isolated network segment for services that need to be accessible from the internet while maintaining strict separation from the internal LAN.

## 4. Traffic Flow through Gateways

*   **Internal (East-West) Traffic:** Traffic between different VLANs is routed directly by the MikroTik CRS520-4XS-16XQ-RM using its internal VLAN gateways. OPNsense is not involved in this path, ensuring high performance.
*   **External (North-South) Traffic:** All traffic destined for the internet (or originating from it) is routed by the MikroTik to the OPNsense VM, which then acts as the internet gateway, applying security policies before forwarding.

## 5. High-Level Topology

The bjoin.studio network is segmented into multiple VLANs, all of which are routed through the central MikroTik CRS520-4XS-16XQ-RM core switch. The OPNsense firewall acts as the secure gateway for internet traffic.

*   **Collapsed Core Design:** The network utilizes a collapsed core design, where the MikroTik CRS520-4XS-16XQ-RM serves as both the core and distribution layer.
*   **VLAN Segmentation:** Traffic is logically separated into distinct VLANs for different purposes (e.g., Production, Stage, Studio, Workshop, Management, Guest).
*   **Traffic Flow Policies:** By default, all inter-VLAN traffic is blocked by the firewall. Rules must be explicitly created to allow traffic to flow between VLANs.