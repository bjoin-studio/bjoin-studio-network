# Network Topology and Physical Cabling Guide (Revised)

This document provides a step-by-step guide for physically connecting the network hardware for the bjoin.studio project. This revised guide reflects connecting the firewall directly to the Sodola switch.

## High-Level Topology Flow

The network follows a layered approach, starting from the internet and moving inwards to the distribution and access layers.

```
[Internet] -> [Netgear 6220 (ISP Router)] -> [Protectli FW4B (Firewall)] -> [Sodola 8-Port 10G (Distribution Switch)] -> [Other Switches] -> [End Devices]
```

---

## Step-by-Step Cabling Instructions

Follow these connections in order.

### 1. Internet to Firewall

This connection provides the internet uplink to your entire network.

| Source Device  | Source Port  | Destination Device | Destination Port | Cable Type | Purpose      |
|:---------------|:-------------|:-------------------|:-----------------|:-----------|:-------------|
| Netgear 6220   | Any LAN Port | Protectli FW4B     | WAN Port         | Ethernet   | WAN Uplink   |

---

### 2. Firewall to Distribution Switch (Sodola)

This is the most critical link in your network. It carries all tagged VLAN traffic from your firewall to the rest of the network.

| Source Device  | Source Port | Destination Device | Destination Port | Cable Type | Purpose         |
|:---------------|:------------|:-------------------|:-----------------|:-----------|:----------------|
| Protectli FW4B | LAN Port    | Sodola 8-Port 10G  | Port 5           | Ethernet   | Main VLAN Trunk |

---

### 3. Distribution Switch (Sodola) to Other Switches

These connections distribute the VLANs from your main distribution switch (Sodola) to the other switches. These are all **trunk links**.

| Source Device     | Source Port                    | Destination Device | Destination Port           | Cable Type / Required Adapter      |
|:------------------|:-------------------------------|:-------------------|:---------------------------|:-----------------------------------|
| Sodola 8-Port 10G | Port 2 (with RJ45 Transceiver) | BitEngine SW08XM   | Port 1 (10G)               | Ethernet                           |
| Sodola 8-Port 10G | Port 3 (SFP+)                  | Cisco Nexus 9236C  | Any Port                   | SFP+ to QSFP28 Adapter/Cable       |
| Sodola 8-Port 10G | Port 8                         | Netgear GS108Ev4   | Port 1 (1G)                | Ethernet                           |

---

### 4. Connecting Unmanaged Switches

Your unmanaged switches (like the **Netgear ProSafe GS105**) cannot understand VLAN tags. Therefore, they must be connected to **ACCESS ports** on a managed switch, not trunk ports.

**Example:** To use the Netgear GS105 for devices in the "Production - General" VLAN (VLAN 11):

1.  Configure a spare port on the **Netgear GS108Ev4** as an **ACCESS port** for VLAN 11.
2.  Connect the Netgear GS105 to this port.
3.  Any device you plug into the GS105 will now be in VLAN 11.

---

### 5. Connecting End Devices

Connect servers, workstations, and other devices to the appropriate access switches based on the VLAN they need to be in. For example:

*   A **10G Render Node** would connect to a 10G port on the **BitEngine SW08XM** or **Sodola 10G**, with the port configured as an ACCESS port for the "Production - High-performance" VLAN (VLAN 12).
*   A **100G Media Server** would connect to a 100G port on the **Cisco Nexus 9236C**, with the port configured as an ACCESS port for the "Studio - Ultra-high bandwidth" VLAN (VLAN 33).
*   A standard **Office Workstation** would connect to a 1G port on the **Netgear GS108Ev4**, with the port configured as an ACCESS port for the "Production - General" VLAN (VLAN 11).

