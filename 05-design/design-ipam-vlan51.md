# IPAM Design for VLAN 51 (Management)

- **VLAN ID:** 51
- **Zone:** Management
- **Subnet:** `10.20.51.0/24`
- **Gateway:** `10.20.51.1`

## Purpose

This VLAN is for Network Infrastructure (MGMT-WIRED-1).

## Allocation Structure

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

## Rationale

This detailed, granular structure is necessary for the management VLAN as it contains many different types of critical infrastructure. Each category of device has a dedicated range to improve organization, simplify firewall rules, and reduce the risk of IP conflicts.
