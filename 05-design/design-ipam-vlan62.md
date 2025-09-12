# IPAM Design for VLAN 62 (Guest)

- **VLAN ID:** 62
- **Zone:** Guest
- **Subnet:** `10.20.62.0/24`
- **Gateway:** `10.20.62.1`

## Purpose

This VLAN is for Reserved (GUEST-RESV-1).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.62.1` | **Gateway** | OPNsense Gateway |
| `10.20.62.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is reserved for devices with static IP addresses only, for future guest network use.
