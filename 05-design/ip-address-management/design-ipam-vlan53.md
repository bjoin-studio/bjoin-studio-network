# IPAM Design for VLAN 53 (Management)

- **VLAN ID:** 53
- **Zone:** Management
- **Subnet:** `10.20.53.0/24`
- **Gateway:** `10.20.53.1`

## Purpose

This VLAN is for Monitoring devices (MGMT-WIRED-100).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.53.1` | **Gateway** | OPNsense Gateway |
| `10.20.53.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.53.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.53.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports both static and dynamic assignments for monitoring devices.
