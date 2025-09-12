# IPAM Design for VLAN 35 (Studio)

- **VLAN ID:** 35
- **Zone:** Studio
- **Subnet:** `10.20.35.0/24`
- **Gateway:** `10.20.35.1`

## Purpose

This VLAN is for Monitoring (STUDIO-MONITOR).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.35.1` | **Gateway** | OPNsense Gateway |
| `10.20.35.2 - .254` | **Static Assignments** | Reserved for monitoring devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned monitoring devices, ensuring stability and predictability for studio monitoring.
