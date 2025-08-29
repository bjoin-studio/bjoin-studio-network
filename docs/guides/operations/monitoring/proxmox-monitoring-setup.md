# Monitoring Proxmox with Grafana and Prometheus

This runbook provides a step-by-step guide for setting up a monitoring solution for a Proxmox PVE host using Grafana and Prometheus.

## Overview

The monitoring setup consists of three main components:

1.  **Prometheus PVE Exporter:** A service that runs on the Proxmox host and exports metrics in a format that Prometheus can understand.
2.  **Prometheus:** A time-series database that scrapes and stores the metrics from the Proxmox PVE Exporter.
3.  **Grafana:** A visualization tool that connects to Prometheus as a data source to display the metrics in dashboards.

## Prerequisites

*   A Proxmox PVE host to be monitored.
*   A machine to run Grafana and Prometheus (in this case, a Raspberry Pi with Docker).
*   Network connectivity between the Proxmox host and the monitoring machine.

## Installation Steps

### Step 1: Install Prometheus PVE Exporter on Proxmox Host

These steps need to be performed on your Proxmox host (`pmx-01.bjoin.studio`) by connecting to it via SSH.

**1. Create a dedicated Proxmox VE user**

Create a read-only user for the exporter for security. You will be prompted to set a password for the new user.

```bash
pveum user add pve-exporter@pve --password-fd 0
pveum acl modify / -user pve-exporter@pve -role PVEAuditor
```

**2. Create a Linux user**

Create a dedicated system user to run the exporter as a daemon:

```bash
useradd -s /bin/false pve-exporter
```

**3. Create a virtual environment and install the exporter**

Create a Python virtual environment and install the `prometheus-pve-exporter` package using `pip`:

```bash
apt update
apt install -y python3-venv
python3 -m venv /opt/prometheus-pve-exporter
source /opt/prometheus-pve-exporter/bin/activate
pip install prometheus-pve-exporter
deactivate
```

**4. Configure the exporter**

Create a configuration file for the exporter at `/etc/prometheus/pve.yml`. Replace `<password>` with the password you set in Step 1.

```yaml
default:
  user: pve-exporter@pve
  password: <password>
  verify_ssl: false
```

Set the correct permissions for the configuration file:

```bash
chown -v root:pve-exporter /etc/prometheus/pve.yml
chmod -v 640 /etc/prometheus/pve.yml
```

**5. Create a systemd service**

Create a systemd service file at `/etc/systemd/system/prometheus-pve-exporter.service` to run the exporter automatically:

```ini
[Unit]
Description=Prometheus PVE Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=pve-exporter
Group=pve-exporter
Type=simple
ExecStart=/opt/prometheus-pve-exporter/bin/pve_exporter /etc/prometheus/pve.yml
Restart=always

[Install]
WantedBy=multi-user.target
```

Reload the systemd daemon, then enable and start the service:

```bash
systemctl daemon-reload
systemctl enable prometheus-pve-exporter
systemctl start prometheus-pve-exporter
```

After completing these steps, the Prometheus PVE exporter should be installed and running on your Proxmox host.

### Step 2: Install and Configure Prometheus on the Raspberry Pi

These steps are performed on the Raspberry Pi.

**1. Create a Docker Network**

```bash
docker network create monitoring
```

**2. Create a directory for the Prometheus configuration**

```bash
mkdir -p 6-configuration/prometheus
```

**3. Create the `prometheus.yml` file**

Create a file named `6-configuration/prometheus/prometheus.yml` with the following content. This is a minimal configuration that scrapes Prometheus itself. The Proxmox host will be added later.

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  # Add the Proxmox VE scrape configuration here later
  # - job_name: 'pve'
  #   static_configs:
  #     - targets: ['<proxmox-host-ip>:9221']
```

**4. Create a Docker volume**

```bash
docker volume create prometheus-data
```

**5. Run the Prometheus container**

This command will run the Prometheus container on the `monitoring` network, mounting the configuration file and the data volume.

```bash
docker run -d -p 9090:9090 --name=prometheus --restart=unless-stopped -v $(pwd)/6-configuration/prometheus/prometheus.yml:/etc/prometheus/prometheus.yml -v prometheus-data:/prometheus --network=monitoring prom/prometheus
```

### Step 3: Configure Grafana Data Source and Dashboard

These steps are performed in the Grafana web interface.

**1. Add the Prometheus Data Source**

1.  Open Grafana by navigating to `http://<your-raspberry-pi-ip>:3000`.
2.  Log in with your credentials.
3.  On the left-hand menu, go to **Connections** > **Data Sources**.
4.  Click the **Add new connection** button.
5.  Select **Prometheus** from the list.
6.  In the **URL** field, enter `http://prometheus:9090`.
7.  Click the **Save & test** button.

**2. Import the Grafana Dashboard**

1.  On the left-hand menu, go to **Dashboards**.
2.  Click the **New** button and select **Import**.
3.  In the **Import via grafana.com** field, enter the dashboard ID: `10347`.
4.  Click the **Load** button.
5.  On the next screen, you may be prompted to select a Prometheus data source. Choose the one you just added.
6.  Click the **Import** button.
