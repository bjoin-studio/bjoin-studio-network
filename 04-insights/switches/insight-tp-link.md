# Insights for Working with TP-Link Switches

This document consolidates key learnings and configuration patterns for TP-Link switches, based on experiences within the bjoin.studio network.

## 1. L3 Interface and Management IP

### Insight: Assign IPs to VLAN Interfaces, Not Physical Ports or LAGs

On TP-Link L2+ or L3-Lite switches, you cannot assign an IP address directly to a physical port or a Link Aggregation Group (LAG) interface when it's part of a tagged VLAN setup. The correct method is to use a Switched Virtual Interface (SVI), which TP-Link calls a "VLAN Interface" under the **L3 Features > Interface** menu.

**Correct Procedure for Management IP:**
1.  Navigate to **L3 Features > Interface**.
2.  Click **Add** to create a new interface.
3.  Select the desired management VLAN (e.g., VLAN 51).
4.  Set the **IP Address Mode** to **Static**.
5.  Enter the static IP address, subnet mask, and default gateway for the switch.

## 2. LACP and LAG Configuration

### Insight: Use LACP, Not Static LAG

TP-Link switches offer both Static LAG and LACP (802.3ad) configuration. For production environments, **always use LACP**.

*   **LACP (Recommended):** A dynamic protocol that actively negotiates the link bundle. It can detect link failures and automatically remove a bad link from the LAG, preventing packet loss.
*   **Static LAG:** A manual configuration with no failure detection. It is less robust and should only be used if the connecting device does not support LACP.

**Configuration Steps:**
1.  Navigate to the **LACP Config** page.
2.  For the desired member ports, set **Status** to **Enabled**.
3.  Set **Mode** to **Active** (to initiate LACP negotiation) rather than Passive.
4.  Ensure all member ports are assigned to the same **Group ID**.

### Insight: Use IP-Based Hashing for Better Load Balancing

For a LAG connecting to a router or another switch in a multi-VLAN environment, the best hashing algorithm is based on IP addresses.

*   **Recommended:** **SRC IP + DST IP**. This provides the best traffic distribution by creating a hash based on the source and destination IP addresses of the actual traffic flows, avoiding hotspots that can occur with MAC-based hashing when traffic is primarily to/from a single router.

### Insight: Configure VLANs on the LAG, Not Member Ports

Once ports are bundled into a LAG, that LAG acts as a single logical interface. All VLAN configuration must be done on the LAG itself, not on the individual physical ports that are members of the LAG.

*   **Correct Method:** In the VLAN configuration menus, use the **`LAGs` tab** to assign VLAN membership to `LAG1`, `LAG2`, etc.
*   **Incorrect Method:** Do not use the `UNIT1` tab to assign VLANs to the individual physical ports (e.g., 1/0/25, 1/0/26) that are part of the LAG. This will cause configuration conflicts.

## 3. VLAN Port Configuration (Trunk vs. Access)

### Insight: TP-Link Uses "Tagged" and "Untagged" for Port Modes

TP-Link's web interface uses specific terminology for defining trunk and access ports within the **802.1Q VLAN** menu.

*   **Trunk Port (Carries Multiple VLANs):** A port is configured as a trunk by making it a **`Tagged`** member of every VLAN you want it to carry.

*   **Access Port (Carries a Single VLAN):** A port is configured as an access port with two steps:
    1.  Make the port an **`Untagged`** member of the desired VLAN.
    2.  Set the port's **`PVID`** (Port VLAN ID) to match the VLAN ID. This ensures any untagged traffic from a connected device (like a computer) is correctly placed into that VLAN.

### Insight: Trunk Ports Require Specific VLAN Hygiene

For a trunk link (like an LACP LAG) to function correctly and securely, apply the following settings:

1.  **Use Tagged Membership:** The LAG interface must be a **`Tagged`** member of any VLAN it carries.
2.  **Remove from Default VLAN:** The LAG should be explicitly removed as a member of the default VLAN (VLAN 1) to prevent unintended traffic.
3.  **Set PVID to an Unused VLAN:** The PVID of the LAG should be set to `1` or another unused VLAN. Since a trunk should only receive tagged traffic, this prevents any accidental untagged frames from leaking into a production VLAN.

## 4. System Configuration

### Insight: Configuration Must Be Manually Saved

TP-Link switches **do not automatically save the running configuration**. Any changes made will be lost if the switch reboots or loses power.

*   **Action:** Always click the **Save Configuration** button (typically in the top menu bar or under a System/Maintenance menu) after making changes.
*   **CLI Command:** The equivalent CLI command is `copy running-config startup-config` or simply `write`.