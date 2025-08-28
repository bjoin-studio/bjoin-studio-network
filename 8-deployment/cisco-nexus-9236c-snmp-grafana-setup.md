# Cisco Nexus 9236C - SNMP and Grafana Integration Runbook

This runbook details the steps to configure SNMP on a Cisco Nexus 9236C switch and integrate its monitoring data into Grafana.

## 1. Configure SNMP on Cisco Nexus 9236C

Access the switch via console or SSH and enter global configuration mode.

```cli
configure terminal
```

### 1.1. Configure SNMPv2c Community String (Read-Only)

It is recommended to use SNMPv3 for enhanced security, but SNMPv2c is simpler for basic monitoring. Replace `YOUR_SNMP_COMMUNITY_STRING` with a strong, unique string.

```cli
snmp-server community YOUR_SNMP_COMMUNITY_STRING group network-operator
```

### 1.2. Configure SNMP Host (NMS)

Specify the IP address of your Network Management Station (NMS), which will be querying the switch (e.g., your Prometheus server or Grafana host if it's directly querying).

```cli
snmp-server host 192.168.1.100 community YOUR_SNMP_COMMUNITY_STRING use-vrf default
```
Replace `192.168.1.100` with the actual IP address of your NMS.

### 1.3. (Optional) Configure SNMPv3 (Recommended for Production)

SNMPv3 provides authentication and encryption.

```cli
snmp-server user YOUR_SNMPV3_USER network-admin auth md5 YOUR_AUTH_PASSWORD priv des YOUR_PRIV_PASSWORD
snmp-server group network-admin v3 auth priv
```
Replace `YOUR_SNMPV3_USER`, `YOUR_AUTH_PASSWORD`, and `YOUR_PRIV_PASSWORD` with secure credentials.

### 1.4. Save Configuration

```cli
copy running-config startup-config
```

## 2. Integrate with Grafana (via Prometheus/SNMP Exporter)

To get SNMP data into Grafana, you typically use an SNMP Exporter (e.g., Prometheus SNMP Exporter) that scrapes the switch and exposes metrics for Prometheus. Grafana then queries Prometheus.

### 2.1. Deploy Prometheus SNMP Exporter

Refer to the Prometheus SNMP Exporter documentation for deployment. You will need to configure a `snmp.yml` file with your switch's IP and SNMP community/credentials.

Example `snmp.yml` snippet for SNMPv2c:

```yaml
# snmp.yml
modules:
  if_mib:
    walk: [ifMib]
    get: [sysDescr, sysUpTime]
  # Add other MIBs as needed
```

Example Prometheus `prometheus.yml` scrape configuration:

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'cisco_nexus_9236c_snmp'
    static_configs:
      - targets: ['192.168.1.1'] # IP address of your Cisco Nexus switch
    metrics_path: /snmp
    params:
      module: [if_mib] # Use the module defined in snmp.yml
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: YOUR_SNMP_EXPORTER_IP:9116 # Address of your SNMP Exporter
```
Replace `192.168.1.1` with your switch's IP and `YOUR_SNMP_EXPORTER_IP:9116` with the address of your SNMP Exporter.

### 2.2. Configure Grafana Dashboard

1.  **Add Prometheus Data Source:** In Grafana, add your Prometheus instance as a data source.
2.  **Import/Create Dashboard:**
    *   You can import pre-built SNMP dashboards from Grafana Labs (e.g., Node Exporter Full, if you're also monitoring the host running the exporter).
    *   Alternatively, create a custom dashboard using Prometheus queries based on the SNMP metrics exposed by the exporter (e.g., `ifInOctets`, `ifOutOctets` for interface traffic).

## 3. Verification

*   **Verify SNMP on Switch:**
    ```cli
    show snmp community
    show snmp host
    ```
*   **Verify SNMP Exporter Logs:** Check the logs of your SNMP Exporter for successful scrapes.
*   **Verify Prometheus Targets:** Check the Prometheus UI (`/targets` endpoint) to ensure your SNMP target is up and scraping.
*   **Verify Grafana Data:** Check your Grafana dashboard for incoming SNMP data from the switch.
