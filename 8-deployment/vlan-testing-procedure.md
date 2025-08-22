# VLAN Testing Procedure

This runbook provides a systematic procedure for testing and validating the configuration of individual VLANs on the network. Following these steps will ensure that DHCP, DNS, and firewall rules are all working as expected.

## 1. Prerequisites

*   OPNsense is configured with all VLANs, DHCP servers, and firewall rules as per the master design document.
*   Managed switches are configured with the appropriate VLANs and trunk links, as per the `sodola-switch-vlan-configuration.md` runbook.
*   A test device (e.g., a laptop with an Ethernet port).

## 2. Systematic Testing Workflow

For each test case in the table below, follow this four-step process.

### Step 1: Connect to the VLAN

*   Connect your test device to the specified **Test Port** on the Sodola switch. These ports have been pre-configured as access ports for their respective VLANs.

### Step 2: Verify IP Address

*   On your test device, ensure it automatically receives an IP address from the correct **Expected DHCP Range**. You can verify this in your device's network settings (`ipconfig` or `ip addr`).
*   If you do not receive an IP, troubleshoot the DHCP server settings in OPNsense for that VLAN.

### Step 3: Verify Gateway and Internet Connectivity

*   Open a terminal or command prompt.
*   Ping the VLAN's **Gateway IP**. A success confirms the switch and firewall interface are correctly configured.
*   Ping a public address like `8.8.8.8`. A success confirms outbound NAT and internet access for the VLAN.

### Step 4: Verify Firewall Rules

*   Attempt to ping the target specified in the **Firewall Test** column.
*   Compare your result to the **Expected Result**. A `FAIL` can be a **SUCCESS** if you are testing a security rule meant to block traffic.

## 3. VLAN-Specific Test Plan

Use this table to validate key VLANs across your network.

| VLAN to Test | Test Port (Sodola) | Expected DHCP Range | Gateway (Ping Target) | Firewall Test | Expected Result |
|:---|:---|:---|:---|:---|:---|
| **11: Production Wired** | Port 5 | `10.20.11.100 – 200` | `10.20.11.1` | Ping Studio Gateway `10.20.31.1` | ❌ **FAIL** |
| **14: Production Wifi** | (Requires AP) | `10.20.14.100 – 200` | `10.20.14.1` | Ping Guest Gateway `10.20.64.1` | ❌ **FAIL** |
| **15: Production Monitoring** | (Manual IP) | `10.20.15.100 – 200` | `10.20.15.1` | Ping any other VLAN Gateway | ❌ **FAIL** (Should be isolated) |
| **21: Stage Wired** | Port 6 | `10.20.21.100 – 200` | `10.20.21.1` | Ping Production Gateway `10.20.11.1` | ✅ **SUCCESS** (Assumed) |
| **32: Studio 10Gb** | (Manual Port) | `10.20.32.100 – 200` | `10.20.32.1` | Ping Production Gateway `10.20.11.1` | ✅ **SUCCESS** (Full visibility) |
| **41: Workshop Wired** | Port 7 | `10.20.41.100 – 200` | `10.20.41.1` | Ping Studio Gateway `10.20.31.1` | ❌ **FAIL** (Isolated) |
| **54: Management Wifi** | (Requires AP) | `10.20.54.100 – 200` | `10.20.54.1` | Ping Guest Gateway `10.20.64.1` | ❌ **FAIL** |
| **64: Guest Wifi** | (Requires AP) | `10.20.64.100 – 200` | `10.20.64.1` | Ping Production Gateway `10.20.11.1` | ❌ **FAIL** (Internet only) |

**Note on WiFi Testing:** To test a WiFi VLAN, you must first connect a Wireless Access Point to a switch port configured for that VLAN, then connect your test device to the corresponding wireless network.