# OPNsense Guest WiFi VLAN Configuration (VLAN 61)

This guide provides step-by-step instructions for configuring the Guest WiFi VLAN. This zone is for providing internet access to visitors and must be completely isolated from the internal network.

## 1. VLAN Definition

| VLAN ID | Name             | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:-----------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **61**  | GUEST_WIRED_1    | `10.20.61.0/24`  | `10.20.61.1`   | `10.20.61.100 – 200` | Guest Wired (1Gb)                            |
| **64**  | GUEST_WIFI       | `10.20.64.0/24`  | `10.20.64.1`   | `10.20.64.100 – 200` | Guest Wireless                               |
| **65**  | GUEST_MONITOR    | `10.20.65.0/24`  | `10.20.65.1`   | `10.20.65.100 – 200` | Guest Monitoring                             |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create, Assign, and Enable Interface

**Note:** OPNsense and your switches will use the **802.1Q** VLAN standard, which is the universal protocol for this type of network segmentation. When you create a VLAN, this is the standard being used.

Follow the procedures in the previous guides to create VLANs (61, 64, 65) and assign them to enabled interfaces with static IPs as defined in the table above.

### Step 2.2: Configure DHCP Server

Enable the DHCP server for each Guest VLAN interface and set the correct IP range. It is also a good idea to set the DNS servers here to public ones (e.g., `1.1.1.1`, `8.8.8.8`) directly, rather than your internal DNS.

### Step 2.3: Firewall Rules

The key principle for the Guest WiFi is **internet only**.

Navigate to **Firewall > Rules > GUEST_WIRED_1**.

1.  **Block All Internal Access:** Create a rule at the top to block any traffic from the `GUEST_WIRED_1 net` to all internal networks.
    -   **Action:** Block
    -   **Source:** `GUEST_WIRED_1 net`
    -   **Destination:** `RFC 1918` (This is a built-in alias for all private IP address space)
2.  **Allow Internet Access:** Create a rule below the block rule to allow traffic to any other destination.
    -   **Action:** Pass
    -   **Source:** `GUEST_WIRED_1 net`
    -   **Destination:** `Any`

This simple rule set ensures guests can access the internet but are strictly prohibited from accessing any of your internal network resources.

Apply similar rules for **GUEST_WIFI** and **GUEST_MONITOR**.
