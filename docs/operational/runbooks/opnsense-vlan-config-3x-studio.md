# OPNsense Studio VLAN Configuration (VLANs 31, 32, 33, 34)

This guide provides step-by-step instructions for configuring the Studio VLANs. This is the core creative environment for editing, color grading, and VFX.

## 1. VLAN Definitions

| VLAN ID | Name             | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:-----------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **31**  | STUDIO_GENERAL   | `10.20.31.0/24`  | `10.20.31.1`   | `10.20.31.100 – 200` | For general creative workstations.           |
| **32**  | STUDIO_PERF      | `10.20.32.0/24`  | `10.20.32.1`   | `10.20.32.100 – 200` | For high-performance media editing.          |
| **33**  | STUDIO_ULTRA     | `10.20.33.0/24`  | `10.20.33.1`   | Static only          | For 100G SAN/NAS systems and media servers.  |
| **34**  | STUDIO_WIFI      | `10.20.34.0/24`  | `10.20.34.1`   | `10.20.34.100 – 200` | For creative team wireless devices.          |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create, Assign, and Enable Interfaces

Follow the procedures in the previous guides to create the VLANs (31, 32, 33, 34) and assign them to enabled interfaces with static IPs as defined in the table above.

### Step 2.2: Configure DHCP Server

Enable the DHCP server for each Studio VLAN that requires it (31, 32, 34) and set the correct IP range.

### Step 2.3: Firewall Rules

The high-performance Studio VLANs have broad access, while the general workstations are more restricted.

#### For STUDIO_PERF (VLAN 32) and STUDIO_ULTRA (VLAN 33):
1.  **Allow DNS and Management Access:** Allow traffic to the Management VLAN for DNS and other administrative services.
2.  **Allow Broad Internal Access:** These VLANs need to access assets from other zones. Create a rule to allow traffic *from* `STUDIO_PERF net` *to* `ProductionNet` and `StageNet` aliases.
3.  **Allow Internet:** Allow traffic to `! (RFC 1918)` for internet access.

#### For STUDIO_GENERAL (VLAN 31):
1.  **Allow DNS and Management Access.**
2.  **Block Other Production Zones:** Explicitly block traffic from `STUDIO_GENERAL net` to `StageNet`, `WorkshopNet`, etc.
3.  **Allow Limited Internet.**
