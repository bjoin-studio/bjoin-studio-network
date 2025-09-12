# Network Physical and Logical Connections Guide

This guide provides a comprehensive, step-by-step walkthrough of the physical cabling and logical configuration required to build the bjoin.studio network. It integrates the roles of the OPNsense firewall, Sodola distribution switch, Netgear access switch, and Cisco Nexus core switch to achieve a hybrid routing strategy that balances performance and security.

### 1. Introduction: The Network Backbone

This guide provides a comprehensive, step-by-step walkthrough of the physical cabling and logical configuration required to build the bjoin.studio network. It integrates the roles of the OPNsense firewall, Sodola distribution switch, Netgear access switch, and Cisco Nexus core switch to achieve a hybrid routing strategy that balances performance and security.

### 2. Physical Connections (Step-by-Step Cabling Guide)

This section details where each cable goes. Ensure devices are powered off before making connections.

#### Step 2.1: Internet to OPNsense Firewall (Protectli FW4B)

*   **Device:** ISP Modem/Router
*   **Cable:** Standard Ethernet cable (Cat5e or better)
*   **Connection:** Connect one end to a **LAN port** on your ISP Modem/Router. Connect the other end to the **WAN port** on your OPNsense firewall.
    *   *(Logical Note: OPNsense's WAN port will receive a DHCP address from your ISP modem/router, e.g., `192.168.44.X`.)*

#### Step 2.2: OPNsense Firewall LAN to Sodola Distribution Switch

*   **Device:** OPNsense Firewall
*   **Cable:** Standard Ethernet cable (Cat5e or better)
*   **Connection:** Connect one end to the **LAN port** on your OPNsense firewall. Connect the other end to **Port 8 (1Gb RJ45/SFP+ Transceiver)** on your Sodola KT-NOS SL-SWTGW2C8F switch.
    *   *(Logical Note: This connection is configured as a **TRUNK** on both OPNsense and the Sodola, carrying all your defined VLANs (11, 21, 31, 41, 51, 61, and others from your design document).)*

#### Step 2.3: Sodola Distribution Switch to Netgear GS108Ev4 Access Switch

*   **Device:** Sodola KT-NOS SL-SWTGW2C8F
*   **Cable:** Standard Ethernet cable (Cat5e or better)
*   **Connection:** Connect one end to **Port 7** on your Sodola switch. Connect the other end to **Port 8** on your Netgear GS108Ev4 switch.
    *   *(Logical Note: This connection is also configured as a **TRUNK** on both switches, carrying all relevant VLANs to the Netgear access layer.)*

#### Step 2.4: Sodola Distribution Switch to Cisco Nexus 9236C Core Switch (NEW High-Speed Link)

*   **Device:** Sodola KT-NOS SL-SWTGW2C8F and Cisco Nexus 9236C
*   **Cable:** 1 QSFP to 4xSFP+ Breakout Cable
*   **Connection:**
    *   Connect the **single QSFP end** of the cable to one of the **QSFP28 ports** on your Cisco Nexus 9236C (e.g., `Ethernet1/37`).
    *   Connect the **four SFP+ ends** of the cable to four available **10G SFP+ ports** on your Sodola switch (e.g., `TE1`, `TE2`, `TE3`, `TE4`).
    *   *(Logical Note: These four physical links will be bundled into a **Link Aggregation Group (LAG)** on the Sodola and a **Port-Channel** on the Nexus, providing a high-bandwidth trunk connection for all VLANs.)*

#### Step 2.5: Cisco Nexus 9236C Management to GS105 Unmanaged Switch

*   **Device:** Cisco Nexus 9236C
*   **Cable:** Standard Ethernet cable (Cat5e or better)
*   **Connection:** Connect one end to the **dedicated management port (`mgmt0`, with the network icon)** on your Cisco Nexus 9236C. Connect the other end to any available port on your **GS105 unmanaged switch**.
    *   *(Logical Note: This provides network access to the Nexus's management interface (`10.20.51.2`) for SSH and other management protocols. Since the GS105 is unmanaged, it acts as an access port for VLAN 51.)*

#### Step 2.6: GS105 Unmanaged Switch to Management Workstation (Your iMac)

*   **Device:** GS105 Unmanaged Switch
*   **Cable:** Standard Ethernet cable (Cat5e or better)
*   **Connection:** Connect one end to any available port on your **GS105 unmanaged switch**. Connect the other end to the Ethernet port on your **iMac**.
    *   *(Logical Note: Your iMac should be configured to obtain an IP address in VLAN 51, allowing it to communicate with the Nexus management interface.)*

#### Step 2.7: End Devices to Netgear GS108Ev4 Access Switch

*   **Device:** Netgear GS108Ev4
*   **Cable:** Standard Ethernet cables (Cat5e or better)
*   **Connection:** Connect your workstations, NAS, servers, and other end devices to the appropriate **access ports** (Ports 1-7) on the Netgear GS108Ev4, based on their intended VLAN (e.g., a workstation for Studio VLAN 31 connects to Port 3).

### 3. Logical Configuration Overview (Step-by-Step)

This section summarizes the configuration needed on each device to bring the network to life. Refer to specific runbooks for detailed commands.

#### Step 3.1: OPNsense Firewall Configuration

*   **VLANs:** Ensure all VLANs (11, 21, 31, 41, 51, 61, and others from your design) are created and assigned to the LAN interface as tagged VLANs.
*   **DHCP:** Configure DHCP servers for VLANs that require dynamic IP assignment.
*   **Firewall Rules:** Implement firewall rules to control traffic between VLANs and to/from the Internet.
*   **Routing Adjustments (Post-Nexus Config):**
    *   **Remove Gateway IPs:** For VLANs 12, 22, 32, and 33, remove their gateway IP addresses from the OPNsense interfaces.
    *   **Add Static Routes:** Add static routes for `10.20.12.0/24`, `10.20.22.0/24`, `10.20.32.0/24`, and `10.20.33.0/24`, all pointing back to the Nexus switch's management IP (`10.20.51.2`).

#### Step 3.2: Sodola KT-NOS SL-SWTGW2C8F Switch Configuration

*   **VLANs:** Ensure all VLANs (1, 11-65) are defined.
*   **Port 8 (Uplink to OPNsense):** Configure as a trunk port, allowing all VLANs.
*   **Port 7 (Uplink to Netgear GS108Ev4):** Configure as a trunk port, allowing all relevant VLANs.
*   **Access Ports (TE1-TE6):** Configure as access ports for their respective VLANs (11, 21, 31, 41, 51, 61).
*   **NEW: LAG to Cisco Nexus:**
    *   Bundle the four SFP+ ports (e.g., `TE1` to `TE4`) into a LAG.
    *   Configure this LAG as a trunk, allowing all VLANs (1, 11-65).

#### Step 3.3: Netgear GS108Ev4 Switch Configuration (Manual via Web GUI)

*   **VLANs:** Create VLANs 1, 11, 21, 31, 41, 51, 61.
*   **Port 8 (Uplink to Sodola):** Configure as a trunk port, allowing VLANs 1, 11, 21, 31, 41, 51, 61.
*   **Access Ports (1-7):** Configure as access ports for their respective VLANs (e.g., Port 1 for VLAN 11, Port 2 for VLAN 21, etc.), ensuring correct PVIDs.
*   **Save Configuration:** Persist changes to startup configuration.

#### Step 3.4: Cisco Nexus 9236C Core Switch Configuration

*   **Initial Setup:** Hostname (`n9k-01.bjoin.studio`), management IP (`10.20.51.2/24` on `mgmt0`), default gateway (`10.20.51.1`), SSH enabled.
*   **Enable Features:** `feature vlan`, `feature interface-vlan`.
*   **Create All VLANs:** Define all VLANs (1, 11-65) on the Nexus.
*   **Configure SVIs (Layer 3 Interfaces):** Create SVIs for VLANs 12, 22, 32, 33, assigning them their respective gateway IPs (`10.20.12.1`, `10.20.22.1`, `10.20.32.1`, `10.20.33.1`).
*   **Configure Port-Channel to Sodola:**
    *   Bundle the QSFP28 port (e.g., `Ethernet1/37`) into a Port-Channel.
    *   Configure this Port-Channel as a trunk, allowing all VLANs (1, 11-65).
*   **Save Configuration:** Persist changes to startup configuration.

### 4. Verification

*   **Ping Tests:** Verify connectivity between devices in the same VLAN and across VLANs (after routing is configured).
*   **SSH Access:** Confirm remote SSH access to all managed devices.
*   **VLAN Connectivity Tests:** Ensure devices are correctly assigned to their VLANs and can communicate as expected.
