# OPNsense Studio VLAN Configuration (VLANs 31, 32, 33, 34)

This guide provides step-by-step instructions for configuring the Studio VLANs. This is the core creative environment for editing, color grading, and VFX.

## 1. VLAN Definitions

| VLAN ID | Name             | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:-----------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **31**  | STUDIO_WIRED_1   | `10.20.31.0/24`  | `10.20.31.1`   | `10.20.31.100 – 200` | Studio Wired (1Gb)                           |
| **32**  | STUDIO_WIRED_10   | `10.20.32.0/24`  | `10.20.32.1`   | `10.20.32.100 – 200` | Studio Wired (10Gb)                          |
| **33**  | STUDIO_WIRED_100   | `10.20.33.0/24`  | `10.20.33.1`   | Static only          | Studio Wired (100Gb)                         |
| **34**  | STUDIO_WIFI      | `10.20.34.0/24`  | `10.20.34.1`   | `10.20.34.100 – 200` | Studio Wireless                              |
| **35**  | STUDIO_MONITOR   | `10.20.35.0/24`  | `10.20.35.1`   | `10.20.35.100 – 200` | Studio Monitoring                            |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create, Assign, and Enable Interfaces

**Note:** OPNsense and your switches will use the **802.1Q** VLAN standard, which is the universal protocol for this type of network segmentation. When you create a VLAN, this is the standard being used.

Follow the procedures in the previous guides to create the VLANs (31, 32, 33, 34, 35) and assign them to enabled interfaces with static IPs as defined in the table above.

### Step 2.2: Configure DHCP Server

Enable the DHCP server for each Studio VLAN that requires it (31, 32, 34, 35) and set the correct IP range.

### Step 2.3: Firewall Rules

The high-performance Studio VLANs have broad access, while the general workstations are more restricted.

#### For STUDIO_WIRED_10 (VLAN 32) and STUDIO_WIRED_100 (VLAN 33):
1.  **Allow DNS and Management Access:** Allow traffic to the Management VLAN for DNS and other administrative services.
2.  **Allow Broad Internal Access:** These VLANs need to access assets from other zones. Create a rule to allow traffic *from* `STUDIO_WIRED_10 net` *to* `ProductionNet` and `StageNet` aliases.
3.  **Allow Internet:** Allow traffic to `! (RFC 1918)` for internet access.

#### For STUDIO_WIRED_1 (VLAN 31):
1.  **Allow DNS and Management Access.**
2.  **Block Other Production Zones:** Explicitly block traffic from `STUDIO_WIRED_1 net` to `StageNet`, `WorkshopNet`, etc.
3.  **Allow Limited Internet.

Apply similar rules for **STUDIO_WIFI** and **STUDIO_MONITOR**.**
