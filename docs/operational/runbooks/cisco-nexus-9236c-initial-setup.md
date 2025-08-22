# Cisco Nexus 9236C Initial Setup Guide

This guide provides the essential steps for the initial configuration of the Cisco Nexus 9236C switch. This process requires console access and cannot be done through the network initially.

## 1. Prerequisites

### Hardware & Software

*   **Cisco Console Cable:** An RJ-45 to Serial (DB-9) or USB console cable (typically light blue).
*   **Computer with Serial/USB Port:** A laptop or desktop computer to connect to the switch.
*   **Terminal Emulator Program:**
    *   **Windows:** PuTTY, SecureCRT, or Tera Term.
    *   **macOS/Linux:** The built-in `screen` or `minicom` commands.

## 2. Connecting to the Console

The initial setup must be performed via a direct console connection.

1.  **Identify the Console Port:** On the rear of the switch, locate the **RJ-45 console port**. It is typically located next to the management (`mgmt0`) port and does not have a network icon.
2.  **Connect the Cable:**
    *   Plug the **RJ-45** end of the console cable into the console port on the switch.
    *   Plug the other end (serial or USB) into your computer.

## 3. Terminal Emulator Settings

Open your terminal emulator program and configure the connection with the following settings. These must be exact.

*   **Baud Rate:** `9600`
*   **Data Bits:** `8`
*   **Parity:** `None`
*   **Stop Bits:** `1`
*   **Flow Control:** `None`

Once connected, you should see a command-line prompt from the switch.

## 4. Initial Configuration Steps

These steps will guide you through the basic configuration required to get the switch on the network for further management.

### Step 4.1: Enter Configuration Mode

After logging in with the default credentials (if any), you must enter global configuration mode.

```
switch# configure terminal
switch(config)#
```

### Step 4.2: Set the Admin Password

For security, the first step should always be to set a strong password for the `admin` user.

```
switch(config)# username admin password YOUR_STRONG_PASSWORD_HERE
```

### Step 4.3: Configure the Management Interface (`mgmt0`)

This step assigns an IP address to the dedicated management port (the one with the network icon), allowing you to manage the switch over the network.

```
switch(config)# interface mgmt0
switch(config-if)# ip address 10.20.51.2/24
switch(config-if)# no shutdown
```

### Step 4.4: Configure the Default Gateway

The switch needs a default gateway to communicate with devices outside of its own subnet.

```
switch(config)# ip route 0.0.0.0/0 10.20.51.1
```

### Step 4.5: Enable SSH Access

Enable the SSH service to allow for secure remote management over the network.

```
switch(config)# feature ssh
```

### Step 4.6: Save the Configuration

This is a critical step. The `copy running-config startup-config` command saves your changes to the switch's non-volatile memory, so they will persist after a reboot.

```
switch(config)# copy running-config startup-config
```

## 5. Post-Configuration Access

After completing and saving the initial configuration, you can disconnect the console cable.

You can now manage the Cisco switch remotely by connecting to its management IP address via SSH:

```
ssh admin@10.20.51.2
```

---

## Real-World Experience and Troubleshooting Notes

During the initial setup of the Cisco Nexus 9236C, the following situations and solutions were encountered:

#### 1. Power On Auto Provisioning (POAP) Prompt

Upon initial boot, the switch attempts POAP. If it fails to find a configuration, it will present a prompt:

```
- Abort Power On Auto Provisioning [yes - continue with normal setup, skip - bypass password and basic configuration, no - continue with Power On Auto Provisioning] (yes/skip/no)[no]:
```

**Action:** Type `yes` and press `Enter` to abort POAP and proceed with normal setup.

#### 2. System Admin Account Setup

After aborting POAP, the switch prompts for basic admin account setup:

```
Do you want to enforce secure password standard (yes/no) [y]:
```
**Action:** Press `Enter` to accept `y`.

```
Enter the password for "admin":
Confirm the password for "admin":
```
**Action:** Enter and confirm a strong password for the `admin` user.

#### 3. Basic System Configuration Dialog

The switch then asks if you want to enter the basic configuration dialog:

```
Would you like to enter the basic configuration dialog (yes/no):
```
**Action:** Type `no` and press `Enter` to skip the dialog and configure manually.

#### 4. User Access Verification (Login Prompt)

After skipping the basic dialog, the switch may present a login prompt:

