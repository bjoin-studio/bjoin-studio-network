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

---

## 4. Extending a VLAN Across a Routed Trunk Link

To provide access to a specific Layer 2 network (e.g., the Management Network, VLAN 51) from an access port on a different switch, the VLAN must be extended across the main trunk link.

### Scenario

A device plugged into an access port on the TP-Link SG3428X needed to reach the MikroTik's primary management IP (`10.20.51.14`), which lives on the core management bridge.

### Logical Flow

`[Device on TP-Link Port] <> [Access Port (Untagged VLAN 51)] <> [TP-Link Switch Logic] <> [Trunk Port LAG1 (Tagged VLAN 51)] <> [40G Link] <> [MikroTik Trunk Port (Tagged VLAN 51)] <> [MikroTik Bridge] <> [MikroTik Management IP]`

### Configuration Method

This was achieved by configuring both switches to pass VLAN 51 traffic over the 40Gbps LACP trunk.

#### On the "Access" Switch (TP-Link)

1.  **Ensure VLAN Exists:** The target VLAN (51) must be created.
2.  **Configure Trunk Port:** The trunk interface (`LAG1`) must be set as a **`Tagged`** member of the VLAN.
3.  **Configure Access Port:** The desired user-facing port (e.g., Port 1) must be set as an **`Untagged`** member of the VLAN.
4.  **Set Access Port PVID:** The access port's PVID must be set to the VLAN ID (51) to ensure incoming untagged traffic is correctly placed into that VLAN.

#### On the "Core" Switch (MikroTik)

1.  **Create VLAN Interface on Trunk:** A new virtual VLAN interface (e.g., `VLAN51-on-Trunk`) is created on the bond/LAG interface for the target VLAN ID.
2.  **Bridge the VLAN Interface:** This new VLAN interface is then added as a port to the main destination `bridge` that holds the target Layer 2 network.

This is the standard methodology for extending a Layer 2 segment across a routed network core.
