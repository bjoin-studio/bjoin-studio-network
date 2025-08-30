# Monitoring TrueNAS with Prometheus

This document outlines the recommended methods for monitoring TrueNAS (both CORE and SCALE) using Prometheus. Specifically, `truenas-01.bjoin.studio`, which is a TrueNAS Community Edition 25.04 (SCALE) virtual machine hosted on `pmx-01.bjoin.studio` (Proxmox PVE), is the focus of this monitoring setup.

## Method 1: Using the Built-in Graphite Exporter (Recommended)

TrueNAS includes built-in functionality to export its reporting data in a Graphite-compatible format. This allows TrueNAS to send its system metrics to a Graphite server or a Graphite-compatible data collection service for storage and visualization. This is the recommended approach as it uses native TrueNAS functionality and does not require installing third-party software directly on the TrueNAS host.

The overall architecture is as follows:

```
TrueNAS -> Graphite Exporter -> Prometheus -> Grafana
```

### 1. Configure TrueNAS Reporting

First, configure TrueNAS to send its metrics to a Graphite server. Even though we are using Prometheus, the `graphite_exporter` will act as this server.

1.  **Access Reporting Exporters:** In the TrueNAS UI, navigate to `Reporting` from the side-menu, and then locate the `Reporting Exporters` section.
2.  **Add Graphite Exporter:** Click `Add` to create a new reporting exporter.
3.  **Configure Graphite Settings:** Fill in the following fields:
    *   **Name:** Provide a unique name for this exporter instance (e.g., `TrueNAS01GraphiteExporter`).
    *   **Type:** Select `GRAPHITE` as the export type.
    *   **Enable:** Check this box to activate the exporter.
    *   **Destination IP:** Enter the IP address of your `graphite_exporter` instance. **This is the machine where the `graphite_exporter` Docker container (or standalone application) is running.** For your setup, this would be `10.20.51.103` (the IP of `monitor-01.bjoin.studio`).
    *   **Destination Port:** Specify the port number that the `graphite_exporter` is listening on for incoming data. The default port for Graphite is `2003`.
    *   **Prefix:** Define a prefix for the metrics. **Recommended: `truenas-01`** (to reflect the specific TrueNAS instance).
    *   **Namespace:** Define a namespace for the metrics. Recommended: `metrics`.
    *   **Update Every:** (Optional) How often metrics are sent (in seconds). The default value is usually fine. You can leave it as is.
    *   **Buffer On Failures:** (Optional) Whether to buffer metrics if sending fails. **Recommended: Check this box** to prevent data loss during temporary network issues.
    *   **Send Names Instead Of IDs:** (Optional) Whether to send chart names instead of internal IDs. **Recommended: Check this box** for more human-readable metric names in Prometheus and Grafana.
    *   **Matching Charts:** (Optional) You can select specific charts to export, or leave blank to export all.
4.  **Save:** Click `Save` to apply the configuration.

Once configured and enabled, TrueNAS will automatically export its reporting metrics to the specified Graphite server, allowing for centralized monitoring and analysis of your TrueNAS system's performance.

### 2. Set up the Graphite Exporter

**Important:** Ensure the `graphite_exporter` is running on `monitor-01.bjoin.studio` (10.20.51.103) *before* configuring TrueNAS to send metrics to it.

The `graphite_exporter` is a Prometheus community-maintained exporter that ingests Graphite data and exposes it as Prometheus metrics.

You can run the `graphite_exporter` as a Docker container. Here is an example `docker run` command:

```bash
docker run -d \
  --name graphite_exporter \
  -p 9108:9108 \
  -p 9109:9109/udp \
  -p 2003:2003 \
  --restart=unless-stopped \
  --network=monitoring \
  prom/graphite-exporter
```

### 3. Configure Prometheus to Scrape the Exporter

Finally, configure your Prometheus instance to scrape the `graphite_exporter`. Add the following job to your `prometheus.yml` configuration:

```yaml
scrape_configs:
  - job_name: 'truenas'
    static_configs:
      - targets: ['graphite_exporter:9108']
```

### 4. Configure Grafana Data Source

Before importing a dashboard, you need to configure Grafana to use Prometheus as a data source.

1.  **Access Grafana:** Open your web browser and go to your Grafana instance (e.g., `http://monitor-01.bjoin.studio:3000`).
2.  **Add Data Source:**
    *   In the Grafana UI, navigate to **Connections** (usually a plug icon on the left sidebar).
    *   Click on **Data sources**.
    *   Click the **Add new data source** button.
3.  **Select Prometheus:** From the list of data source types, choose **Prometheus**.
4.  **Configure Prometheus Data Source:**
    *   **Name:** Give it a descriptive name, like `Prometheus` or `Local Prometheus`.
    *   **URL:** This is the address where Grafana can reach your Prometheus server. Since Prometheus is running on the same machine as Grafana and likely exposed on its default port `9090`, you would use: `http://localhost:9090`.
    *   Leave other settings as default unless you have specific requirements.
5.  **Save & Test:** Click the **Save & test** button. You should see a "Data source is working" message.

### 5. Find a Grafana Dashboard

Once the data is flowing into Prometheus, you can find a suitable Grafana dashboard for TrueNAS on the official Grafana website. Go to [grafana.com/grafana/dashboards/](https://grafana.com/grafana/dashboards/) and search for "TrueNAS" or "TrueNAS SCALE". Look for dashboards that explicitly mention Prometheus as their data source.

## Method 2: Using the Node Exporter

Alternatively, you can use the standard Prometheus `node_exporter` to gather host-level metrics from TrueNAS. This is a viable option but may not provide as many TrueNAS-specific metrics as the Graphite method.

### For TrueNAS SCALE

You can run the `node_exporter` as a containerized application directly on TrueNAS SCALE.

### For TrueNAS CORE

You will need to install the `node_exporter` within a jail. Be aware that by default, the exporter will only have access to the jail's metrics, not the host's. Advanced configuration is required to expose host metrics to the jail, which is beyond the scope of this document.

## Conclusion

For most use cases, the `graphite_exporter` method is the most comprehensive and recommended way to monitor TrueNAS with Prometheus. It provides a rich set of metrics with minimal modification to the TrueNAS system itself.
