# IPAM Design for VLAN 24 (Stage)

- **VLAN ID:** 24
- **Zone:** Stage
- **Subnet:** `10.20.24.0/24`
- **Gateway:** `10.20.24.1`

## Purpose

This VLAN is for WiFi clients (STAGE-WIFI).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.24.1` | **Gateway** | OPNsense Gateway |
| `10.20.24.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.24.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.24.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure supports a large number of dynamic WiFi clients while allowing for specific devices to have reserved static IPs if needed in the staging environment.
