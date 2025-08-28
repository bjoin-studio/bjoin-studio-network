# Monitoring OPNsense with Grafana and Prometheus

This document outlines methods for monitoring OPNsense firewalls using Prometheus and Grafana.

## Overview

For comprehensive monitoring of OPNsense, you can combine two approaches:

1.  **Node Exporter Plugin:** For basic system metrics (CPU, memory, disk, network interfaces).
2.  **Dedicated OPNsense Exporter:** For more in-depth OPNsense-specific metrics, including firewall states, VPNs, and other services.

Both exporters will expose metrics that Prometheus can scrape, and then Grafana can be used for visualization.

## Prerequisites

*   An OPNsense firewall to be monitored.
*   A machine running Prometheus and Grafana (e.g., your Raspberry Pi).
*   Network connectivity between the monitoring machine and the OPNsense firewall.

## Installation Steps

### Method 1: Using the `os-node_exporter` Plugin (Basic System Metrics)

OPNsense offers a `node_exporter` plugin that provides fundamental operating system metrics in a Prometheus-compatible format. This is installed directly on the OPNsense firewall.

**1. Install and Enable the `os-node_exporter` Plugin on OPNsense**

1.  Log in to your OPNsense web interface.
2.  Navigate to **System** > **Firmware** > **Plugins**.
3.  Search for `os-node_exporter` and click the `+` icon to install it.
4.  After installation, navigate to **Services** > **Node Exporter**.
5.  Check **Enable Node Exporter**.
6.  Ensure the **Listen Port** is set to `9100` (default).
7.  Click **Save**.

**2. Configure Prometheus to Scrape OPNsense Node Exporter**

Add the following job to your `prometheus.yml` configuration on your Raspberry Pi:

```yaml
scrape_configs:
  - job_name: 'opnsense_node'
    static_configs:
      - targets: ['<OPNsense_IP_or_FQDN>:9100']
```

Replace `<OPNsense_IP_or_FQDN>` with the actual IP address or fully qualified domain name of your OPNsense firewall.

**3. Import a Grafana Dashboard for Node Exporter**

Standard Node Exporter dashboards can be used. A popular one is dashboard ID `1860` on grafana.com.

### Method 2: Using a Dedicated OPNsense Exporter (Detailed OPNsense Metrics)

For more in-depth metrics specific to OPNsense, its plugins, and services, it's recommended to use a dedicated OPNsense Exporter. This exporter connects to the OPNsense API and can be run on any machine with network access to the OPNsense API (e.g., your Raspberry Pi).

**1. Enable OPNsense API Access and Create API Key**

1.  Log in to your OPNsense web interface.
2.  Navigate to **System** > **Access** > **Users**.
3.  Create a new user (e.g., `prometheus-api`) or use an existing one. Ensure this user has appropriate permissions to access the API (e.g., `System: API: Access`).
4.  Navigate to **System** > **Access** > **API**.
5.  Click `+` to add a new API key. Select the user you created/chose. Note down the **Key** and **Secret**.

**2. Run the OPNsense Exporter Docker Container**

Run the OPNsense Exporter on your Raspberry Pi. Replace the placeholders with your OPNsense details and API key/secret.

```bash
docker run -d \
  --name opnsense_exporter \
  -p 8080:8080 \
  --restart=unless-stopped \
  --network=monitoring \
  ghcr.io/athennamind/opnsense-exporter:latest \
  /opnsense-exporter \
  --opnsense.protocol=https \
  --opnsense.address=<OPNsense_IP_or_FQDN> \
  --opnsense.api-key=<your-api-key> \
  --opnsense.api-secret=<your-api-secret> \
  --exporter.instance-label=opnsense
```

Replace `<OPNsense_IP_or_FQDN>`, `<your-api-key>`, and `<your-api-secret>` with your actual values.

**3. Configure Prometheus to Scrape OPNsense Exporter**

Add the following job to your `prometheus.yml` configuration on your Raspberry Pi:

```yaml
scrape_configs:
  - job_name: 'opnsense_exporter'
    static_configs:
      - targets: ['opnsense_exporter:8080']
```

**4. Import a Grafana Dashboard for OPNsense Exporter**

A dashboard specifically designed for the OPNsense Exporter can be imported into Grafana using ID `21113`.

## Conclusion

By combining these two approaches, you can achieve comprehensive monitoring of your OPNsense firewall with Prometheus and Grafana. The `node_exporter` provides basic system health, while the dedicated OPNsense Exporter offers deep insights into firewall-specific metrics.
