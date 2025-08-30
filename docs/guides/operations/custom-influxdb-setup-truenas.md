# Custom InfluxDB Setup Guide for TrueNAS SCALE

This guide provides instructions for installing a fully-configurable InfluxDB instance on TrueNAS SCALE using the "Custom App" feature. 

## Overview

The standard InfluxDB application available in the TrueNAS marketplace is a simple Docker image launch that lacks the ability to configure advanced settings, such as adding extra network ports (like UDP for a Graphite listener) or setting necessary environment variables.

This custom installation method bypasses these limitations by providing a complete Kubernetes manifest, giving you full control over the application's configuration.

## Step 1: Create the Storage Dataset

Before installing the app, ensure you have a dedicated dataset on your TrueNAS server for InfluxDB to store its data.

1.  Navigate to **Storage** in the TrueNAS UI.
2.  Create a new dataset. For example, inside a pool named `home-pool`, you might create a dataset named `influxdb_data`.
3.  Take note of the full path to this dataset on the TrueNAS host. It will typically be `/mnt/YOUR_POOL_NAME/YOUR_DATASET_NAME` (e.g., `/mnt/home-pool/influxdb_data`).

## Step 2: Install the Custom Application

1.  Navigate to the **Apps** page in the TrueNAS UI.
2.  If you have a previous version of InfluxDB installed, **Delete** it now.
3.  Click the **"Launch Custom App"** button.
4.  Give the application a name (e.g., `influxdb-custom`).
5.  In the **"Application Definition"** text area, copy and paste the entire YAML code block below.

**⚠️ Important:** Before pasting, find the `path:` line near the end of the YAML and replace `/mnt/home-pool/influxdb_data` with the actual path to the dataset you created in Step 1.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: influxdb-custom-service
spec:
  selector:
    app: influxdb-custom
  ports:
    - name: http
      protocol: TCP
      port: 8086
      targetPort: 8086
    - name: graphite
      protocol: UDP
      port: 2003
      targetPort: 2003
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: influxdb-custom-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: influxdb-custom
  template:
    metadata:
      labels:
        app: influxdb-custom
    spec:
      securityContext:
        runAsUser: 568
        runAsGroup: 568
        fsGroup: 568
      containers:
        - name: influxdb
          image: influxdb:latest
          env:
            - name: INFLUXDB_GRAPHITE_ENABLED
              value: "true"
            - name: INFLUXDB_GRAPHITE_DATABASE
              value: "influxdb-bucket-truenas-01/_"
          ports:
            - containerPort: 8086
              protocol: TCP
            - containerPort: 2003
              protocol: UDP
          volumeMounts:
            - name: influxdb-data
              mountPath: /var/lib/influxdb2
      volumes:
        - name: influxdb-data
          hostPath:
            path: /mnt/home-pool/influxdb_data
            type: Directory
```

6.  Click **Save**. The application will now deploy with the correct settings.

## Step 3: Configure TrueNAS Reporting

With the custom InfluxDB running, you now need to tell TrueNAS to send its metrics to the Graphite listener we just configured.

1.  In the TrueNAS UI, go to **Reporting** and click the settings cog icon to get to the **Reporting Exporters**.
2.  Click **Add** to create a new exporter.
3.  Configure it as follows:
    *   **Name:** `InfluxDB-Graphite-Exporter`
    *   **Type:** `GRAPHITE`
    *   **Destination IP:** The IP address of your TrueNAS server.
    *   **Destination Port:** `2003`
    *   **Protocol:** `UDP`
    *   **Enable** the exporter.
4.  **Save** the new exporter.

## Step 4: Next Steps

After a few minutes, data should begin flowing from TrueNAS into your InfluxDB bucket. 

From here, the process of setting up the initial InfluxDB user/bucket and connecting Grafana is the same as before. You can follow the original guide for those steps:

*   **[InfluxDB and Grafana Integration Setup](../configuration/monitoring/influxdb-setup.md)**
