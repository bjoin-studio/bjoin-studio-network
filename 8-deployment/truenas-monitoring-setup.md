# Monitoring TrueNAS with Prometheus

This document outlines the recommended methods for monitoring TrueNAS (both CORE and SCALE) using Prometheus.

## Method 1: Using the Built-in Graphite Exporter (Recommended)

TrueNAS provides built-in support for exporting metrics in the Graphite format. This is the recommended approach as it uses native TrueNAS functionality and does not require installing third-party software directly on the TrueNAS host.

The overall architecture is as follows:

```
TrueNAS -> Graphite Exporter -> Prometheus -> Grafana
```

### 1. Configure TrueNAS Reporting

First, configure TrueNAS to send its metrics to a Graphite server. Even though we are using Prometheus, the `graphite_exporter` will act as this server.

1.  In the TrueNAS UI, navigate to `System -> Reporting`.
2.  Under "Graphite Server", enter the IP address and port of where you will be running the `graphite_exporter`. The default port for Graphite is `2003`.

### 2. Set up the Graphite Exporter

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

### 4. Find a Grafana Dashboard

Once the data is flowing into Prometheus, you can find a suitable Grafana dashboard for TrueNAS on the official Grafana website. A popular choice is the dashboard with ID `12713`.

## Method 2: Using the Node Exporter

Alternatively, you can use the standard Prometheus `node_exporter` to gather host-level metrics from TrueNAS. This is a viable option but may not provide as many TrueNAS-specific metrics as the Graphite method.

### For TrueNAS SCALE

You can run the `node_exporter` as a containerized application directly on TrueNAS SCALE.

### For TrueNAS CORE

You will need to install the `node_exporter` within a jail. Be aware that by default, the exporter will only have access to the jail's metrics, not the host's. Advanced configuration is required to expose host metrics to the jail, which is beyond the scope of this document.

## Conclusion

For most use cases, the `graphite_exporter` method is the most comprehensive and recommended way to monitor TrueNAS with Prometheus. It provides a rich set of metrics with minimal modification to the TrueNAS system itself.
