## Netgear GS108Ev4 Switch VLAN Configuration

This guide provides step-by-step instructions for configuring VLANs on the Netgear GS108Ev4 switch, specifically for integrating it into a network with a Sodola switch and providing VLAN 51 access to DHCP hosts.

**Proposed Topology:**
*   **Sodola TE7 (Trunk, All VLANs Tagged)** <---> **GS108Ev4 Port 8**
*   **Netgear GS105** <---> **GS108Ev4 Port 5**
*   DHCP hosts will connect to the GS105 (or other GS108Ev4 ports) and receive IP addresses from VLAN 51 (10.20.51.0/24).

**Assumptions:**
*   The GS108Ev4 is in its default state or has its VLANs deactivated.
*   The GS108Ev4 will connect to Sodola TE7 on Port 8.
*   The GS105 will connect to GS108Ev4 Port 5.

**Configuration Steps for Netgear GS108Ev4:**

1.  **Access the Web Management Interface:**
    *   Open a web browser and navigate to the IP address assigned to your GS108Ev4.
    *   Log in with your credentials.

2.  **Configure Management IP Address:**
    *   Navigate to the `System` or `IP Configuration` menu (the exact path may vary depending on firmware version).
    *   Configure the following settings:
        *   **IP Address:** `10.20.51.5`
        *   **Subnet Mask:** `255.255.255.0`
        *   **Default Gateway:** `10.20.51.1` (assuming your OPNsense firewall is the gateway for VLAN 51)
    *   Click `APPLY` or `SAVE` to save these settings.

3.  **Activate Advanced 802.1Q VLAN Mode:**
    *   From the top menu, select `SWITCHING`.
    *   From the left menu, select `VLAN`.
    *   In the `Advanced 802.1Q VLAN` section, click the `ACTIVATE MODE` button.
    *   Confirm the action when prompted (this will clear any existing VLAN settings).

4.  **Set Management VLAN:**
    *   Navigate to `SWITCHING > VLAN`.
    *   In the `Advanced 802.1Q VLAN` section, at the bottom of the configuration page, locate the `Management VLAN` field.
    *   Set the `Management VLAN` to `51`.
    *   Click `APPLY` or `SAVE` to save this setting.

5.  **Create VLAN 51:**
    *   In the `Advanced 802.1Q VLAN` pane, click the `ADD VLAN` button.
    *   For `VLAN Name`, enter `Management` (or a descriptive name like `VLAN51-Mgmt`).
    *   For `VLAN ID`, enter `51`.
    *   Initially, you can set all ports to `E` (Exclude) or `U` (Untagged). We'll configure them specifically in the next steps.
    *   Click `APPLY`.

6.  **Configure Port 8 (Connected to Sodola TE7):**
    *   This port will receive tagged traffic from the Sodola switch.
    *   In the `Advanced 802.1Q VLAN` table, click on the row for `VLAN 51` and then click the `EDIT` button.
    *   For **Port 8**, select `T` (Tagged). This makes Port 8 a tagged member of VLAN 51.
    *   If you need to pass other VLANs from the Sodola through the GS108Ev4, repeat this step for those VLANs on Port 8.
    *   Click `APPLY`.

7.  **Configure Port 5 (Connected to Netgear GS105):**
    *   This port will send/receive untagged traffic for VLAN 51 to the GS105.
    *   In the `Advanced 802.1Q VLAN` table, click on the row for `VLAN 51` and then click the `EDIT` button.
    *   For **Port 5**, select `U` (Untagged). This makes Port 5 an untagged member of VLAN 51.
    *   Click `APPLY`.

8.  **Set PVID for Port 5:**
    *   Navigate back to `SWITCHING > VLAN`.
    *   In the right pane, locate the `PVID Table` section and click the `PVID Table` link.
    *   For **Port 5**, select `VLAN 51` from the dropdown menu. This ensures any untagged traffic entering Port 5 is assigned to VLAN 51.
    *   Click `APPLY`.

9.  **Configure other access ports (if needed):**
    *   If you want other ports on the GS108Ev4 to directly provide untagged access to VLAN 51, repeat steps 5 and 6 for those ports.

10.  **Save Configuration:**
    *   After making all changes, ensure you save the configuration to the switch's startup configuration. Look for a `SAVE` button or a similar option in the web interface.

**Important Notes:**
*   **Netgear GS105:** If the GS105 is an unmanaged switch, no configuration is needed on it; it will simply pass the untagged VLAN 51 traffic. If it's a managed switch, ensure its uplink port to the GS108Ev4 is configured as an untagged port for VLAN 51, and its PVID is 51.
*   **DHCP Server:** Ensure your DHCP server for the 10.20.51.0/24 network is properly configured and reachable via VLAN 51 (typically on your OPNsense firewall).