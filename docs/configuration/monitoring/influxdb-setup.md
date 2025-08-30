# InfluxDB and Grafana Integration Setup

This document provides instructions for installing InfluxDB on TrueNAS SCALE and connecting it as a data source to a Grafana instance.

## 1. Installing InfluxDB on TrueNAS SCALE

TrueNAS SCALE supports running Docker containers through its "Apps" feature. We will use this to install InfluxDB.

1.  **Navigate to "Apps" in TrueNAS:**
    Open your TrueNAS web interface and go to the "Apps" section.

2.  **Launch Docker Image:**
    Click on the "Launch Docker Image" button.

3.  **Configure the InfluxDB Application:**
    Fill in the application configuration as follows:

    *   **Application Name:** `influxdb`
    *   **Image Repository:** `influxdb`
    *   **Image Tag:** `latest` (or a specific version like `2.7`)

4.  **Container Entrypoint:**
    Leave this blank to use the default entrypoint of the InfluxDB image.

5.  **Container Environment Variables:**
    You can leave this empty for a basic setup. For a more secure setup, you should configure an organization, bucket, and token here.

6.  **Networking:**
    *   **Port Forwarding:** Add a port forward for the InfluxDB API.
        *   **Container Port:** `8086`
        *   **Node Port:** `8086` (or another available port on your TrueNAS host)

7.  **Storage:**
    To ensure your InfluxDB data persists across container restarts, you need to mount a dataset from your TrueNAS pool into the container.

    *   **Create a Dataset:** In TrueNAS, under "Storage", create a new dataset for your InfluxDB data (e.g., `your-pool/influxdb-data`).
    *   **Mount the Dataset:** In the app configuration, under "Storage", mount the dataset you created to the following path in the container: `/var/lib/influxdb2`

8.  **Review and Save:**
    Review your configuration and click "Save" to launch the InfluxDB container.

9.  **Initial InfluxDB Setup:**
    *   Once the container is running, access the InfluxDB UI at `http://<truenas-ip>:8086`.
    *   You will be prompted to create an initial user, password, organization, and bucket. **Save this information securely, as you will need it to configure Grafana.**

## 2. Connecting InfluxDB to Grafana

Now, let's add InfluxDB as a data source in Grafana.

1.  **Access Your Grafana Instance:**
    Open your Grafana UI in a web browser (e.g., `http://monitor-01.bjoin.studio:3000`).

2.  **Add a New Data Source:**
    *   Navigate to "Connections" > "Data Sources".
    *   Click "Add new data source".
    *   Select "InfluxDB" from the list.

3.  **Configure the InfluxDB Data Source:**

    *   **Name:** `InfluxDB_TrueNAS` (or another descriptive name).
    *   **Query Language:** Select `Flux`. This is critical for InfluxDB v2.x.
    *   **URL:** `http://10.20.51.81:8086` (the IP of your TrueNAS server and the port you forwarded).
    *   **Authentication:**
        *   **Organization:** The organization you created during the InfluxDB setup.
        *   **Token:** The token you generated during the InfluxDB setup.
        *   **Default Bucket:** The bucket you created during the InfluxDB setup.

    > **💡 Example Configuration:**
    > *   **Name:** `InfluxDB-TrueNAS-01`
    > *   **Organization:** `Bjoin Studio`
    > *   **Default Bucket:** `influxdb-bucket-truenas-01`

4.  **Save & Test:**
    Click "Save & Test". You should see a message indicating that the data source is working.

You can now create dashboards in Grafana using the data stored in InfluxDB.

## 3. Troubleshooting

### Issue: App is "Stopped" after installation

If the InfluxDB application installs but remains in the "Stopped" state, it is most likely a storage permission issue.

1.  In the TrueNAS UI, go to **System Settings** > **Shell**.
2.  Execute the following commands to grant the InfluxDB user (UID 568) access to the datasets you created. (Assuming your pool is `home-pool` and datasets are `influxdb_data` and `influxdb_config`).

    ```bash
    sudo chown -R 568:568 /mnt/home-pool/influxdb_data
    sudo chown -R 568:568 /mnt/home-pool/influxdb_config
    ```
3.  Go back to the **Apps** page and start the InfluxDB application.

### Issue: "unauthorized access error" in Grafana

When you click "Save & Test" in Grafana, you see the error `unauthorized: unauthorized access error reading buckets`.

This means Grafana can reach InfluxDB, but the authentication token is invalid or lacks permissions.

1.  **Generate a New Token:** Go to your InfluxDB UI (`http://10.20.51.81:8086`).
2.  Navigate to **Load Data** > **API Tokens**.
3.  Click **+ Generate API Token** and select **All Access API Token**.
4.  Give it a description (e.g., `grafana-token`) and save it.
5.  Copy the new token string.
6.  **Update Grafana:** Go back to the Grafana data source settings, paste the new token into the **Token** field, and click **Save & Test** again.
7.  **Verify Organization:** Ensure the **Organization** name in Grafana exactly matches the one in InfluxDB (it is case-sensitive).
