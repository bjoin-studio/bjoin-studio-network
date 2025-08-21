import os
import subprocess
import logging
import json
import datetime
import re
import time

__version__ = "v2026.08.20.01"

# --- Configuration --- #
PROGRAM_NAME = "WORKSTATION_CONFIGURATION"

# --- Setup Logging --- #
LOG_DIR = "/var/log/workstation_config"
os.makedirs(LOG_DIR, exist_ok=True)

log_filename = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M_%S") + "-SETUP_FREEIPA_SERVER.log"
LOG_FILE = os.path.join(LOG_DIR, log_filename)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# --- Helper Functions --- #
def run_command(command, check=True, capture_output=True, log_output=True):
    cmd_str = ' '.join(command)
    if log_output:
        logger.info(f"Executing: {cmd_str}")
    try:
        result = subprocess.run(command, check=check, capture_output=capture_output, text=True)
        if log_output:
            if result.stdout:
                logger.info(f"Stdout:\n{result.stdout.strip()}")
            if result.stderr:
                logger.error(f"Stderr:\n{result.stderr.strip()}")
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {cmd_str}")
        logger.error(f"Return Code: {e.returncode}")
        logger.error(f"Stdout:\n{e.stdout.strip()}")
        logger.error(f"Stderr:\n{e.stderr.strip()}")
        raise
    except FileNotFoundError:
        logger.error(f"Command not found: {command[0]}")
        raise

def generate_banner(text, char='=', length=79):
    padding = (length - len(text) - 4) // 2
    return f"# {char * padding} {text} {char * padding} #"

def print_separator(char='-', length=79):
    logger.info(char * length)

def is_hostname_resolvable(hostname):
    try:
        # Try to resolve the hostname using dig. If it resolves, it's in use.
        # We redirect stderr to /dev/null to suppress dig's error messages for non-existent domains.
        result = subprocess.run(["dig", "+short", hostname], capture_output=True, text=True, check=False)
        if result.returncode == 0 and result.stdout.strip():
            logger.info(f"Hostname {hostname} resolves to {result.stdout.strip()}. It is in use.")
            return True
        else:
            logger.info(f"Hostname {hostname} does not resolve. It is available.")
            return False
    except FileNotFoundError:
        logger.error("'dig' command not found. Cannot check hostname resolvability. Please install bind-utils or dnsutils.")
        exit(1)
    except Exception as e:
        logger.error(f"Error checking hostname resolvability for {hostname}: {e}")
        exit(1)

def set_system_hostname(new_hostname_long):
    logger.info(f"Attempting to set system hostname to {new_hostname_long}...")
    try:
        run_command(["hostnamectl", "set-hostname", new_hostname_long])
        logger.info(f"System hostname successfully set to {new_hostname_long}.")
        # Give systemd-resolved a moment to catch up if it's in use
        time.sleep(2)
    except subprocess.CalledProcessError:
        logger.error(f"Failed to set system hostname to {new_hostname_long}. Please check permissions or try manually.")
        exit(1)

