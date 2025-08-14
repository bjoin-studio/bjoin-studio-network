# OPNsense Production VLAN Configuration (VLANs 11, 12, 14)

This guide provides step-by-step instructions for configuring the Production VLANs (11, 12, and 14) in OPNsense. These VLANs are used for general office work, administrative tasks, and high-performance rendering.

## 1. VLAN Definitions

| VLAN ID | Name           | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:---------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **11**  | PROD_WIRED_1   | `10.20.11.0/24`  | `10.20.11.1`   | `10.20.11.100 – 200` | Production Wired (1Gb)                       |
| **12**  | PROD_WIRED_2   | `10.20.12.0/24`  | `10.20.12.1`   | `10.20.12.100 – 200` | Production Wired (10Gb)                      |
| **14**  | PROD_WIFI      | `10.20.14.0/24`  | `10.20.14.1`   | `10.20.14.100 – 200` | Production Wireless                          |
| **15**  | PROD_MONITOR   | `10.20.15.0/24`  | `10.20.15.1`   | `10.20.15.100 – 200` | Production Monitoring                        |

---

## 2. Step-by-Step Configuration

These steps assume you have already configured your LAN and WAN interfaces.

### Step 2.1: Create the VLANs

**Note:** OPNsense and your switches will use the **802.1Q** VLAN standard, which is the universal protocol for this type of network segmentation. When you create a VLAN, this is the standard being used.

For each VLAN (11, 12, 14, 15):

1.  Navigate to **Interfaces > Other Types > VLAN**.
2.  Click **+ Add**.
3.  Fill in the details:
    -   **Parent interface:** Your main LAN interface (e.g., `igb1`).
    -   **VLAN tag:** The VLAN ID (`11`, `12`, `14`, or `15`).
    -   **Description:** A clear name (e.g., `PROD_WIRED_1`).
4.  Click **Save**. Repeat for all three VLANs.

### Step 2.2: Assign and Enable the Interfaces

1.  Navigate to **Interfaces > Assignments**.
2.  Assign each new VLAN to an interface.
3.  Click on each new interface to configure it:
    -   Check the **Enable** box.
    -   Change the **Description** to the VLAN name (e.g., `PROD_WIRED_1`).
    -   Set **IPv4 Configuration Type** to **Static**.
    -   Set the **IPv4 Address** (e.g., `10.20.11.1` / `24`).
    -   Click **Save** and **Apply Changes**.
4.  Repeat for all three Production interfaces.

### Step 2.3: Configure DHCP Server

1.  Navigate to **Services > DHCPv4**.
2.  You will see a tab for each new interface (e.g., `PROD_GENERAL`).
3.  For each interface, enable the DHCP server and set the **Range** as defined in the table above.
4.  Click **Save**.

### Step 2.4: Firewall Rules

Navigate to **Firewall > Rules** and select the tab for each Production VLAN to create these rules.

#### For PROD_WIRED_1 (VLAN 11):

1.  **Allow DNS:** Allow traffic to your DNS servers (e.g., `10.20.51.10`, `10.20.51.11`) on port 53.
2.  **Allow Internet Access:** Allow traffic from `PROD_WIRED_1 net` to any destination, but block it from reaching internal production zones.
    -   **Action:** Pass
    -   **Source:** `PROD_WIRED_1 net`
    -   **Destination:** `! (RFC 1918)` (This is an alias that means "not any internal IP address")
3.  **Block Internal Production Zones:** Add rules to explicitly block traffic from `PROD_WIRED_1 net` to `StageNet`, `StudioNet`, and `WorkshopNet` aliases.

Apply similar rules for **PROD_WIRED_2**, **PROD_WIFI**, and **PROD_MONITOR**.
