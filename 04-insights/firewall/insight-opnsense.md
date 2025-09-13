# Insights for OPNsense

This document provides setup guidance and best practices for configuring OPNsense in the bjoin.studio network.

## 1. OPNsense Setup Guide

This section guides you through installing and configuring OPNsense to act as the network's perimeter firewall.

### 🔹 1.1 Installation & Initial Access

*   **A Note on Interfaces:** During the OPNsense installation, it is critical to correctly identify and assign the network interfaces. The `WAN` interface should be connected to your ISP modem, and the `LAN` interface should be connected to your internal network core switch.

#### 🧰 Requirements
- Compatible x86 hardware (e.g., HP Z620 with a multi-port NIC)
- USB stick (at least 4GB)
- Monitor + keyboard (for initial setup)
- Internet access via ISP Modem

#### 🧾 Installation Steps
1. **Download OPNsense ISO**
   - Visit [OPNsense Downloads](https://opnsense.org/download/)
   - Select: `AMD64`, `VGA`, latest stable release

2. **Create Bootable USB**
   - Use [Rufus](https://rufus.ie/) or BalenaEtcher
   - Write the ISO to your USB stick

3. **Install OPNsense**
   - Boot the target machine from the USB stick.
   - Follow the installer prompts.
   - Choose ZFS (recommended for reliability).
   - Assign interfaces correctly during the setup process.

4. **Access Web GUI**
   - Connect a laptop to the LAN network.
   - Navigate to the default LAN IP `https://192.168.1.1` (or the IP you configure).
   - Default credentials: `admin / opnsense`
   - Change the password immediately upon first login.

### 🔹 1.2 Firewall Rule Best Practices

*   **Default Deny:** Start with a default-deny rule on all interfaces. This ensures that only traffic that is explicitly allowed is permitted.
*   **Be Specific:** Create granular rules for the traffic you want to allow. Avoid using "any" for source, destination, or port whenever possible.
*   **Use Aliases:** Use aliases for IP addresses, ports, and networks. This makes rules much easier to read, manage, and update.
*   **Documentation:** Add clear and concise descriptions to every firewall rule to explain its purpose, the reason for its existence, and any relevant ticket numbers.
*   **Order Matters:** The firewall processes rules from top to bottom. The first rule that matches a packet is the one that is applied. Place more specific rules before more general (e.g., `allow all`) rules.
