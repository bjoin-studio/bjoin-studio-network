# OPNsense Workshop VLAN Configuration (VLANs 41, 44)

This guide provides step-by-step instructions for configuring the Workshop VLANs. This zone is for engineering and prototyping and is highly isolated.

## 1. VLAN Definitions

| VLAN ID | Name             | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:-----------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **41**  | WORKSHOP_ENG     | `10.20.41.0/24`  | `10.20.41.1`   | `10.20.41.100 – 200` | For CAD stations and engineering.            |
| **44**  | WORKSHOP_WIFI    | `10.20.44.0/24`  | `10.20.44.1`   | `10.20.44.100 – 200` | For tool-connected devices and diagnostics.  |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create, Assign, and Enable Interfaces

Follow the procedures in the previous guides to create the VLANs (41, 44) and assign them to enabled interfaces with static IPs as defined in the table above.

### Step 2.2: Configure DHCP Server

Enable the DHCP server for each Workshop VLAN interface and set the correct IP range.

### Step 2.3: Firewall Rules

The key principle for the Workshop is **complete isolation**.

Navigate to **Firewall > Rules** and select the tab for each Workshop VLAN.

1.  **Allow DNS (Optional):** If you need name resolution *within* the workshop, allow traffic to your internal DNS servers. If not, you can skip this.
2.  **Block All Outbound Traffic:** Create a rule that blocks any traffic from the `WORKSHOP_ENG net` to any destination.
    -   **Action:** Block
    -   **Source:** `WORKSHOP_ENG net`
    -   **Destination:** `Any`

This simple, restrictive rule set ensures the Workshop VLANs cannot access the internet or any other internal network zone.
