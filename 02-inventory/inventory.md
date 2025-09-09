# Equipment List

This document lists the network, storage, and computer equipment used in the bjoin.studio network.

## Network Equipment

*   **ISP Modem:** (Unknown brand)
*   **Firewall:** [Protectli FW4B](https://protectli.com/vault-fw4b/) (opnsense-fw.bjoin.studio) - 4 x 1Gb Ethernet ports
    *   [Manual](https://protectli.com/kb/protectli-vault-fw4b-manual/)
*   **Firewall:** HP Z620 Workstation (opnsense-fw-hpz620-1)
    *   1x 10Gb Solarflare SFC9020
    *   1x Intel 4-Port 82571EB/82571GB
    *   1x Intel 82579LM (onboard)
    *   1x Intel 82574L (onboard)
*   **Distribution Switch:** [TP-Link SG3428X](https://www.tp-link.com/us/business-networking/omada-sdn-switch/sg3428x/) 24-Port Gigabit L2+ Managed Switch with 4 10GE SFP+ Slots
    *   [Data Sheet](https://static.tp-link.com/upload/product-overview/2021/202103/20210311/JetStream%20L2+%20Managed%20Switches%20Datasheet.pdf)
*   **Core Switch:** [Cisco NEXUS 9236c](https://www.cisco.com/c/en/us/products/switches/nexus-9236c-switch/index.html) 36 port 100Gb Ethernet Managed Switch
    *   [Data Sheet](https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-switches/datasheet-c78-735989.html)
*   **Core Switch:** [MikroTik CRS520-4XS-16XQ-RM](https://mikrotik.com/product/crs520_4xs_16xq_rm) 16x 100Gb, 4x 25Gb, 2x 10Gb Ethernet Switch
    *   [Manual](https://help.mikrotik.com/docs/display/UM/CRS520-4XS-16XQ-RM)
*   **Core Switch:** [MikroTik CRS504-4XQ-IN](https://mikrotik.com/product/crs504_4xq_in) 4x 100Gb Ethernet Switch
    *   [Manual](https://help.mikrotik.com/docs/display/UM/CRS504-4XQ-IN)
*   **Access Switch:** [Sodola KT-NOS SL-SWTGW2C8F](https://sodola-network.com/products/10g-sfp-switch-8-port-10g-sfp-unmanaged-switch-10g-ethernet-switch-with-2-port-10g-rj45-10g-fiber-switch-plug-play-fanless-metal-vlan-qos) 8 port 10Gb Ethernet Managed Switch
    *   [Manual](https://sodola-network.com/pages/download)
*   **Access Switch:** Bitengine SW08XM 8 port 1Gb Ethernet Managed Switch
*   **Access Switch:** [Netgear GS108Ev4](https://www.netgear.com/business/wired/switches/plus/gs108e/) 8 port 1Gb Ethernet Managed Switch
    *   [Data Sheet](https://www.netgear.com/media/GS108Ev3_tcm148-69377.pdf)
*   **Unmanaged Switch:** [Netgear GS105](https://www.netgear.com/home/wired/switches/unmanaged/gs105/) 5 port 1Gb Ethernet Unmanaged Switch
    *   [Data Sheet](https://www.netgear.com/media/GS105_108_116_DS_tcm148-69371.pdf)

## Storage Equipment

*   **NAS:** [QNAP TS-h1290FX](https://www.qnap.com/en-us/product/ts-h1290fx) NVMe NAS (qnap.bjoin.studio) - [ConnectX-6](https://www.nvidia.com/en-us/networking/ethernet-adapters/connectx-6-dx/) - 2x 100Gb Ethernet Ports
    *   [Manual](https://docs.qnap.com/operating-system/quts-hero/5.0.x/en-us/)

## Workstation Equipment

*   **SuperMicro Workstation:** (jupiter.bjoin.studio) - [ConnectX-6](https://www.nvidia.com/en-us/networking/ethernet-adapters/connectx-6-dx/) - 2x 100Gb Ethernet Ports
*   **Mac Studio M3 Ultra:** (mercury.bjoin.studio) - Thunderbolt to Intel dual 25Gb Ethernet Ports

## General Equipment

*   **iMac 27":** (venus.bjoin.studio) - 2x 1Gb Ethernet Ports
*   **iMac Pro:** (mars.bjoin.studio) - 10Gb Ethernet Port
*   **Mac Pro 6,1:** (pmx-01.bjoin.studio) (Proxmox 9 / FreeIPA VM)
