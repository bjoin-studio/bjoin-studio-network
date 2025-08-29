# Backup and Recovery Plan

## 1. Introduction

This document outlines the backup and recovery procedures for the bjoin.studio network infrastructure. The goal is to ensure that critical network services and configurations can be restored quickly and reliably in the event of a failure.

## 2. Scope

This plan covers the following critical components:

*   OPNsense Firewall configuration.
*   Proxmox VE host configuration.
*   Virtual Machines (VMs) and Containers hosted on Proxmox, with a high priority on the FreeIPA servers.
*   Network switch configurations.

## 3. Backup Strategy

### 3.1. OPNsense Firewall

*   **Method:** Automatic configuration backups via the OPNsense web GUI.
*   **Frequency:** Daily at 1:00 AM.
*   **Storage:** Backups are automatically pushed to a dedicated dataset on the TrueNAS server.
*   **Retention:** 30 daily backups, 12 monthly backups, and 3 yearly backups.

### 3.2. Proxmox VE Host

*   **Method:** Manual backup of the `/etc/proxmox/` directory.
*   **Frequency:** After any significant change to the host configuration (e.g., adding new storage, network changes).
*   **Storage:** The backup archive is stored on the TrueNAS server.

### 3.3. VMs and Containers

*   **Method:** Proxmox VE scheduled backups.
*   **Frequency:**
    *   **FreeIPA Servers (VMs):** Daily at 2:00 AM.
    *   **Other VMs and Containers:** Weekly on Sundays at 3:00 AM.
*   **Storage:** Backups are stored on a dedicated NFS share on the TrueNAS server.
*   **Retention:** 7 daily backups and 4 weekly backups for FreeIPA. 4 weekly backups for all other VMs and containers.

### 3.4. Network Switches

*   **Method:** Manual backup of the running configuration via the switch's CLI or web interface.
*   **Frequency:** After any configuration change.
*   **Storage:** Configuration files are stored in the `cfg/` directory of this Git repository.

## 4. Recovery Procedures

### 4.1. Restoring OPNsense Configuration

1.  **Install OPNsense:** Perform a fresh installation of OPNsense on a new device.
2.  **Initial Configuration:** Configure the LAN interface with a static IP address to allow access to the web GUI.
3.  **Restore Backup:**
    *   Navigate to `System > Configuration > Backups`.
    *   Locate the latest backup file from the TrueNAS server.
    *   Upload and restore the configuration.
    *   The system will reboot with the restored configuration.

### 4.2. Restoring Proxmox VE Host

1.  **Install Proxmox VE:** Perform a fresh installation of Proxmox VE on the new hardware.
2.  **Basic Configuration:** Configure the network interfaces and storage to match the previous setup.
3.  **Restore Configuration:** Copy the backed-up files from `/etc/proxmox/` to the new host.
4.  **Reboot:** Reboot the host for the changes to take effect.

### 4.3. Restoring a VM or Container

1.  **Navigate to Backup Storage:** In the Proxmox web GUI, navigate to the backup storage location.
2.  **Select Backup:** Select the VM or container and the desired backup date.
3.  **Restore:** Click the "Restore" button and follow the prompts.

### 4.4. Restoring a Network Switch Configuration

1.  **Access the Switch:** Connect to the switch via the console port or SSH.
2.  **Copy Configuration:** Copy the configuration from the `cfg/` directory in this repository to the switch's startup configuration.
3.  **Reboot:** Reboot the switch for the configuration to take effect.

## 5. Backup Testing

*   **Frequency:** Quarterly.
*   **Procedure:**
    1.  Restore a non-critical VM from backup to a new VM ID.
    2.  Verify that the restored VM boots and that all services are running.
    3.  Restore the OPNsense configuration to a test VM.
    4.  Document the results of the test in the `docs/lifecycle/change-management-log.md` file.
