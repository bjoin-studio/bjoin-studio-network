# TrueNAS Server Setup Guide

This document outlines the steps for setting up a TrueNAS server to provide NFS shares for FreeIPA user home directories.

## 1. TrueNAS Installation

*   Download TrueNAS CORE/SCALE ISO.
*   Install TrueNAS on your chosen hardware.

## 2. Network Configuration

*   Configure network interfaces (IP address, subnet mask, gateway, DNS).
*   Ensure the TrueNAS server is reachable from your FreeIPA server.

## 3. ZFS Pool and Dataset Creation

*   Create a ZFS pool for your data.
*   Create a dataset specifically for FreeIPA home directories (e.g., `pool/home_dirs`).

### 3.1. Disk Passthrough (Proxmox)

If you are running TrueNAS as a virtual machine on Proxmox, it is recommended to pass through physical disks directly to the TrueNAS VM for optimal performance and data integrity. This allows TrueNAS to have direct control over the disks.

For detailed instructions on how to pass through physical disks to a virtual machine in Proxmox, refer to the official Proxmox documentation:

*   [Passthrough Physical Disk to Virtual Machine (VM)](https://pve.proxmox.com/wiki/Passthrough_Physical_Disk_to_Virtual_Machine_(VM))

## 4. NFS Share Configuration

*   Configure an NFS share for the `home_dirs` dataset.
*   Set appropriate permissions and access controls for the FreeIPA server.

## 5. FreeIPA Integration

*   Verify NFS connectivity from the FreeIPA server.
*   Update the `setup-freeipa-server.py` script with the correct TrueNAS IP and NFS export path.

## 6. Testing

*   Test user home directory creation and access from FreeIPA clients.

## 7. Persistent Network Configuration from the Console

If you cannot use the Web UI, the recommended way to set a persistent static IP address is through the TrueNAS SCALE console menu. The process has a specific quirk.

**Symptom:** After disabling DHCP for an interface (e.g., `ens18`), there is no obvious option to set a static IP address.

**Solution:** The key is to add the static IP as an "alias" to the interface.

1.  Access the console menu. If you are in the regular shell, you can launch it by typing:
    ```bash
    /etc/netcli
    ```
2.  From the main menu, select **1) Configure Network Interfaces**.
3.  Choose the interface you want to configure (e.g., `ens18`).
4.  Answer the prompts as follows:
    *   Remove the interface? **No**
    *   Configure interface for DHCP? **No**
    *   Configure IPv6? **No** (unless needed)
    *   Add any aliases for this interface? **Yes**
5.  Enter your desired static IP address in CIDR notation (e.g., `10.20.51.81/24`).

The system will test the new configuration and, if successful, save it permanently. This is the correct method to ensure your static IP persists across reboots.