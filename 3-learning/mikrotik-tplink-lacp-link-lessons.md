# Key Learnings: LACP LAG between MikroTik and TP-Link Switches

This document captures the key lessons and troubleshooting steps involved in successfully establishing a 40Gbps LACP aggregated link between a MikroTik CRS520 core switch and a TP-Link SG3428X switch.

## 1. The Root Cause: L3 Ambiguity and IP Conflicts

The most critical issue encountered was a Layer 3 configuration conflict on the MikroTik router. The router had two separate interfaces (a bridge and a VLAN interface) with IP addresses in the same subnet.

*   **Problem:** A router cannot have two interfaces connected to the same IP subnet. It creates ambiguity, causing the routing table to have two equal-cost routes to the same destination. This leads to unpredictable behavior, including failed ARP requests and pings.
*   **Lesson:** Always ensure that every IP subnet on a router is reachable through only one interface.

## 2. Best Practice: Dedicated Point-to-Point Links

The definitive solution to the L3 conflict was to treat the link between the two switches as a dedicated point-to-point network.

*   **Solution:** A new, dedicated VLAN (e.g., VLAN 4090) and a small, dedicated subnet (e.g., a `/30` subnet like `10.254.254.0/30`) were created exclusively for this link.
*   **Lesson:** For routed links between core network devices, use a dedicated "transit" VLAN and subnet. This isolates the link from other networks (like the main management network) and provides clarity, stability, and security.

## 3. L3 Interfaces on VLANs (SVIs)

On both the MikroTik and TP-Link switches, IP addresses could not be assigned directly to the LAG (bond) interface for a tagged link.

*   **Procedure:** The correct method is to create a Switched Virtual Interface (SVI), more commonly known as a "VLAN Interface".
    1.  Create the VLAN (e.g., VLAN 4090).
    2.  Create the LACP LAG.
    3.  Configure the LAG as a **Tagged** member of the new VLAN.
    4.  Create a virtual "VLAN Interface" for the new VLAN ID.
    5.  Assign the IP address to this virtual VLAN Interface.
*   **Lesson:** On L2+ or L3-Lite switches, routing is handled by VLAN interfaces, not by physical or LAG interfaces directly.

## 4. Detailed VLAN Port Configuration (TP-Link)

For a trunk link to function correctly, several specific L2 settings were required on the TP-Link LAG.

*   **Tagged Membership:** The LAG must be a **`Tagged`** member of the desired VLAN (e.g., VLAN 4090). It should not be `Untagged`.
*   **VLAN 1 Membership:** The LAG should be removed as a member of the default VLAN (VLAN 1). A trunk port should only be a member of the VLANs it is explicitly configured to carry.
*   **PVID (Port VLAN ID):** The PVID of the LAG should be set to `1` (or another unused, non-trunked VLAN). The PVID dictates which VLAN untagged traffic belongs to. Since all traffic on our trunk is tagged, this setting prevents untagged traffic from being accidentally assigned to our point-to-point VLAN.

## 5. MikroTik Bond Link Monitoring

The default `link-monitoring=mii` setting on a MikroTik bond can be misleading.

*   **Problem:** `mii` mode only checks for a physical carrier signal. It will report the bond as "RUNNING" even if the LACP negotiation has failed, as long as the cables are plugged in.
*   **Better Options:**
    *   `link-monitoring=mii,lacp`: This is the ideal setting, as it monitors both the physical link and the LACP negotiation status. However, it was not supported by the RouterOS version on the device.
    *   `link-monitoring=arp`: This was the chosen solution. It provides reliable L3 monitoring by sending ARP requests to a specified target IP on the other side of the link.
*   **Lesson:** Use the most specific link monitoring available. For L3 links, `arp` monitoring is a robust alternative when `lacp` monitoring is not available.

## 6. Physical Layer: Breakout Cable Types

An initial point of confusion was the type of breakout cable being used.

*   **DAC (Direct Attach Copper):** These are copper cables with integrated transceivers. The correct MikroTik interface setting is `10G-baseCR`.
*   **AOC (Active Optical Cable):** These are fiber optic cables with integrated transceivers. The correct MikroTik interface setting is `10G-baseSR/LR`.
*   **Lesson:** Always verify the exact type of cable (DAC or AOC) to ensure the correct physical layer settings are applied on the switch interface.
