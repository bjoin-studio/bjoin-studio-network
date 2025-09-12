# IPAM Design for VLAN 65 (Guest)

- **VLAN ID:** 65
- **Zone:** Guest
- **Subnet:** `10.20.65.0/24`
- **Gateway:** `10.20.65.1`

## Purpose

This VLAN is for Monitoring (GUEST-MONITOR).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.65.1` | **Gateway** | OPNsense Gateway |
| `10.20.65.2 - .254` | **Static Assignments** | Reserved for monitoring devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned monitoring devices, ensuring stability and predictability for guest network monitoring.
