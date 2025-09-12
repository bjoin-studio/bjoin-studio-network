# IPAM Design for VLAN 54 (Management)

- **VLAN ID:** 54
- **Zone:** Management
- **Subnet:** `10.20.54.0/24`
- **Gateway:** `10.20.54.1`

## Purpose

This VLAN is for WiFi (MGMT-WIFI).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.54.1` | **Gateway** | OPNsense Gateway |
| `10.20.54.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is for statically assigned WiFi infrastructure, such as access point management interfaces.
