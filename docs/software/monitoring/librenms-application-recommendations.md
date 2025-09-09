# LibreNMS Application Recommendations for Comprehensive Monitoring

This document provides recommendations for which LibreNMS applications to enable, tailored to common monitoring requirements across network, storage, power, and endpoint devices. It also includes general recommendations for a robust monitoring setup.

## I. Network Monitoring (Switches, Firewall)

*   **SNMP:** Absolutely essential. This is the primary protocol LibreNMS uses to gather data from network devices like switches and firewalls. It will provide interface statistics (traffic, errors, discards), CPU/memory usage, uptime, and more. Ensure SNMP is enabled and configured on all your switches and firewalls.
*   **Nginx / Apache:** If your firewall or any network appliance runs a web server (e.g., for its management interface), enabling these can provide insights into its web service performance.
*   **NTP Client / NTP Server / Chronyd:** Crucial for time synchronization. Monitoring these ensures your network devices and servers have accurate time.
*   **BIND / Unbound / PowerDNS (dnsdist, Recursor, PowerDNS):** If you run any DNS servers on your network (e.g., on your firewall or a dedicated server), enable the relevant one. DNS monitoring is critical for network health.
*   **DHCP Stats:** If your firewall or a dedicated server acts as a DHCP server, monitoring its statistics (lease usage, errors) is important for client connectivity.
*   **Fail2ban:** If you're using Fail2ban for intrusion prevention, monitoring its logs and actions can be valuable.
*   **Suricata / Suricata Extract:** If your firewall (like OPNsense) runs Suricata for IDS/IPS, enabling these will allow LibreNMS to monitor its alerts and performance.
*   **Wireguard:** If you're using Wireguard VPNs on your firewall or other devices, this will help monitor their status.

## II. NAS Monitoring (Storage, Heat, Failures)

*   **ZFS:** Highly Recommended for TrueNAS/FreeNAS. This will provide detailed metrics on your ZFS pools, datasets, ARC cache, and disk health, directly addressing your "storage, heat, failures" requirements for ZFS-based NAS.
*   **SMART:** Essential for any NAS with local drives. This monitors the Self-Monitoring, Analysis and Reporting Technology data from your hard drives, providing early warnings of impending drive failures.
*   **NFS Server / NFS Stats / NFS v3 Stats / NFS:** If your NAS provides NFS shares, these will monitor the performance and usage of those shares.
*   **Docker:** If your NAS runs Docker containers (e.g., TrueNAS SCALE), monitoring Docker can give you insights into container resource usage.
*   **MySQL / Postgres / Redis / Memcached:** If your NAS hosts any of these database/caching services for other applications, enable them.
*   **Systemd:** For general service monitoring on Linux-based NAS systems.
*   **OS Updates:** To track pending OS updates on your NAS.

## III. UPS Battery Backups

*   **UPS apcups / UPS nut:** Essential. Enable the one that matches your UPS brand/protocol. This will monitor battery status, load, runtime, input/output voltage, and alert you to power events.

## IV. Workstation Monitoring (Uptime, Local Storage, OS, Heat, Failures, etc.)

*   **SNMP:** While less common on standard workstations, if you can enable SNMP on them (e.g., via an agent), it's a good general monitoring method.
*   **Linux Config Files / Linux Softnet Stat:** For Linux workstations, these provide core OS metrics.
*   **SMART:** For monitoring the health of local hard drives on workstations.
*   **OS Updates:** To track pending OS updates on your workstations.
*   **Systemd:** For monitoring services on Linux workstations.
*   **Random entropy:** Useful for monitoring system entropy, which can impact cryptographic operations.
*   **Socket Statistics:** For detailed network socket usage.
*   **Logsize:** To monitor the size of important log files.

## V. Beyond (General Recommendations for a Robust Setup)

*   **PHP-FPM:** Since LibreNMS itself is a PHP application, monitoring PHP-FPM is crucial for its own performance and stability.
*   **MySQL:** LibreNMS's own database. Monitoring it ensures LibreNMS itself is healthy.
*   **Redis / Memcached:** LibreNMS uses these for caching. Monitoring them ensures LibreNMS's performance.
*   **OS Level Virtualization:** If you run VMs or containers on your workstations (e.g., via KVM, VirtualBox, or Docker Desktop), this can provide insights into their resource usage.
*   **Proxmox:** If you have Proxmox VE hosts, this is essential for monitoring your virtualization environment.
*   **Elasticsearch/Opensearch:** If you have a centralized logging solution using these, monitoring them is important.
*   **Certificate:** To monitor SSL/TLS certificate expiration on any web services or devices.

This selection provides a strong foundation for monitoring your specified infrastructure, covering uptime, performance, health, and potential failures across your network, storage, power, and endpoints. It also includes the core components that ensure LibreNMS itself is running optimally. You can always enable more applications later as your monitoring needs evolve or as you identify specific services you want to track.
