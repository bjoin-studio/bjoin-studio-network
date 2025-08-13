# OPNsense Management VLAN Configuration (VLANs 51-53)

This guide provides step-by-step instructions for configuring the Management VLANs (51, 52, and 53) in OPNsense. These VLANs are critical for network security and administration.

## 1. VLAN Definitions

| VLAN ID | Name             | Subnet           | Gateway IP     | Purpose                                      |
|:--------|:-----------------|:-----------------|:---------------|:---------------------------------------------|
| **51**  | MGMT_DEVICES     | `10.20.51.0/24`  | `10.20.51.1`   | For direct management of network hardware.   |
| **52**  | MGMT_RESERVED    | `10.20.52.0/24`  | `10.20.52.1`   | Reserved for future management needs.        |
| **53**  | MGMT_MONITORING  | `10.20.53.0/24`  | `10.20.53.1`   | For telemetry, syslog, and monitoring traffic. |

---

## 2. Step-by-Step Configuration

These steps assume you have already configured your LAN and WAN interfaces as per the `opnsense-initial-setup-guide.md`.

### Step 2.1: Create the VLANs

For each VLAN (51, 52, 53):

1.  Navigate to **Interfaces > Other Types > VLAN**.
2.  Click **+ Add**.
3.  Fill in the details:
    -   **Parent interface:** Your main LAN interface (e.g., `igb1`).
    -   **VLAN tag:** The VLAN ID (`51`, `52`, or `53`).
    -   **Description:** A clear name (e.g., `MGMT_DEVICES`, `MGMT_MONITORING`).
4.  Click **Save**. Repeat for all three VLANs.

### Step 2.2: Assign and Enable the Interfaces

1.  Navigate to **Interfaces > Assignments**.
2.  You will see your new VLANs available in the "New interface" dropdown.
3.  Click the **+** button to assign each VLAN. They will be named `OPT1`, `OPT2`, etc. by default.
4.  Click on each new `OPTx` interface to configure it:
    -   Check the **Enable** box.
    -   Change the **Description** to the VLAN name (e.g., `MGMT_DEVICES`).
    -   Set **IPv4 Configuration Type** to **Static**.
    -   Under "Static IPv4 configuration", set the IP address (e.g., `10.20.51.1` / `24`).
    -   Click **Save** and **Apply Changes**.
5.  Repeat for all three management interfaces.

### Step 2.3: Configure DHCP Server (Optional)

While most devices on these VLANs should have static IPs, you can set up a DHCP server for specific use cases.

1.  Navigate to **Services > DHCPv4 > [MGMT_MONITORING]**.
2.  Check **Enable DHCP server**.
3.  Set a small **Range** (e.g., `10.20.53.100` to `10.20.53.150`).
4.  Click **Save**.

### Step 2.4: Firewall Rules

It is critical to restrict access to these management VLANs.

1.  Navigate to **Firewall > Rules > [MGMT_DEVICES]**.
2.  Add a rule to allow access from a specific, secured admin workstation or VLAN.
    -   **Action:** Pass
    -   **Interface:** MGMT_DEVICES
    -   **Protocol:** Any
    -   **Source:** (e.g., an alias for your admin PC's IP)
    -   **Destination:** This Firewall
3.  Add a "Block All" rule at the bottom to prevent any other access.
    -   **Action:** Block
    -   **Interface:** MGMT_DEVICES
    -   **Protocol:** Any
    -   **Source:** Any
    -   **Destination:** Any

Apply similar restrictive rules to the other management VLANs, only allowing traffic from trusted sources.