# --- Main Script Logic --- #
def get_network_info():
    logger.info("Gathering network information...")
    
    # Get IP address
    ip_address = run_command(["hostname", "-I"], capture_output=True).stdout.split()[0]
    logger.info(f"IP Address: {ip_address}")

    # Get domain from /etc/resolv.conf
    domain = ""
    try:
        with open("/etc/resolv.conf", "r") as f:
            for line in f:
                if line.strip().startswith("search"):
                    domain = line.strip().split(None, 1)[1].split()[0]
                    break
        if not domain:
            logger.warning("'search' domain not found in /etc/resolv.conf. Attempting to derive from current hostname.")
            # Get current hostname to derive domain if resolv.conf fails
            current_hostname_output = run_command(["hostnamectl"], capture_output=True).stdout
            current_hostname_long = ""
            for line in current_hostname_output.splitlines():
                if "Static hostname" in line:
                    current_hostname_long = line.split(":")[-1].strip()
                    break
            if '.' in current_hostname_long:
                domain = '.'.join(current_hostname_long.split('.')[1:])
                logger.info(f"Derived domain from current hostname: {domain}")
            else:
                logger.error("Could not determine domain from /etc/resolv.conf or current hostname. Please configure manually.")
                exit(1)
    except FileNotFoundError:
        logger.error("/etc/resolv.conf not found. Cannot determine domain automatically.")
        exit(1)
    logger.info(f"Determined Domain: {domain}")

    # Determine FreeIPA server hostname (ipa-01, ipa-02, etc.)
    base_hostname = "ipa-"
    hostname_counter = 1
    new_hostname_short = ""
    new_hostname_long = ""

    while True:
        proposed_hostname_short = f"{base_hostname}{hostname_counter:02d}"
        proposed_hostname_long = f"{proposed_hostname_short}.{domain}"
        
        logger.info(f"Checking availability of {proposed_hostname_long}...")
        if not is_hostname_resolvable(proposed_hostname_long):
            new_hostname_short = proposed_hostname_short
            new_hostname_long = proposed_hostname_long
            logger.info(f"Selected available hostname: {new_hostname_long}")
            break
        else:
            hostname_counter += 1
            if hostname_counter > 99: # Prevent infinite loop for very large numbers
                logger.error("Exceeded ipa-99.domain.name. Cannot find an available hostname.")
                exit(1)
    
    # Set the system's hostname to the newly determined FreeIPA server hostname
    set_system_hostname(new_hostname_long)

    # Verify the hostname change (optional, but good for robustness)
    current_hostname_output = run_command(["hostnamectl"], capture_output=True).stdout
    verified_hostname_short = ""
    verified_hostname_long = ""
    for line in current_hostname_output.splitlines():
        if "Static hostname" in line:
            verified_hostname_long = line.split(":")[-1].strip()
            verified_hostname_short = verified_hostname_long.split('.')[0]
            break
    
    if verified_hostname_long != new_hostname_long:
        logger.error(f"Hostname verification failed. Expected {new_hostname_long}, but found {verified_hostname_long}.")
        exit(1)
    
    logger.info(f"Final system hostname: {verified_hostname_long}")

    return verified_hostname_short, verified_hostname_long, ip_address, domain

def load_network_preferences(config_path):
    logger.info(f"Loading network preferences from {config_path}...")
    try:
        with open(config_path, 'r') as f:
            prefs = json.load(f)
        logger.info("Network preferences loaded successfully.")
        return prefs
    except FileNotFoundError:
        logger.error(f"Network preferences file not found: {config_path}")
        exit(1)
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from {config_path}. Check file format.")
        exit(1)

def confirm_network_prefs_modified():
    confirm = input("Have you modified the network preferences file? (yes/no): ").lower()
    if confirm != "yes":
        logger.error("Please modify the network preferences file before running this script.")
        exit(1)

def check_prerequisites():
    logger.info("Checking prerequisites...")
    try:
        run_command(["command", "-v", "jq"], check=True, capture_output=False, log_output=False)
        logger.info("jq is installed.")
    except subprocess.CalledProcessError:
        logger.warning("jq is not installed. It's recommended for better JSON processing.")
        logger.warning("You can install it with: sudo dnf install -y jq (or equivalent for your OS)")
    logger.info("Prerequisites check completed.")

def update_system():
    logger.info(generate_banner("WORKSTATION PREPARATION STARTED"))
    print_separator()

    logger.info("Echoing /etc/hosts into the program log...")
    logger.info(generate_banner("START OF /ETC/HOSTS"))
    hosts_content = run_command(["cat", "/etc/hosts"]).stdout
    logger.info(hosts_content.strip())
    logger.info(generate_banner("END OF /ETC/HOSTS"))
    print_separator()

    logger.info("Updating packages...")
    print_separator()
    run_command(["dnf", "update", "-y"])
    print_separator()

    logger.info("Installing Extra Packages for Enterprise Linux...")
    print_separator()
    run_command(["dnf", "install", "-y", "epel-release"])
    run_command(["/usr/bin/crb", "enable"])
    print_separator()

    logger.info("Upgrading packages (if available)...")
    print_separator()
    run_command(["dnf", "upgrade", "-y"])
    print_separator()

    logger.info("Installing Extra Applications...")
    print_separator()
    install_log_path = f"/var/tmp/{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')}-install_extra_pkgs.log"
    try:
        run_command([
            "dnf", "install", "-y",
            "ansible", "autofs", "cockpit", "firewalld", "ipcalc", "mlocate", "nano",
            "net-tools", "nfs-utils", "oddjob", "sssd"
        ])
        logger.info("Package installation successful.")
    except subprocess.CalledProcessError:
        logger.error(f"Package installation failed. Check {install_log_path}")
        exit(1)
    print_separator()

    logger.info("Enabling new services...")
    print_separator()
    services_to_enable = [
        "cockpit.socket",
        "autofs",
        "oddjobd",
        "sssd",
        "firewalld"
    ]
    for service in services_to_enable:
        try:
            run_command(["systemctl", "enable", "--now", service])
            logger.info(f"Successfully enabled {service}")
        except subprocess.CalledProcessError:
            logger.error(f"Failed to enable {service}")
    logger.info(generate_banner("WORKSTATION PREPARATION COMPLETED"))
    print_separator()

