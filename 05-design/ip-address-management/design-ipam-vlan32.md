# IPAM Design for VLAN 32 (Studio)

- **VLAN ID:** 32
- **Zone:** Studio
- **Subnet:** `10.20.32.0/24`
- **Gateway:** `10.20.32.1`

## Purpose

This VLAN is for High-performance editing (STUDIO-WIRED-10).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.32.1` | **Gateway** | OPNsense Gateway |
| `10.20.32.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.32.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.32.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports both static and dynamic assignments for high-performance editing workstations.
