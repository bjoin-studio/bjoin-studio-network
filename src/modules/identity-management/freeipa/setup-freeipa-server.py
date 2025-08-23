import os
import subprocess
import logging
import json
import datetime
import re
import time
import sys

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
def run_command(command, check=True, capture_output=True, log_output=True, interactive=False):
    """
    Enhanced command runner with support for interactive commands
    """
    cmd_str = ' '.join(command)
    if log_output:
        logger.info(f"Executing: {cmd_str}")
    
    try:
        if interactive:
            # For interactive commands, don't capture output and allow direct terminal interaction
            result = subprocess.run(command, check=check, text=True)
            # Create a dummy result object for consistency
            class DummyResult:
                def __init__(self):
                    self.returncode = 0
                    self.stdout = ""
                    self.stderr = ""
            return DummyResult()
        else:
            # For non-interactive commands, use the original behavior
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
        if hasattr(e, 'stdout') and e.stdout:
            logger.error(f"Stdout:\n{e.stdout.strip()}")
        if hasattr(e, 'stderr') and e.stderr:
            logger.error(f"Stderr:\n{e.stderr.strip()}")
        raise
    except FileNotFoundError:
        logger.error(f"Command not found: {command[0]}")
        raise

def run_command_with_input(command, input_text=None, check=True):
    """
    Run command with predefined input (for semi-interactive commands)
    """
    cmd_str = ' '.join(command)
    logger.info(f"Executing with input: {cmd_str}")
    
    try:
        result = subprocess.run(
            command, 
            input=input_text, 
            check=check, 
            capture_output=True, 
            text=True
        )
        if result.stdout:
            logger.info(f"Stdout:\n{result.stdout.strip()}")
        if result.stderr:
            logger.error(f"Stderr:\n{result.stderr.strip()}")
        return result
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {cmd_str}")
        logger.error(f"Return Code: {e.returncode}")
        if e.stdout:
            logger.error(f"Stdout:\n{e.stdout.strip()}")
        if e.stderr:
            logger.error(f"Stderr:\n{e.stderr.strip()}")
        raise

def update_etc_hosts(prefs):
    logger.info(generate_banner("UPDATING /ETC/HOSTS"))
    print_separator()

    network_hosts = prefs.get('network_hosts', [])
    if not network_hosts:
        logger.warning("No network hosts found in preferences. Skipping /etc/hosts update.")
        return

    try:
        with open("/etc/hosts", "r") as f:
            current_hosts_content = f.readlines()
    except FileNotFoundError:
        logger.error("/etc/hosts not found. Cannot update.")
        return

    hosts_to_add = []
    for host_data in network_hosts:
        ip_address = host_data.get('ipv4_address')
        fqdn = host_data.get('fqdn')
        hostname = fqdn.split('.')[0] if fqdn else ""

        if not ip_address or not fqdn:
            logger.warning(f"Skipping host due in network_hosts due to missing IP or FQDN: {host_data}")
            continue

        # Construct the line to add, including FQDN and short hostname as alias
        host_line = f"{ip_address}\t{fqdn}\t{hostname}\n"

        # Check if the line (or a similar entry for the IP/FQDN) already exists
        found = False
        for line in current_hosts_content:
            if ip_address in line and (fqdn in line or hostname in line):
                found = True
                break
        
        if not found:
            hosts_to_add.append(host_line)
            logger.info(f"Adding to /etc/hosts: {host_line.strip()}")
        else:
            logger.info(f"Entry for {fqdn} already exists in /etc/hosts. Skipping.")

    if hosts_to_add:
        try:
            # Use sudo and tee to append to /etc/hosts
            append_command = ["sudo", "tee", "-a", "/etc/hosts"]
            process = subprocess.run(append_command, input=''.join(hosts_to_add), check=True, capture_output=True, text=True)
            if process.returncode == 0:
                logger.info("/etc/hosts updated successfully.")
            else:
                logger.error(f"Failed to update /etc/hosts. Stderr: {process.stderr.strip()}")
        except subprocess.CalledProcessError:
            logger.error("Failed to update /etc/hosts. Check permissions.")
    else:
        logger.info("No new entries to add to /etc/hosts.")

    print_separator()


def generate_banner(text, char='=', length=79):
    padding = (length - len(text) - 4) // 2
    return f"# {char * padding} {text} {char * padding} #"

def print_separator(char='-', length=79):
    logger.info(char * length)

