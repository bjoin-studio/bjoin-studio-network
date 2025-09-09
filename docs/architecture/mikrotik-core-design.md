# Alternative Network Design: MikroTik Core

This document outlines an alternative network design for the bjoin.studio network, proposing the MikroTik CRS504-4XQ-IN as the core switch.

## Proposed Hierarchy

*   **Core Switch:** MikroTik CRS504-4XQ-IN
*   **Distribution Switch:** TP-Link TL-SG3428X
*   **Access Switch:** Sodola KT-NOS SL-SWTGW2C8F (for 10Gb devices)
*   **Access Switch:** Netgear GS108Ev4 (for 1Gb devices)
*   **Firewall/Router:** Protectli FW4B (OPNsense)

## Rationale

This design aims to leverage the MikroTik CRS504-4XQ-IN's 100Gb capabilities in a more compact and potentially quieter form factor, while still maintaining a robust hierarchical network structure.

## Component Roles and Connectivity

### Core Switch: MikroTik CRS504-4XQ-IN

*   **Role:** The central, high-bandwidth backbone of the network.
*   **Connectivity:**
    *   Connects to the TP-Link TL-SG3428X (Distribution Switch) via 10Gb or 25Gb links.
    *   Connects to other high-bandwidth devices or external links as needed.

### Distribution Switch: TP-Link TL-SG3428X

*   **Role:** Aggregates traffic from access layer switches and provides L3 routing between VLANs.
*   **Connectivity:**
    *   **Uplink:** Connects to the MikroTik CRS504-4XQ-IN (Core Switch) via its 10GE SFP+ slots.
    *   **Downlink:** Connects to access switches (Sodola, Netgear GS108Ev4) and directly connected 1Gb devices.
    *   **Firewall:** Connects to the Protectli FW4B (OPNsense) for centralized VLAN routing and internet access.

### Access Switch: Sodola KT-NOS SL-SWTGW2C8F

*   **Role:** Provides dedicated 10Gb access for high-bandwidth devices.
*   **Connectivity:**
    *   **Uplink:** Connects to the TP-Link TL-SG3428X (Distribution Switch) via 10Gb links.
    *   **Downlink:** Connects to 10Gb servers, NAS, and high-performance workstations.

### Access Switch: Netgear GS108Ev4

*   **Role:** Provides 1Gb access for standard devices.
*   **Connectivity:**
    *   **Uplink:** Connects to the TP-Link TL-SG3428X (Distribution Switch) via 1Gb links.
    *   **Downlink:** Connects to standard workstations, IP phones, WAPs, etc.

### Firewall/Router: Protectli FW4B (OPNsense)

*   **Role:** Network firewall, router, and internet gateway.
*   **Connectivity:**
    *   **WAN:** Connects to the ISP Modem.
    *   **LAN:** Connects to the TP-Link TL-SG3428X (Distribution Switch) for centralized VLAN routing and security.

## Detailed Physical Connectivity

This section outlines the specific port-level connections and bonding configurations for the proposed design.

*   **Internet to Protectli (OPNsense):**
    *   ISP Modem (WAN) to Protectli FW4B (OPNsense) 1Gb WAN port.
*   **Protectli (OPNsense) to TP-Link SG3428X:**
    *   Protectli FW4B (OPNsense) 1Gb LAN port to TP-Link SG3428X Port 24 (TRUNK - all VLANs).
*   **TP-Link SG3428X to MikroTik CRS504-4XQ-IN (Core Uplink):**
    *   TP-Link SG3428X Ports 25-28 (4x10Gb SFP+) bonded (LAG) to MikroTik CRS504-4XQ-IN Port 1 (100Gb QSFP28, configured for 40Gb or 4x10Gb breakout) (TRUNK - all VLANs).
*   **MikroTik CRS504-4XQ-IN to Sodola KT-NOS SL-SWTGW2C8F (10Gb Access Uplink):**
    *   MikroTik CRS504-4XQ-IN Port 2 (100Gb QSFP28, configured for 40Gb or 4x10Gb breakout) to Sodola KT-NOS SL-SWTGW2C8F Ports 1-4 (10Gb, bonded) (TRUNK - all VLANs).
*   **MikroTik CRS504-4XQ-IN to QNAP TS-h1290FX NVMe NAS:**
    *   MikroTik CRS504-4XQ-IN Port 3 (100Gb QSFP28) to QNAP TS-h1290FX NVMe NAS Port 1 (100Gb) (TRUNK - all VLANs).
*   **MikroTik CRS504-4XQ-IN to Linux Connect-X6 Server:**
    *   MikroTik CRS504-4XQ-IN Port 4 (100Gb QSFP28) to Linux Connect-X6 Server Port 1 (e.g., 100Gb) (TRUNK - all VLANs).
*   **Sodola KT-NOS SL-SWTGW2C8F to BitEngine SW08XM (Inter-Access Link):**
    *   Sodola KT-NOS SL-SWTGW2C8F Ports 5-6 (10Gb) bonded (LAG) to BitEngine SW08XM Ports 5-6 (10Gb) (TRUNK - all VLANs).

**Remaining Ports for Expansion:**
*   **Sodola KT-NOS SL-SWTGW2C8F:** 2 x 10Gb SFP+ ports left (ports 7-8).
*   **BitEngine SW08XM:** 6 x 10Gb RJ45 ports left.
