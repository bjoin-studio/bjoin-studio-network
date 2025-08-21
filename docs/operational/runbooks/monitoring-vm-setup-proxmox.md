# Monitoring VM Setup Guide for Proxmox

This guide provides step-by-step instructions for creating and configuring a dedicated monitoring virtual machine on your Proxmox VE host (`pmx-01.bjoin.studio`). This VM will serve as the central point for collecting network and system metrics, logs, and flow data.

## 1. VM Specifications

*   **Hostname:** `mon-01.bjoin.studio` (or `mon-02`, etc., for additional monitoring VMs)
*   **Purpose:** Centralized monitoring (e.g., Prometheus, Grafana, ELK stack, Zabbix server, flow collector).
*   **Operating System:** Rocky Linux 9 (consistent with other infrastructure VMs).
*   **Network:** Dedicated to `VLAN 55` (Management Monitoring).

### Recommended Resources

These are starting recommendations. Adjust based on the scale of your monitoring needs (number of devices, data retention, etc.).

*   **CPU:** 2-4 Cores
*   **Memory:** 4-8 GB RAM
*   **Disk:** 50-100 GB (SCSI, Thin Provisioned) - Consider a larger disk or separate storage for long-term data retention if using time-series databases.

## 2. Virtual Machine (VM) Creation in Proxmox

Follow these steps in the Proxmox web interface (`https://10.20.51.20:8006`).

### Step 2.1: Create VM Wizard

1.  Click **"Create VM"** in the top right corner.

### Step 2.2: General

*   **Node:** Select `pmx-01`
*   **VM ID:** (Leave as default, Proxmox will assign)
*   **Name:** `mon-01.bjoin.studio`
*   Click **"Next"**

### Step 2.3: OS

*   **Do not use any media:** Select "Do not use any media" for now. We will attach the ISO later.
*   **Guest OS:**
    *   **Type:** `Linux`
    *   **Version:** `6.x or later kernel`
*   Click **"Next"**

### Step 2.4: System

*   **Graphic card:** `Default`
*   **SCSI Controller:** `VirtIO SCSI single` (Recommended for performance)
*   **QEMU Guest Agent:** Check `QEMU Guest Agent` (Highly recommended for better integration)
*   Click **"Next"**

### Step 2.5: Disks

*   **Bus/Device:** `SCSI`
*   **Storage:** Select your preferred storage (e.g., `local-lvm`)
*   **Disk size:** Enter `50` (for 50 GB)
*   **Cache:** `Default (no cache)` or `Write back` for better performance (at higher risk)
*   **Discard:** Check `Discard` (for thin provisioning efficiency)
*   Click **"Next"**

### Step 2.6: CPU

*   **Sockets:** `1`
*   **Cores:** Enter `2` (or `4` if more processing power is needed)
*   **Type:** `host` (Recommended for best performance if CPU features match)
*   Click **"Next"**

### Step 2.7: Memory

*   **Memory (MB):** Enter `4096` (for 4 GB) or `8192` (for 8 GB)
*   Click **"Next"**

### Step 2.8: Network

*   **Bridge:** Select `vmbr55` (This is the bridge for VLAN 55 - Management Monitoring)
*   **VLAN Tag:** (Leave blank, as `vmbr55` is already VLAN-aware)
*   **Model:** `VirtIO (paravirtualized)` (Recommended for performance)
*   Click **"Next"**

### Step 2.9: Confirm

*   Review all settings.
*   Check `Start after created` if you want it to boot immediately.
*   Click **"Finish"**

## 3. Operating System Installation (Rocky Linux 9)

After the VM is created, attach the Rocky Linux 9 ISO to its CD/DVD drive and start the VM.

1.  **Boot from ISO:** In the Proxmox console, ensure the VM boots from the attached ISO.
2.  **Follow Installation Prompts:** Proceed with the standard Rocky Linux 9 installation.
3.  **Network Configuration:**
    *   During installation, go to `Network & Host Name`.
    *   Select the Ethernet interface.
    *   Click `Configure...` and go to the `IPv4 Settings` tab.
    *   **Method:** Manual
    *   **Addresses:** Click `Add`
        *   **Address:** `10.20.55.10` (or another available IP in VLAN 55)
        *   **Netmask:** `24`
        *   **Gateway:** `10.20.55.1` (your OPNsense interface for VLAN 55)
    *   **DNS servers:** `10.20.51.10` (your FreeIPA server)
    *   Set the **Hostname** to `mon-01.bjoin.studio`.
4.  Complete the installation and reboot.

## 4. Post-Installation Basic Setup

After the VM reboots, connect to it via SSH or the Proxmox console.

1.  **Update System:**
    ```bash
    sudo dnf update -y
    ```
2.  **Set Hostname (if not already set):**
    ```bash
    sudo hostnamectl set-hostname mon-01.bjoin.studio
    ```
3.  **Install QEMU Guest Agent:**
    ```bash
    sudo dnf install qemu-guest-agent -y
    sudo systemctl enable --now qemu-guest-agent
    ```
4.  **Enroll in FreeIPA:**
    Follow the client enrollment steps in the `freeipa-server-setup-guide.md` to join `mon-01.bjoin.studio` to your FreeIPA domain. This will centralize user management and DNS.

## 5. Monitoring Specific Setup (High-Level)

Once the VM is set up and enrolled in FreeIPA, you can proceed with installing your chosen monitoring tools.

*   **Install Monitoring Agents:** For collecting system metrics from other servers, install agents like Node Exporter (for Prometheus) or Telegraf.
*   **Install Monitoring Server Software:** Deploy your chosen monitoring solution (e.g., Prometheus, Grafana, Zabbix, ELK stack components, flow collector).
*   **Configure Data Sources:** Point your monitoring tools to collect data from your network devices (via SNMP, NetFlow/sFlow) and other servers (via agents).

For more details on network monitoring concepts and configuration, refer to the `network-monitoring-setup.md` runbook.
