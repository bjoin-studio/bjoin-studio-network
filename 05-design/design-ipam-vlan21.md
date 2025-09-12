# IPAM Design for VLAN 21 (Stage)

- **VLAN ID:** 21
- **Zone:** Stage
- **Subnet:** `10.20.21.0/24`
- **Gateway:** `10.20.21.1`

## Purpose

This VLAN is for Capture & control devices (STAGE-WIRED-1).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.21.1` | **Gateway** | OPNsense Gateway |
| `10.20.21.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.21.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.21.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure provides a dedicated range for static assignments while leaving a large pool for dynamic clients, suitable for a staging environment.
