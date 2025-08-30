# Bootstrap FreeIPA Client

This document outlines the steps to enroll a Linux client to the FreeIPA server (`ipa-01.bjoin.studio`) and configure it to mount user home directories from the TrueNAS server (`truenas-01.bjoin.studio`).

## 1. Enroll Linux Client to FreeIPA

To enroll a Linux client to the FreeIPA domain, follow these general steps. Specific commands may vary slightly depending on your Linux distribution (e.g., Debian/Ubuntu, RHEL/CentOS).

1.  **Ensure Network Connectivity:** Verify that the client can resolve `ipa-01.bjoin.studio` and reach it on the necessary FreeIPA ports (e.g., 80, 443, 389, 636, 88, 464).

2.  **Install FreeIPA Client Package:**
    ```bash
    # Example for Debian/Ubuntu
    sudo apt update
    sudo apt install freeipa-client

    # Example for RHEL/CentOS
    sudo dnf install freeipa-client
    ```

3.  **Run the FreeIPA Client Enrollment Command:**
    ```bash
    sudo ipa-client-install --mkhomedir --enable-dns-updates --server=ipa-01.bjoin.studio --domain=bjoin.studio --realm=BJOIN.STUDIO
    ```
    *   You will be prompted for the FreeIPA admin password or a one-time password for enrollment.
    *   `--mkhomedir`: This option is typically used to automatically create home directories locally. However, we will override this with an NFS mount for `/home`.
    *   `--enable-dns-updates`: Allows the client to update its DNS record in FreeIPA.

4.  **Verify Enrollment:**
    ```bash
    ipa-getkeytab -s ipa-01.bjoin.studio -p host/$(hostname) -k /etc/krb5.keytab
    kinit admin
    ipa host-show $(hostname)
    ```

## 2. Mount Home Directories from TrueNAS via NFS

Instead of local home directories, we will configure the client to mount `/home` from `truenas-01.bjoin.studio` using NFS.

1.  **Install NFS Client Utilities:**
    ```bash
    # Example for Debian/Ubuntu
    sudo apt install nfs-common

    # Example for RHEL/CentOS
    sudo dnf install nfs-utils
    ```

2.  **Create a temporary mount point (if `/home` is not empty or you want to test first):**
    ```bash
    sudo mkdir /mnt/home_temp
    ```

3.  **Test the NFS Mount:**
    ```bash
    sudo mount truenas-01.bjoin.studio:/mnt/home-pool/home-directories /mnt/home_temp
    ls /mnt/home_temp
    sudo umount /mnt/home_temp
    sudo rmdir /mnt/home_temp
    ```

4.  **Configure `/etc/fstab` for Persistent Mount:**
    Before modifying `/etc/fstab`, ensure that the `/home` directory on the client is empty or backed up if it contains any data. If `/home` is not empty, the existing content will be hidden by the NFS mount.

    Add the following line to `/etc/fstab`:
    ```
    truenas-01.bjoin.studio:/mnt/home-pool/home-directories /home nfs auto,nofail,rw,sync,hard,intr,noatime,rsize=8192,wsize=8192,actimeo=0 0 0
    ```
    *   `auto`: Mounts at boot.
    *   `nofail`: Continues booting even if the mount fails.
    *   `rw`: Read-write access.
    *   `sync`: Synchronous writes.
    *   `hard,intr`: Hard mount with interruptible operations.
    *   `noatime`: Do not update access times on files.
    *   `rsize=8192,wsize=8192`: Set read/write buffer sizes (can be tuned).
    *   `actimeo=0`: Disable attribute caching (ensures immediate consistency).

5.  **Mount all entries from `/etc/fstab` (or reboot):**
    ```bash
    sudo mount -a
    ```

6.  **Verify the Mount:**
    ```bash
    df -h /home
    ```
    You should see the TrueNAS share mounted as `/home`.

## 3. Post-Enrollment and Home Directory Configuration

With FreeIPA enrollment and NFS home directories configured, users authenticated via FreeIPA will have their home directories automatically available from the TrueNAS share when they log in.