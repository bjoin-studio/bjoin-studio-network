# VLAN Testing Procedure

This runbook provides a systematic procedure for testing and validating the configuration of individual VLANs on the network. Following these steps will ensure that DHCP, DNS, and firewall rules are all working as expected.

## 1. Prerequisites

*   OPNsense is configured with all VLANs, DHCP servers, and firewall rules.
*   Managed switches (e.g., Sodola, Netgear GS108Ev4) are configured with the appropriate VLANs and trunk links.
*   A test device (e.g., a laptop with an Ethernet port).

## 2. VLAN Testing Plan

This plan should be repeated for each VLAN you intend to test.

### Step 2.1: Configure an Access Port

To test a VLAN, you must first have a port that provides untagged access to it.

1.  Choose a spare port on a managed switch (e.g., Sodola or Netgear GS108Ev4).
2.  In the switch's web GUI, configure the chosen port as an **access port** for the target VLAN (e.g., VLAN 21 for Stage).
    *   Set the port as an **Untagged** member of the VLAN.
    *   Set the port's **PVID** to the same VLAN ID.

**Note:** For initial testing, **Port 8 on the Sodola switch** is pre-configured as an access port for **VLAN 11**.

### Step 2.2: Connect a Test Device

*   Connect your test device (e.g., laptop) to the access port you just configured.

### Step 2.3: Verify IP Address

*   On your test device, ensure it automatically receives an IP address from the correct DHCP range for that VLAN. You can verify this in your device's network settings (e.g., `ipconfig` on Windows, `ifconfig` or `ip addr` on macOS/Linux).

| VLAN ID | Zone       | Expected DHCP Range    |
|:--------|:-----------|:-----------------------|
| **11**  | Production | `10.20.11.100 – 200`   |
| **21**  | Stage      | `10.20.21.100 – 200`   |
| **31**  | Studio     | `10.20.31.100 – 200`   |
| **41**  | Workshop   | `10.20.41.100 – 200`   |

If you do not receive an IP address, troubleshoot the DHCP server settings in OPNsense for that VLAN and the port configuration on the switch.

### Step 2.4: Test Connectivity

Once your device has a valid IP address, perform the following tests from the command line (Terminal or Command Prompt).

#### 1. Ping the Gateway

This test confirms basic connectivity to the OPNsense firewall from within the VLAN.

*   For VLAN 11: `ping 10.20.11.1`
*   For VLAN 21: `ping 10.20.21.1`
*   For VLAN 31: `ping 10.20.31.1`
*   For VLAN 41: `ping 10.20.41.1`

A successful ping confirms that the VLAN is correctly configured on the switch and the firewall interface is responding.

#### 2. Ping a Public DNS Server

This test confirms that the VLAN has a valid path to the internet.

*   Run the command: `ping 8.8.8.8`

A successful ping confirms that your WAN gateway and outbound NAT rules are working correctly for this VLAN.

#### 3. Test Firewall Rules (Inter-VLAN Connectivity)

This is the most important test for verifying your network segmentation and security policies. Attempt to ping the gateway of another VLAN to see if the firewall rules you created are being enforced.

**Example Test:**

*   Connect your test device to an access port for **VLAN 41 (Workshop)**.
*   Attempt to ping the gateway of **VLAN 31 (Studio)**:
    *   `ping 10.20.31.1`

**Expected Result:** According to the "Routing & Visibility Matrix" in the network design, traffic from the Workshop VLAN to the Studio VLAN should be blocked. Therefore, this ping should **fail**. A failed ping in this case is a **success** for your security policy.

Repeat this test for other source/destination VLAN combinations to fully validate your firewall ruleset.
