# Client Automount Configuration Guide

This guide provides step-by-step instructions for configuring Linux and macOS clients to automatically mount NFS home directories and other network shares via FreeIPA's automount service.

## 1. FreeIPA Server-Side Setup (Recap)

Before configuring clients, ensure the following automount maps are set up in your FreeIPA server (`ipa-01.bjoin.studio`). We configured these in a previous session.

### 1.1. `auto.home` Map (for user home directories)

This map is typically used for `/home` directories, where `&` is replaced by the username.

```bash
# Create the auto.home map
ipa automountmap-add default auto.home --desc='User home directories'

# Add master map entry for /home
ipa automountkey-add default auto.master --key=/home --info=auto.home

# Add wildcard key for user directories
# Replace 10.20.51.81 and /mnt/home-pool/home-directories with your NFS server and export path
ipa automountkey-add default auto.home --key='*' --info='-fstype=nfs,rw,hard,intr 10.20.51.81:/mnt/home-pool/home-directories/&'
```

### 1.2. `auto_nfs` Map (for generic NFS shares)

This map can be used for other general NFS shares, mounted under a common base directory like `/nfs`.

```bash
# Create the auto_nfs map
ipa automountmap-add default auto_nfs --desc='Generic NFS shares'

# Add master map entry for /nfs
ipa automountkey-add default auto.master --key=/nfs --info=auto_nfs

# Add a sample entry to auto_nfs (e.g., for a /data share from hypothetical storage-server-01)
# Replace storage-server-01.bjoin.studio and /export/data with your server and export path
ipa automountkey-add default auto_nfs --key=data --info='-fstype=nfs,rw,hard,intr storage-server-01.bjoin.studio:/export/data'
```

## 2. Linux Client Configuration (e.g., Fedora, Rocky Linux)

For Linux clients, `ipa-client-install` typically configures `autofs` automatically. You just need to ensure the `autofs` service is running.

### 2.1. Prerequisites

Ensure `autofs` is installed:

```bash
sudo dnf install autofs -y
```

### 2.2. Verify `autofs` Configuration

`ipa-client-install` should have configured `/etc/auto.master` to point to SSSD for automount maps. Verify this entry exists:

```bash
grep sss /etc/auto.master
```

Expected output:
```
/home program:/usr/sbin/sssd-autofs --uid=0 --gid=0 --map-name=auto.home
/nfs program:/usr/sbin/sssd-autofs --uid=0 --gid=0 --map-name=auto_nfs
```

### 2.3. Start and Enable `autofs` Service

```bash
sudo systemctl enable --now autofs
```

### 2.4. Test Automount

Once `autofs` is running, try to access a user's home directory or an NFS share. The directory will appear empty until you try to access a file within it.

- **Test `auto.home`:** (Replace `phil.man` with an actual FreeIPA user)

```bash
ls /home/phil.man
```

- **Test `auto_nfs`:** (Replace `data` with the key you added to `auto_nfs`)

```bash
ls /nfs/data
```

## 3. macOS Client Configuration

macOS uses `auto_master` for its master automount map. Configuration is done via `Directory Utility` or by manually editing files.

### 3.1. Prerequisites

Ensure your macOS client is bound to the FreeIPA domain. This is typically done via **System Settings > Users & Groups > Login Options > Network Account Server > Join**.

### 3.2. Edit `auto_master`

Open the `auto_master` file for editing. This file defines the top-level mount points.

```bash
sudo nano /etc/auto_master
```

Add the following lines to the end of the file:

```
# FreeIPA Automount Maps
/home		auto_home	-nobrowse,hidefromfinder
/nfs		auto_nfs	-nobrowse,hidefromfinder
```

Save and exit the file.

### 3.3. Create Map Files

Now, create the individual map files that `auto_master` points to.

#### 3.3.1. `auto_home` (for user home directories)

Create `/etc/auto_home`:

```bash
sudo nano /etc/auto_home
```

Paste the following content. Replace `truenas-01.bjoin.studio` and `/mnt/home-pool/home-directories` with your NFS server and export path.

```
# FreeIPA Home Directory Map
* -fstype=nfs,rw,hard,intr,resvport,nfsvers=3,proto=tcp truenas-01.bjoin.studio:/mnt/home-pool/home-directories/&
```

#### 3.3.2. `auto_nfs` (for generic NFS shares)

Create `/etc/auto_nfs`:

```bash
sudo nano /etc/auto_nfs
```

Paste the following content, adapted from your example. Remember to replace the placeholder IPs with your actual server IPs.

```
# FreeIPA Generic NFS Map

# Synology: Jacksonville
/mnt/ADSK_BACKUP                -fstype=nfs,rw,resvport,nfsvers=4       10.20.51.X:/volume1/ADSK_BACKUP
/mnt/ARCHIVE                    -fstype=nfs,rw,resvport,nfsvers=4       10.20.51.X:/volume1/ARCHIVE
/mnt/PROJEKTS                   -fstype=nfs,rw,resvport,nfsvers=4       10.20.51.X:/volume1/PROJEKTS
/mnt/RESOURCES                  -fstype=nfs,rw,resvport,nfsvers=4       10.20.51.X:/volume1/RESOURCES

# MyCloudPR4100: Kampala
/mnt/COMPLETED_PROJEKTS         -fstype=nfs,rw,resvport,nfsvers=3       10.20.51.Y:/mnt/HD/HD_a2/COMPLETED_PROJEKTS

# TrueNAS: Kowloon
/mnt/COMMON                     -fstype=nfs,rw,resvport,nfsvers=4       truenas-01.bjoin.studio:/mnt/home-pool/common
```

### 3.4. Reload Automount Service

After making changes to `auto_master` or any of the map files, you need to reload the automount service.

```bash
sudo automount -vc
```

### 3.5. Test Automount

- **Test `auto.home`:** (Replace `phil.man` with an actual FreeIPA user)

```bash
ls /home/phil.man
```

- **Test `auto_nfs`:** (Replace `data` with the key you added to `auto_nfs`)

```bash
ls /nfs/data
```

## 4. Troubleshooting

- **Check `autofs` status (Linux):** `sudo systemctl status autofs`
- **Check `automount` status (macOS):** `sudo automount -vc` (look for errors in the output)
- **Verify NFS server export:** Ensure the NFS server is exporting the shares correctly and its firewall allows access from the client.
- **Client Firewall:** Ensure the client's firewall (e.g., `firewalld` on Linux) allows NFS traffic (ports 2049, 111, etc.).
- **Permissions:** Check file system permissions on the NFS server.