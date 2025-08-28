# Setting up HTTPS (TLS) for Docker on Raspberry Pi

This guide provides step-by-step instructions to configure your Docker daemon on a Raspberry Pi to use HTTPS (TLS) for secure remote connections. This involves generating SSL certificates and configuring both the Docker daemon and your Docker client.

## Prerequisites

*   Docker must be installed and running on your Raspberry Pi.
*   You need `sudo` privileges on your Raspberry Pi.
*   Ensure your Raspberry Pi has a static IP address or a reliable hostname that you will use to connect to it.

## Step 1: Generate TLS Certificates

You will generate a Certificate Authority (CA) certificate, a server certificate for the Docker daemon, and a client certificate for your Docker client. Perform these steps on your **Raspberry Pi**.

1.  **Create a directory for certificates:**

    ```bash
    mkdir -p ~/docker-certs
    cd ~/docker-certs
    ```

2.  **Generate CA private key and certificate:**
    This CA will sign both your server and client certificates. Remember the passphrase you set for `ca-key.pem`.

    ```bash
    openssl genrsa -aes256 -out ca-key.pem 4096
    openssl req -new -x509 -days 365 -key ca-key.pem -sha256 -out ca.pem
    ```

3.  **Generate Server Key and Certificate Signing Request (CSR):**
    The server certificate will be used by the Docker daemon on your Raspberry Pi. **Replace `<Raspberry_Pi_IP_or_Hostname>` with the actual IP address or hostname of your Raspberry Pi that you will use to connect to it.** This is crucial for TLS verification.

    ```bash
    openssl genrsa -out server-key.pem 4096
    openssl req -subj "/CN=<Raspberry_Pi_IP_or_Hostname>" -new -key server-key.pem -out server.csr
    ```

4.  **Create an Extfile for Server Certificate (to allow IP/hostname in SAN):**
    Create a file named `extfile.cnf` with the following content. **Replace `<Raspberry_Pi_IP_or_Hostname>` with your actual IP/hostname.** If you have multiple, list them separated by commas (e.g., `IP:192.168.1.100,DNS:raspberrypi.local`).

    ```ini
    extendedKeyUsage = serverAuth
    subjectAltName = IP:<Raspberry_Pi_IP_or_Hostname>,DNS:<Raspberry_Pi_IP_or_Hostname>
    ```

5.  **Sign the Server Certificate with your CA:**
    You will be prompted for the CA key passphrase.

    ```bash
    openssl x509 -req -days 365 -in server.csr -CA ca.pem -CAkey ca-key.pem \
      -CAcreateserial -out server-cert.pem -extfile extfile.cnf
    ```

6.  **Generate Client Key and Certificate Signing Request (CSR):**
    This certificate will be used by your client machine to connect to the Docker daemon.

    ```bash
    openssl genrsa -out client-key.pem 4096
    openssl req -subj "/CN=client" -new -key client-key.pem -out client.csr
    ```

7.  **Create an Extfile for Client Certificate:**
    Create a file named `extfile-client.cnf` with the following content:

    ```ini
    extendedKeyUsage = clientAuth
    ```

8.  **Sign the Client Certificate with your CA:**
    You will be prompted for the CA key passphrase.

    ```bash
    openssl x509 -req -days 365 -in client.csr -CA ca.pem -CAkey ca-key.pem \
      -CAcreateserial -out client-cert.pem -extfile extfile-client.cnf
    ```

9.  **Clean up CSR files and set permissions:**
    You can remove the `.csr` and `.cnf` files as they are no longer needed. It's crucial to set correct permissions for your private keys.

    ```bash
    rm *.csr *.cnf
    chmod -v 0400 ca-key.pem client-key.pem server-key.pem
    chmod -v 0444 ca.pem client-cert.pem server-cert.pem
    ```

    At this point, you should have the following files in `~/docker-certs` on your Raspberry Pi:
    *   `ca.pem`: CA public certificate
    *   `ca-key.pem`: CA private key
    *   `server-cert.pem`: Docker daemon server public certificate
    *   `server-key.pem`: Docker daemon server private key
    *   `client-cert.pem`: Docker client public certificate
    *   `client-key.pem`: Docker client private key

## Step 2: Configure the Docker Daemon on Raspberry Pi

Now that you have the certificates, you need to configure the Docker daemon to use them and listen for remote connections over TLS. Perform these steps on your **Raspberry Pi**.

1.  **Move the server certificates to a secure location:**
    It's recommended to store the server certificates in a dedicated directory, for example, `/etc/docker/certs.d/`.

    ```bash
    sudo mkdir -p /etc/docker/certs.d
    sudo cp ~/docker-certs/server-cert.pem /etc/docker/certs.d/server-cert.pem
    sudo cp ~/docker-certs/server-key.pem /etc/docker/certs.d/server-key.pem
    sudo cp ~/docker-certs/ca.pem /etc/docker/certs.d/ca.pem
    ```

