# IPAM Design for VLAN 44 (Workshop)

- **VLAN ID:** 44
- **Zone:** Workshop
- **Subnet:** `10.20.44.0/24`
- **Gateway:** `10.20.44.1`

## Purpose

This VLAN is for WiFi clients (WORKSHOP-WIFI).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.44.1` | **Gateway** | OPNsense Gateway |
| `10.20.44.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.44.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.44.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports a large number of dynamic WiFi clients in the workshop while allowing for specific devices to have reserved static IPs if needed.
