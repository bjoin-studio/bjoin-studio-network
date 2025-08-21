# FreeIPA Server Installation Guide for Proxmox

This guide details how to set up a FreeIPA server as a virtual machine on `pmx-01.bjoin.studio`.

## 1. Virtual Machine (VM) Creation

In the Proxmox web UI, create a new VM with the following specifications.

### General:
- **Node:** `pmx-01`
- **VM ID:** (Proxmox will assign one, e.g., 100)
- **Name:** `ipa-01.bjoin.studio`

### OS:
- **Type:** Linux
- **Version:** Use a recent version (e.g., 6.x or later).
- **ISO Image:** Upload a Rocky Linux 9 ISO to your Proxmox ISO storage.

### System:
- **Guest Agent:** Enable `QEMU Guest Agent` for better management.
- **SCSI Controller:** `VirtIO SCSI single`

### Disks:
- **Bus/Device:** `SCSI`
- **Disk size:** At least `40 GB`.

### CPU:
- **Cores:** At least `2`.

### Memory:
- **Memory:** At least `4096 MB` (4 GB).

### Network:
- **Bridge:** `vmbr51`
- **VLAN Tag:** (Leave blank, as the bridge handles it)
- **Model:** `VirtIO (paravirtualized)`

## 2. Operating System Installation (Rocky Linux 9)

1.  Start the VM and open the console.
2.  Follow the Rocky Linux 9 installation prompts.
3.  **Network Configuration:**
    - During installation, go to `Network & Host Name`.
    - Select the Ethernet interface.
    - Click `Configure...` and go to the `IPv4 Settings` tab.
    - **Method:** Manual
    - **Addresses:** Click `Add`
        - **Address:** `10.20.51.10`
        - **Netmask:** `24`
        - **Gateway:** `10.20.51.1`
    - **DNS servers:** `10.20.51.10` (itself)
    - **Search domains:** `bjoin.studio`
    - Set the **Hostname** to `ipa-01.bjoin.studio`.
4.  Complete the installation and reboot.

## 3. FreeIPA Server Installation

After the VM is running, connect to it via SSH or the Proxmox console.

### 1. Update System and Set Hostname

```bash
sudo dnf update -y
sudo hostnamectl set-hostname ipa-01.bjoin.studio
```

### 2. Install FreeIPA Server Packages

```bash
sudo dnf module enable idm:DL1 -y
sudo dnf install ipa-server ipa-server-dns -y
```

### 3. Run the Installation Script

This interactive script will prompt you for configuration details. Use the values below.

```bash
sudo ipa-server-install
```

**Key Prompts:**
- **Server host name:** `ipa-01.bjoin.studio`
- **Domain name:** `bjoin.studio`
- **Realm name:** `BJOIN.STUDIO` (by default, this is the uppercase of your domain)
- **Directory Manager password:** (Enter a strong password)
- **IPA master password:** (Enter a strong password)
- **Configure integrated DNS:** `yes`
- **Configure chrony as NTP client:** `yes`

Review the configuration and, if correct, type `yes` to continue.

### 4. Configure Firewall

The `ipa-server-install` script configures the firewall on the FreeIPA host itself. The rules below are for your main network firewall (e.g., OPNsense).

```bash
sudo firewall-cmd --add-service=freeipa-ldap --add-service=freeipa-ldaps --permanent
sudo firewall-cmd --reload
```

### 5. Verify Installation

Authenticate as the FreeIPA admin user:

```bash
kinit admin
```

Check that your user is found:

```bash
ipa user-find admin
```

Your FreeIPA server is now ready. You can access its web UI at `https://ipa-01.bjoin.studio/`.

---

## 4. VLAN Integration and Firewall Rules

### Network Location

The FreeIPA server is placed in the **`MGMT` VLAN (VLAN 51)**. This is a security best practice, as it isolates the network's most critical identity service from general user traffic.

### Firewall Configuration

For devices in other VLANs (e.g., `PROD_PERF`, `STUDIO_GENERAL`) to authenticate and get DNS from FreeIPA, you must configure rules on your main network firewall (OPNsense).

The basic principle is to create rules that allow traffic **FROM** a client VLAN (e.g., `VLAN 31 - STUDIO_GENERAL`) **TO** the FreeIPA server's IP address (`10.20.51.10`).

Here are the essential ports to open:

