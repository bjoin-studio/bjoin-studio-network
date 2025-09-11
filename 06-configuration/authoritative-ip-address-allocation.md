# Structured IP Address Management Plan

This document outlines a structured and logical approach to IP address allocation for the management network (VLAN 51, `10.20.51.0/24`).

## Rationale for a Structured Approach

Adopting a structured IP allocation scheme provides several key advantages over organic assignment:

*   **Clarity & Readability:** A device's function can be inferred from its IP address, simplifying network comprehension for all team members. For example, an IP in the `.40-.59` range is immediately identifiable as a hypervisor.
*   **Scalability:** By reserving blocks of addresses for specific roles, the network can grow predictably. New switches, servers, or other devices can be added to their designated block without causing conflicts or requiring re-addressing of other asset types.
*   **Simplified Management:** This structure makes it significantly easier to create and manage firewall rules, access control lists (ACLs), and monitoring configurations. For instance, a single rule can be applied to the entire hypervisor range (`10.20.51.40/28`).
*   **Reduced Errors:** A clear plan minimizes the risk of IP conflicts and misconfigurations, which are common when addresses are assigned without a system.

---

## Proposed Allocation Structure

This table defines the recommended logical grouping for the `10.20.51.0/24` subnet.


| IP range | Asset group | Purpose & notes |
| :-- | :-- | :-- |
| 10.20.51.1 | **Primary gateway** | Default gateway/virtual IP for the subnet. |
| 10.20.51.2 – .9 | **Gateways & firewalls** | HA/secondary VIPs, dedicated firewall interfaces, router services. |
| 10.20.51.10 – .19 | **Core switches** | Distribution/backbone switches, stack management IPs. |
| 10.20.51.20 – .29 | **Core switches** | Switch Trunking, stack management IPs. |
| 10.20.51.30 – .59 | **Access switches** | Edge switches for endpoints and AP uplinks. |
| 10.20.51.60 – .79 | **Hypervisor hosts** | Proxmox/ESXi host management (e.g., pmx-01, pmx-02). |
| 10.20.51.80 – .99 | **Infrastructure servers** | Identity/DNS (FreeIPA), monitoring (LibreNMS), automation (Ansible), jump hosts. |
| 10.20.51.100 – .200 | **DHCP pool** | Dynamic clients, provisioning, testing. Do not assign statics here. |
| 10.20.51.201 – .219 | **Storage & appliances** | NAS/SAN controllers (TrueNAS), UPS, PDU, NTP/PTP, out-of-band appliance UIs. |
| 10.20.51.220 – .239 | **Out-of-band management** | IPMI/iDRAC/iLO BMC interfaces. |
| 10.20.51.240 – .249 | **Reserved/future infrastructure** | Growth space for any static infrastructure roles. |
| 10.20.51.250 – .254 | **Special use** | Anycast VIPs, VRRP/HSRP, testing statics. Avoid .255 (broadcast). |

---

#### Implementation tips
- **DHCP scope:** 10.20.51.100–10.20.51.200 with reservations only inside that range if you must, otherwise prefer static IPs outside the pool.
- **Exclusions:** Ensure the DHCP server has explicit exclusions for 10.20.51.1–.99 and 10.20.51.201–.254.
- **Documentation:** Add hostnames and roles next to each assigned static (e.g., 10.20.51.61 pmx-01) to prevent drift.
- **Gateway HA:** If using VRRP/HSRP/Carp, put the VIP at .1 and use .2/.3 for member devices.

---

## New IP Assignments for Existing Equipment

This table provides a concrete migration plan, mapping existing devices to their new, logical IP addresses within the proposed structure.

