# Network Monitoring Setup Guide

This guide provides a comprehensive walkthrough for setting up a modern, open-source monitoring stack for your network using Prometheus, Grafana, and Docker.

## 1. Architecture Overview

We will deploy a monitoring stack on a dedicated virtual machine. This is a best practice that isolates monitoring services from the infrastructure they are monitoring.

- **Components:**
    - **Prometheus:** The core time-series database that collects and stores metrics.
    - **Grafana:** The visualization layer for creating dashboards.
    - **Node Exporter:** An agent to expose system-level metrics from your Linux VMs (Proxmox, FreeIPA, etc.).
    - **SNMP Exporter:** A tool to query your network switches (Cisco, Sodola, Netgear) via the SNMP protocol.
- **Deployment Method:** We will use Docker and Docker Compose to containerize these services for easy management, updates, and deployment.

## 2. Step 1: Create the Monitoring VM in Proxmox

In the Proxmox web interface (`https://10.20.51.20:8006`), create a new VM with the following specifications.

### 2.1. VM Specifications

- **Hostname:** `mon-01.bjoin.studio`
- **OS:** Ubuntu Server 22.04 LTS
- **Network:** Management VLAN (VLAN 51)
- **Static IP:** `10.20.51.30/24`
- **Gateway:** `10.20.51.1`
- **DNS Server:** `10.20.51.10` (your FreeIPA server)
- **CPU:** 2 Cores
- **Memory:** 4096 MB (4 GB)
- **Disk:** 50 GB

### 2.2. Proxmox VM Creation Steps

1.  Click **"Create VM"**.
2.  **General:**
    -   **Node:** `pmx-01`
    -   **Name:** `mon-01.bjoin.studio`
3.  **OS:**
    -   Select your uploaded **Ubuntu Server 22.04 LTS ISO**.
    -   **Guest OS:** `Linux`, Version `6.x or kernel`.
4.  **System:**
    -   Check **`QEMU Guest Agent`**.
5.  **Disks:**
    -   **Bus/Device:** `SCSI`
    -   **Disk size:** `50`
6.  **CPU:**
    -   **Cores:** `2`
7.  **Memory:**
    -   **Memory (MB):** `4096`
8.  **Network:**
    -   **Bridge:** `vmbr51` (The bridge for the Management VLAN)
    -   **Model:** `VirtIO (paravirtualized)`
9.  **Confirm** and click **Finish**.

### 2.3. OS Installation (Ubuntu Server)

1.  Start the VM and open the console.
2.  Follow the Ubuntu Server installation prompts.
3.  During the network configuration step, select **"Edit IPv4"** and set it to **"Manual"**.
4.  Enter the static IP configuration defined above.
5.  Complete the installation and reboot.

## 3. Step 2: Install Docker and Docker Compose

SSH into your new `mon-01.bjoin.studio` VM and run the following commands to install Docker.

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

## 4. Step 3: Prepare and Launch the Monitoring Stack

After logging back in, create a directory structure and the configuration files for your monitoring stack.

```bash
mkdir ~/monitoring && cd ~/monitoring
mkdir -p prometheus/rules
mkdir -p grafana/data
mkdir snmp_exporter
```

### 4.1. `docker-compose.yml`

Create this file with `nano docker-compose.yml` and paste the following:

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

### 4.2. `prometheus/prometheus.yml`

Create this file with `nano prometheus/prometheus.yml`. This is a starting point; you will add your devices here.

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
    # Note: You must install the os-node-exporter plugin on OPNsense for this to work
    static_configs:
      - targets: ['10.20.51.1:9100']

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

### 4.3. `snmp_exporter/snmp.yml`

Create this file with `nano snmp_exporter/snmp.yml`.

```yaml
if_mib:
  walk: [ifDescr, ifType, ifMtu, ifSpeed, ifPhysAddress, ifAdminStatus, ifOperStatus, ifLastChange, ifInOctets, ifInUcastPkts, ifInNUcastPkts, ifInDiscards, ifInErrors, ifInUnknownProtos, ifOutOctets, ifOutUcastPkts, ifOutNUcastPkts, ifOutDiscards, ifOutErrors, ifOutQLen, ifSpecific]
```

### 4.4. Launch the Stack

From the `~/monitoring` directory, run:

```bash
docker compose up -d
```

## 5. Step 4: Configure Grafana

1.  Open your web browser and navigate to `http://mon-01.bjoin.studio:3000`
2.  Log in with default credentials: `admin` / `admin` (change the password when prompted).
3.  Go to **Connections > Data sources** and click **Add new data source**.
4.  Select **Prometheus**.
5.  For the **Prometheus server URL**, enter: `http://prometheus:9090`
6.  Click **Save & Test**.

## 6. Next Steps

Your monitoring stack is now running!

- **Add Targets:** Edit `prometheus/prometheus.yml` to add the IPs of your other servers and switches.
- **Install Exporters:** On other Linux hosts (like `ipa-01`), you need to install `node_exporter`.
- **Find Dashboards:** Explore the official [Grafana Dashboards](https://grafana.com/grafana/dashboards/) website to import pre-built dashboards for OPNsense, Node Exporter, and more.
