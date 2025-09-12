# IPAM Design for VLAN 23 (Stage)

- **VLAN ID:** 23
- **Zone:** Stage
- **Subnet:** `10.20.23.0/24`
- **Gateway:** `10.20.23.1`

## Purpose

This VLAN is for Reserved (STAGE-RESERVED).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.23.1` | **Gateway** | OPNsense Gateway |
| `10.20.23.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is reserved for devices with static IP addresses only, ensuring a controlled and predictable environment for future staging use.
