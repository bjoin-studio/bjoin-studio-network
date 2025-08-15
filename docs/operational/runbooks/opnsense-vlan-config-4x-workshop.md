# OPNsense Workshop VLAN Configuration (VLANs 41-45)

This guide provides step-by-step instructions for configuring the Workshop VLANs (41-45). This zone is for engineering and prototyping and is highly isolated.

## 1. VLAN Definitions

| VLAN ID | Name | Purpose | Subnet | Gateway IP | DHCP Range |
|:---|:---|:---|:---|:---|:---|
| **41** | `WORKSHOP_WIRED_1G` | Workshop Wired (1Gb) | `10.20.41.0/24` | `10.20.41.1` | `10.20.41.100 – 200` |
| **42** | `WORKSHOP_RESERVED_1`| Workshop Reserved | `10.20.42.0/24` | `10.20.42.1` | Static only |
| **43** | `WORKSHOP_RESERVED_2`| Workshop Reserved | `10.20.43.0/24` | `10.20.43.1` | Static only |
| **44** | `WORKSHOP_WIFI` | Workshop Wifi | `10.20.44.0/24` | `10.20.44.1` | `10.20.44.100 – 200` |
| **45** | `WORKSHOP_MONITOR` | Workshop Monitoring | `10.20.45.0/24` | `10.20.45.1` | `10.20.45.100 – 200` |

---

## 2. Step-by-Step Configuration

Follow the same procedure as the Production guide to create, assign, and enable the five Workshop VLANs and configure their DHCP servers.

### Firewall Rules

The key principle for the Workshop is **complete isolation**.

#### For All Workshop VLANs (41, 42, 43, 44, 45):
1.  **Block All Traffic:** Create a single rule for each VLAN interface to **block** all traffic from the VLAN's subnet to `Any`.
2.  **Allow DNS (Optional):** If you need DNS for a specific purpose, add a `Pass` rule for port 53 to your DNS servers *above* the block rule.

This simple, restrictive rule set ensures the Workshop zone cannot access the internet or any other internal network zone.