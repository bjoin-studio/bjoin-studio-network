# Data Flow Diagrams

This document illustrates the data flow for several key scenarios on the bjoin.studio network.

## Scenario 1: High-Speed Storage Access

This scenario shows a SuperMicro Workstation accessing the QNAP NAS. Both devices are on high-speed ports on the Cisco Nexus 9236c switch.

```
+------------------------+
| SuperMicro Workstation |
| (jupiter.bjoin.studio) |
+-----------+------------+
            | 100GbE LAG
+-----------+------------+
|   Cisco NEXUS 9236c    |
| (L3 Routing Enabled)   |
+-----------+------------+
            | 100GbE LAG
+-----------+------------+
| QNAP TS-h1290FX        |
| (qnap.bjoin.studio)    |
+------------------------+
```

*   **Data Path:** The traffic flows directly from the workstation to the switch, is routed by the switch at high speed, and then sent directly to the NAS. The OPNsense firewall is not involved in this data path.

---

## Scenario 2: Internet Access from a Workstation

This scenario shows a user on an iMac accessing the internet.

```
+----------------------+
| iMac                 |
| (venus.bjoin.studio) |
+----------+-----------+
           | 1GbE
+----------+-----------+
| Netgear GS108Ev4     |
+----------+-----------+
           | 1GbE Trunk
+----------+-----------+
| Sodola KT-NOS        |
+----------+-----------+
           | 1GbE Trunk
+----------+-----------+
| OPNsense Firewall    |
+----------+-----------+
           | WAN
+----------+-----------+
| Internet             |
+----------------------+
```

*   **Data Path:** The traffic flows from the iMac to the Netgear switch, then to the Sodola switch, and finally to the OPNsense firewall. The firewall then performs NAT and sends the traffic to the internet.

---

## Scenario 3: Proxmox Host Management

This scenario shows an administrator accessing the Proxmox host's web interface.

```
+----------------------+
| Admin Workstation    |
| (VLAN 11)            |
+----------+-----------+
           | 1GbE
+----------+-----------+
| Access Switch        |
+----------+-----------+
           | Trunk
+----------+-----------+
| OPNsense Firewall    |
| (Routing between     |
|  VLAN 11 and VLAN 51)|
+----------+-----------+
           | Trunk
+----------+-----------+
| Sodola KT-NOS        |
+----------+-----------+
           | 1GbE Access Port (VLAN 51)
+----------+-----------+
| Proxmox Host         |
| (pmx-01.bjoin.studio)|
+----------------------+
```

*   **Data Path:** The administrator's traffic goes from their workstation to the firewall. The firewall then routes the traffic from the admin's VLAN to the Management VLAN (VLAN 51) and sends it to the Proxmox host via the Sodola switch.