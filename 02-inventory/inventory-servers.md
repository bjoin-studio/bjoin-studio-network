# Server Inventory


## Storage Equipment

*   **NAS:** [QNAP TS-h1290FX](https://www.qnap.com/en-us/product/ts-h1290fx) NVMe NAS (qnap.bjoin.studio) - [ConnectX-6](https://www.nvidia.com/en-us/networking/ethernet-adapters/connectx-6-dx/) - 2x 100Gb Ethernet Ports
    *   [Manual](https://docs.qnap.com/operating-system/quts-hero/5.0.x/en-us/)

## Workstations


- [**Apple Mac Pro Workstation**](servers/apple-mac-pro-6-1.md)
- [**HP Z620 Workstation**](servers/hp-z620.md)

*   **SuperMicro Workstation:** (jupiter.bjoin.studio) - [ConnectX-6](https://www.nvidia.com/en-us/networking/ethernet-adapters/connectx-6-dx/) - 2x 100Gb Ethernet Ports
*   **Mac Studio M3 Ultra:** (mercury.bjoin.studio) - Thunderbolt to Intel dual 25Gb Ethernet Ports

## General Equipment

*   **iMac 27":** (venus.bjoin.studio) - 2x 1Gb Ethernet Ports
*   **iMac Pro:** (mars.bjoin.studio) - 10Gb Ethernet Port
*   **Mac Pro 6,1:** (pmx-01.bjoin.studio) (Proxmox 9 / FreeIPA VM)

*   **Firewall:** HP Z620 Workstation (opnsense-vm-1.bjoin.studio)
    *   1x Intel 82574L (onboard) - used by host
    *   1x Intel 82579LM (onboard) - used by host
    *   1x 10Gb Solarflare SFC9020 - opnsense LAN 10.20.51.1
    *   1x Intel 4-Port 82571EB/82571GB - opnsense WAN (to intenet)


## 100 Gb Ethernet

- [**MikroTik CRS520-4XS-16XQ-RM**](https://mikrotik.com/product/crs520_4xs_16xq_rm)  
Layer 2 / Layer 3 Managed Ethernet Switch  
   - 16x 100Gb (QSFP)  
   - 4x 25Gb (SFP28)  
   - 2x 1Gb (RJ45)  
   - 1x Console (RJ45)  
   - [Manual](https://help.mikrotik.com/docs/display/UM/CRS520-4XS-16XQ-RM)

