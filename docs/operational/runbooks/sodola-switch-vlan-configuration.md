# Sodola 8-Port 10G Switch VLAN Configuration

This guide provides step-by-step instructions for configuring VLANs on the Sodola KT-NOS SL-SWTGW2C8F managed switch. This switch acts as the main distribution switch in the bjoin.studio network.

## 1. Prerequisites

*   OPNsense firewall is configured with all necessary VLANs as defined in `bjoin-studio-network-design.md`.
*   You have access to the Sodola switch's web management interface (e.g., `http://10.20.51.3`).

## 2. Key VLAN Concepts on Managed Switches

*   **Tagged Port (Trunk Port):** A port that carries traffic for multiple VLANs. Each frame leaving or entering this port will have an 802.1Q VLAN tag. Used for connections between switches and to the firewall.
*   **Untagged Port (Access Port):** A port that carries traffic for only one VLAN. Frames leaving or entering this port do not have a VLAN tag. Used for connecting end devices (computers, servers, printers).
*   **PVID (Port VLAN ID):** For an untagged port, the PVID specifies which VLAN untagged traffic entering that port belongs to.

## 3. Accessing the Switch

1.  Ensure your laptop is connected to a port on the Sodola switch that is configured for VLAN 51 (Management).
2.  Open a web browser and navigate to `http://10.20.51.3`.
3.  Log in with your credentials.

## 4. Changing the Management VLAN (from Default VLAN 1 to 51)

For security, the switch's management interface should be moved from the default VLAN 1 to the dedicated management VLAN 51. This is a one-time setup process.

The switch's web GUI has three key submenus under the main **VLAN Menu**:
*   **Create VLAN**
*   **VLAN Configuration Membership**
*   **Port Setting**

### Step 4.1: Create VLAN 51

*   Navigate to the **Create VLAN** submenu.
*   If VLAN 51 is not already in the list, create it.

### Step 4.2: Configure Port Settings (PVID)

This step configures a dedicated, *untagged* port that you can use to directly manage the switch. We will use **Port 8** as the dedicated management port in this guide.

*   Navigate to the **Port Setting** submenu.
*   For **Port 8**, set its **PVID** to **51**.

This tells the switch: "Any device that plugs into Port 8 and sends normal, untagged traffic should be considered part of VLAN 51."

### Step 4.3: Configure VLAN Membership

*   Navigate to the **VLAN Configuration Membership** submenu.
*   Select **VLAN 51** to configure its port membership.
    *   **Port 8 (Your Management Port):** Set this to **Untagged**.
    *   **TE1 (Uplink to Firewall):** Set this to **Tagged**. This is essential for the trunk to carry management traffic.
    *   **Other Ports:** You can leave them as "Not Member" for now.

### Step 4.4: Change the Switch's Management IP and VLAN

*   Navigate to the **System** or **IP Configuration** menu.
*   Configure the following:
    *   **IP Address:** `10.20.51.3`
    *   **Subnet Mask:** `255.255.255.0`
    *   **Default Gateway:** `10.20.51.1`
    *   **Management VLAN:** Change this setting from `1` to **`51`**.

**IMPORTANT:** You will lose access. To regain it, connect your computer to **Port 8** and set a static IP on your computer (e.g., `10.20.51.99`).

## 5. Step-by-Step VLAN Configuration

Navigate to the VLAN configuration section in the switch's web interface.

### Step 5.1: Create All VLANs

You must create all VLANs from the master design plan. Navigate to the **Create VLAN** submenu and add the following entries one by one. The name should match the purpose from the design document.

