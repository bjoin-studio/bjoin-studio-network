# Sodola 8-Port 10G Switch VLAN Configuration

This guide provides step-by-step instructions for configuring VLANs on the Sodola 8-Port 10G managed switch. This switch acts as the main distribution switch in the bjoin.studio network.

## 1. Prerequisites

*   OPNsense firewall is configured with all necessary VLANs (11-61).
*   You have access to the Sodola switch's web management interface (e.g., `http://10.20.51.3`).

## 2. Key VLAN Concepts on Managed Switches

*   **Tagged Port (Trunk Port):** A port that carries traffic for multiple VLANs. Each frame leaving or entering this port will have an 802.1Q VLAN tag. Used for connections between switches and to the firewall.
*   **Untagged Port (Access Port):** A port that carries traffic for only one VLAN. Frames leaving or entering this port do not have a VLAN tag. Used for connecting end devices (computers, servers, printers) or unmanaged switches.
*   **PVID (Port VLAN ID):** For an untagged port, the PVID specifies which VLAN untagged traffic entering that port belongs to.

## 3. Accessing the Switch

1.  Ensure your laptop is connected to a port on the Sodola switch that is configured for VLAN 51 (Management).
2.  Open a web browser and navigate to `http://10.20.51.3`.
3.  Log in with your credentials.

## 4. Changing the Management VLAN (from Default VLAN 1 to 51)

For security, the switch's management interface should be moved from the default VLAN 1 to the dedicated management VLAN 51. This guide assumes you are initially connected to the switch on its default IP on VLAN 1.

The switch's web GUI provides three key submenus under the main **VLAN Menu**:
*   **Create VLAN**
*   **VLAN Configuration Membership**
*   **Port Setting**

Here is the step-by-step process to move the management interface to VLAN 51.

### Step 4.1: Create VLAN 51

The switch must be aware that VLAN 51 exists before you can assign it to anything.

*   Navigate to the **Create VLAN** submenu.
*   If VLAN 51 is not already in the list, create it.

### Step 4.2: Configure Port Settings (PVID)

This step configures a dedicated, *untagged* port that you can use to directly manage the switch. We will use **Port 6** as the example from the runbook.

*   Navigate to the **Port Setting** submenu. This is where you configure the **PVID (Port VLAN ID)**.
*   For **Port 6**, set its **PVID** to **51**.

This tells the switch: "Any device that plugs into Port 6 and sends normal, untagged traffic should be considered part of VLAN 51."

### Step 4.3: Configure VLAN Membership

Now, you must define how VLAN 51 behaves on all critical ports.

*   Navigate to the **VLAN Configuration Membership** submenu.
*   Select **VLAN 51** to configure its port membership.
    *   **Port 6 (Your Management Port):** Set this to **Untagged**. This makes it an access port for VLAN 51.
    *   **Port 1 (Uplink to Firewall):** Set this to **Tagged**. This is essential for the trunk to carry management traffic.
    *   **Port 4 (Uplink to Netgear):** Set this to **Tagged**. This is also a trunk port.
    *   **Other Ports:** You can leave them as "Not Member" for now.

### Step 4.4: Change the Switch's Management IP and VLAN

This is the final step. You must find the settings for the switch's own IP address. This is typically **not** in the VLAN menu.

*   Look for a different top-level menu, such as **"System"**, **"Management"**, or **"IP Configuration"**.
*   Inside that menu, configure the following:
    *   **IP Address:** `10.20.51.3`
    *   **Subnet Mask:** `255.255.255.0`
    *   **Default Gateway:** `10.20.51.1`
    *   **Management VLAN:** Change this setting from `1` to **`51`**.

**IMPORTANT: You will lose access to the switch after applying these changes.**

To regain access, you must:
1.  Connect your computer directly to **Port 6** (the untagged port you configured).
2.  Ensure your computer has a static IP in the same subnet (e.g., `10.20.51.99`).
3.  Navigate to the new management IP in your browser: **`http://10.20.51.3`**.

## 5. Step-by-Step VLAN Configuration

Navigate to the VLAN configuration section in the switch's web interface (usually under "VLAN" or "802.1Q VLAN").

### Step 5.1: Create All VLANs

