# IPAM Design for VLAN 25 (Stage)

- **VLAN ID:** 25
- **Zone:** Stage
- **Subnet:** `10.20.25.0/24`
- **Gateway:** `10.20.25.1`

## Purpose

This VLAN is for Monitoring (STAGE_MONITOR).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.25.1` | **Gateway** | OPNsense Gateway |
| `10.20.25.2 - .254` | **Static Assignments** | Reserved for monitoring devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned monitoring devices, ensuring stability and predictability for staging monitoring.
