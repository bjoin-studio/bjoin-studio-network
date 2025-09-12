# IPAM Design for VLAN 33 (Studio)

- **VLAN ID:** 33
- **Zone:** Studio
- **Subnet:** `10.20.33.0/24`
- **Gateway:** `10.20.33.1`

## Purpose

This VLAN is for Servers (STUDIO-WIRED-100).

## Allocation Structure

| IP Range | Asset Group | Purpose & Notes |
| :--- | :--- | :--- |
| `10.20.33.1` | **Gateway** | OPNsense Gateway |
| `10.20.33.2 - .254` | **Static Assignments** | Reserved for servers requiring a fixed IP. |

## Rationale

With no DHCP, this VLAN is dedicated to statically assigned servers, ensuring maximum stability and predictability.