| Hostname | Device Type | New IP Address | Old IP Address | Notes |
| :--- | :--- | :--- | :--- | :--- |
| `opnsense-fw` | Gateway | **`10.20.51.1`** | `10.20.51.1` | No change (Primary Gateway) |
| `opnsense-fw-hpz620-1` | Firewall | **`10.20.51.2`** | `10.20.51.9` | Secondary firewall |
| | | | | |
| `cisco-nexus-1` | Core Switch | **`10.20.51.10`** | `10.20.51.2` | |
| `mikrotik-crs520-1` | Core Switch | **`10.20.51.11`** | `10.20.51.6` | |
| `mikrotik-crs504-1` | Core Switch | **`10.20.51.12`** | `10.20.51.7` | |
| `tp-link-sg3428x-1` | Core Switch | **`10.20.51.13`** | `10.20.51.4` | Classified as Core/Distro |
| | | | | |
| `bitengine-10g-1` | Access Switch | **`10.20.51.20`** | `10.20.51.3` | |
| `netgear-gs108ev4-1` | Access Switch | **`10.20.51.21`** | `10.20.51.5` | |
| `sodola-10g-1` | Access Switch | **`10.20.51.22`** | `10.20.51.8` | |
| | | | | |
| `pmx-01.bjoin.studio` | Hypervisor Host | **`10.20.51.40`** | `10.20.51.20` | |
| `pmx-02.bjoin.studio` | Hypervisor Host | **`10.20.51.41`** | `10.20.51.40` | Made sequential with pmx-01 |
| | | | | |
| `ipa1.bjoin.studio` | Infra Server | **`10.20.51.60`** | `10.20.51.10` | FreeIPA Primary |
| `ipa2.bjoin.studio` | Infra Server | **`10.20.51.61`** | `10.20.51.11` | FreeIPA Secondary |
| | | | | |
| `nas-01.bjoin.studio` | Storage | **`10.20.51.80`** | `10.20.33.10` | Mgmt IP moved to VLAN 51 |
| `san-01.bjoin.studio` | Storage | **`10.20.51.81`** | `10.20.33.11` | Mgmt IP moved to VLAN 51 |

---

# IP Address Management (IPAM)

This document is the central source of truth for all IP address allocations within the bjoin.studio network. Keeping this up-to-date is critical for preventing IP conflicts and maintaining network organization.

## DHCP Scopes Summary

This table provides a quick overview of the DHCP ranges for each VLAN.

| VLAN ID | Zone         | Subnet           | Gateway IP     | DHCP Range                  | Notes                                      |
|:--------|:-------------|:-----------------|:---------------|:----------------------------|:-------------------------------------------|
| 11      | Production   | `10.20.11.0/24`  | `10.20.11.1`   | `10.20.11.100 – 200`        | General workstations (PROD-WIRED-1)        |
| 12      | Production   | `10.20.12.0/24`  | `10.20.12.1`   | `10.20.12.100 – 200`        | High-performance nodes (PROD-WIRED-10)     |
| 13      | Production   | `10.20.13.0/24`  | `10.20.13.1`   | `none`                      | Reserved (PROD-RESERVED)                   |
| 14      | Production   | `10.20.14.0/24`  | `10.20.14.1`   | `10.20.14.100 – 200`        | WiFi clients (PROD-WIFI)                   |
| 15      | Production   | `10.20.15.0/24`  | `10.20.15.1`   | `none`                      | Monitoring (PROD-MONITOR)                  |
| 21      | Stage        | `10.20.21.0/24`  | `10.20.21.1`   | `10.20.21.100 – 200`        | Capture & control devices (STAGE-WIRED-1)  |
| 22      | Stage        | `10.20.22.0/24`  | `10.20.22.1`   | `10.20.22.100 – 200`        | Image transfer servers (STAGE-WIRED-10)    |
| 23      | Stage        | `10.20.23.0/24`  | `10.20.23.1`   | `none`                      | Reserved (STAGE-RESERVED)                  |
| 24      | Stage        | `10.20.24.0/24`  | `10.20.24.1`   | `10.20.24.100 – 200`        | WiFi clients (STAGE-WIFI)                  |
| 25      | Stage        | `10.20.25.0/24`  | `10.20.25.1`   | `none`                      | Monitoring (STAGE_MONITOR)                 |
| 31      | Studio       | `10.20.31.0/24`  | `10.20.31.1`   | `10.20.31.100 – 200`        | Creative workstations (STUDIO-WIRED_1)     |
| 32      | Studio       | `10.20.32.0/24`  | `10.20.32.1`   | `10.20.32.100 – 200`        | High-performance editing (STUDIO-WIRED-10) |
| 33      | Studio       | `10.20.33.0/24`  | `10.20.33.1`   | `none`                      | Servers (STUDIO-WIRED-100)                 |
| 34      | Studio       | `10.20.34.0/24`  | `10.20.34.1`   | `10.20.34.100 – 200`        | WiFi clients (STUDIO-WIFI)                 |
| 35      | Studio       | `10.20.35.0/24`  | `10.20.35.1`   | `none`                      | Monitoring (STUDIO-MONITOR)                |
| 41      | Workshop     | `10.20.41.0/24`  | `10.20.41.1`   | `10.20.41.100 – 200`        | Engineering stations (WORKSHOP-WIRED-1)    |
| 42      | Workshop     | `10.20.42.0/24`  | `10.20.42.1`   | `none`                      | Reserved (WORKSHOP-RESV-1)                 |
| 43      | Workshop     | `10.20.43.0/24`  | `10.20.43.1`   | `none`                      | Reserved (WORKSHOP-RESV-2)                 |
| 44      | Workshop     | `10.20.44.0/24`  | `10.20.44.1`   | `10.20.44.100 – 200`        | WiFi clients (WORKSHOP-WIFI)               |
| 45      | Workshop     | `10.20.45.0/24`  | `10.20.45.1`   | `none`                      | Monitoring (WORKSHOP-MONITOR)              |
| 51      | Management   | `10.20.51.0/24`  | `10.20.51.1`   | `none`                      | Network Infrastructure (MGMT-WIRED-1)      |
| 52      | Management   | `10.20.52.0/24`  | `10.20.52.1`   | `none`                      | Reserved (MGMT-WIRED-10)                   |
| 53      | Management   | `10.20.53.0/24`  | `10.20.53.1`   | `10.20.53.100 – 200`        | Monitoring devices (MGMT-WIRED-100)        |
| 54      | Management   | `10.20.54.0/24`  | `10.20.54.1`   | `none`                      | WiFi (MGMT-WIFI)                           |
| 55      | Management   | `10.20.55.0/24`  | `10.20.55.1`   | `none`                      | Monitoring (MGMT-MONITOR)                  |
| 61      | Guest        | `10.20.61.0/24`  | `10.20.61.1`   | `10.20.61.100 – 200`        | Visitor Devices (GUEST-WIRED-1)            |
| 62      | Guest        | `10.20.62.0/24`  | `10.20.62.1`   | `none`                      | Reserved (GUEST-RESV-1)                    |
| 63      | Guest        | `10.20.63.0/24`  | `10.20.63.1`   | `none`                      | Reserved (GUEST-RESV-2)                    |
| 64      | Guest        | `10.20.64.0/24`  | `10.20.64.1`   | `10.20.64.100 – 200`        | WiFi (GUEST-WIFI)                          |
| 65      | Guest        | `10.20.65.0/24`  | `10.20.65.1`   | `none`                      | Monitoring (GUEST-MONITOR)                 |

