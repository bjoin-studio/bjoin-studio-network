# OPNsense Stage VLAN Configuration (VLANs 21-25)

This guide provides step-by-step instructions for configuring the Stage VLANs (21-25) in OPNsense. These VLANs are for devices used during production shoots, such as cameras, lighting, and control systems.

## 1. VLAN Definitions

| VLAN ID | Name | Purpose | Subnet | Gateway IP | DHCP Range |
|:---|:---|:---|:---|:---|:---|
| **21** | `STAGE_WIRED_1G` | Stage Wired (1Gb) | `10.20.21.0/24` | `10.20.21.1` | `10.20.21.100 – 200` |
| **22** | `STAGE_WIRED_10G` | Stage Wired (10Gb) | `10.20.22.0/24` | `10.20.22.1` | `10.20.22.100 – 200` |
| **23** | `STAGE_RESERVED` | Stage Reserved | `10.20.23.0/24` | `10.20.23.1` | Static only |
| **24** | `STAGE_WIFI` | Stage Wifi | `10.20.24.0/24` | `10.20.24.1` | `10.20.24.100 – 200` |
| **25** | `STAGE_MONITOR` | Stage Monitoring | `10.20.25.0/24` | `10.20.25.1` | `10.20.25.100 – 200` |

---

## 2. Step-by-Step Configuration

Follow the same procedure as the Production guide to create, assign, and enable the five Stage VLANs and configure their DHCP servers.

### Firewall Rules

The key principle for the Stage VLANs is to allow them to send data to the Studio zone, but otherwise be isolated.

#### For General VLANs (21, 22, 24):
1.  **Allow DNS:** Allow traffic to your DNS servers.
2.  **Allow Media Ingest to Studio:** Create a rule to allow traffic *from* the VLAN's subnet (e.g., `STAGE_WIRED_10G net`) *to* the `StudioNet` alias (you should create an alias for all Studio VLANs).
3.  **Block Other Internal Traffic:** Add a rule to block traffic from the VLAN's subnet to the `RFC 1918` alias to prevent access to other zones.
4.  **Allow Internet:** Add a final rule to allow traffic to `! RFC 1918` for internet access.

#### For STAGE_MONITOR (VLAN 25):
*   This VLAN should be isolated. Create a rule to **block** all traffic from `STAGE_MONITOR net` to `Any`.

#### For STAGE_RESERVED (VLAN 23):
*   This VLAN should have no devices. Create a single rule to **block** all traffic from `STAGE_RESERVED net` to `Any`.
