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
