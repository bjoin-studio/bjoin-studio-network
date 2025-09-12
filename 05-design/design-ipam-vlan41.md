# IPAM Design for VLAN 41 (Workshop)

- **VLAN ID:** 41
- **Zone:** Workshop
- **Subnet:** `10.20.41.0/24`
- **Gateway:** `10.20.41.1`

## Purpose

This VLAN is for Engineering stations (WORKSHOP-WIRED-1).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.41.1` | **Gateway** | OPNsense Gateway |
| `10.20.41.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.41.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.41.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure provides a dedicated range for static assignments for engineering stations while leaving a large pool for dynamic clients.
