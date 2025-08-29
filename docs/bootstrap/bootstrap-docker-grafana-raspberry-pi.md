# Deploying Grafana with Docker on a Raspberry Pi

This runbook details the process for installing and configuring Grafana using Docker on a Raspberry Pi.

## Prerequisites

*   A Raspberry Pi with Docker installed.
*   Network connectivity to the Raspberry Pi.

## Installation Steps

1.  **Create a Docker Network:**
    Create a dedicated Docker network for the monitoring services to communicate with each other.

    ```bash
    docker network create monitoring
    ```

2.  **Create a Docker Volume:**
    Create a dedicated Docker volume to ensure Grafana's data (dashboards, data sources, etc.) persists across container restarts and updates.

    ```bash
    docker volume create grafana-storage
    ```

3.  **Start the Grafana Container:**
    Run the official Grafana Docker image on the `monitoring` network. This command starts the container in detached mode, maps the default Grafana port, configures it to restart automatically, and mounts the volume created in the previous step.

    ```bash
    docker run -d \
      --name=grafana \
      -p 3000:3000 \
      --restart=unless-stopped \
      -v grafana-storage:/var/lib/grafana \
      --network=monitoring \
      grafana/grafana
    ```

## Accessing Grafana

Once the container is running, you can access the Grafana web interface by navigating to the IP address of your Raspberry Pi on port 3000.

*   **URL:** `http://<your-raspberry-pi-ip>:3000`
    *   *Example:* `http://10.10.201.80:3000`

*   **Default Credentials:**
    *   **Username:** `admin`
    *   **Password:** `admin`

You will be required to change the default password upon your first login.
