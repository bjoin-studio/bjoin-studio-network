# OPNsense Management VLAN Configuration (VLANs 51-55)

This guide provides step-by-step instructions for configuring the Management VLANs (51-55) in OPNsense. This zone is for network device control, administrative access, and monitoring.

## 1. VLAN Definitions

| VLAN ID | Name | Purpose | Subnet | Gateway IP | DHCP Range |
|:---|:---|:---|:---|:---|:---|
| **51** | `MGMT_WIRED_1G` | Management Wired (1Gb) | `10.20.51.0/24` | `10.20.51.1` | `10.20.51.100 – 200` |
| **52** | `MGMT_RESERVED_1` | Management Reserved | `10.20.52.0/24` | `10.20.52.1` | Static only |
| **53** | `MGMT_RESERVED_2` | Management Reserved | `10.20.53.0/24` | `10.20.53.1` | Static only |
| **54** | `MGMT_WIFI` | Management Wifi | `10.20.54.0/24` | `10.20.54.1` | `10.20.54.100 – 200` |
| **55** | `MGMT_MONITOR` | Management Monitoring | `10.20.55.0/24` | `10.20.55.1` | `10.20.55.100 – 200` |

---

## 2. Step-by-Step Configuration

Follow the same procedure as the other OPNsense guides to create, assign, and enable the five Management VLANs and configure their DHCP servers.

### Firewall Rules

The Management zone is highly privileged and trusted. The primary security principle is that **no other VLAN should be allowed to initiate traffic *to* the Management VLAN**. These rules are configured on the other VLANs' interfaces. The rules below govern outbound traffic *from* the Management VLANs.

#### For MGMT_WIRED_1G (VLAN 51) and MGMT_WIFI (VLAN 54):
*   These VLANs are for trusted administrators and need broad access to manage other network resources.
1.  **Allow Full Internal and Internet Access:** Create a single `Pass` rule.
    -   **Action:** Pass
    -   **Source:** `MGMT_WIRED_1G net` (or `MGMT_WIFI net`)
    -   **Destination:** `Any`

#### For MGMT_MONITOR (VLAN 55):
*   This VLAN should be isolated to only collect data.
1.  **Block All Traffic:** Create a rule to **block** all traffic from `MGMT_MONITOR net` to `Any`.
2.  **Add Pass Rules if Needed:** If your monitoring tools need to send data to a specific server, add a specific `Pass` rule for that traffic *above* the block rule.

#### For Reserved VLANs (52, 53):
*   These VLANs should have no devices. For security, create a single rule on each interface to **block** all traffic from the VLAN's subnet to `Any`.