def is_hostname_resolvable(hostname):
    try:
        # Try to resolve the hostname using dig. If it resolves, it's in use.
        result = subprocess.run(["dig", "+short", hostname], capture_output=True, text=True, check=False)
        if result.returncode == 0 and result.stdout.strip():
            logger.info(f"Hostname {hostname} resolves to {result.stdout.strip()}. It is in use.")
            return True
        else:
            logger.info(f"Hostname {hostname} does not resolve. It is available.")
            return False
    except FileNotFoundError:
        logger.error("'dig' command not found. Cannot check hostname resolvability. Please install bind-utils or dnsutils.")
        sys.exit(1)
    except Exception as e:
        logger.error(f"Error checking hostname resolvability for {hostname}: {e}")
        sys.exit(1)

def set_system_hostname(new_hostname_long):
    logger.info(f"Attempting to set system hostname to {new_hostname_long}...")
    try:
        run_command(["hostnamectl", "set-hostname", new_hostname_long])
        logger.info(f"System hostname successfully set to {new_hostname_long}.")
        # Give systemd-resolved a moment to catch up if it's in use
        time.sleep(2)
    except subprocess.CalledProcessError:
        logger.error(f"Failed to set system hostname to {new_hostname_long}. Please check permissions or try manually.")
        sys.exit(1)

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
                sys.exit(1)
    except FileNotFoundError:
        logger.error("/etc/resolv.conf not found. Cannot determine domain automatically.")
        sys.exit(1)
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
                sys.exit(1)
    
    # Set the system's hostname to the newly determined FreeIPA server hostname
    set_system_hostname(new_hostname_long)

    # Verify the hostname change
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
        sys.exit(1)
    
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
        sys.exit(1)
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from {config_path}. Check file format.")
        sys.exit(1)


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
    # Use DEBIAN_FRONTEND=noninteractive equivalent and ensure non-interactive
    env = os.environ.copy()
    env['DEBIAN_FRONTEND'] = 'noninteractive'
    run_command(["dnf", "update", "-y", "--assumeyes"], interactive=False)
    print_separator()

    logger.info("Installing Extra Packages for Enterprise Linux...")
    print_separator()
    run_command(["dnf", "install", "-y", "--assumeyes", "epel-release"], interactive=False)
    run_command(["/usr/bin/crb", "enable"], interactive=False)
    print_separator()

    logger.info("Upgrading packages (if available)...")
    print_separator()
    run_command(["dnf", "upgrade", "-y", "--assumeyes"], interactive=False)
    print_separator()

    logger.info("Installing Extra Applications...")
    print_separator()
    try:
        run_command([
            "dnf", "install", "-y", "--assumeyes",
            "ansible", "autofs", "cockpit", "firewalld", "ipcalc", "mlocate", "nano",
            "net-tools", "nfs-utils", "oddjob", "sssd"
        ], interactive=False)
        logger.info("Package installation successful.")
    except subprocess.CalledProcessError:
        logger.error("Package installation failed.")
        sys.exit(1)
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
        if "already exists" in str(e):
            logger.warning("Automount map 'default' already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount map 'default'")
            sys.exit(1)

    # 2. Add automount location
    try:
        run_command(["ipa", "automountlocation-add", "default"])
        logger.info("Automount location 'default' added.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            logger.warning("Automount location 'default' already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount location 'default'")
            sys.exit(1)

    # 3. Add automount key for /home
    try:
        run_command([
            "ipa", "automountkey-add", "default", "/home",
            f"--posix={nfs_server_ip}:{nfs_export_path}"
        ])
        logger.info(f"Automount key for /home added: {nfs_server_ip}:{nfs_export_path}")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e):
            logger.warning("Automount key for /home already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount key for /home")
            sys.exit(1)

    logger.info("Automount configuration in FreeIPA complete.")
    logger.info(generate_banner("AUTOFSD CONFIGURATION IN FREEIPA COMPLETED"))
    print_separator()

