# IPAM Design for VLAN 52 (Management)

- **VLAN ID:** 52
- **Zone:** Management
- **Subnet:** `10.20.52.0/24`
- **Gateway:** `10.20.52.1`

## Purpose

This VLAN is for Reserved (MGMT-WIRED-10).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.52.1` | **Gateway** | OPNsense Gateway |
| `10.20.52.2 - .254` | **Static Assignments** | Reserved for devices requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is reserved for devices with static IP addresses only, ensuring a controlled and predictable environment for future management use.
