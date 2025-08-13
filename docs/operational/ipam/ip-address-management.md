# IP Address Management (IPAM)

This document is the central source of truth for all IP address allocations within the bjoin.studio network. Keeping this up-to-date is critical for preventing IP conflicts and maintaining network organization.

## DHCP Scopes Summary

This table provides a quick overview of the DHCP ranges for each VLAN.

| VLAN ID | Zone         | Subnet           | Gateway IP     | DHCP Range                  | Notes                                      |
|:--------|:-------------|:-----------------|:---------------|:----------------------------|:-------------------------------------------|
| 11      | Production   | `10.20.11.0/24`  | `10.20.11.1`   | `10.20.11.100 – 200`        | General workstations                       |
| 12      | Production   | `10.20.12.0/24`  | `10.20.12.1`   | `10.20.12.100 – 200`        | High-performance nodes                     |
| 14      | Production   | `10.20.14.0/24`  | `10.20.14.1`   | `10.20.14.100 – 200`        | WiFi clients                               |
| 21      | Stage        | `10.20.21.0/24`  | `10.20.21.1`   | `10.20.21.100 – 200`        | Capture & control devices                  |
| 22      | Stage        | `10.20.22.0/24`  | `10.20.22.1`   | `10.20.22.100 – 200`        | Image transfer servers                     |
| 24      | Stage        | `10.20.24.0/24`  | `10.20.24.1`   | `10.20.24.100 – 200`        | WiFi clients                               |
| 31      | Studio       | `10.20.31.0/24`  | `10.20.31.1`   | `10.20.31.100 – 200`        | Creative workstations                      |
| 32      | Studio       | `10.20.32.0/24`  | `10.20.32.1`   | `10.20.32.100 – 200`        | High-performance editing                   |
| 34      | Studio       | `10.20.34.0/24`  | `10.20.34.1`   | `10.20.34.100 – 200`        | WiFi clients                               |
| 41      | Workshop     | `10.20.41.0/24`  | `10.20.41.1`   | `10.20.41.100 – 200`        | Engineering stations                       |
| 44      | Workshop     | `10.20.44.0/24`  | `10.20.44.1`   | `10.20.44.100 – 200`        | WiFi clients                               |
| 53      | Management   | `10.20.53.0/24`  | `10.20.53.1`   | `10.20.53.100 – 200`        | Monitoring devices                         |
| 61      | Guest WiFi   | `10.20.61.0/24`  | `10.20.61.1`   | `10.20.61.100 – 200`        | Visitor devices                            |

---

## Static IP Assignments

Reserved IP Range for Static Assignments: `.2` to `.99` in each subnet.

### Network Infrastructure (VLAN 51)

| IP Address     | Device Hostname        | MAC Address        | Notes                            |
|:---------------|:-----------------------|:-------------------|:---------------------------------|
| `10.20.51.1`   | `opnsense-fw`          | (from hardware)    | OPNsense LAN Gateway             |
| `10.20.51.2`   | `cisco-nexus-1`        | (from hardware)    | 100G Core Switch                 |
| `10.20.51.3`   | `sodola-10g-1`         | (from hardware)    | Distribution Switch              |
| `10.20.51.4`   | `bitengine-10g-1`      | (from hardware)    | Access Switch                    |
| `10.20.51.5`   | `netgear-gs108ev4-1`   | (from hardware)    | Access Switch                    |
| `10.20.51.10`  | `ipa1.bjoin.studio`    | (from hardware)    | Primary FreeIPA / DNS Server     |
| `10.20.51.11`  | `ipa2.bjoin.studio`    | (from hardware)    | Secondary FreeIPA / DNS Server   |
| `10.20.51.20`  | `pmx-01.bjoin.studio`  | (from hardware)    | Proxmox VE Hypervisor Host       |

### Management - Reserved (VLAN 52)

| IP Address     | Device Hostname        | MAC Address        | Notes                            |
|:---------------|:-----------------------|:-------------------|:---------------------------------|
|                |                        |                    |                                  |

### Management - Monitoring (VLAN 53)

| IP Address     | Device Hostname        | MAC Address        | Notes                            |
|:---------------|:-----------------------|:-------------------|:---------------------------------|
|                |                        |                    |                                  |

### Servers (VLAN 33)

| IP Address     | Device Hostname        | MAC Address        | Notes                            |
|:---------------|:-----------------------|:-------------------|:---------------------------------|
| `10.20.33.10`  | `nas-01.bjoin.studio`  | (from hardware)    | Main NAS Storage                 |
| `10.20.33.11`  | `san-01.bjoin.studio`  | (from hardware)    | SAN Controller                   |

### Printers

| IP Address     | Device Name            | MAC Address        | Location                         |
|:---------------|:-----------------------|:-------------------|:---------------------------------|
|                |                        |                    |                                  |