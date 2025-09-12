# IPAM Design for VLAN 45 (Workshop)

- **VLAN ID:** 45
- **Zone:** Workshop
- **Subnet:** `10.20.45.0/24`
- **Gateway:** `10.20.45.1`

## Purpose

This VLAN is for Monitoring (WORKSHOP-MONITOR).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.45.1` | **Gateway** | OPNsense Gateway |
| `10.20.45.2 - .254` | **Static Assignments** | Reserved for monitoring devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned monitoring devices, ensuring stability and predictability for workshop monitoring.
