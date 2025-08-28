# Monitoring Across VLANs and with SNMP

This guide explains the concepts and steps required to monitor devices across different VLANs and to monitor SNMP-enabled devices using your Prometheus and Grafana setup.

## 1. Monitoring Across Separate VLANs

Your network is segmented into multiple VLANs for security and organization. Your monitoring server (running Prometheus) resides in one of these VLANs (e.g., the Management VLAN). To monitor a target device (like a web server or database) in a different VLAN (e.g., the Production VLAN), you must explicitly allow the monitoring traffic to pass through the firewall.

### How It Works

1.  **Exporter:** The target device runs a Prometheus exporter (e.g., `node_exporter` on port 9100) that exposes metrics.
2.  **Firewall Rule:** You create a rule in OPNsense that allows the IP address of your Prometheus server to connect to the IP address of the target device on its exporter port (e.g., allow `192.168.50.10` to access `192.168.10.100:9100`).
3.  **Prometheus Target:** You add the target device's IP address and port to your `prometheus.yml` configuration.
4.  **Grafana Visualization:** Once Prometheus is scraping the data, you can build dashboards in Grafana to visualize it. You can use labels in Prometheus to tag metrics by VLAN, allowing you to easily filter and create VLAN-specific dashboards.

This architecture ensures that your network remains secure by default, while allowing specific, controlled access for monitoring.

## 2. Monitoring SNMP-Enabled Devices

Many network devices (switches, firewalls, printers, NAS devices) do not have Prometheus exporters but support the Simple Network Management Protocol (SNMP). You can monitor these devices by using a special translator called `snmp_exporter`.

### How It Works

The data flows like this: `Device -> SNMP -> snmp_exporter -> Prometheus -> Grafana`

1.  **Enable SNMP on the Target Device:** First, you need to enable the SNMP service on the device you want to monitor (e.g., a Cisco switch or your QNAP NAS). You will typically configure an SNMP version (v2c is common) and a "community string" (which acts like a password).

2.  **Configure `snmp_exporter`:** The `snmp_exporter` needs to know how to connect to your devices and what metrics to ask for. This is done in its configuration file, `snmp.yml`. You define "modules" that specify the OIDs (Object Identifiers) to query for a particular device type.

3.  **Configure Prometheus to Scrape `snmp_exporter`:** You then configure a job in your `prometheus.yml` file. This job tells Prometheus to scrape the `snmp_exporter` itself, passing the IP address of the final target device as a parameter. Prometheus never talks to the end device directly.

    ```yaml
    scrape_configs:
      - job_name: 'snmp'
        static_configs:
          - targets:
              - 192.168.1.2  # IP of the switch to monitor
        relabel_configs:
          - source_labels: [__address__]
            target_label: __param_target
          - source_labels: [__param_target]
            target_label: instance
          - target_label: __address__
            replacement: 127.0.0.1:9116  # Address of the snmp_exporter
    ```

4.  **Visualize in Grafana:** Once the SNMP data is in Prometheus, you can build dashboards in Grafana just like any other metric. You can create graphs for network bandwidth per port, device uptime, CPU temperature, or any other data point exposed via SNMP.

By using `snmp_exporter`, you can bring a huge range of devices into your central monitoring system, providing a single pane of glass for your entire network infrastructure.
