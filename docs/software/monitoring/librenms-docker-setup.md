# LibreNMS Docker Setup Guide

This document outlines the steps to get LibreNMS running using Docker Compose, incorporating best practices and solutions to common setup issues.

## 1. Files Created

Two files have been created in the `/home/bjoin-studio/workspace/GitHub/bjoin-studio-network/docker/librenms/` directory:

*   `docker-compose.yml`: Defines the LibreNMS services (web, database, memcached, redis, snmpd, cron).
*   `.env`: Contains environment variables for database credentials and application key. **You MUST edit this file to set strong, unique passwords.**

## 2. Important: Configure `.env` and Generate APP_KEY

Before starting LibreNMS, you **must** edit the `.env` file and replace `your_db_password_here` and `your_db_root_password_here` with strong, unique passwords.

Additionally, the `APP_KEY` needs to be a valid, randomly generated key. The placeholder `APP_KEY=SomeRandomStringGeneratedByLibreNMS` is not sufficient and will cause errors.

1.  **Edit `.env`:**
    ```bash
    nano /home/bjoin-studio/workspace/GitHub/bjoin-studio-network/docker/librenms/.env
    ```
    Set your `DB_PASSWORD` and `DB_ROOT_PASSWORD`.

2.  **Generate APP_KEY:**
    Start only the `librenms` service temporarily to generate the key:
    ```bash
    cd /home/bjoin-studio/workspace/GitHub/bjoin-studio-network/docker/librenms
    docker compose up -d librenms
    ```
    Once the `librenms` container is running, execute the following command to generate a valid `APP_KEY`:
    ```bash
    docker exec librenms php artisan key:generate --show
    ```
    Copy the output (e.g., `base64:YOUR_GENERATED_KEY_HERE=`).

3.  **Update `.env` with generated APP_KEY:**
    Edit the `.env` file again and replace the placeholder `APP_KEY=SomeRandomStringGeneratedByLibreNMS` with the key you just generated.

## 3. Ensure Correct Database Collation

LibreNMS requires the MariaDB database to use `utf8` character set and `utf8_unicode_ci` collation. If the database was created with a different collation (e.g., `utf8mb4_general_ci`), it will cause errors.

1.  **Stop all LibreNMS containers:**
    ```bash
    cd /home/bjoin-studio/workspace/GitHub/bjoin-studio-network/docker/librenms
    docker compose down
    ```

2.  **Start only the database service:**
    ```bash
    docker compose up -d db
    ```

3.  **Drop and recreate the `librenms` database with correct collation:**
    Replace `YOUR_DB_ROOT_PASSWORD` with your `DB_ROOT_PASSWORD` from the `.env` file.
    ```bash
    docker exec librenms_db mysql -u root -p'YOUR_DB_ROOT_PASSWORD' -e "DROP DATABASE IF EXISTS librenms; CREATE DATABASE librenms CHARACTER SET utf8 COLLATE utf8_unicode_ci;"
    ```

## 4. Start All LibreNMS Services

Now that the `.env` is configured and the database collation is correct, start all LibreNMS services:

```bash
cd /home/bjoin-studio/workspace/GitHub/bjoin-studio-network/docker/librenms
docker compose up -d
```

This command will:
*   Download the necessary Docker images (if not already downloaded).
*   Create and start the containers in detached mode (in the background).
*   LibreNMS will automatically perform database migrations and seeding on its first run with an empty database.

## 5. Access LibreNMS Web Interface

Once the containers are running (this might take a few minutes for the first boot), you can access the LibreNMS web interface in your browser:

```
http://localhost:8000
```

(If you changed the port in `docker-compose.yml`, use your chosen port instead of `8000`.)

## 6. Create Admin User

Instead of using the web interface for initial user creation, it's more reliable to create an admin user via the command line.

1.  **Execute the user add command:**
    Replace `YOUR_ADMIN_PASSWORD` with your desired password for the admin user.
    ```bash
    docker exec -u librenms librenms php /opt/librenms/artisan user:add admin --password='YOUR_ADMIN_PASSWORD' --role=admin
    ```

2.  **Log in:**
    You can now log in to the LibreNMS web interface using the username `admin` and the password you set.

## 7. Next Steps

After the initial setup and admin user creation, you can begin adding devices to LibreNMS for monitoring.
