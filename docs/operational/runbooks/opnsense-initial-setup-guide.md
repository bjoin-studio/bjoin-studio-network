# OPNsense Initial Installation and LAN Trunk Configuration

This guide provides the definitive, step-by-step procedure for installing OPNsense and correctly configuring the physical LAN port as a VLAN trunk without losing access.

## 1. Purpose of this Guide

The goal of this procedure is to configure your OPNsense firewall in a "Router-on-a-Stick" model. This means a single physical LAN port will act as a "trunk," carrying all tagged VLAN traffic to and from your managed switch. This is a powerful, standard practice for building secure and scalable networks. This guide walks you through the critical switchover process of moving from a default "flat" LAN to a secure, VLAN-based management interface.

## 2. Prerequisites

Before you begin, it is critical that you have:
1.  Read and understood the master `bjoin-studio-network-design.md` document.
2.  Pre-configured an access port for **VLAN 51** on your managed switch, as described in the `sodola-switch-vlan-configuration.md` runbook. You will need this to regain access to the firewall.

---

## 3. Installation

Follow the installation steps from the previous guide to install OPNsense on the Protectli Vault. After the installation and reboot, OPNsense will boot from the internal storage.

## 4. Initial Console Configuration

After the first boot, you will use the console to set up a unique, temporary IP address for the initial web-based configuration.

1.  On the first boot, the OPNsense console will ask to assign your physical **WAN** and **LAN** ports. Complete this assignment.
2.  By default, OPNsense assigns `192.168.1.1` to the LAN interface. We will now change this to our unique temporary address, `192.168.101.1`.
3.  From the main console menu, select option **`2) Set interface IP address`**.
4.  Select the **LAN** interface to configure.
5.  When asked to `Configure IPv4 address on LAN via DHCP?`, enter **`n`** for No.
6.  Enter the new LAN IPv4 address: **`192.168.101.1`**
7.  Enter the new LAN subnet bit count: **`24`**
8.  For the upstream gateway, press **Enter** for none.
9.  When asked to `Configure IPv6 address on LAN via DHCP6?`, enter **`n`** for No.
10. When asked to `Do you want to enable the DHCP server on LAN?`, enter **`y`** for Yes.
11. Enter the start address of the DHCP range: **`192.168.101.100`**
12. Enter the end address of the DHCP range: **`192.168.101.200`**
13. When asked to `Do you want to revert to HTTP as the web GUI protocol?`, enter **`n`** for No.

After saving, the firewall is now listening on `https://192.168.101.1`. You can proceed to the first Web GUI login.

## 5. First Web GUI Login & Creating the Management VLAN

The goal of this step is to create our new Management VLAN interface *before* we change the physical LAN port's configuration.

**Important Note on Physical vs. Logical Interfaces:**
Your Protectli vault has four physical ports (WAN, LAN, OPT1, OPT2). In our "Router-on-a-Stick" design, we intentionally leave the physical **OPT1** and **OPT2** ports disconnected and unassigned. All our internal VLANs will run over the single physical **LAN** port. The following steps will create a *logical* VLAN interface which OPNsense might *name* OPT1 by default, causing confusion. The key is that we are building on the LAN port only.

1.  Connect your laptop to a switch that is connected to the firewall's physical **LAN** port.
2.  Your laptop should get an IP address in the `192.168.101.x` range.
3.  Open a browser and navigate to `https://192.168.101.1`.
4.  Log in with the default credentials (`root` / `opnsense`).
5.  **Skip the setup wizard for now.** We will run it later.
6.  Navigate to **Interfaces > Other Types > VLAN**.
7.  Click **+ Add** and create your Management VLAN:
    -   **Parent interface:** Select your physical **LAN** interface (e.g., `igb1`). **Do not select the physical OPT1/igb2 port.**
    -   **VLAN tag:** `51`
    -   **Description:** `Management VLAN 51`
8.  Navigate to **Interfaces > Assignments**.
9.  You will see a new VLAN available. Click the **+** button to assign it. It will be named `OPT1` by default.
    -   **CRITICAL CLARIFICATION:** This `OPT1` is a **logical name** assigned by OPNsense. It is **NOT** the same as your physical `OPT1` port. This is a known point of confusion.
10. Click on the new `OPT1` interface to configure it:
    -   Check the **Enable** box.
    -   Change the **Description** to `MGMT_DEVICES`. (This is why we rename it immediately, to avoid confusion).
    -   Set **IPv4 Configuration Type** to **Static**.
    -   In the "Static IPv4 configuration" section, set the IP address: `10.20.51.1` / `24`.
    -   Click **Save** and then **Apply Changes**.

## 6. The Critical Switchover: Reconfiguring the LAN Port

This is the most important step. We will now remove the IP address from the physical LAN port, turning it into a pure VLAN trunk. 

**WARNING:** You will lose access to the Web GUI at `https://192.168.101.1` after this step. This is expected. Ensure your laptop is physically connected to a **MANAGED switch port** that has been configured as an **ACCESS port for VLAN 51** before you proceed.

1.  Navigate to **Interfaces > [LAN]**.
2.  Set the **IPv4 Configuration Type** to **None**.
3.  Delete any IP addresses listed in the configuration.
4.  Click **Save** and **Apply Changes**.

## 7. Reconnecting and Final Verification

The firewall is now only accessible via the VLAN 51 interface.

1.  Ensure your laptop is plugged into the switch port you configured for VLAN 51.
2.  Manually set your laptop's IP address to be on the Management subnet (e.g., IP: `10.20.51.99`, Subnet: `255.255.255.0`, Gateway: `10.20.51.1`).
3.  Open your browser and navigate to the new management address: **`https://10.20.51.1`**.
4.  Log in. You can now run the initial setup wizard if you wish.

## 8. Next Steps

Success! Your physical LAN port is now a proper trunk, and your management interface is correctly and securely isolated on VLAN 51.

You are now ready to implement the full network design.

Refer to the **🛠️ OPNsense Setup Guide** section within the main **`bjoin-studio-network-design.md`** document for detailed, step-by-step instructions on:
*   Creating all other VLAN interfaces
*   Configuring DHCP servers for each VLAN
*   Implementing the firewall rules from the Routing & Visibility Matrix