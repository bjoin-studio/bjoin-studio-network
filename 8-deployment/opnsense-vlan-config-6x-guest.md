# OPNsense Guest VLAN Configuration (VLANs 61-65)

This guide provides step-by-step instructions for configuring the Guest VLANs (61-65). This zone is for providing internet access to visitors and must be completely isolated from the internal network.

## 1. VLAN Definitions

| VLAN ID | Name | Purpose | Subnet | Gateway IP | DHCP Range |
|:---|:---|:---|:---|:---|:---|
| **61** | `GUEST_WIRED_1G` | Guest Wired (1Gb) | `10.20.61.0/24` | `10.20.61.1` | `10.20.61.100 – 200` |
| **62** | `GUEST_RESERVED_1` | Guest Reserved | `10.20.62.0/24` | `10.20.62.1` | Static only |
| **63** | `GUEST_RESERVED_2` | Guest Reserved | `10.20.63.0/24` | `10.20.63.1` | Static only |
| **64** | `GUEST_WIFI` | Guest Wifi | `10.20.64.0/24` | `10.20.64.1` | `10.20.64.100 – 200` |
| **65** | `GUEST_MONITOR` | Guest Monitoring | `10.20.65.0/24` | `10.20.65.1` | `10.20.65.100 – 200` |

---

## 2. Step-by-Step Configuration

Follow the same procedure as the Production guide to create, assign, and enable the five Guest VLANs and configure their DHCP servers.

### Firewall Rules

The key principle for the Guest zone is **internet only**.

#### For All Guest VLANs (61, 62, 63, 64, 65):
1.  **Block All Internal Access:** Create a rule at the top to **block** any traffic from the VLAN's subnet to the `RFC 1918` alias (all private IP space).
2.  **Allow Internet Access:** Create a second rule to **pass** traffic from the VLAN's subnet to `Any`.

This simple rule set ensures guests can access the internet but are strictly prohibited from accessing any internal resources.