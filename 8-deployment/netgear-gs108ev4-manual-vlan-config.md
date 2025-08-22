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

## 3. Creating VLANs (1, 11, 21, 31, 41, 51, 61)

You will create each required VLAN and assign it a name.

1.  In the "Advanced 802.1Q VLAN" pane, click the **ADD VLAN** button.
2.  Specify the settings for the new VLAN:
    *   **VLAN Name:** Enter a descriptive name (e.g., `Default`, `PRODUCTION`).
    *   **VLAN ID:** Enter the corresponding VLAN ID (e.g., `1`, `11`, `21`, `31`, `41`, `51`, `61`).
    *   **Ports:** For now, you can leave all ports as "Exclude" (E). We will configure port membership in the next step.
3.  Click the **APPLY** button.
4.  Repeat steps 1-3 for each VLAN you need to create:
    *   **VLAN 1:** Default
    *   **VLAN 11:** PRODUCTION
    *   **VLAN 21:** STAGE
    *   **VLAN 31:** STUDIO
    *   **VLAN 41:** WORKSHOP
    *   **VLAN 51:** MANAGEMENT
    *   **VLAN 61:** GUEST

## 4. Configuring Port Membership and PVIDs

This step involves setting each port's VLAN membership (Tagged/Untagged/Excluded) and its PVID (Port VLAN ID) according to the switch's current configuration.

1.  In the "Advanced 802.1Q VLAN" pane, you will see a table listing your created VLANs.
2.  For each VLAN, click the **EDIT** button in its row.
3.  You will see a representation of the switch ports. For each port, select its membership:
    *   **T (Tagged):** For Trunk ports, traffic for this VLAN will be tagged.
    *   **U (Untagged):** For Access ports, traffic for this VLAN will be untagged. A port can only be an untagged member of one VLAN.
    *   **E (Excluded):** The port is not a member of this VLAN.

4.  **Configure each port's VLAN membership and PVIDs as follows:**

    *   **VLAN 1 (Default):**
        *   Port 1: **U** (Untagged)
        *   Port 2: **U** (Untagged)
        *   Port 3: **U** (Untagged)
        *   Port 4: **U** (Untagged)
        *   Port 5: **E** (Excluded)
        *   Port 6: **U** (Untagged)
        *   Port 7: **U** (Untagged)
        *   Port 8: **U** (Untagged) - This is the native VLAN for the trunk port.

    *   **VLAN 11 (PRODUCTION):**
        *   Port 1: **U** (Untagged)
        *   Port 8: **T** (Tagged)
        *   Others: **E** (Excluded)

    *   **VLAN 21 (STAGE):**
        *   Port 2: **U** (Untagged)
        *   Port 8: **T** (Tagged)
        *   Others: **E** (Excluded)

    *   **VLAN 31 (STUDIO):**
        *   Port 3: **U** (Untagged)
        *   Port 8: **T** (Tagged)
        *   Others: **E** (Excluded)

    *   **VLAN 41 (WORKSHOP):**
        *   Port 4: **U** (Untagged)
        *   Port 8: **T** (Tagged)
        *   Others: **E** (Excluded)

    *   **VLAN 51 (MANAGEMENT):**
        *   Port 5: **U** (Untagged)
        *   Port 8: **T** (Tagged)
        *   Others: **E** (Excluded)

    *   **VLAN 61 (GUEST):**
        *   Port 6: **U** (Untagged)
        *   Port 8: **T** (Tagged)
        *   Others: **E** (Excluded)

5.  After configuring each VLAN's port membership, click **APPLY**.

6.  **Set Port VLAN IDs (PVIDs):**
    Navigate to the **PVID Table** section (usually under the VLAN menu) to explicitly set the PVID for each port. Ensure the PVID matches the untagged VLAN for access ports.

    *   **Port 1 PVID:** `11`
    *   **Port 2 PVID:** `21`
    *   **Port 3 PVID:** `31`
    *   **Port 4 PVID:** `41`
    *   **Port 5 PVID:** `51`
    *   **Port 6 PVID:** `61`
    *   **Port 7 PVID:** `1`
    *   **Port 8 PVID:** `1` (This is the native VLAN for the trunk port)

7.  Click **APPLY** after setting PVIDs.