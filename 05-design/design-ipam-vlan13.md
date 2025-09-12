# IPAM Design for VLAN 13 (Production)

- **VLAN ID:** 13
- **Zone:** Production
- **Subnet:** `10.20.13.0/24`
- **Gateway:** `10.20.13.1`

## Purpose

This VLAN is for Reserved (PROD-RESERVED).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.13.1` | **Gateway** | OPNsense Gateway |
| `10.20.13.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is reserved for devices with static IP addresses only, ensuring a controlled and predictable environment.