2.  **Configure `daemon.json`:**
    You need to edit the Docker daemon configuration file, typically located at `/etc/docker/daemon.json`. If it doesn't exist, create it.

    ```bash
    sudo nano /etc/docker/daemon.json
    ```

    Add or modify the file with the following content. **Replace `<Raspberry_Pi_IP_or_Hostname>` with the actual IP address or hostname you used when generating the server certificate.** The standard TLS port for Docker is `2376`.

    ```json
    {
      "hosts": ["tcp://0.0.0.0:2376", "unix:///var/run/docker.sock"],
      "tls": true,
      "tlscacert": "/etc/docker/certs.d/ca.pem",
      "tlscert": "/etc/docker/certs.d/server-cert.pem",
      "tlskey": "/etc/docker/certs.d/server-key.pem",
      "tlsverify": true
    }
    ```

    Save and exit the editor (Ctrl+X, Y, Enter for nano).

3.  **Restart the Docker daemon:**
    For the changes to take effect, you must restart the Docker service.

    ```bash
    sudo systemctl daemon-reload
    sudo systemctl restart docker
    ```

4.  **Verify Docker daemon status:**
    Check if the Docker daemon is running correctly.

    ```bash
    sudo systemctl status docker
    ```
    Look for messages indicating it's listening on port 2376 and using TLS.

## Step 3: Configure the Docker Client

Now you need to configure your client machine (e.g., your laptop or another computer) to connect securely to the Docker daemon on your Raspberry Pi.

1.  **Copy Client Certificates to Your Client Machine:**
    You need to transfer the `ca.pem`, `client-cert.pem`, and `client-key.pem` files from your Raspberry Pi to your client machine. You can use `scp` or any other secure file transfer method.

    On your **client machine**, create a directory for the certificates, for example, `~/.docker/certs/raspberrypi/`:

    ```bash
    mkdir -p ~/.docker/certs/raspberrypi/
    ```

    On your **Raspberry Pi**, copy the files to your client machine (replace `your_username` and `your_client_ip` with your actual details):

    ```bash
    scp ~/docker-certs/ca.pem ~/docker-certs/client-cert.pem ~/docker-certs/client-key.pem your_username@your_client_ip:~/.docker/certs/raspberrypi/
    ```
    Alternatively, if you are already on your client machine and have SSH access to the Raspberry Pi:

    ```bash
    scp pi@<Raspberry_Pi_IP_or_Hostname>:~/docker-certs/ca.pem ~/.docker/certs/raspberrypi/
    scp pi@<Raspberry_Pi_IP_or_Hostname>:~/docker-certs/client-cert.pem ~/.docker/certs/raspberrypi/
    scp pi@<Raspberry_Pi_IP_or_Hostname>:~/docker-certs/client-key.pem ~/.docker/certs/raspberrypi/
    ```

2.  **Set Environment Variables for Docker Client:**
    On your **client machine**, you can set environment variables to tell the Docker client how to connect to the remote daemon.

    ```bash
    export DOCKER_HOST=tcp://<Raspberry_Pi_IP_or_Hostname>:2376
    export DOCKER_TLS_VERIFY=1
    export DOCKER_CERT_PATH=~/.docker/certs/raspberrypi/
    ```
    *   Replace `<Raspberry_Pi_IP_or_Hostname>` with the IP address or hostname of your Raspberry Pi.
    *   To make these settings permanent, you can add them to your shell's configuration file (e.g., `~/.bashrc`, `~/.zshrc`, or `~/.profile`) and then `source` the file (e.g., `source ~/.bashrc`).

3.  **Test the Connection:**
    Now, try running a Docker command from your client machine.

    ```bash
    docker ps
    ```
    If everything is configured correctly, you should see the running containers on your Raspberry Pi. If you encounter issues, ensure firewall rules on your Raspberry Pi allow incoming connections on port 2376.

## Security Considerations:

*   **Firewall:** Ensure that port `2376` is open on your Raspberry Pi's firewall (e.g., `ufw allow 2376/tcp`).
*   **Certificate Security:** Keep your `ca-key.pem` and `client-key.pem` files secure, as they can be used to generate new certificates or impersonate clients.
*   **IP/Hostname:** The `Common Name` or `Subject Alternative Name` in your server certificate *must* match the IP address or hostname you use to connect from your client. If it doesn't, you will get certificate validation errors.
*   **Alternative Connection Methods:** For even greater security, consider using an SSH tunnel or VPN instead of directly exposing the Docker daemon over the internet, especially if your Raspberry Pi is publicly accessible. Docker also supports connecting via SSH directly (`DOCKER_HOST=ssh://user@host`), which can be simpler if you already have SSH set up and don't need a full TLS setup.