| Port      | Protocol | Service        | Purpose                               |
| :-------- | :------- | :------------- | :------------------------------------ |
| `53`      | TCP/UDP  | **DNS**        | Domain Name Resolution                |
| `88`      | TCP/UDP  | **Kerberos**   | Authentication                        |
| `123`     | UDP      | **NTP**        | Time Synchronization (critical for Kerberos) |
| `389`     | TCP      | **LDAP**       | Directory Lookups                     |
| `443`     | TCP      | **HTTPS**      | Accessing the FreeIPA Web UI          |
| `464`     | TCP/UDP  | **Kerberos Pwd** | Password changes                    |
| `636`     | TCP      | **LDAPS**      | Secure Directory Lookups              |

---

## 5. FreeIPA Integration and Advanced Access Control

FreeIPA provides powerful features to manage access to your network resources centrally. This section covers how to integrate clients and manage advanced access controls.

### 5.1 Client Enrollment

To leverage FreeIPA's centralized authentication and management, client machines (Linux servers, macOS workstations) need to be enrolled into the FreeIPA domain. This typically involves installing the `ipa-client` package and running `ipa-client-install`.

**Linux Client (e.g., Rocky Linux 9):
**
```bash
sudo dnf install ipa-client -y
sudo ipa-client-install --mkhomedir --enable-dns-autodiscovery
```

**macOS Client:
**
macOS can be joined to the FreeIPA domain using the Directory Utility or the `dsconfigad` command-line tool. This allows users to log in with their FreeIPA credentials.

```bash
sudo dsconfigad -add ipa-01.bjoin.studio -domain bjoin.studio -username admin -password <admin_password> -force -mobile enable -localhome enable -useuncpath enable -alldomains enable
```

### 5.2 Sudo Rules Management

FreeIPA allows you to define and manage `sudo` rules centrally, eliminating the need to manage `/etc/sudoers` files on individual machines. This ensures consistent and auditable administrative access.

**Example: Granting `sysadmins` full `sudo` access on all hosts:
**
```bash
# Create a Sudo Command Group (optional, for specific commands)
# ipa sudocmd-add /usr/bin/systemctl --desc='Systemctl command'

# Create a Sudo Rule
ipa sudorule-add sysadmin_full_access --desc='Full sudo access for sysadmins'

# Add the 'sysadmins' group to the rule
ipa sudorule-add-group sysadmin_full_access --groups=sysadmins

# Apply the rule to all hosts (or specific host groups)
ipa sudorule-add-host sysadmin_full_access --hosts=all

# Grant ALL commands (or specific command groups)
ipa sudorule-add-allow_command sysadmin_full_access --sudocmds=ALL

# Enable the rule
ipa sudorule-enable sysadmin_full_access
```

### 5.3 Host-Based Access Control (HBAC)

HBAC rules control which users or groups are allowed to log into specific hosts or host groups. This is crucial for securing your servers.

**Example: Allow `sysadmins` to log into `servers` host group:
**
```bash
# Create a Host Group (if not already defined)
# ipa hostgroup-add servers --desc='All Linux servers'
# ipa hostgroup-add-member servers --hosts=server01.bjoin.studio,server02.bjoin.studio

# Create an HBAC Rule
ipa hbacrule-add sysadmin_server_access --desc='Allow sysadmins to log into servers'

# Add the 'sysadmins' group to the rule
ipa hbacrule-add-user sysadmin_server_access --groups=sysadmins

# Add the 'servers' host group to the rule
ipa hbacrule-add-host sysadmin_server_access --hostgroups=servers

# Allow access to all services (or specific services like sshd)
ipa hbacrule-add-service sysadmin_server_access --services=all

# Enable the rule
ipa hbacrule-enable sysadmin_server_access
```

### 5.4 Integration with Network Services

FreeIPA can integrate with various network services to provide centralized authentication and authorization.

*   **NFS (Network File System):** FreeIPA provides Kerberos authentication for NFS shares, ensuring secure access to shared storage. Clients will use their FreeIPA credentials to mount NFS shares.
*   **SMB/CIFS (Samba):** Samba can be configured to authenticate against FreeIPA, allowing Windows clients and macOS clients to access SMB shares using their FreeIPA credentials.
*   **SSH (Secure Shell):** FreeIPA manages SSH public keys and can enforce HBAC rules for SSH access, providing a secure and centralized way to manage remote access to your servers.
