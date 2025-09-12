# IPAM Design for VLAN 64 (Guest)

- **VLAN ID:** 64
- **Zone:** Guest
- **Subnet:** `10.20.64.0/24`
- **Gateway:** `10.20.64.1`

## Purpose

This VLAN is for WiFi (GUEST-WIFI).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.64.1` | **Gateway** | OPNsense Gateway |
| `10.20.64.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.64.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.64.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure provides a large DHCP pool for transient guest WiFi devices.
