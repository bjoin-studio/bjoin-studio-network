# Network Monitoring Setup Guide

This guide provides a comprehensive walkthrough for setting up a modern, open-source monitoring stack for your network using Prometheus, Grafana, and Docker.

## 1. Architecture Overview

We will deploy a monitoring stack on a dedicated virtual machine. The components are:

- **Prometheus:** The core time-series database that collects and stores metrics.
- **Grafana:** The visualization layer for creating dashboards.
- **Node Exporter:** An agent to expose system-level metrics from your Linux VMs (Proxmox, FreeIPA, etc.).
- **SNMP Exporter:** A tool to query your network switches (Cisco, Sodola, Netgear) via the SNMP protocol and translate the data for Prometheus.
- **Docker & Docker Compose:** To containerize these services for easy management and deployment.

## 2. Step 1: Create the Monitoring VM

In the Proxmox web UI, create a new VM with the following specifications.

- **Name:** `mon-01.bjoin.studio`
- **OS:** Ubuntu Server 22.04 LTS (or Debian 12).
- **Disk size:** At least `40 GB`.
- **CPU:** `2` cores.
- **Memory:** `4096 MB` (4 GB).
- **Network:** Assign it to the **Management VLAN (51)** with a static IP address, for example:
    - **IP Address:** `10.20.51.30/24`
    - **Gateway:** `10.20.51.1`
    - **DNS Server:** `10.20.51.10` (your FreeIPA server)

## 3. Step 2: Install Docker and Docker Compose

SSH into your new `mon-01` VM and run the following commands to install Docker.

```bash
# Update package lists
sudo apt-get update

# Install prerequisites
sudo apt-get install -y ca-certificates curl gnupg

# Add Docker's official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Set up the Docker repository
echo \
  "deb [arch=\"$(dpkg --print-architecture)\" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  \"$(. /etc/os-release && echo \"$VERSION_CODENAME\")\" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Add your user to the docker group to run docker without sudo
sudo usermod -aG docker $USER

# Log out and log back in for the group change to take effect
exit
```

After logging back in, you can proceed.

## 4. Step 3: Prepare the Monitoring Stack Configuration

We will create a directory to hold all of our configuration files.

```bash
# Create a directory for your monitoring stack
mkdir ~/monitoring
cd ~/monitoring

# Create a directory for Prometheus configuration
mkdir -p prometheus/rules

# Create a directory for Grafana data
mkdir -p grafana/data

# Create a directory for SNMP Exporter configuration
mkdir snmp_exporter
```

Now, create the following three configuration files inside the `~/monitoring` directory.

### 1. `docker-compose.yml`

Create a file named `docker-compose.yml`:
```bash
nano docker-compose.yml
```
Paste the following content:
```yaml
version: '3.8'

services:
  prometheus:
    image: prom/prometheus:latest
    container_name: prometheus
    restart: unless-stopped
    volumes:
      - ./prometheus:/etc/prometheus/
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
    ports:
      - "9090:9090"

  grafana:
    image: grafana/grafana-oss:latest
    container_name: grafana
    restart: unless-stopped
    volumes:
      - ./grafana/data:/var/lib/grafana
    ports:
      - "3000:3000"

  node_exporter:
    image: prom/node-exporter:latest
    container_name: node_exporter
    restart: unless-stopped
    pid: host
    volumes:
      - /:/host:ro,rslave
    command:
      - '--path.rootfs=/host'

  snmp_exporter:
    image: prom/snmp-exporter:latest
    container_name: snmp_exporter
    restart: unless-stopped
    volumes:
      - ./snmp_exporter:/etc/snmp_exporter
    ports:
      - "9116:9116"
```

### 2. `prometheus/prometheus.yml`

Create a file named `prometheus.yml` inside the `prometheus` directory:
```bash
nano prometheus/prometheus.yml
```
Paste the following content. This is a starting point; you will add your devices here.
```yaml
global:
  scrape_interval: 30s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node'
    static_configs:
      - targets: ['node_exporter:9100'] # The monitoring VM itself
      # Add other Linux/Proxmox/TrueNAS hosts here
      # - targets: ['10.20.51.10:9100'] # ipa-01
      # - targets: ['10.20.51.20:9100'] # pmx-01

  - job_name: 'opnsense'
    static_configs:
      - targets: ['10.20.51.1:9100'] # OPNsense firewall

  - job_name: 'snmp'
    static_configs:
      - targets:
        # Add your switch IPs here
        # - 10.20.51.2  # Example: Sodola Switch
        # - 10.20.51.5  # Example: Netgear Switch
    metrics_path: /snmp
    params:
      module: [if_mib]
    relabel_configs:
      - source_labels: [__address__]
        target_label: __param_target
      - source_labels: [__param_target]
        target_label: instance
      - target_label: __address__
        replacement: snmp_exporter:9116
```

### 3. `snmp_exporter/snmp.yml`

Create a file named `snmp.yml` inside the `snmp_exporter` directory:
```bash
nano snmp_exporter/snmp.yml
```
Paste the following content. This is a generic configuration that works for most switches.
```yaml
if_mib:
  walk: [ifDescr, ifType, ifMtu, ifSpeed, ifPhysAddress, ifAdminStatus, ifOperStatus, ifLastChange, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInDiscards, ifInErrors, ifInUnknownProtos, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutDiscards, ifOutErrors, ifOutQLen, ifSpecific]
  lookups:
    - old_names: [ifAdminStatus, ifOperStatus]
      new_name: ifStatus
      enum_map:
        1: "up"
        2: "down"
        3: "testing"
```

## 5. Step 4: Launch the Monitoring Stack

Now that all the configuration files are in place, you can start all the services.

From the `~/monitoring` directory, run:
```bash
docker compose up -d
```
This will download the container images and start them in the background.

## 6. Step 5: Configure Grafana

1.  Open your web browser and navigate to your monitoring server's IP at port 3000: `http://10.20.51.30:3000`
2.  Log in with the default credentials: `admin` / `admin`. You will be prompted to change the password.
3.  From the main menu, go to **Connections > Data sources**.
4.  Click **Add new data source**.
5.  Select **Prometheus**.
6.  For the **Prometheus server URL**, enter: `http://prometheus:9090`
7.  Click **Save & Test**. You should see a message saying "Data source is working".

## 7. Next Steps

Your monitoring stack is now running!

- **Add Targets:** Edit the `prometheus/prometheus.yml` file to add the IP addresses of your other servers and switches.
- **Install Exporters:** For other Linux hosts (like `ipa-01` and `pmx-01`), you will need to install the `node_exporter` service on them.
- **Find Dashboards:** Explore the official [Grafana Dashboards](https://grafana.com/grafana/dashboards/) website. You can find pre-built dashboards for thousands of applications and devices (e.g., search for "OPNsense" or "Node Exporter Full") and import them into your Grafana instance.