# IPAM Design for VLAN 15 (Production)

- **VLAN ID:** 15
- **Zone:** Production
- **Subnet:** `10.20.15.0/24`
- **Gateway:** `10.20.15.1`

## Purpose

This VLAN is for Monitoring (PROD-MONITOR).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.15.1` | **Gateway** | OPNsense Gateway |
| `10.20.15.2 - .254` | **Static Assignments** | Reserved for monitoring devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned monitoring devices, ensuring stability and predictability for critical monitoring infrastructure.
