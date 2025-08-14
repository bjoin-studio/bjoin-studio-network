# OPNsense Initial Installation and LAN Trunk Configuration

This guide provides the definitive, step-by-step procedure for installing OPNsense and correctly configuring the physical LAN port as a VLAN trunk without losing access.

## 1. Installation

Follow the installation steps from the previous guide to install OPNsense on the Protectli Vault. After the installation and reboot, OPNsense will boot from the internal storage.

## 2. Initial Console Configuration

1.  On the first boot, the OPNsense console will ask to assign interfaces. 
2.  Assign your physical **WAN** and **LAN** ports. Do **not** set up any VLANs from the console menu.
3.  OPNsense will assign the default IP `192.168.1.1` to your physical LAN port. This is a **temporary** address that we will use for initial setup only.

## 3. First Web GUI Login & Creating the Management VLAN

The goal of this step is to create our new Management VLAN interface *before* we change the physical LAN port's configuration.

1.  Connect your laptop to a switch that is connected to the firewall's **LAN** port.
2.  Your laptop should get an IP address in the `192.168.1.x` range.
3.  Open a browser and navigate to `https://192.168.1.1`.
4.  Log in with the default credentials (`root` / `opnsense`).
5.  **Skip the setup wizard for now.** We will run it later.
    
    **Troubleshooting Note:** If you cannot access the Web GUI at this stage, ensure the `lighttpd` service is running. From the console, you may need to enable it by running `echo 'lighttpd_enable="yes"' >> /etc/rc.conf` and then `service lighttpd start`.
6.  Navigate to **Interfaces > Other Types > VLAN**.
7.  Click **+ Add** and create your Management VLAN:
    -   **Parent interface:** Select your physical LAN interface (e.g., `igb1`).
    -   **VLAN tag:** `51`
    -   **Description:** `Management VLAN 51`
8.  Navigate to **Interfaces > Assignments**.
9.  You will see a new VLAN available. Click the **+** button to assign it. It will be named `OPT1` by default.
10. Click on the new `OPT1` interface to configure it:
    -   Check the **Enable** box.
    -   Change the **Description** to `MGMT_DEVICES`.
    -   Set **IPv4 Configuration Type** to **Static**.
    -   In the "Static IPv4 configuration" section, set the IP address: `10.20.51.1` / `24`.
    -   Click **Save** and then **Apply Changes**.

At this point, you have two active interfaces: the physical `LAN` at `192.168.1.1` and the new virtual `MGMT_DEVICES` at `10.20.51.1`.

## 4. The Critical Switchover: Reconfiguring the LAN Port

This is the most important step. We will now remove the IP address from the physical LAN port, turning it into a pure VLAN trunk. 

**WARNING:** You will lose access to the Web GUI at `https://192.168.1.1` after this step. This is expected. Ensure your laptop is physically connected to a **MANAGED switch port** that has been configured as an **ACCESS port for VLAN 51** before you proceed.

1.  Navigate to **Interfaces > [LAN]**.
2.  Set the **IPv4 Configuration Type** to **None**.
3.  Delete any IP addresses listed in the configuration.
4.  Click **Save** and **Apply Changes**.

## 5. Reconnecting and Final Verification

The firewall is now only accessible via the VLAN 51 interface.

1.  Ensure your laptop is plugged into the switch port you configured for VLAN 51.
2.  Manually set your laptop's IP address to be on the Management subnet (e.g., IP: `10.20.51.99`, Subnet: `255.255.255.0`, Gateway: `10.20.51.1`).
3.  Open your browser and navigate to the new management address: **`https://10.20.51.1`**.
4.  Log in. You can now run the initial setup wizard if you wish.

Success! Your physical LAN port is now a proper trunk, and your management interface is correctly and securely isolated on VLAN 51. You can now proceed to create all your other VLAN interfaces.