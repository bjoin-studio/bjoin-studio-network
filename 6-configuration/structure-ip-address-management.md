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

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.51.1 - .9` | **Gateways & Firewalls** | For core network routing and security appliances. The `.1` address is the primary gateway. |
| `10.20.51.10 - .19` | **Core Switches** | Backbone switches that handle major network traffic (e.g., Cisco Nexus, MikroTik 100G). |
| `10.20.51.20 - .39` | **Access Switches** | Edge switches that connect endpoints to the network (e.g., TP-Link, Netgear, Sodola). |
| `10.20.51.40 - .59` | **Hypervisor Hosts** | Management interfaces for virtualization hosts like Proxmox or ESXi (e.g., `pmx-01`, `pmx-02`). |
| `10.20.51.60 - .79` | **Infrastructure Servers** | Core service servers like FreeIPA (Identity/DNS), monitoring, and automation (e.g., Ansible). |
| `10.20.51.80 - .99` | **Storage & Appliances** | Management interfaces for NAS/SAN controllers, UPS systems, and other hardware appliances. |
| `10.20.51.100 - .119`| **Out-of-Band Mgmt** | For IPMI, iDRAC, and other remote server management interfaces. |
| `10.20.51.120 - .199`| **Reserved / Future Use** | A large block left available for future device categories or expansion of existing ones. |
| `10.20.51.200 - .254`| **DHCP / Testing** | Optional range for temporary devices or for provisioning new hosts before assigning a static IP. |

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
