# Insights for Network Hardware

This document provides an overview of the capabilities of the Ethernet switches used in the bjoin.studio network.

## 1. Ethernet Switch Capabilities

The network utilizes three types of switches, each with distinct capabilities. Understanding their roles is key to understanding the network's design.

| Switch Type              | Configurable | VLAN Support | Routing (Inter-VLAN) | Use Case                      |
|:-------------------------|:-------------|:-------------|:---------------------|:------------------------------|
| **Layer 2/3 Managed**    | ✅ Yes       | ✅ Yes       | ✅ Yes               | Core network routing          |
| **Layer 2 Managed**      | ✅ Yes       | ✅ Yes       | ❌ No                | LAN segmentation, access ports|
| **Unmanaged**            | ❌ No        | ❌ No        | ❌ No                | Small, simple plug-and-play   |

*   **Layer 2/3 Managed Switch:** The core of the network. Combines standard Layer 2 switching (based on MAC addresses) with Layer 3 routing (based on IP addresses). It is responsible for all high-speed routing between different VLANs.

*   **Layer 2 Managed Switch:** The workhorse for connecting end devices. It understands VLANs, allowing it to create access ports for specific VLANs and trunk ports to carry multiple VLANs, but it cannot route traffic *between* them.

*   **Unmanaged Switch:** A simple plug-and-play device for basic connectivity. It has no concept of VLANs and is only suitable for expanding port counts within a single, untagged network segment.

## 2. Hardware Inventory

This list serves as a quick inventory of the primary network switching hardware.

### 100 Gb Ethernet Switches (L2/L3)
*   **MikroTik CRS520-4XS-16XQ-RM**
*   **MikroTik CRS504-4XQ-IN**
*   **Cisco NEXUS 9236c**

### 10 Gb Ethernet Switches (L2)
*   **Sodola KT-NOS SL-SWTGW2C8F**
*   **Bitengine SW08XM**

### 1 Gb Ethernet Switches (L2)
*   **TP-Link SG3428X**
*   **Netgear GS108Ev4**
*   **Netgear GS105** (Unmanaged)
