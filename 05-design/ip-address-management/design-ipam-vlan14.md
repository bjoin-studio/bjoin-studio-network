# IPAM Design for VLAN 14 (Production)

- **VLAN ID:** 14
- **Zone:** Production
- **Subnet:** `10.20.14.0/24`
- **Gateway:** `10.20.14.1`

## Purpose

This VLAN is for WiFi clients (PROD-WIFI).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.14.1` | **Gateway** | OPNsense Gateway |
| `10.20.14.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.14.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.14.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports a large number of dynamic WiFi clients while allowing for specific devices to have reserved static IPs if needed.