def configure_autofs_in_ipa(nfs_server_ip, nfs_export_path, domain):
    logger.info(generate_banner("AUTOFSD CONFIGURATION IN FREEIPA STARTED"))
    print_separator()

    logger.info(f"Configuring automount map for /home from NFS server {nfs_server_ip}:{nfs_export_path}...")

    # 1. Add automount map
    try:
        run_command(["ipa", "automountmap-add", "default"])
        logger.info("Automount map 'default' added.")
    except subprocess.CalledProcessError as e:
        if "already exists" in e.stderr:
            logger.warning("Automount map 'default' already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount map 'default': {e.stderr}")
            exit(1)

    # 2. Add automount location
    try:
        run_command(["ipa", "automountlocation-add", "default"])
        logger.info("Automount location 'default' added.")
    except subprocess.CalledProcessError as e:
        if "already exists" in e.stderr:
            logger.warning("Automount location 'default' already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount location 'default': {e.stderr}")
            exit(1)

    # 3. Add automount key for /home
    # The key is the mount point relative to the automount map (e.g., /home/user -> /user)
    # The value is the NFS export path
    try:
        run_command([
            "ipa", "automountkey-add", "default", "/home",
            f"--posix={nfs_server_ip}:{nfs_export_path}"
        ])
        logger.info(f"Automount key for /home added: {nfs_server_ip}:{nfs_export_path}")
    except subprocess.CalledProcessError as e:
        if "already exists" in e.stderr:
            logger.warning("Automount key for /home already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount key for /home: {e.stderr}")
            exit(1)

    logger.info("Automount configuration in FreeIPA complete.")
    logger.info(generate_banner("AUTOFSD CONFIGURATION IN FREEIPA COMPLETED"))
    print_separator()

def install_freeipa_server(prefs, hostname_short, ip_address, domain):
    logger.info(generate_banner("FREEIPA SERVER INSTALLATION & CONFIGURATION STARTED"))
    print_separator()

    logger.info("Downloading the FreeIPA software...")
    print_separator()
    install_log_path = f"/var/tmp/{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')}-freeipa-server-download.log"
    try:
        run_command(["dnf", "install", "-y", "freeipa-server", "freeipa-server-dns"])
        logger.info("FreeIPA server software downloaded successfully.")
    except subprocess.CalledProcessError:
        logger.error(f"FreeIPA server software download failed. Check {install_log_path}")
        exit(1)
    print_separator()

    logger.info("Installing & Configuring the FreeIPA Server software...")
    print_separator()
    install_log_path = f"/var/tmp/{datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')}-freeipa-server-installation.log"

    ipa_install_cmd = [
        "ipa-server-install",
        f"--realm={domain.upper()}", # Use uppercase domain for realm
        f"--domain={domain}",
        f"--hostname={hostname_short}.{domain}",
        f"--ip-address={ip_address}",
        "--setup-dns",
        "--no-forwarders",
        "--auto-reverse",
        "--idstart=100000"
    ]
    run_command(ipa_install_cmd)
    logger.info("FreeIPA server installed and configured.")
    print_separator()

    logger.info("Creating IPA management scripts...")
    ipa_create_host_script = f"#!/bin/bash\n# Usage: ipa_create_host.sh <hostname> <ip>\nipa host-add $1.{domain} --ip-address=$2\n"
    ipa_create_group_script = "#!/bin/bash\n# Usage: ipa_create_group.sh <groupname>\nipa group-add $1\n"
    ipa_create_user_script = f"#!/bin/bash\n# Usage: ipa_create_user.sh <username> <firstname> <lastname>\nipa user-add $1 --first=$2 --last=$3 --homedir=/home/$1\n"

    with open("/usr/local/bin/ipa_create_host.sh", "w") as f: f.write(ipa_create_host_script)
    with open("/usr/local/bin/ipa_create_group.sh", "w") as f: f.write(ipa_create_group_script)
    with open("/usr/local/bin/ipa_create_user.sh", "w") as f: f.write(ipa_create_user_script)

    run_command(["chmod", "+x", "/usr/local/bin/ipa_create_*.sh"])
    logger.info("IPA management scripts created and made executable.")
    print_separator()

    logger.info("Logging in as FreeIPA admin...")
    run_command(["kinit", "admin"])
    logger.info("Logged in as FreeIPA admin.")
    logger.info(generate_banner("FREEIPA SERVER INSTALLATION & CONFIGURATION COMPLETED"))
    print_separator()

