# Overview bjoin.studio

## Table of Contents
1. [**Introduction**](#introduction)
2. [**HP Z620 Workstation**](#hp-z620-workstation)
3. [**Apple Mac Pro 6,1 Workstation**](#apple-mac-pro-61-workstation)
4. [**Protectli Vault FW4B**](#protectli-vault-fw4b)
5. [**QNAP TS-h1290FX**](#qnap-ts-h1290fx)
6. [**ASUSTOR Flashstor 12 Pro FS6712X**](#asustor-flashstor-12-pro-fs6712x)
7. [**MikroTik CRS520-4XS-16XQ-RM**](#mikrotik-crs520-4xs-16xq-rm)
8. [**MikroTik CRS504-4XQ-IN**](#mikrotik-crs504-4xq-in)
9. [**Cisco Nexus 9236C**](#cisco-nexus-9236c)
10. [**TP-Link SG3428X**](#tp-link-sg3428x)
11. [**Sodola KT-NOS SL-SWTGW2C8F**](#sodola-kt-nos-sl-swtgw2c8f)
12. [**Bitengine SW08XM**](#bitengine-sw08xm)
13. [**Netgear GS108Ev4**](#netgear-gs108ev4)
14. [**Netgear GS105**](#netgear-gs105)
15. [**Mac Studio M3 Ultra**](#mac-studio-m3-ultra)
16. [**MacBook Pro M1 (2020)**](#macbook-pro-m1-2020)
17. [**iMac Pro (2017)**](#imac-pro-2017)
18. [**iMac 5K (2017)**](#imac-5k-2017)


---

## Introduction

This document outlines the redesign of the bjoin.studio network, including the rationale, strategic goals, and implementation plan. It serves as a living reference that will evolve alongside the infrastructure.

[Back to Table of Contents](#table-of-contents)

---

## HP Z620 Workstation
```
| Hostname(s)                            |  IP Address(es)   |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| proxmox-61.bjoin.studio                |    10.20.51.61    |   51   |  ----/----  |
| opnsense-master.bjoin.studio           |    10.20.51.2     |   51   |  ----/----  |
```

## Apple Mac Pro 6,1 Workstation
```
| Hostname(s)                            |  IP Address(es)   |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| proxmox-62.bjoin.studio                |    10.20.51.62    |   51   |  ----/----  |
| ipa-vm-01.bjoin.studio                 |    10.20.51.81    |   51   |  ----/----  |
```

## Protectli Vault FW4B
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| opnsense-backup.bjoin.studio           |    10.20.51.3     |   51   |  ----/----  |
```

[Back to Table of Contents](#table-of-contents)

---

## QNAP TS-h1290FX
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| qnap-01.bjoin.studio                   |    10.20.51.201   |   51   |  ----/----  |
```

## ASUSTOR Flashstor 12 Pro FS6712X
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| asustor-01.bjoin.studio                |    10.20.51.202   |   51   |  ----/----  |
```

[Back to Table of Contents](#table-of-contents)

---

## MikroTik CRS520-4XS-16XQ-RM
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| crs520-core.bjoin.studio               |    10.20.51.11    |   51   |  ----/----  |
| crs520-qsfp.bjoin.studio               |    10.20.51.21    |  4090  |  ----/----  |
```

## MikroTik CRS504-4XQ-IN
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| crs504-access.bjoin.studio             |    10.20.51.12    |   51   |  ----/----  |
```

## Cisco Nexus 9236C
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| nexus-9236c.bjoin.studio               |    10.20.51.13    |   51   |  ----/----  |
```

## TP-Link SG3428X
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| tplink-sg3428x.bjoin.studio            |    10.20.51.14    |   51   |  ----/----  |
| tplink-sg3428x-qsfp.bjoin.studio       |    10.20.51.24    |  4090  |  ----/----  |
```

## Sodola KT-NOS SL-SWTGW2C8F
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| sodola-10g.bjoin.studio                |    10.20.51.15    |   51   |  ----/----  |
```

## Bitengine SW08XM
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| bitengine-sw08xm.bjoin.studio          |    10.20.51.16    |   51   |  ----/----  |
```

## Netgear GS108Ev4
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| netgear-gs108e.bjoin.studio            |    10.20.51.17    |   51   |  ----/----  |
```

## Netgear GS105
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| netgear-gs105.bjoin.studio             |    10.20.51.18    |   51   |  ----/----  |
```

[Back to Table of Contents](#table-of-contents)

---

## Mac Studio M3 Ultra
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| macstudio-ultra.bjoin.studio           |    10.20.51.50    |   51   |  ----/----  |
```

## MacBook Pro M1 (2020)
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| macbookpro-m1.bjoin.studio             |    10.20.51.53    |   51   |  ----/----  |
```

## iMac Pro (2017)
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| imacpro-2017.bjoin.studio              |    10.20.51.51    |   51   |  ----/----  |
```

## iMac 5K (2017)
```
| Hostname(s)                            | IP Address(es)    |  VLAN  |  Cable ID   |
| -------------------------------------- | ----------------- | ------ | ----------- |
| imac5k-2017.bjoin.studio               |    10.20.51.52    |   51   |  ----/----  |
```

[Back to Table of Contents](#table-of-contents)

---
