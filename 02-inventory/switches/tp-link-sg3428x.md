# TP-Link SG3428X

## Description
Layer 2+ Managed Ethernet Switch  
Enterprise-grade switch with 10Gb uplinks and Omada SDN integration.

- **System Details**
    - <details>
        <summary>Hardware Inventory</summary>

        <details>
        <summary>Ports</summary>

            - 24x 1Gb RJ45  
            - 4x 10Gb SFP+  
            - 1x RJ45 Console  
            - 1x Micro-USB Console

        </details>

        <details>
        <summary>CPU & Memory</summary>

            - 256MB DRAM  
            - 32MB Flash

        </details>

        <details>
        <summary>Power</summary>

            - 100–240V AC, 50/60Hz  
            - Max consumption: 23.6W  
            - Fanless design

        </details>

        <details>
        <summary>Operating System</summary>

            - Omada SDN / Web CLI / SNMP / RMON  
            - Supports VLAN, ACL, QoS, IGMP Snooping, Static Routing

        </details>

        <details>
        <summary>Data Sheet</summary>

            - [TP-Link SG3428X Datasheet](https://static.tp-link.com/upload/product-overview/2021/202103/20210311/JetStream%20L2+%20Managed%20Switches%20Datasheet.pdf)

        </details>

    </details>

## Role
- **Access Switch**
    - <details>
        <summary>Functions</summary>

        - Aggregates 1Gb endpoints  
        - Uplinks to 10Gb core switches  
        - VLAN segmentation and QoS for edge devices

        </details>
    </details>

## Identification

| Hostname(s)               | IP Address(es)   | VLAN  | Cable ID   |
|---------------------------|------------------|-------|------------|
| `tplink-sg3428x.bjoin.studio` | `10.20.51.30` | `51`  | `----/----` |

## Port Map – TP-Link SG3428X

| Port | Connected Device         | VLAN | Mode   | Notes                      |
|------|--------------------------|------|--------|----------------------------|
| 1    | HP Z620 Workstation      | 51   | Access | Proxmox Host               |
| 2    | FreeIPA Server           | 51   | Access | Identity/DNS               |
| 3    | TrueNAS Storage          | 51   | Access | ZFS over NFS               |
| 4    | Sodola 10Gb Switch (Uplink) | 51 | Trunk  | VLAN trunk to 10Gb switch |
| 5–24 | Open                     | —    | Access | Available for endpoints    |
| SFP1 | CRS504 Aggregation       | 51   | Trunk  | 10Gb uplink                |
| SFP2 | Cisco Nexus 9236C        | 51   | Trunk  | 10Gb uplink                |
| SFP3 | Open                     | —    | —      |                            |
| SFP4 | Open                     | —    | —      |                            |
