# Apple Mac Pro 6,1 Workstation

## Description
High-performance single-socket workstation

- **System Details**
    - <details>
        <summary>Hardware Inventory</summary>
        <details>
        <summary>CPU</summary>

            1 x Intel XEON E5-2697v2 12-Core

        </details>
        <details>
        <summary>RAM</summary>

            64GB DDR3 ECC Registered

        </details>

        <details>
        <summary>Network Interfaces</summary>

            - 1x Intel 82574L (onboard) - Proxmox Host Connection
            - 1x Intel 82579LM (onboard) - Proxmox Host Management
            - 1x Intel 4-Port 82571EB/82571GB — OPNsense VM [WAN]  
            - 1x 10Gb Solarflare SFC9020 — OPNsense VM [LAN] (VLAN Trunk & Firewall)

        </details>

        <details>
        <summary>Storage</summary>

            - 1x 1TB SSD – Boot  
            - 2x 2TB USB SSD (ZFS MIRROR)
            - 2x 2TB USB SSD (ZFS MIRROR)

        </details>

        <details>
        <summary>Power</summary>

            - 1x 650W

        </details>
    </details>

## Role
- **Virtualization Host**
    - <details>
        <summary>Hypervisor</summary>

        - ProxmoxPVE 9  

        </details>
    </details>

- **Virtualized Roles**
    - <details>
        <summary>Identity, Policy and Audit Server</summary>

        - FreeIPA VM  

        </details>
    </details>

## Identification

|  Hostname(s)                           |  IP Address(es)   |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| `proxmox-42.bjoin.studio`              |   `10.20.51.42`   |  `51`  | `----/----` |
| `ipa-vm-01.bjoin.studio`               |   `10.20.51.61`   |  `51`  | `----/----` |
