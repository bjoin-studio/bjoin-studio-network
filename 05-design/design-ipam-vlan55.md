# IPAM Design for VLAN 55 (Management)

- **VLAN ID:** 55
- **Zone:** Management
- **Subnet:** `10.20.55.0/24`
- **Gateway:** `10.20.55.1`

## Purpose

This VLAN is for Monitoring (MGMT-MONITOR).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.55.1` | **Gateway** | OPNsense Gateway |
| `10.20.55.2 - .254` | **Static Assignments** | Reserved for monitoring devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned monitoring devices, ensuring stability and predictability for management-zone monitoring.
