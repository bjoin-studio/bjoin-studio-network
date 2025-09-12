# IPAM Design for VLAN 12 (Production)

- **VLAN ID:** 12
- **Zone:** Production
- **Subnet:** `10.20.12.0/24`
- **Gateway:** `10.20.12.1`

## Purpose

This VLAN is for High-performance nodes (PROD-WIRED-10).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.12.1` | **Gateway** | OPNsense Gateway |
| `10.20.12.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.12.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.12.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure provides a dedicated range for static assignments while leaving a large pool for dynamic clients, which is ideal for a high-performance user VLAN.
