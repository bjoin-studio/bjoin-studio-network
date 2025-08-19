# Network Design Considerations for bjoin.studio

This document summarizes key insights and considerations regarding the bjoin.studio network architecture, particularly concerning performance optimization and hardware capabilities.

## 1. Inter-VLAN Routing Bottleneck with Protectli Firewall

**Insight:** The Protectli firewall, while capable, is equipped with 1Gbps Ethernet ports. When used as the central "router-on-a-stick" for inter-VLAN routing, this creates a significant bottleneck.

**Hardware Detail:** The Protectli Vault features **4x 1Gbps RJ45 Ethernet ports** (LAN, WAN, OPT1, OPT2). Its primary capability is firewalling and routing, with its overall throughput limited by these 1Gbps interfaces.

**Implication:** All traffic passing between different VLANs (e.g., from the Studio VLAN to the Production VLAN) will be limited to a maximum throughput of 1Gbps, regardless of the 10Gbps and 100Gbps capabilities of the connected switches (Sodola, BitEngine, Cisco Nexus).

**Considerations:**
*   If high-speed inter-VLAN communication is critical (e.g., for large file transfers between different network segments), this 1Gbps limitation will impact performance.
*   For true high-speed inter-VLAN routing, a firewall/router with 10Gbps or higher interfaces would be required.
*   Alternatively, inter-VLAN routing could be offloaded to a Layer 3 switch like the Cisco Nexus 9236C, which has 100Gbps capabilities. This would involve configuring VLAN interfaces and routing on the Nexus.

## 2. Maximizing Intra-VLAN Speed

**Insight:** While inter-VLAN routing may be limited by the firewall, communication *within* the same VLAN can achieve the maximum speed of the connected switch.

**Implication:** To maximize speed for devices that frequently communicate within their own VLAN:
*   Connect 10Gbps devices (e.g., render nodes, file servers) to 10Gbps switches like the Sodola or BitEngine.
*   Connect 100Gbps devices (e.g., SAN/NAS systems) to the Cisco Nexus 9236C.

## 3. Hierarchical Network Design

**Insight:** The current hardware inventory supports a robust hierarchical network design (Core, Distribution, Access layers).

**Roles of Key Devices:**

*   **Cisco Nexus 9236C (100Gb):**
    *   **Role:** Ideal for the **Core Layer**, providing a high-speed backbone and central routing point.
    *   **Ports:** Features **36x 100Gbps QSFP28 ports**.
    *   **Capabilities:** Designed for extremely high throughput and low latency, with a backplane capacity capable of handling line-rate traffic across all ports simultaneously. Supports advanced Layer 3 routing.

*   **Sodola KT-NOS SL-SWTGW2C8F (10Gb):**
    *   **Role:** Suitable for the **Distribution Layer**, connecting the core/firewall to access switches and providing 10Gb connectivity.
    *   **Ports:** Equipped with **8x 10Gbps SFP+ ports**.
    *   **Capabilities:** Offers wire-speed switching for 10Gbps traffic, making it suitable for aggregating high-bandwidth access devices or connecting to a core switch.

*   **BitEngine SW08XM (10Gb):**
    *   **Role:** Functions as an **Aggregation/Access Layer** switch, providing 10Gb access for high-bandwidth devices.
    *   **Ports:** Features **8x 10Gbps RJ45 ports**.
    *   **Capabilities:** Provides high-speed copper connectivity for 10Gbps devices, with a switching capacity designed for line-rate performance across its ports.

*   **Netgear GS108Ev4 (1Gb Managed):**
    *   **Role:** Acts as a **Managed Access Layer** switch, providing 1Gb access for general devices and extending VLANs to unmanaged switches.
    *   **Ports:** Has **8x 1Gbps RJ45 ports**.
    *   **Capabilities:** Offers basic Layer 2 switching with VLAN support, suitable for connecting standard 1Gbps workstations and peripherals.

*   **Netgear GS105 (1Gb Unmanaged):**
    *   **Role:** Serves as a basic **Access Layer** extension, suitable for single-VLAN device connections.
    *   **Ports:** Features **5x 1Gbps RJ45 ports**.
    *   **Capabilities:** Simple plug-and-play 1Gbps switching, without any management or VLAN capabilities.

**Recommendation:** Adhering to this hierarchical structure helps in managing network complexity, optimizing traffic flow, and simplifying troubleshooting.