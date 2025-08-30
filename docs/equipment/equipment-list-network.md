# Network Equipment

*   **Access Switch:** Bitengine SW08XM 8 port 10Gb Ethernet Managed Switch
*   **Access Switch:** Netgear GS108Ev4 8 port 1Gb Ethernet Managed Switch
*   **Core Switch:** Cisco NEXUS 9236c 36 port 100Gb Ethernet Managed Switch
*   **Distribution Switch:** Sodola KT-NOS SL-SWTGW2C8F 8 port 10Gb Ethernet Managed Switch
*   **Firewall:** Protectli FW4B (opnsense-fw.bjoin.studio) - 4 x 1Gb Ethernet ports
*   **ISP Modem:** (Unknown brand)
*   **Managed PoE Switch:** TP-Link TL-SG2428P (Jetstream 24 Port Gigabit Smart Managed PoE Switch) - 24 PoE+ Ports @250W, 4 SFP Slots
*   **Unmanaged Switch:** Netgear GS105 5 port 1Gb Ethernet Unmanaged Switch

## Proposed Usage

Based on an optimized network strategy, here's the proposed role for each piece of equipment:

*   **Cisco NEXUS 9236C (Core Switch):**
    *   **Role:** The central, high-bandwidth backbone of the network.
    *   **Usage:** All high-speed inter-switch links (especially 10Gb and higher) terminate here. Connect the TP-Link TL-SG2428P via 4x10Gb breakout to a 100Gb port. Dedicated 10Gb devices (servers, storage) can connect directly.

*   **TP-Link TL-SG2428P (Managed PoE Switch):**
    *   **Role:** Primary access and distribution switch, handling most client connections, PoE, and aggregating traffic to the core.
    *   **Usage:**
        *   **Uplink:** 4x10Gb SFP+ to the Nexus (using breakout cables).
        *   **Firewall:** Connect one 1Gb port from the Protectli FW4B (OPNsense) for centralized VLAN routing.
        *   **Access Ports:** Utilize its 24 PoE+ Gigabit ports for Wireless Access Points (WAPs), IP Cameras, VoIP Phones, and standard workstations.
        *   **Downlink:** Connect the Netgear GS108Ev4 for additional 1Gb access.

*   **Sodola KT-NOS SL-SWTGW2C8F (Distribution Switch) & Bitengine SW08XM (Access Switch):**
    *   **Role:** Dedicated high-speed access switches for devices requiring native 10Gb connectivity.
    *   **Usage:**
        *   **Uplink:** 10Gb link to the Nexus (or to the TP-Link if inter-switch 10Gb is preferred).
        *   **Access Ports:** Connect servers, NAS, or high-performance workstations that need 10Gb speeds.

*   **Netgear GS108Ev4 (Access Switch):**
    *   **Role:** Extends 1Gb access from the TP-Link.
    *   **Usage:** Connects to a Gigabit port on the TP-Link. Provides additional 1Gb access ports for standard devices not requiring PoE.

*   **Protectli FW4B (Firewall):**
    *   **Role:** Network firewall and router.
    *   **Usage:** Connects to the TP-Link TL-SG2428P to provide routing, security, and internet access for all VLANs.

*   **Netgear GS105 (Unmanaged Switch):**
    *   **Role:** To be minimized or phased out in a managed network.
    *   **Usage:** Only for isolated, non-critical devices in segments where management is not required. Consider replacing with a managed switch for better control and visibility.

*   **ISP Modem:**
    *   **Role:** Provides internet connectivity.
    *   **Usage:** Connects to the WAN port of the Protectli FW4B (OPNsense).