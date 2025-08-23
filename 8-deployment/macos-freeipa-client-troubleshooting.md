# macOS FreeIPA Client Troubleshooting Guide

This guide provides solutions for common DNS and Kerberos issues encountered when connecting a macOS client to a FreeIPA domain for the first time, especially when the Mac has not been formally enrolled as a client.

## Symptom 1: Cannot Resolve Hostnames

You try to access the FreeIPA web UI at `https://ipa-01.bjoin.studio` or ping the hostname, but you receive an error.

*   **Browser Error:** `This site can’t be reached` / `DNS_PROBE_FINISHED_NXDOMAIN`
*   **Ping Error:** `ping: cannot resolve ipa-01.bjoin.studio: Unknown host`

This indicates that your Mac is not using the FreeIPA server for DNS resolution.

### Diagnosis Step 1: Verify Server-Side DNS

First, confirm the FreeIPA DNS server is working correctly by running a direct `nslookup` from your Mac's terminal. This command specifically queries your IPA server.

```bash
nslookup ipa-01.bjoin.studio 10.20.51.10
```

A successful response will look like this, confirming the server's DNS service is running:
```
Server:		10.20.51.10
Address:	10.20.51.10#53

Name:	ipa-01.bjoin.studio
Address: 10.20.51.10
```

### Diagnosis Step 2: Check Your Mac's DNS Configuration

The most reliable way to check the active DNS configuration on macOS is with the `scutil` command.

```bash
scutil --dns
```

Look at the first `resolver` section in the output. If the `nameserver` listed is not your FreeIPA server's IP (`10.20.51.10`), you have found the problem. This often happens when multiple network interfaces (e.g., Wi-Fi and Ethernet) are active.

### Solution: Prioritize the Correct Network Interface

You must tell macOS to prioritize the network connection that is on the FreeIPA network.

1.  Open **System Settings > Network**.
2.  At the bottom of the list of network interfaces, click the **three-dots icon (...)**.
3.  From the menu, choose **Set Service Order...**.
4.  In the new window, **drag your Ethernet connection (or the interface connected to the FreeIPA VLAN) to the top of the list.**
5.  Click **OK**, then click **Apply**.
6.  Flush the DNS cache to ensure the changes take effect immediately:
    ```bash
    sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
    ```

After this, running `ping ipa-01.bjoin.studio` should succeed.

## Symptom 2: `kinit` Fails for Kerberos

After fixing DNS, you try to get a Kerberos ticket with `kinit admin`, but it fails.

*   **Error 1:** `kinit: krb5_parse_name: Configuration file does not specify default realm`
    *   **Cause:** Your Mac doesn't have a Kerberos configuration file.

*   **Error 2:** `kinit: krb5_get_init_creds: unable to reach any KDC in realm BJOIN.STUDIO`
    *   **Cause:** Your Mac found the Kerberos config file but could not resolve the KDC's hostname, usually due to the DNS issues described above.

### Solution: Create `/etc/krb5.conf`

To allow command-line Kerberos tools to work, you need to create a configuration file.

1.  Run this command in your terminal:
    ```bash
    sudo nano /etc/krb5.conf
    ```
2.  Paste the following content into the editor:
    ```ini
    [libdefaults]
     default_realm = BJOIN.STUDIO
     dns_lookup_realm = true
     dns_lookup_kdc = true

    [realms]
     BJOIN.STUDIO = {
      kdc = ipa-01.bjoin.studio
      admin_server = ipa-01.bjoin.studio
     }

    [domain_realm]
     .bjoin.studio = BJOIN.STUDIO
     bjoin.studio = BJOIN.STUDIO
    ```
3.  Press `Ctrl+X`, then `Y`, then `Enter` to save the file.

After creating this file and ensuring your DNS is configured correctly, `kinit admin` will succeed.
