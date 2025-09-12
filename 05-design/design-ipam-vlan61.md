# IPAM Design for VLAN 61 (Guest)

- **VLAN ID:** 61
- **Zone:** Guest
- **Subnet:** `10.20.61.0/24`
- **Gateway:** `10.20.61.1`

## Purpose

This VLAN is for Visitor Devices (GUEST-WIRED-1).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.61.1` | **Gateway** | OPNsense Gateway |
| `10.20.61.2 - .99` | **Static Assignments** | Reserved for devices requiring a fixed IP. |
| `10.20.61.100 - .200`| **DHCP Pool** | For general client use. |
| `10.20.61.201 - .254`| **Reserved** | Future use. |

## Rationale

This structure provides a large DHCP pool for transient guest devices, with a small static range available if needed.
