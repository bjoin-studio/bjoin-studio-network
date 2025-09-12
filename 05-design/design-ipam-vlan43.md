# IPAM Design for VLAN 43 (Workshop)

- **VLAN ID:** 43
- **Zone:** Workshop
- **Subnet:** `10.20.43.0/24`
- **Gateway:** `10.20.43.1`

## Purpose

This VLAN is for Reserved (WORKSHOP-RESV-2).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.43.1` | **Gateway** | OPNsense Gateway |
| `10.20.43.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is reserved for devices with static IP addresses only, ensuring a controlled and predictable environment for future workshop use.
