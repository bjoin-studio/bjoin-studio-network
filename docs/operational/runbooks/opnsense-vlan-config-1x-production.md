# OPNsense Production VLAN Configuration (VLANs 11-15)

This guide provides step-by-step instructions for configuring the Production VLANs (11-15) in OPNsense. These VLANs are used for general office work, administrative tasks, and network monitoring.

## 1. VLAN Definitions

This table is a subset of the master design plan, focused only on the Production zone.

| VLAN ID | Name | Purpose | Subnet | Gateway IP | DHCP Range |
|:---|:---|:---|:---|:---|:---|
| **11** | `PROD_WIRED_1G` | Production Wired (1Gb) | `10.20.11.0/24` | `10.20.11.1` | `10.20.11.100 – 200` |
| **12** | `PROD_WIRED_10G` | Production Wired (10Gb) | `10.20.12.0/24` | `10.20.12.1` | `10.20.12.100 – 200` |
| **13** | `PROD_RESERVED` | Production Reserved | `10.20.13.0/24` | `10.20.13.1` | Static only |
| **14** | `PROD_WIFI` | Production Wifi | `10.20.14.0/24` | `10.20.14.1` | `10.20.14.100 – 200` |
| **15** | `PROD_MONITOR` | Production Monitoring | `10.20.15.0/24` | `10.20.15.1` | `10.20.15.100 – 200` |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create the VLANs

For each VLAN (11, 12, 13, 14, 15):

1.  Navigate to **Interfaces > Other Types > VLAN**.
2.  Click **+ Add**.
3.  Fill in the details:
    -   **Parent interface:** Your main LAN interface (e.g., `igb1`).
    -   **VLAN tag:** The VLAN ID.
    -   **Description:** A clear name (e.g., `PROD_WIRED_1G`).
4.  Click **Save**. Repeat for all five VLANs.

### Step 2.2: Assign and Enable the Interfaces

1.  Navigate to **Interfaces > Assignments**.
2.  Assign each new VLAN to an interface.
3.  Click on each new interface to configure it:
    -   Check the **Enable** box.
    -   Change the **Description** to the VLAN name from the table.
    -   Set **IPv4 Configuration Type** to **Static**.
    -   Set the **IPv4 Address** (e.g., `10.20.11.1` / `24`).
    -   Click **Save** and **Apply Changes**.
4.  Repeat for all five Production interfaces.

### Step 2.3: Configure DHCP Server

1.  Navigate to **Services > DHCPv4**.
2.  You will see a tab for each new interface.
3.  For each interface that requires DHCP (11, 12, 14, 15), enable the DHCP server and set the **Range** as defined in the table above.
4.  **VLAN 13 (PROD_RESERVED)** does not require a DHCP server.
5.  Click **Save** on each tab.

### Step 2.4: Firewall Rules

Navigate to **Firewall > Rules** and select the tab for each Production VLAN to create these rules. A key principle is that the Production zone should not be able to initiate contact with other zones like Stage or Studio.

#### For General VLANs (11, 12, 14):
1.  **Allow DNS:** Create a rule to allow traffic to your DNS servers (e.g., `10.20.51.10`) on port 53.
2.  **Allow Internet Access:** Create a rule allowing traffic from the VLAN's subnet (e.g., `PROD_WIRED_1G net`) to any destination *not* in the local network.
    -   **Action:** Pass
    -   **Source:** `PROD_WIRED_1G net`
    -   **Destination:** `! RFC 1918` (This is an alias for all private IP space)
3.  **Block Other Zones:** Add a rule at the bottom to block all traffic from this VLAN's subnet to the `RFC 1918` alias. This ensures no traffic can reach other internal zones.

#### For PROD_MONITOR (VLAN 15):
*   This VLAN should be isolated. Create a rule to **block** all traffic from `PROD_MONITOR net` to `Any`.
*   If your monitoring tools need to send data to a central server (e.g., in the Management VLAN), you can add a specific `Pass` rule for that traffic *above* the block rule.

#### For PROD_RESERVED (VLAN 13):
*   This VLAN should have no devices. For security, create a single rule to **block** all traffic from `PROD_RESERVED net` to `Any`.