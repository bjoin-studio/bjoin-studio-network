# IPAM Design for VLAN 31 (Studio)

- **VLAN ID:** 31
- **Zone:** Studio
- **Subnet:** `10.20.31.0/24`
- **Gateway:** `10.20.31.1`

## Purpose

This VLAN is for Creative workstations (STUDIO-WIRED_1).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.31.1` | **Gateway** | OPNsense Gateway |
| `10.20.31.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.31.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.31.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure provides a dedicated range for static assignments for creative workstations while leaving a large pool for dynamic clients.
