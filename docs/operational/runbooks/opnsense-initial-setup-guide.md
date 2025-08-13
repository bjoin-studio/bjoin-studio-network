# OPNsense Installation and Initial Setup on Protectli Vault

This guide provides step-by-step instructions for installing OPNsense on a Protectli device and performing the initial WAN and LAN configuration for the bjoin.studio network.

## 1. Prerequisites

### Hardware
- Protectli Vault (Model: FW4B)
- USB stick (at least 4GB)
- Monitor and Keyboard
- Internet connection (from ISP modem/router, e.g., Netgear 6220)
- Computer for accessing the Web GUI

### Software
- Latest OPNsense VGA image (`.img.bz2` file) from the [OPNsense website](https://opnsense.org/download/).
- A tool like [balenaEtcher](https://www.balena.io/etcher/) or [Rufus](https://rufus.ie/) to create a bootable USB drive.

## 2. Creating the Bootable USB

1.  Download the OPNsense image. Ensure you get the `vga` version.
2.  Use your chosen tool to write the downloaded image to the USB stick. This will erase the USB stick.

## 3. OPNsense Installation on the Protectli Vault

1.  Connect the Protectli Vault to a monitor and keyboard.
2.  Insert the bootable USB drive into one of the USB ports.
3.  Power on the device. It should automatically boot from the USB drive.
4.  When prompted, log in with the default credentials:
    -   **Username:** `installer`
    -   **Password:** `opnsense`
5.  Follow the on-screen installer prompts. The default options are generally safe.
    -   It is highly recommended to choose the **ZFS** file system for reliability and boot environment features.
6.  Once the installation is complete, the system will prompt you to reboot. Select **Reboot** and **immediately remove the USB stick** so you don't boot into the installer again.

## 4. Initial Configuration (First Boot)

After rebooting, OPNsense will boot from the internal storage.

### Assigning Network Interfaces (Console)

1.  OPNsense will ask if you want to set up VLANs now. Enter `n` (No) for now; we will do this from the web interface later.
2.  You will be prompted to assign the **WAN** interface. Identify the physical network port on the Protectli that is connected to your upstream ISP router (e.g., the Netgear 6220). Enter its interface name (e.g., `igb0`, `em0`).
3.  Next, you will be prompted to assign the **LAN** interface. Identify the physical port connected to your internal network switch and enter its interface name.
4.  You may be prompted to assign optional interfaces. Press `Enter` to skip this for now.
5.  Confirm the assignments. OPNsense will configure the interfaces and the LAN port will be assigned the default IP address `192.168.1.1`.

### Accessing the Web GUI

1.  Connect your computer to a port on your main LAN switch.
2.  Your computer should receive an IP address from OPNsense via DHCP in the `192.168.1.0/24` range.
3.  Open a web browser and navigate to `http://192.168.1.1`.
4.  Log in with the default credentials:
    -   **Username:** `root`
    -   **Password:** `opnsense`
5.  Complete the initial setup wizard. It is highly recommended to change the `root` password during this wizard.

## 5. Configuring WAN and LAN Interfaces (Web GUI)

### WAN Interface

1.  Navigate to **Interfaces > [WAN]**.
2.  Set **IPv4 Configuration Type** to **DHCP**. This allows OPNsense to get its WAN IP address from your upstream router.
3.  Ensure "Block private networks" and "Block bogon networks" are checked at the bottom of the page.
4.  Save and apply the changes.

### LAN Interface

This step reconfigures the LAN interface to match your defined IP scheme for the Management VLAN.

1.  Navigate to **Interfaces > [LAN]**.
2.  Set **IPv4 Configuration Type** to **Static**.
3.  Under the "Static IPv4 configuration" section, set the IP address to the gateway for your Management VLAN:
    -   **IPv4 Address:** `10.20.51.1` / `24`
4.  Save and apply the changes.

**You will be disconnected.** You must now change your computer's IP address to be on the new LAN subnet (e.g., set it statically to `10.20.51.10/24`) to reconnect to the Web GUI at its new address: `http://10.20.51.1`.

---

## 6. OPNsense Setup Wizard Configuration

Once you log in to the Web GUI for the first time (or after a factory reset), you will be greeted by the setup wizard. Here are the recommended settings for your bjoin.studio environment.

| Wizard Step      | Parameter          | Recommended Value         | Notes                                                                                                                            |
|:-----------------|:-------------------|:--------------------------|:---------------------------------------------------------------------------------------------------------------------------------|
| **General Info** | Hostname           | `opnsense-fw`             | A simple, descriptive name for your firewall.                                                                                    |
|                  | Domain             | `bjoin.studio`            | This is the domain for your entire internal network.                                                                             |
|                  | Primary DNS        | `1.1.1.1`                 | Use a public DNS server for now to ensure internet access works. You can change this later to an internal DNS server (e.g., FreeIPA). |
|                  | Secondary DNS      | `1.0.0.1`                 | A reliable public DNS backup.                                                                                                    |
| **Time Server**  | Timezone           | `Your_Time_Zone`          | **Important:** Select your correct local timezone (e.g., `America/New_York`).                                                    |
| **WAN Config**   | Selected Type      | `DHCP`                    | This should already be correct from the initial setup.                                                                           |
| **LAN Config**   | LAN IP Address     | `10.20.51.1`              | This should also be correct from the initial setup.                                                                              |
| **Root Password**| Root Password      | `YourNewSecurePassword`   | **Crucial:** Change the default password now to a strong, unique one.                                                              |

---

This concludes the initial installation and basic configuration. The next step is to create all the VLANs as defined in the main network design document.