---

## Static IP Assignments

Reserved IP Range for Static Assignments: `.2` to `.99` in each subnet.

### Network Infrastructure (VLAN 51)

| IP Address     | Device Hostname        | MAC Address        | Notes                            |
|:---------------|:-----------------------|:-------------------|:---------------------------------|
| `10.20.51.1`   | `opnsense-fw`          | (from hardware)    | OPNsense LAN Gateway             |
| `10.20.51.2`   | `cisco-nexus-1`        | (from hardware)    | 100G Core Switch                 |
| `10.20.51.3`   | `bitengine-10g-1`      | (from hardware)    | Access Switch                    |
| `10.20.51.13`  | `tp-link-sg3428x-1`    | (from hardware)    | Distribution Switch              |
| `10.20.51.21`  | `netgear-gs108ev4-1`   | (from hardware)    | Access Switch                    |
| `10.20.51.14`  | `mikrotik-crs520-1`    | (from hardware)    | 100G Core Switch                 |
| `10.20.51.12`  | `mikrotik-crs504-1`    | (from hardware)    | 100G Core Switch                 |
| `10.20.51.22`  | `sodola-10g-1`         | (from hardware)    | Access Switch                    |
| `10.20.51.9`   | `opnsense-fw-hpz620-1` | (from hardware)    | OPNsense Firewall (High Perf)    |
| `10.20.51.10`  | `ipa1.bjoin.studio`    | (from hardware)    | Primary FreeIPA / DNS Server     |
| `10.20.51.11`  | `ipa2.bjoin.studio`    | (from hardware)    | Secondary FreeIPA / DNS Server   |
| `10.20.51.20`  | `pmx-01.bjoin.studio`  | (from hardware)    | Proxmox VE Hypervisor Host       |
| `10.20.51.40`  | `pmx-02.bjoin.studio`  | (from hardware)    | Proxmox VE Hypervisor Host       |

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
