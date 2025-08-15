# OPNsense Studio VLAN Configuration (VLANs 31-35)

This guide provides step-by-step instructions for configuring the Studio VLANs (31-35). This is the core creative environment for editing, color grading, and VFX.

## 1. VLAN Definitions

| VLAN ID | Name | Purpose | Subnet | Gateway IP | DHCP Range |
|:---|:---|:---|:---|:---|:---|
| **31** | `STUDIO_WIRED_1G` | Studio Wired (1Gb) | `10.20.31.0/24` | `10.20.31.1` | `10.20.31.100 – 200` |
| **32** | `STUDIO_WIRED_10G` | Studio Wired (10Gb) | `10.20.32.0/24` | `10.20.32.1` | `10.20.32.100 – 200` |
| **33** | `STUDIO_WIRED_100G`| Studio Wired (100Gb)| `10.20.33.0/24` | `10.20.33.1` | Static only |
| **34** | `STUDIO_WIFI` | Studio Wifi | `10.20.34.0/24` | `10.20.34.1` | `10.20.34.100 – 200` |
| **35** | `STUDIO_MONITOR` | Studio Monitoring | `10.20.35.0/24` | `10.20.35.1` | `10.20.35.100 – 200` |

---

## 2. Step-by-Step Configuration

Follow the same procedure as the Production guide to create, assign, and enable the five Studio VLANs and configure their DHCP servers.

### Firewall Rules

The high-performance Studio VLANs (32, 33) have broad access, while the general workstations are more restricted.

#### For High-Performance VLANs (32, 33):
1.  **Allow DNS and Management Access.**
2.  **Allow Broad Internal Access:** These VLANs need to access assets from other zones. Create a rule to allow traffic *from* the VLAN's subnet *to* `ProductionNet` and `StageNet` aliases.
3.  **Allow Internet.**

#### For General VLANs (31, 34):
1.  **Allow DNS and Management Access.**
2.  **Block Other Production Zones:** Explicitly block traffic from the VLAN's subnet to `StageNet`, `WorkshopNet`, etc.
3.  **Allow Limited Internet.**

#### For STUDIO_MONITOR (VLAN 35):
*   This VLAN should be isolated. Create a rule to **block** all traffic from `STUDIO_MONITOR net` to `Any`.