# IPAM Design for VLAN 34 (Studio)

- **VLAN ID:** 34
- **Zone:** Studio
- **Subnet:** `10.20.34.0/24`
- **Gateway:** `10.20.34.1`

## Purpose

This VLAN is for WiFi clients (STUDIO-WIFI).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.34.1` | **Gateway** | OPNsense Gateway |
| `10.20.34.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.34.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.34.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports a large number of dynamic WiFi clients in the studio while allowing for specific devices to have reserved static IPs if needed.
