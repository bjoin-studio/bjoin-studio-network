# IPAM Design for VLAN 22 (Stage)

- **VLAN ID:** 22
- **Zone:** Stage
- **Subnet:** `10.20.22.0/24`
- **Gateway:** `10.20.22.1`

## Purpose

This VLAN is for Image transfer servers (STAGE-WIRED-10).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.22.1` | **Gateway** | OPNsense Gateway |
| `10.20.22.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.22.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.22.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports both static and dynamic assignments, providing flexibility for image transfer servers and related devices.
