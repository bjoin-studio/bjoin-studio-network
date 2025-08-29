# Static IP Address Assignments

This document records all static IP address assignments within the bjoin.studio network.

## How to Use This Document

*   **Record New Assignments:** When assigning a new static IP, add an entry to the relevant subnet section.
*   **Check Availability:** Before assigning an IP, consult this document and perform a network scan (e.g., using `nmap` or `arp-scan`) to ensure the IP is not currently in use.
*   **Update Changes:** Keep this document updated with any changes to static IP configurations.

## Subnet: 10.20.51.0/24 (Monitoring Network)

| Hostname / FQDN | IP Address | Purpose / Description | Status |
| :---------------- | :--------- | :-------------------- | :----- |
| `monitor-01.bjoin.studio` | `10.20.51.X` | Grafana Monitoring Station | Planned |