def install_freeipa_server(prefs, hostname_short, ip_address, domain):
    logger.info(generate_banner("FREEIPA SERVER INSTALLATION & CONFIGURATION STARTED"))
    print_separator()

    logger.info("Downloading the FreeIPA software...")
    print_separator()
    try:
        run_command(["dnf", "install", "-y", "--assumeyes", "freeipa-server", "freeipa-server-dns"], interactive=False)
        logger.info("FreeIPA server software downloaded successfully.")
    except subprocess.CalledProcessError:
        logger.error("FreeIPA server software download failed.")
        sys.exit(1)
    print_separator()

    logger.info("Installing & Configuring the FreeIPA Server software...")
    print_separator()

    # Get passwords from user before starting installation
    print("\n" + "="*60)
    print("FREEIPA INSTALLATION REQUIRES PASSWORDS")
    print("="*60)
    
    # Option 1: Use environment variables (recommended for automation)
    ds_password = os.environ.get('IPA_DS_PASSWORD')
    admin_password = os.environ.get('IPA_ADMIN_PASSWORD')
    
    if not ds_password or not admin_password:
        print("Please set environment variables IPA_DS_PASSWORD and IPA_ADMIN_PASSWORD")
        print("Or modify the script to include hardcoded passwords (less secure)")
        print("\nExample:")
        print("export IPA_DS_PASSWORD='YourDirectoryManagerPassword123!'")
        print("export IPA_ADMIN_PASSWORD='YourAdminPassword123!'")
        sys.exit(1)

    ipa_install_cmd = [
        "ipa-server-install",
        "--unattended",  # This is crucial for non-interactive installation
        f"--realm={domain.upper()}",
        f"--domain={domain}",
        f"--hostname={hostname_short}.{domain}",
        f"--ip-address={ip_address}",
        "--setup-dns",
        "--no-forwarders",
        "--auto-reverse",
        "--idstart=100000",
        f"--ds-password={ds_password}",
        f"--admin-password={admin_password}"
    ]
    
    logger.info("Starting FreeIPA installation (this may take several minutes)...")
    try:
        # Run the installation command with interactive=True to allow it to work properly
        run_command(ipa_install_cmd, interactive=True)
        logger.info("FreeIPA server installed and configured.")
    except subprocess.CalledProcessError:
        logger.error("FreeIPA installation failed. Check the logs for details.")
        sys.exit(1)
    print_separator()

    logger.info("Creating IPA management scripts...")
    ipa_create_host_script = f"#!/bin/bash\n# Usage: ipa_create_host.sh <hostname> <ip>\nipa host-add $1.{domain} --ip-address=$2\n"
    ipa_create_group_script = "#!/bin/bash\n# Usage: ipa_create_group.sh <groupname>\nipa group-add $1\n"
    ipa_create_user_script = f"#!/bin/bash\n# Usage: ipa_create_user.sh <username> <firstname> <lastname>\nipa user-add $1 --first=$2 --last=$3 --homedir=/home/$1\n"

    with open("/usr/local/bin/ipa_create_host.sh", "w") as f: 
        f.write(ipa_create_host_script)
    with open("/usr/local/bin/ipa_create_group.sh", "w") as f: 
        f.write(ipa_create_group_script)
    with open("/usr/local/bin/ipa_create_user.sh", "w") as f: 
        f.write(ipa_create_user_script)

    run_command(["chmod", "+x", "/usr/local/bin/ipa_create_host.sh"])
    run_command(["chmod", "+x", "/usr/local/bin/ipa_create_group.sh"])
    run_command(["chmod", "+x", "/usr/local/bin/ipa_create_user.sh"])
    logger.info("IPA management scripts created and made executable.")
    print_separator()

    logger.info("Obtaining Kerberos ticket for admin...")
    try:
        # Use kinit with password from environment
        run_command_with_input(["kinit", "admin"], input_text=f"{admin_password}\n")
        logger.info("Successfully obtained Kerberos ticket for admin.")
    except subprocess.CalledProcessError:
        logger.error("Failed to obtain Kerberos ticket. Please run 'kinit admin' manually after installation.")
    
    logger.info(generate_banner("FREEIPA SERVER INSTALLATION & CONFIGURATION COMPLETED"))
    print_separator()

def enroll_freeipa_hosts(prefs, domain):
    logger.info(generate_banner("FREEIPA HOST ENROLMENT STARTED"))
    print_separator()

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

    # Check if running as root
    if os.geteuid() != 0:
        logger.error("This script must be run as root or with sudo privileges.")
        sys.exit(1)

    # --- Initial Setup --- #
    hostname_short, hostname_long, ip_address, domain = get_network_info()
    
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate up to WORKSTATION_CONFIGURATION root
    program_root_dir = os.path.abspath(os.path.join(current_script_dir, "..", "..", "..", ".."))
    network_prefs_path = os.path.join(program_root_dir, "inventory", "network_data", "network_inventory.json")

    prefs = load_network_preferences(network_prefs_path)
    check_prerequisites()
    update_etc_hosts(prefs)

    # --- System Update and Preparation --- #
    update_system()

    # --- FreeIPA Server Installation --- #
    install_freeipa_server(prefs, hostname_short, ip_address, domain)

    # --- AUTOFSD Configuration in FreeIPA --- #
    # Get NFS server details from preferences or use defaults
    nfs_server_ip = "10.20.51.81"  # Replace with actual NFS server IP
    nfs_export_path = "/mnt/home-pool/home-directories"  # Replace with actual path
    configure_autofs_in_ipa(nfs_server_ip, nfs_export_path, domain)

    # --- FreeIPA Host Enrollment --- #
    enroll_freeipa_hosts(prefs, domain)

    logger.info("Installation completed successfully!")
    logger.info("Please reboot the system to complete the setup.")
    logger.info(generate_banner("SETUP FREEIPA SERVER COMPLETED"))
    print_separator()

if __name__ == '__main__':
    main()