*   VLAN 11: `Production Wired (1Gb)`
*   VLAN 12: `Production Wired (10Gb)`
*   VLAN 13: `Production Reserved`
*   VLAN 14: `Production Wifi`
*   VLAN 15: `Production Monitoring`
*   VLAN 21: `Stage Wired (1Gb)`
*   VLAN 22: `Stage Wired (10Gb)`
*   VLAN 23: `Stage Reserved`
*   VLAN 24: `Stage Wifi`
*   VLAN 25: `Stage Monitoring`
*   VLAN 31: `Studio Wired (1Gb)`
*   VLAN 32: `Studio Wired (10Gb)`
*   VLAN 33: `Studio Wired (100Gb)`
*   VLAN 34: `Studio Wifi`
*   VLAN 35: `Studio Monitoring`
*   VLAN 41: `Workshop Wired (1Gb)`
*   VLAN 42: `Workshop Reserved`
*   VLAN 43: `Workshop Reserved`
*   VLAN 44: `Workshop Wifi`
*   VLAN 45: `Workshop Monitoring`
*   VLAN 51: `Management Wired (1Gb)`
*   VLAN 52: `Management Reserved`
*   VLAN 53: `Management Reserved`
*   VLAN 54: `Management Wifi`
*   VLAN 55: `Management Monitoring`
*   VLAN 61: `Guest Wired (1Gb)`
*   VLAN 62: `Guest Reserved`
*   VLAN 63: `Guest Reserved`
*   VLAN 64: `Guest Wifi`
*   VLAN 65: `Guest Monitoring`

### Step 5.2: Configure Port VLAN Membership

This is the most critical step. The following is the new recommended configuration based on your requirements.

| Port | Role | VLAN Membership (Tagged/Untagged) | PVID | Notes |
|:-----|:-----|:----------------------------------|:-----|:------|
| **TE1** | Access: Production (10Gb) | VLAN 11 (Untagged) | 11 | For high-speed Production workstations or servers. |
| **TE2** | Access: Stage (10Gb) | VLAN 21 (Untagged) | 21 | For high-speed Stage workstations or servers. |
| **TE3** | Access: Studio (10Gb) | VLAN 31 (Untagged) | 31 | For high-speed Studio workstations or servers. |
| **TE4** | Access: Workshop (10Gb) | VLAN 41 (Untagged) | 41 | For high-speed Workshop devices. |
| **TE5** | Access: Management (10Gb) | VLAN 51 (Untagged) | 51 | For high-speed Management devices (e.g., Proxmox host). |
| **TE6** | Access: Guest (10Gb) | VLAN 61 (Untagged) | 61 | For high-speed Guest devices. |
| **TE7** | **Uplink to Switches** | All VLANs (Tagged) | 1 | Trunk to other switches (e.g., Netgear GS108Ev4). |
| **TE8** | **Uplink to Firewall** | All VLANs (Tagged) | 1 | Main "Router-on-a-Stick" trunk to OPNsense. |

**Configuration Steps in Web GUI:**

1.  **Configure Trunk Ports (TE7, TE8):**
    *   Go to **VLAN Configuration Membership**.
    *   For **each VLAN ID** you created, set ports **TE7 and TE8** to **Tagged**.
    *   Go to the **Port Setting** submenu.
    *   Ensure the **PVID** for **TE7 and TE8** is set to **1** (default).

2.  **Configure Access Ports (TE1-TE6):**
    *   Go to **VLAN Configuration Membership**.
    *   For **VLAN 11**, set **TE1** to **Untagged**.
    *   For **VLAN 21**, set **TE2** to **Untagged**.
    *   For **VLAN 31**, set **TE3** to **Untagged**.
    *   For **VLAN 41**, set **TE4** to **Untagged**.
    *   For **VLAN 51**, set **TE5** to **Untagged**.
    *   For **VLAN 61**, set **TE6** to **Untagged**.
    *   For each of these ports, ensure they are **not members** of any other VLAN.

3.  **Set PVID for Access Ports (TE1-TE6):**
    *   Go to the **Port Setting** submenu.
    *   Set **PVID** for **TE1** to **11**.
    *   Set **PVID** for **TE2** to **21**.
    *   Set **PVID** for **TE3** to **31**.
    *   Set **PVID** for **TE4** to **41**.
    *   Set **PVID** for **TE5** to **51**.
    *   Set **PVID** for **TE6** to **61**.

## 6. Save Configuration

**Important:** After making all changes, ensure you save the configuration to the switch's startup-config. Otherwise, changes will be lost on reboot.
