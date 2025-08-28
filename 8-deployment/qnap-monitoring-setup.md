# Monitoring QNAP with Prometheus and Grafana

This guide provides step-by-step instructions for setting up Prometheus and Grafana to monitor a QNAP NAS. The recommended method uses the `qnapexporter` application, which is specifically designed for this purpose.

## 1. Install `qnapexporter` on your QNAP

The `qnapexporter` is a dedicated exporter that runs on your QNAP and provides metrics in a format that Prometheus can understand.

- **Download the package**: Go to the `qnapexporter` releases page on GitHub and download the latest `.qpkg` file.
- **Manual Installation**: Open the **App Center** on your QNAP, click the "Install Manually" icon (a gear with a plus sign), and select the downloaded `.qpkg` file to install it.

## 2. Configure Prometheus to Scrape QNAP Metrics

You need to configure your Prometheus server to collect the data from the `qnapexporter`.

- **Edit `prometheus.yml`**: Add the following job to your Prometheus configuration file:

  ```yaml
  scrape_configs:
    - job_name: 'qnap'
      static_configs:
        - targets: ['<your-qnap-ip>:9094']
  ```
  *Replace `<your-qnap-ip>` with the actual IP address of your QNAP device. The default port for the exporter is `9094`.*

- **Restart Prometheus**: Reload your Prometheus configuration for the changes to take effect.

## 3. Import Grafana Dashboards

The `qnapexporter` project provides pre-built Grafana dashboards that you can import directly.

- **Download Dashboards**: Go to the `/dashboards` directory in the `qnapexporter` GitHub repository and download the JSON files.
- **Import into Grafana**: In Grafana, go to the "+" icon on the left menu, select "Import," and upload the JSON files. This will create ready-to-use dashboards for your QNAP.

## Alternative Method

For more advanced or customized setups, you can use a combination of SNMP and a Telegraf agent:

1.  **Enable SNMP** on your QNAP device through the Control Panel.
2.  **Configure a Telegraf agent** to poll your QNAP's SNMP service for metrics.
3.  **Configure Telegraf** to send the collected metrics to your Prometheus or InfluxDB instance.
4.  **Create Grafana dashboards** manually to visualize the data.

This method is more flexible but requires significantly more configuration.