```
User Access Verification
switch login:
```
**Action:** Log in as `admin` with the password set previously.

#### 5. SSH Key Generation Error

When attempting to generate SSH keys (`ssh key rsa 2048`), the switch might report that keys already exist:

```
ERROR: Cannot configure run ssh key without force as the config is already existing
```
**Action:** Regenerate the keys using the `force` option: `ssh key rsa 2048 force`.

#### 6. Physical Management Port Connection

To enable SSH access from the network, the dedicated management port (`mgmt0`, typically with a network icon) must be connected to the management network.

**Action:** Connect an RJ45 cable from the `mgmt0` port on the Cisco 9236C to an access port on your management VLAN (e.g., on the GS105 unmanaged switch, assuming it's connected to VLAN 51).

**Verification:** After connecting, verify network connectivity by pinging the switch's management IP (`10.20.51.2`) from your management workstation, then attempt SSH.

#### 7. High-Speed Uplink Configuration (QSFP Breakout & LAG)

Configuring the 40Gbps uplink to the Sodola switch involved several steps and troubleshooting:

*   **QSFP Port Identification:** The QSFP28 ports on the Nexus were identified (e.g., `Ethernet1/1` was used for the breakout).
*   **Transceiver Detection:** Initially, the Nexus did not detect the QSFP transceiver (`XCVR not inserted`). This was resolved by firmly re-seating the QSFP end of the breakout cable.
*   **Breakout Mode:** The QSFP port was configured for breakout mode (`interface breakout module 1 port 1-4 map 10g`) to split it into four 10Gb interfaces (e.g., `Eth1/1/1` to `Eth1/1/4`).
*   **Interface Activation:** The individual 10Gb breakout interfaces were brought up (`no shutdown`).
*   **Port-Channel Creation:** These four 10Gb interfaces were added to a Port-Channel (`channel-group 1 mode on`) on the Nexus, creating a single logical 40Gbps link.
*   **Sodola LAG Configuration:** The corresponding Link Aggregation Group (LAG1) was configured on the Sodola switch via its web GUI. This involved:
    *   Setting the Load Balance Algorithm to `IP-MAC Address`.
    *   Adding `TE1`, `TE2`, `TE3`, `TE4` as static members of LAG1.
    *   Configuring LAG1 as a `Trunk` port, allowing all VLANs (1, 11-65).
    *   Setting LAG1's PVID to `1` (to match the Nexus native VLAN).
    *   **Troubleshooting:** Initial configuration errors on the Sodola side (physical ports `TE1-TE4` incorrectly configured as `access` mode) were identified and corrected via the web GUI.
*   **Link Verification:** The successful establishment of the 40Gbps link was verified by checking the link status of individual interfaces and the LAG/Port-Channel on both the Nexus and Sodola switches.

---

## 8. Backing Up the Configuration

It is crucial to regularly back up your Cisco Nexus 9236C's configuration for disaster recovery and to track changes. The most secure and recommended method is to use SCP (Secure Copy Protocol).

### Command to Back Up Running Configuration via SCP

Run the following command from the Nexus switch's privileged EXEC mode (`n9k-01.bjoin.studio#`):

```cli
copy running-config scp://venus-admin@10.20.51.99/Users/venus-admin/Documents/workspace/GitHub/bjoin-studio/bjoin-studio-network/cfg/cisco_NEXUS9236c/n9k-01_running-config.cfg
```

**Explanation:**

*   `running-config`: Specifies that you want to copy the currently active configuration.
*   `scp://`: Indicates the use of SCP for the transfer.
*   `venus-admin@10.20.51.99`: Your username and the IP address of your iMac (which acts as the SCP server).
*   `/Users/venus-admin/Documents/workspace/GitHub/bjoin-studio/bjoin-studio-network/cfg/cisco_NEXUS9236c/n9k-01_running-config.cfg`: The full path and desired filename on your iMac where the configuration will be saved.

**Prompts:**

After entering the command, the switch will prompt you for:

*   **`Enter vrf (If no input, current vrf 'default' is considered):`**: Type `management` and press `Enter` (as your `mgmt0` interface is in the management VRF).
*   **`Password:`**: Enter the password for your `venus-admin` user on your iMac.

### Alternative: Copy-Paste from `show running-config`

If SCP is not feasible, you can always copy the output of `show running-config` directly from your console or SSH session and paste it into a text file on your computer.
