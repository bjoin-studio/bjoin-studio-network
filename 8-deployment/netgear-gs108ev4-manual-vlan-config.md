# Netgear GS108Ev4 Manual VLAN Configuration Guide

This guide provides step-by-step instructions for configuring VLANs and port settings on your Netgear GS108Ev4 (firmware v1.0.1.3) switch using its web-based graphical user interface (GUI).

**Important Note:** This switch model does not support command-line interface (CLI) access for configuration. All settings must be applied manually through the web GUI.

## 1. Accessing the Switch Web Interface

1.  Open a web browser from a computer connected to the same network as the switch.
2.  Enter the IP address of the switch (e.g., `10.20.51.5`) in the browser's address bar.
3.  A login window will open. Enter the device management password. (The default password is `password`. You should change this immediately upon first login).
4.  The HOME page will display.

## 2. Activating Advanced 802.1Q VLAN Mode

The Netgear GS108Ev4 supports "Advanced 802.1Q VLAN" mode, which is necessary for creating tagged (trunk) ports and untagged (access) ports with specific VLAN IDs.

1.  From the menu at the top of the page, select **SWITCHING**.
2.  From the menu on the left, select **VLAN**.
3.  In the "Advanced 802.1Q VLAN" section, click the **ACTIVATE MODE** button.
4.  A pop-up warning window will open, informing you that current VLAN settings will be lost. Click **CONTINUE**.
5.  Your settings are saved, and VLAN 1 is added by default, with all ports as untagged members.

## 3. Creating VLANs (1, 11-15, 21-25, 31-35, 41-45, 51-55, 61-65)

You will create each required VLAN and assign it a name. For a full list of VLANs and their purposes, refer to the `bjoin-studio-network-design.md` document.

1.  In the "Advanced 802.1Q VLAN" pane, click the **ADD VLAN** button.
2.  Specify the settings for the new VLAN:
    *   **VLAN Name:** Enter a descriptive name (e.g., `Default`, `PRODUCTION_1Gb`).
    *   **VLAN ID:** Enter the corresponding VLAN ID (e.g., `1`, `11`).
    *   **Ports:** For now, you can leave all ports as "Exclude" (E). We will configure port membership in the next step.
3.  Click the **APPLY** button.
4.  Repeat steps 1-3 for all VLANs defined in your network design.

## 4. Configuring Port Membership and PVIDs

This step involves setting each port's VLAN membership (Tagged/Untagged/Excluded) and its PVID (Port VLAN ID) according to your desired configuration.

1.  In the "Advanced 802.1Q VLAN" pane, you will see a table listing your created VLANs.
2.  For each VLAN, click the **EDIT** button in its row.
3.  You will see a representation of the switch ports. For each port, select its membership:
    *   **T (Tagged):** For Trunk ports, traffic for this VLAN will be tagged.
    *   **U (Untagged):** For Access ports, traffic for this VLAN will be untagged. A port can only be an untagged member of one VLAN.
    *   **E (Excluded):** The port is not a member of this VLAN.

### Configuring Port 7 as a Trunk Port (All VLANs)

To configure Port 7 as a trunk port that carries all VLANs (1, 11-15, 21-25, 31-35, 41-45, 51-55, 61-65):

1.  For **VLAN 1 (Default)**:
    *   Set Port 7 to **U (Untagged)**. This makes VLAN 1 the Native VLAN for the trunk.
    *   Set all other VLANs (11-15, 21-25, etc.) to **T (Tagged)** for Port 7.
2.  For all other VLANs (11-15, 21-25, 31-35, 41-45, 51-55, 61-65):
    *   Set Port 7 to **T (Tagged)**.
    *   Set all other ports to **E (Excluded)** or **U (Untagged)** as per their specific access VLAN configuration.

### Configuring Other Access Ports (Example: Port 5 for VLAN 51)

To configure an access port (e.g., Port 5 for VLAN 51):

1.  For **VLAN 51 (MANAGEMENT)**:
    *   Set Port 5 to **U (Untagged)**.
    *   Set all other VLANs to **E (Excluded)** for Port 5.
2.  For **VLAN 1 (Default)**:
    *   Set Port 5 to **E (Excluded)**.

### Setting Port VLAN IDs (PVIDs)

Navigate to the **PVID Table** section (usually under the VLAN menu) to explicitly set the PVID for each port. Ensure the PVID matches the untagged VLAN for access ports.

*   **For Port 7 (Trunk):** Set PVID to `1` (the Native VLAN).
*   **For Access Ports (e.g., Port 5):** Set PVID to the VLAN ID of the untagged VLAN (e.g., `51` for Port 5).

After configuring each VLAN's port membership and PVIDs, click **APPLY**.

## 5. Saving Configuration

After making all changes, ensure you save the configuration to the switch's startup configuration to prevent losing your settings after a reboot.

1.  From the menu at the top of the page, select **MAINTENANCE**.
2.  From the menu on the left, select **SAVE CONFIGURATION**.
3.  Click the **SAVE** button.
