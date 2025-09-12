# IPAM Design for VLAN 42 (Workshop)

- **VLAN ID:** 42
- **Zone:** Workshop
- **Subnet:** `10.20.42.0/24`
- **Gateway:** `10.20.42.1`

## Purpose

This VLAN is for Reserved (WORKSHOP-RESV-1).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.42.1` | **Gateway** | OPNsense Gateway |
| `10.20.42.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is reserved for devices with static IP addresses only, ensuring a controlled and predictable environment for future workshop use.