Create all the VLANs that this switch will carry. For the Sodola, this means all VLANs from our design (11, 12, 14, 21, 22, 24, 31, 32, 33, 34, 41, 44, 51, 52, 53, 61).

### Step 5.2: Configure Port VLAN Membership

This is the most critical step. You will define which VLANs each port belongs to and whether traffic is tagged or untagged.

| Port | Role | VLANs (Tagged/Untagged) | PVID | Notes |
|:-----|:-----|:------------------------|:-----|:------|
| **TE1** | **Access Port (Example: Production General)** | VLAN 11 (Untagged) | 11 | For general Production workstations. Requires SFP+ to RJ45 transceiver. |
| **TE2** | **Uplink to BitEngine** | All VLANs (Tagged) | 1 (Default) | Trunk to BitEngine. Requires SFP+ to RJ45 transceiver. |
| **TE3** | **Uplink to Cisco Nexus** | All VLANs (Tagged) | 1 (Default) | Trunk to Cisco Nexus. |
| **TE4** | **Access Port (Example: Stage General)** | VLAN 21 (Untagged) | 21 | For general Stage workstations. Requires SFP+ to RJ45 transceiver. |
| **Port 5** | **Uplink to Firewall** | All VLANs (Tagged) | 1 (Default) | Main trunk from OPNsense. |
| **Port 6** | **Access Port (Example: Management)** | VLAN 51 (Untagged) | 51 | For connecting management devices directly. |
| **Port 7** | **Access Port (Example: Guest WiFi)** | VLAN 61 (Untagged) | 61 | For connecting Guest WiFi Access Points. |
| **Port 8** | **Uplink to Netgear GS108Ev4** | All VLANs (Tagged) | 1 (Default) | Trunk to Netgear GS108Ev4. |

### Understanding the VLAN Membership Table (Sodola Specific)

When configuring VLAN membership on the Sodola switch, you'll encounter specific terminology and port names:

*   **`1UP`:** This indicates that VLAN 1 is configured as the **Untagged** VLAN (also known as the Native VLAN) for that port, and it's also the **PVID** (Port VLAN ID). This is a common and often recommended configuration for trunk ports.
*   **`XXT` (e.g., `11T`, `51T`):** This signifies that the specified VLAN (e.g., VLAN 11, VLAN 51) is configured as a **Tagged** member on that port. This is essential for trunk ports carrying multiple VLANs.
*   **`TE1`, `TE2`, `TE3`, `TE4`:** These are specific names for the 10 Gigabit Ethernet (SFP+) ports on the Sodola switch. In your configuration, `TE2` is the uplink to BitEngine and `TE3` is the uplink to Cisco Nexus. `TE1` and `TE4` are configured as access ports.
*   **`LAG1`:** This refers to a **Link Aggregation Group**. Unless you have intentionally configured multiple physical ports to act as a single logical link (for increased bandwidth or redundancy), you should generally leave `LAG1` untagged or excluded. It's not typically used for standard single-cable connections.

Your configuration for `TE1`, `TE2`, `TE3`, and `TE4` (all relevant VLANs as `XXT` and `1UP`) is correct for their role as trunk ports. While you've included all defined VLANs, a small optimization for future configurations is to only tag VLANs that are actively in use on a given trunk, which can simplify troubleshooting.

**Configuration Steps in Web GUI (General):**
1.  Go to "VLAN" -> "802.1Q VLAN" -> "VLAN Membership" (or similar).
2.  For each VLAN, select it and then configure each port:
    *   **Tagged (T):** For trunk ports (Port 1, 2, 3, 4).
    *   **Untagged (U):** For access ports (Port 5, 6, 7, 8).
    *   **Not Member (N):** For ports that should not carry that VLAN.
3.  Go to "VLAN" -> "802.1Q VLAN" -> "PVID" (or "Port VLAN ID").
4.  For each port, set its PVID. For access ports, this should be the VLAN ID it's untagged for. For trunk ports, it's typically 1 (default) or the ID of the native VLAN if you're using one.

## 6. Save Configuration

**Important:** After making all changes, ensure you save the configuration to the switch's startup-config. Otherwise, changes will be lost on reboot.