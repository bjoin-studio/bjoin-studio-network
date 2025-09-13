# MikroTik CRS520-4XS-16XQ-RM

## Table of Contents

- [Back to Inventory File](../inventory.md)

## Description
Layer 2 / Layer 3 Managed Ethernet Switch  
High-performance enterprise switch with advanced routing capabilities and hardware offloading.

- **System Details**
    - <details>
        <summary>Hardware Inventory</summary>

        <details>
        <summary>Ports</summary>

            - 16x 100Gb QSFP28  
            - 4x 25Gb SFP28  
            - 2x 1Gb RJ45 Ethernet  
            - 1x RJ45 Console

        </details>

        <details>
        <summary>CPU</summary>

            - Quad-core ARM AL52400 @ 2GHz

        </details>

        <details>
        <summary>RAM</summary>

            - 4GB DDR4

        </details>

        <details>
        <summary>Storage</summary>

            - 128MB NAND

        </details>

        <details>
        <summary>Power</summary>

            - Dual hot-swappable AC inputs  
            - Max consumption: 183W  
            - 4x hot-swappable fans

        </details>

        <details>
        <summary>Operating System</summary>

            - RouterOS v7 (License Level 5)

        </details>

        <details>
        <summary>Manual</summary>

            - [CRS520-4XS-16XQ-RM Manual](https://help.mikrotik.com/docs/display/UM/CRS520-4XS-16XQ-RM)

        </details>

    </details>

- [Back to Table of Contents](#table-of-contents)

---

## Role
- **Core Aggregation Switch**
    - <details>
        <summary>Functions</summary>

        - Aggregates high-speed uplinks from hypervisors and storage  
        - Handles Layer 3 routing with hardware offload  
        - Supports OSPF/BGP, ACLs, Jumbo frames, and VPNs

        </details>
    </details>

- [Back to Table of Contents](#table-of-contents)

---

## Identification
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| crs520-core.bjoin.studio               |    10.20.51.11    |   51   |  ----/----  |
| crs520-qsfp.bjoin.studio               |    10.20.51.21    |  4090  |  ----/----  |
```

- [Back to Table of Contents](#table-of-contents)

---
