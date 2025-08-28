# Monitoring FreeIPA with Grafana and Prometheus

This document outlines the recommended method for monitoring FreeIPA using Prometheus and Grafana.

## Overview

Monitoring FreeIPA involves using a dedicated Prometheus exporter to collect metrics from your FreeIPA environment. These metrics are then scraped by Prometheus and visualized in Grafana.

## Prerequisites

*   A FreeIPA server (`ipa-01.bjoin.studio`) to be monitored.
*   A machine running Prometheus and Grafana (e.g., your Raspberry Pi).
*   Network connectivity between the monitoring machine and the FreeIPA server.

## Installation Steps

### Step 1: Run the FreeIPA Exporter Docker Container

The `wwwlde/freeipa-exporter` is a dedicated Prometheus exporter for FreeIPA that collects a wide range of metrics. It can be easily deployed as a Docker container on your Raspberry Pi, connected to the `monitoring` network.

**1. Create a FreeIPA User for the Exporter (Recommended)**

For security, it's recommended to create a dedicated read-only user in FreeIPA for the exporter to use. This user will only need permissions to read FreeIPA data.

**2. Run the FreeIPA Exporter Container**

Replace `<your-freeipa-domain>`, `<bind-dn>`, and `<password>` with your FreeIPA details. The `bind-dn` is typically `uid=<username>,cn=users,cn=accounts,<your-freeipa-domain-base>`. For example, if your domain is `example.com`, the base would be `dc=example,dc=com`.

```bash
docker run -d \
  --name freeipa_exporter \
  -p 9100:9100 \
  --restart=unless-stopped \
  --network=monitoring \
  wwwlde/freeipa-exporter \
  --freeipa.domain=<your-freeipa-domain> \
  --freeipa.bind-dn=<bind-dn> \
  --freeipa.password=<password> \
  --freeipa.insecure-skip-verify
```

**Note:** `--freeipa.insecure-skip-verify` is used to skip SSL certificate verification. For production environments, it's recommended to properly configure SSL/TLS.

### Step 2: Configure Prometheus to Scrape the FreeIPA Exporter

Add the following job to your `prometheus.yml` configuration on your Raspberry Pi:

```yaml
scrape_configs:
  - job_name: 'freeipa'
    static_configs:
      - targets: ['freeipa_exporter:9100']
```

### Step 3: Create a Custom Grafana Dashboard

While a specific pre-built Grafana dashboard ID for FreeIPA might not be readily available, you can create a custom dashboard using the metrics exposed by the `freeipa-exporter`. Some key metrics include:

*   `ipa_users_total`: Total number of users.
*   `ipa_hosts_total`: Total number of hosts.
*   `ipa_services_total`: Total number of services.
*   `ipa_replication_status`: Replication status (0=OK, 1=Error).
*   `ipa_up`: Indicates if the last scrape was successful (1=yes, 0=no).
*   `ipa_scrape_duration_seconds`: Time taken to scrape metrics.

To create a custom dashboard:

1.  Open Grafana and create a new dashboard.
2.  Add new panels and select Prometheus as the data source.
3.  Use PromQL (Prometheus Query Language) to query the `ipa_` metrics exposed by the exporter.

## Conclusion

By following these steps, you can set up comprehensive monitoring for your FreeIPA environment, gaining insights into its health and performance.
