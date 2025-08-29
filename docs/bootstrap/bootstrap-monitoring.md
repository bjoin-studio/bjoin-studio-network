# Bootstrap: Grafana Monitoring Station (monitor-01.bjoin.studio)

This document outlines the steps to configure a Raspberry Pi as a Grafana monitoring station, including setting its hostname, FQDN, static IPv4 address, and enrolling it into FreeIPA.

## 1. Initial Setup and Hostname Configuration

1.  **Update System:**
    ```bash
    sudo apt update
    sudo apt full-upgrade -y
    ```

2.  **Set Short Hostname:**
    Edit `/etc/hostname` and replace its content with `monitor-01`.
    ```bash
    sudo echo "monitor-01" | sudo tee /etc/hostname
    ```

3.  **Update `/etc/hosts`:**
    Ensure `/etc/hosts` contains entries for the new hostname and FQDN. It should look similar to this (adjust IP if necessary, this will be the static IP you assign):
    ```
    127.0.0.1       localhost
    127.0.1.1       monitor-01.bjoin.studio monitor-01

    # The following lines are desirable for IPv6 capable hosts
    ::1     localhost ip6-localhost ip6-loopback
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
    ```
    You can use `sudo nano /etc/hosts` or `sudo vi /etc/hosts` to edit this file.

4.  **Reboot to Apply Hostname Changes:**
    ```bash
    sudo reboot
    ```
    After reboot, verify the hostname:
    ```bash
    hostname
    hostname -f
    ```
    The first command should return `monitor-01` and the second `monitor-01.bjoin.studio`.

## 2. Static IPv4 Address Configuration

This section details how to configure a static IPv4 address for `monitor-01.bjoin.studio` within the `10.20.51.0/24` subnet.

**Important:** Before proceeding, you must select an available IP address from the `10.20.51.0/24` range. Refer to `docs/architecture/static-ip-addresses.md` and perform a network scan to ensure the chosen IP is not in use.

**Example Configuration (using `dhcpcd.conf` - common for Raspberry Pi OS):**

1.  **Edit `dhcpcd.conf`:**
    ```bash
    sudo nano /etc/dhcpcd.conf
    ```
2.  **Add the following lines to the end of the file (replace `YOUR_STATIC_IP`, `YOUR_ROUTER_IP`, and `YOUR_DNS_SERVER_IP` with actual values):**

    ```
    # Static IP configuration for monitor-01
    interface eth0
    static ip_address=YOUR_STATIC_IP/24
    static routers=YOUR_ROUTER_IP
    static domain_name_servers=YOUR_DNS_SERVER_IP
    ```
    *   `YOUR_STATIC_IP`: The chosen static IP address (e.g., `10.20.51.10`).
    *   `YOUR_ROUTER_IP`: The IP address of your default gateway/router in the `10.20.51.0/24` subnet (e.g., `10.20.51.1`).
    *   `YOUR_DNS_SERVER_IP`: The IP address of your DNS server (e.g., `10.20.51.100` or `ipa-01.bjoin.studio`'s IP).

3.  **Restart `dhcpcd` service:**
    ```bash
    sudo systemctl restart dhcpcd
    ```

4.  **Verify IP Address:**
    ```bash
    ip a show eth0
    ```
    Confirm that the `eth0` interface now has the assigned static IP address.

## 3. FreeIPA Enrollment

This section details how to enroll `monitor-01.bjoin.studio` into your FreeIPA domain (`ipa-01.bjoin.studio`).

1.  **Ensure DNS Resolution:**
    Before enrolling, ensure your Raspberry Pi can resolve the FreeIPA server's hostname (`ipa-01.bjoin.studio`). You can test this with `ping ipa-01.bjoin.studio` or `dig ipa-01.bjoin.studio`.
    If DNS resolution fails, temporarily add an entry to `/etc/hosts` on the Raspberry Pi:
    ```
    YOUR_IPA_SERVER_IP ipa-01.bjoin.studio
    ```
    (Replace `YOUR_IPA_SERVER_IP` with the actual IP address of your FreeIPA server).

2.  **Install FreeIPA Client:**
    ```bash
    sudo apt update
    sudo apt install -y freeipa-client
    ```

3.  **Enroll the Client:**
    Use the `ipa-client-install` command. You will be prompted for the FreeIPA admin password.
    ```bash
    sudo ipa-client-install --mkhomedir --enable-dns-updates --force-join --server=ipa-01.bjoin.studio --domain=bjoin.studio --realm=BJOIN.STUDIO -p admin
    ```
    *   `--mkhomedir`: Creates home directories for IPA users on first login.
    *   `--enable-dns-updates`: Allows the client to update its DNS record in FreeIPA (requires appropriate permissions).
    *   `--force-join`: Forces the join even if there are existing entries (use with caution).
    *   `--server=ipa-01.bjoin.studio`: Specifies your FreeIPA server.
    *   `--domain=bjoin.studio`: Your FreeIPA domain.
    *   `--realm=BJOIN.STUDIO`: Your FreeIPA realm (usually uppercase version of domain).
    *   `-p admin`: Prompts for the `admin` user's password for enrollment.

    Alternatively, for a non-interactive enrollment using a one-time password (OTP) generated on the FreeIPA server:
    First, on your FreeIPA server, generate an OTP for the host:
    ```bash
    ipa host-add --random monitor-01.bjoin.studio
    ipa otp-generate --host=monitor-01.bjoin.studio
    ```
    Then, on the Raspberry Pi client:
    ```bash
    sudo ipa-client-install --mkhomedir --enable-dns-updates --force-join --server=ipa-01.bjoin.studio --domain=bjoin.studio --realm=BJOIN.STUDIO --otp=YOUR_OTP_HERE
    ```
    (Replace `YOUR_OTP_HERE` with the OTP generated on the FreeIPA server).

4.  **Verify Enrollment:**
    After enrollment, you can verify the status:
    ```bash
    ipa host-find monitor-01.bjoin.studio
    ```
    You should also be able to log in with an IPA user account.

## 4. Next Steps

*   Proceed with installing Grafana and other monitoring agents as needed.
*   Update `docs/architecture/static-ip-addresses.md` with the final assigned IP address for `monitor-01.bjoin.studio`.