def enroll_freeipa_hosts(prefs, domain):
    logger.info(generate_banner("FREEIPA HOST ENROLMENT STARTED"))
    print_separator()

    confirm = input("Have you modified the hosts file? (yes/no): ").lower()
    if confirm != "yes":
        logger.error("Please modify the hosts file before running this script.")
        exit(1)

    network_hosts = prefs.get('network_hosts', [])
    if not network_hosts:
        logger.warning("No network hosts found in preferences. Skipping host enrollment.")
        return

    for host_data in network_hosts:
        ip_address = host_data.get('ipv4_address')
        hostname = host_data.get('fqdn')

        if not ip_address or not hostname:
            logger.warning(f"Skipping host due to missing IP or FQDN: {host_data}")
            continue

        logger.info(f"Enrolling host: {hostname} with IP: {ip_address}")
        try:
            run_command(["ipa", "host-add", "--force", f"--ip-address={ip_address}", hostname])
            logger.info(f"Successfully enrolled {hostname}")
        except subprocess.CalledProcessError:
            logger.error(f"Failed to enroll {hostname}")
        print_separator()

    logger.info(generate_banner("FREEIPA HOST ENROLMENT COMPLETED"))
    print_separator()

def main():
    logger.info(generate_banner("SETUP FREEIPA SERVER STARTED"))
    print_separator()

    # --- Initial Setup --- #
    hostname_short, hostname_long, ip_address, domain = get_network_info()
    
    # Assuming network_preferences.json is in conf/pref/network_preferences/
    # This path needs to be relative to the PROGRAM_DIR
    # For now, using a placeholder. In a real scenario, PROGRAM_DIR would be passed or derived.
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate up to WORKSTATION_CONFIGURATION root
    program_root_dir = os.path.abspath(os.path.join(current_script_dir, "..", "..", "..", ".."))
    network_prefs_path = os.path.join(program_root_dir, "pref", "network_preferences", "network_hosts_preferences.json")

    prefs = load_network_preferences(network_prefs_path)
    confirm_network_prefs_modified()
    check_prerequisites()

    # --- System Update and Preparation --- #
    update_system()

    # --- FreeIPA Server Installation --- #
    install_freeipa_server(prefs, hostname_short, ip_address, domain)

    # --- AUTOFSD Configuration in FreeIPA --- #
    # Placeholder for NFS server details. Replace with your actual values.
    nfs_server_ip = "10.20.51.4" # Example: IP of your NAS
    nfs_export_path = "/mnt/user/home_dirs" # Example: NFS export path on your NAS
    configure_autofs_in_ipa(nfs_server_ip, nfs_export_path, domain)

    # --- FreeIPA Host Enrollment --- #
    enroll_freeipa_hosts(prefs, domain)

    logger.info("Reboot the system now")
    logger.info(generate_banner("SETUP FREEIPA SERVER COMPLETED"))
    print_separator()

if __name__ == '__main__':
    main()
