# OPNsense Guest WiFi VLAN Configuration (VLAN 61)

This guide provides step-by-step instructions for configuring the Guest WiFi VLAN. This zone is for providing internet access to visitors and must be completely isolated from the internal network.

## 1. VLAN Definition

| VLAN ID | Name         | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:-------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **61**  | GUEST_WIFI   | `10.20.61.0/24`  | `10.20.61.1`   | `10.20.61.100 – 200` | For internet-only access for visitors.       |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create, Assign, and Enable Interface

Follow the procedures in the previous guides to create VLAN 61 and assign it to an enabled interface with a static IP as defined in the table above.

### Step 2.2: Configure DHCP Server

Enable the DHCP server for the `GUEST_WIFI` interface and set the correct IP range. It is also a good idea to set the DNS servers here to public ones (e.g., `1.1.1.1`, `8.8.8.8`) directly, rather than your internal DNS.

### Step 2.3: Firewall Rules

The key principle for the Guest WiFi is **internet only**.

Navigate to **Firewall > Rules > GUEST_WIFI**.

1.  **Block All Internal Access:** Create a rule at the top to block any traffic from the `GUEST_WIFI net` to all internal networks.
    -   **Action:** Block
    -   **Source:** `GUEST_WIFI net`
    -   **Destination:** `RFC 1918` (This is a built-in alias for all private IP address space)
2.  **Allow Internet Access:** Create a rule below the block rule to allow traffic to any other destination.
    -   **Action:** Pass
    -   **Source:** `GUEST_WIFI net`
    -   **Destination:** `Any`

This simple rule set ensures guests can access the internet but are strictly prohibited from accessing any of your internal network resources.
