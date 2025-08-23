# FreeIPA Server Installation Guide for Proxmox

This guide details how to set up a FreeIPA server as a virtual machine on `pmx-01.bjoin.studio`.

## 1. Virtual Machine (VM) Creation

In the Proxmox web UI, create a new VM with the following specifications.

### General:
- **Node:** `pmx-01`
- **VM ID:** (Proxmox will assign one, e.g., 100)
- **Name:** `ipa-01.bjoin.studio`

### OS:
- **Type:** Linux
- **Version:** Use a recent version (e.g., 6.x or later).
- **ISO Image:** Upload a Rocky Linux 9 ISO to your Proxmox ISO storage.

### System:
- **Guest Agent:** Enable `QEMU Guest Agent` for better management.
- **SCSI Controller:** `VirtIO SCSI single`

### Disks:
- **Bus/Device:** `SCSI`
- **Disk size:** At least `40 GB`.

### CPU:
- **Cores:** At least `2`.

### Memory:
- **Memory:** At least `4096 MB` (4 GB).

### Network:
- **Bridge:** `vmbr51`
- **VLAN Tag:** (Leave blank, as the bridge handles it)
- **Model:** `VirtIO (paravirtualized)`

## 2. Operating System Installation (Rocky Linux 9)

1.  Start the VM and open the console.
2.  Follow the Rocky Linux 9 installation prompts.
3.  **Network Configuration:**
    - During installation, go to `Network & Host Name`.
    - Select the Ethernet interface.
    - Click `Configure...` and go to the `IPv4 Settings` tab.
    - **Method:** Manual
    - **Addresses:** Click `Add`
        - **Address:** `10.20.51.10`
        - **Netmask:** `24`
        - **Gateway:** `10.20.51.1`
    - **DNS servers:** `10.20.51.10` (itself)
    - **Search domains:** `bjoin.studio`
    - Set the **Hostname** to `ipa-01.bjoin.studio`.
4.  Complete the installation and reboot.

## 3. FreeIPA Server Installation

After the VM is running, connect to it via SSH or the Proxmox console.

This process is automated by the `setup-freeipa-server.py` script in this repository. It is recommended to use the script to ensure a consistent and correct installation.

### 1. Prepare the Environment

Before running the script, you must set two environment variables for the Directory Manager and Admin passwords.

```bash
export IPA_DS_PASSWORD='YourSecurePassword123!'
export IPA_ADMIN_PASSWORD='YourSecurePassword123!'
```

### 2. Run the Installation Script

Execute the script with `sudo`. It will handle system updates, package installation, and the FreeIPA server setup.

```bash
sudo python3 /path/to/repo/src/modules/identity-management/freeipa/setup-freeipa-server.py
```

The script will provide live output of the installation process.

## 4. Configure Server Firewall (`firewalld`)

The setup script installs and enables the firewall, but the rules must be applied. The `firewall_rules-freeipa.sh` script in this repository contains the complete set of rules for a functioning FreeIPA server.

Run the script on the newly installed `ipa-01` server:

```bash
# Navigate to the script location
cd /path/to/repo/src/modules/firewall/

# Make the script executable
chmod +x firewall_rules-freeipa.sh

# Run the script with sudo
sudo ./firewall_rules-freeipa.sh

# Reload the firewall to apply the new rules
sudo firewall-cmd --reload
```

## 5. Configure Network DNS (OPNsense)

This is a critical step to allow all devices on your network to find and use the new FreeIPA server.
You must configure your main DHCP server on OPNsense to assign the FreeIPA server as the primary DNS server for all your networks.

1.  **Log into the OPNsense Web UI.**
2.  Navigate to **Services > DHCPv4**.
3.  For **each** VLAN interface (e.g., `LAN`, `MGMT_51`, `STUDIO_31`, etc.), do the following:
    -   Click on the interface to open its DHCP settings.
    -   Find the **DNS servers** field.
    -   Delete any existing entries and add the IP of your FreeIPA server: `10.20.51.10`.
    -   Click **Save** at the bottom of the page.
4.  After saving for all interfaces, client devices will need to renew their DHCP lease (e.g., by reconnecting to the network or rebooting) to receive the new DNS settings.

## 6. Verify Installation

From a client machine on the network that has received the new DNS settings, you should now be able to perform these actions successfully:

1.  **Resolve the hostname:**
    ```bash
    ping ipa-01.bjoin.studio
    ```
2.  **Access the Web UI:**
    Open a browser and navigate to `https://ipa-01.bjoin.studio/`

3.  **Authenticate with Kerberos:**
    ```bash
    kinit admin
    ```

## 7. Post-Installation: Client Enrollment & Access Control

Your FreeIPA server is now the central identity and DNS provider for your network. The next steps involve enrolling your client machines and configuring access control rules.

### Client Enrollment

For devices to use FreeIPA for authentication, they must be enrolled as clients. See the `macos-freeipa-client-troubleshooting.md` guide for details on manual configuration and troubleshooting for macOS.

### OPNsense Firewall Rules for Inter-VLAN Traffic

For devices in other VLANs to communicate with the FreeIPA server, you must create firewall rules on OPNsense. The basic principle is to allow traffic **FROM** a client VLAN **TO** the FreeIPA server's IP (`10.20.51.10`) for the necessary ports.

Here are the essential ports to open on your OPNsense firewall:

| Port      | Protocol | Service        | Purpose                               |
| :-------- | :------- | :------------- | :------------------------------------ |
| `53`      | TCP/UDP  | **DNS**        | Domain Name Resolution                |
| `88`      | TCP/UDP  | **Kerberos**   | Authentication                        |
| `123`     | UDP      | **NTP**        | Time Synchronization (critical for Kerberos) |
| `389`     | TCP      | **LDAP**       | Directory Lookups                     |
| `443`     | TCP      | **HTTPS**      | Accessing the FreeIPA Web UI          |
| `464`     | TCP/UDP  | **Kerberos Pwd** | Password changes                    |
| `636`     | TCP      | **LDAPS**      | Secure Directory Lookups              |