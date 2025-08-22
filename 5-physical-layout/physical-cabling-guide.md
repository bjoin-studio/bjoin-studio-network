# Network Topology and Physical Cabling Guide

This document provides a step-by-step guide for physically connecting the network hardware for the bjoin.studio project.

## High-Level Topology Flow

The network follows a layered approach, starting from the internet and moving inwards to the distribution and access layers.

```
[Internet] -> [ISP Modem] -> [Protectli FW4B (Firewall)] -> [Sodola 8-Port 10G (Distribution Switch)] -> [Cisco/BitEngine/Netgear Switches] -> [End Devices]
```

---

## Step-by-Step Cabling Instructions

Follow these connections in order.

### 1. Internet to Firewall

This connection provides the internet uplink to your entire network.

| Source Device  | Source Port  | Destination Device | Destination Port | Cable Type | Purpose      |
|:---------------|:-------------|:-------------------|:-----------------|:-----------|:-------------|
| ISP Modem      | Any LAN Port | Protectli FW4B     | WAN Port         | Ethernet   | WAN Uplink   |

---

### 2. Firewall to Distribution Switch (Sodola)

This is the most critical link in your network. It carries all tagged VLAN traffic from your firewall to the rest of the network.

| Source Device  | Source Port | Destination Device | Destination Port               | Cable Type | Purpose         |
|:---------------|:------------|:-------------------|:-------------------------------|:-----------|:----------------|
| Protectli FW4B | LAN Port    | Sodola 8-Port 10G  | Port 8 (with RJ45 Transceiver) | Ethernet   | Main VLAN Trunk |

---

### 3. Distribution Switch (Sodola) to Core Switch (Cisco)

This is a high-speed LAG trunk that connects your distribution switch to your core switch.

| Source Device     | Source Port(s) | Destination Device | Destination Port(s) | Cable Type / Required Adapter      |
|:------------------|:---------------|:-------------------|:--------------------|:-----------------------------------|
| Sodola 8-Port 10G | Ports 1-4 (LAG)| Cisco Nexus 9236C  | Port 1              | SFP+ to QSFP28 Adapter/Cable       |

---

### 4. Distribution Switch (Sodola) to Access Switches

These connections distribute the VLANs from your main distribution switch (Sodola) to the other access switches.

| Source Device     | Source Port                    | Destination Device | Destination Port           | Cable Type / Required Adapter      |
|:------------------|:-------------------------------|:-------------------|:---------------------------|:-----------------------------------|
| Sodola 8-Port 10G | Port 7 (with SFP+ Transceiver) | Netgear GS108Ev4   | Port 8 (Trunk)             | Ethernet                           |

---

### 5. Connecting the Proxmox Host

This connection provides management access to the Proxmox host.

| Source Device     | Source Port     | Destination Device | Destination Port(s) | Cable Type | Purpose            |
|:------------------|:----------------|:-------------------|:--------------------|:-----------|:-------------------|
| Sodola 8-Port 10G | Port 5 (Access) | Mac Pro 6,1        | 1Gb Ethernet Port   | Ethernet   | Management Access  |

---

### 6. Connecting the QNAP NAS

This is a high-speed LAG connection for the QNAP NAS.

| Source Device     | Source Port(s) | Destination Device | Destination Port(s) | Cable Type | Purpose         |
|:------------------|:---------------|:-------------------|:--------------------|:-----------|:----------------|
| Cisco Nexus 9236C | Ports 3-4 (LAG)| QNAP TS-h1290FX    | Ports 1-2 (LAG)     | Ethernet   | High-Speed Access |

---

### 7. Connecting Unmanaged Switches

Your unmanaged switches (like the **Netgear ProSafe GS105**) cannot understand VLAN tags. Therefore, they must be connected to **ACCESS ports** on a managed switch, not trunk ports.

| Source Device    | Source Port     | Destination Device | Destination Port | Cable Type | Purpose            |
|:-----------------|:----------------|:-------------------|:-----------------|:-----------|:-------------------|
| Netgear GS108Ev4 | Port 5 (Access) | Netgear GS105      | Port 5           | Ethernet   | VLAN 51 Extension  |

---

### 8. Connecting End Devices

Connect servers, workstations, and other devices to the appropriate access switches based on the VLAN they need to be in.