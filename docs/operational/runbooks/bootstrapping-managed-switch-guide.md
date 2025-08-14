# Bootstrapping a New Managed Switch

This guide provides a step-by-step procedure for the initial configuration of a new managed switch (like the Netgear GS108E) before it is ready to be integrated into the main network. This process uses a temporary, isolated network to avoid IP conflicts and access issues.

### Goal
To assign the switch a static IP on the Management VLAN (51) and configure its initial trunk and access ports.

---

### Step 1: Create an Isolated "Airlock" Network

1.  **Disconnect the new managed switch from everything.** It must not be connected to your firewall or any other network device.
2.  Connect **only your laptop** via an Ethernet cable to any port on the new switch (e.g., Port 2).

### Step 2: Manually Configure Your Laptop's IP

1.  Find the switch's factory default IP address. For the Netgear GS108E, this is typically `192.168.0.239`. If you are using a different switch, you may need to check its manual or a sticker on the device.
2.  On your laptop, manually configure your Ethernet adapter's IP address to be on the same subnet as the switch.
    -   **IP Address:** `192.168.0.100`
    -   **Subnet Mask:** `255.255.255.0`
    -   (The Gateway and DNS fields can be left blank for this step).

### Step 3: Log In to the Switch's Web Interface

1.  Open a web browser on your laptop and navigate to the switch's default IP address (e.g., `http://192.168.0.239`).
2.  Log in with the default credentials (for Netgear, this is often `admin` and `password`). You should be prompted to change the password immediately.

### Step 4: The Critical Reconfiguration

You are now talking directly to the switch. We will tell it about its new home on your main network.

1.  **Change the Switch's Management IP Address:**
    -   Navigate to the IP Configuration or System settings page.
    -   Change the IP address settings from DHCP or the default static IP to a **new static IP on our Management VLAN (51)**. Use the IP assigned in the IPAM document.
        -   **IP Address:** `10.20.51.5` (for the Netgear GS108Ev4)
        -   **Subnet Mask:** `255.255.255.0`
        -   **Default Gateway:** `10.20.51.1`
    -   **Apply these settings. You will be disconnected from the web interface immediately. This is expected.**

### Step 5: Reconnect and Final VLAN Configuration

The switch is now configured to live on VLAN 51, but your laptop is still on the old `192.168.0.x` network. Let's fix that and complete the setup.

1.  **Change your Laptop's IP:** Reconfigure your laptop's Ethernet adapter back to the static IP you are using for VLAN 51 testing: `10.20.51.99` / `255.255.255.0`.
2.  **Connect the Switch to the Main Network:**
    -   Connect the switch's **Port 1** (which we will use as the uplink) to a **trunk port** on your main distribution switch (the Sodola).
3.  **Log Back In to the Switch:**
    -   Move your laptop's Ethernet cable to **Port 8** on the Netgear switch.
    -   In your browser, navigate to the switch's **new IP address**: `http://10.20.51.5`.
    -   Log in with the new password you set.
4.  **Final VLAN Setup:**
    -   Navigate to the VLAN -> 802.1Q -> VLAN Configuration page.
    -   Create VLAN `51` if it doesn't exist.
    -   Navigate to the "VLAN Membership" page.
        -   Set **Port 1** (the uplink) to be a **Tagged** member of VLAN 51.
        -   Set **Port 8** (your access port) to be an **Untagged** member of VLAN 51.
    -   Navigate to the "PVID" page and set the PVID for **Port 8** to `51`.

---

The switch is now fully bootstrapped and configured. Port 8 is a functioning access port for VLAN 51, and Port 1 is the trunk uplink to the rest of the network. You can repeat this process for any new managed switch.
