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
def run_command(command, check=True, capture_output=True, log_output=True, interactive=False, timeout=600, show_live_output=False):
    """
    Enhanced command runner with support for interactive commands and live output display
    """
    cmd_str = ' '.join(command)
    if log_output:
        logger.info(f"Executing: {cmd_str}")
    
    try:
        if interactive:
            # For interactive commands, don't capture output and allow direct terminal interaction
            print(f"\n>>> Running interactive command: {cmd_str}")
            result = subprocess.run(command, check=check, text=True, timeout=timeout)
            print(f">>> Interactive command completed with return code: {result.returncode}")
            # Create a dummy result object for consistency
            class DummyResult:
                def __init__(self):
                    self.returncode = 0
                    self.stdout = ""
                    self.stderr = ""
            return DummyResult()
        else:
            # For package management commands, use special handling
            if command[0] in ['dnf', 'yum', 'apt', 'apt-get']:
                return run_package_command(command, check, log_output, timeout)
            
            # For other commands that need live output
            if show_live_output:
                return run_command_with_live_output(command, check, log_output, timeout)
            
            # For other non-interactive commands, use the original behavior
            result = subprocess.run(command, check=check, capture_output=capture_output, text=True, timeout=timeout)
            if log_output:
                if result.stdout:
                    logger.info(f"Stdout:\n{result.stdout.strip()}")
                if result.stderr:
                    logger.error(f"Stderr:\n{result.stderr.strip()}")
            return result
    except subprocess.TimeoutExpired:
        logger.error(f"Command timed out after {timeout} seconds: {cmd_str}")
        print(f">>> TIMEOUT: {cmd_str}")
        raise
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

def run_command_with_live_output(command, check=True, log_output=True, timeout=600):
    """
    Run command with live output display for long-running operations
    """
    cmd_str = ' '.join(command)
    print(f"\n>>> Executing: {cmd_str}")
    print(">>> Live output:")
    
    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=0,  # Unbuffered
            universal_newlines=True
        )
        
        output_lines = []
        start_time = time.time()
        
        while True:
            if process.poll() is not None:
                # Read any remaining output
                remaining = process.stdout.read()
                if remaining:
                    for line in remaining.splitlines():
                        if line.strip():
                            print(f"    {line}")
                            output_lines.append(line)
                            if log_output:
                                logger.info(line)
                break
                
            line = process.stdout.readline()
            if line:
                line = line.rstrip('\n\r')
                if line.strip():
                    print(f"    {line}")
                    output_lines.append(line)
                    if log_output:
                        logger.info(line)
            
            # Check timeout
            if time.time() - start_time > timeout:
                process.kill()
                raise subprocess.TimeoutExpired(command, timeout)
        
        return_code = process.wait()
        print(f">>> Command completed with return code: {return_code}")
        
        class LiveResult:
            def __init__(self, returncode, stdout):
                self.returncode = returncode
                self.stdout = stdout
                self.stderr = ""
        
        result = LiveResult(return_code, '\n'.join(output_lines))
        
        if check and return_code != 0:
            raise subprocess.CalledProcessError(return_code, command, output=result.stdout)
        
        return result
        
    except Exception as e:
        print(f">>> ERROR: {e}")
        raise

def run_package_command(command, check=True, log_output=True, timeout=600):
    """
    Special handling for package management commands with real-time output
    """
    cmd_str = ' '.join(command)
    logger.info(f"Running package command: {cmd_str}")
    print(f"\n>>> Executing: {cmd_str}")
    print(">>> Live output:")
    
    # Set up environment to prevent hanging
    env = os.environ.copy()
    env.update({
        'DEBIAN_FRONTEND': 'noninteractive',
        'NEEDRESTART_MODE': 'a',  # Automatic restart services
        'NEEDRESTART_SUSPEND': '1',  # Suspend needrestart
        'UCF_FORCE_CONFFNEW': '1',  # Use new config files
        'LANG': 'C',  # Use C locale to avoid encoding issues
        'LC_ALL': 'C'
    })
    
    try:
        # Use Popen for better control over the process
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,  # Combine stderr with stdout
            text=True,
            env=env,
            bufsize=0,  # Unbuffered for immediate output
            universal_newlines=True
        )
        
        # Read output in real-time and display immediately
        output_lines = []
        start_time = time.time()
        last_output_time = start_time
        
        while True:
            # Check if process has finished
            if process.poll() is not None:
                # Read any remaining output
                remaining_output = process.stdout.read()
                if remaining_output:
                    for line in remaining_output.splitlines():
                        if line.strip():
                            print(f"    {line}")
                            output_lines.append(line)
                            if log_output:
                                logger.info(f"PKG: {line}")
                break
            
            # Read line with timeout
            try:
                line = process.stdout.readline()
                if line:
                    line = line.rstrip('\n\r')
                    if line.strip():  # Only show non-empty lines
                        print(f"    {line}")
                        output_lines.append(line)
                        if log_output:
                            logger.info(f"PKG: {line}")
                        last_output_time = time.time()
                else:
                    # No output, but process still running - show progress indicator
                    current_time = time.time()
                    if current_time - last_output_time > 10:  # 10 seconds without output
                        elapsed = current_time - start_time
                        print(f"    ... still running ({elapsed:.0f}s elapsed) ...")
                        last_output_time = current_time
                    time.sleep(0.1)  # Small delay to prevent busy waiting
                    
                # Check timeout
                if time.time() - start_time > timeout:
                    raise subprocess.TimeoutExpired(command, timeout)
                    
            except UnicodeDecodeError:
                # Handle encoding issues
                print("    [binary output - skipping line]")
                continue
        
        # Wait for process to complete and get return code
        return_code = process.wait()
        
        print(f">>> Command completed with return code: {return_code}")
        if return_code == 0:
            print(">>> SUCCESS")
        else:
            print(">>> FAILED")
        print()  # Add blank line after command
        
        # Create result object
        class PackageResult:
            def __init__(self, returncode, stdout):
                self.returncode = returncode
                self.stdout = stdout
                self.stderr = ""
        
        result = PackageResult(return_code, '\n'.join(output_lines))
        
        if check and return_code != 0:
            raise subprocess.CalledProcessError(return_code, command, output=result.stdout)
            
        return result
        
    except subprocess.TimeoutExpired:
        logger.error(f"Package command timed out after {timeout} seconds: {cmd_str}")
        print(f">>> TIMEOUT after {timeout} seconds")
        process.kill()
        process.wait()  # Clean up zombie process
        raise
    except KeyboardInterrupt:
        print(f">>> INTERRUPTED by user")
        process.terminate()
        process.wait()
        raise
    except Exception as e:
        logger.error(f"Error running package command: {e}")
        print(f">>> ERROR: {e}")
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
    # Clean DNF cache first to avoid potential issues
    try:
        run_command(["dnf", "clean", "all"])
        logger.info("DNF cache cleaned successfully.")
    except subprocess.CalledProcessError:
        logger.warning("Failed to clean DNF cache, continuing...")
    
    # Update with explicit timeout and better options
    run_command([
        "dnf", "update", "-y", "--assumeyes", "--nogpgcheck", 
        "--skip-broken", "--setopt=timeout=300"
    ], timeout=900)
    print_separator()

    logger.info("Installing Extra Packages for Enterprise Linux...")
    print_separator()
    run_command([
        "dnf", "install", "-y", "--assumeyes", "--nogpgcheck", 
        "--setopt=timeout=300", "epel-release"
    ], timeout=600)
    
    # Enable CRB (CodeReady Builder) repository
    try:
        run_command(["/usr/bin/crb", "enable"], timeout=120)
        logger.info("CRB repository enabled.")
    except subprocess.CalledProcessError:
        logger.warning("Failed to enable CRB repository, continuing...")
    print_separator()

    logger.info("Upgrading packages (if available)...")
    print_separator()
    run_command([
        "dnf", "upgrade", "-y", "--assumeyes", "--nogpgcheck", 
        "--skip-broken", "--setopt=timeout=300"
    ], timeout=900)
    print_separator()

    logger.info("Installing Extra Applications...")
    print_separator()
    packages = [
        "ansible", "autofs", "cockpit", "firewalld", "ipcalc", 
        "mlocate", "nano", "net-tools", "nfs-utils", "oddjob", "sssd"
    ]
    
    try:
        run_command([
            "dnf", "install", "-y", "--assumeyes", "--nogpgcheck",
            "--skip-broken", "--setopt=timeout=300"
        ] + packages, timeout=900)
        logger.info("Package installation successful.")
    except subprocess.CalledProcessError:
        logger.error("Package installation failed.")
        # Try installing packages individually as fallback
        logger.info("Attempting individual package installation...")
        failed_packages = []
        for package in packages:
            try:
                run_command([
                    "dnf", "install", "-y", "--assumeyes", "--nogpgcheck", 
                    "--setopt=timeout=300", package
                ], timeout=300)
                logger.info(f"Successfully installed {package}")
            except subprocess.CalledProcessError:
                logger.error(f"Failed to install {package}")
                failed_packages.append(package)
        
        if failed_packages:
            logger.warning(f"Failed to install: {', '.join(failed_packages)}")
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
            run_command(["systemctl", "enable", "--now", service], timeout=60)
            logger.info(f"Successfully enabled {service}")
        except subprocess.CalledProcessError:
            logger.error(f"Failed to enable {service}")
    logger.info(generate_banner("WORKSTATION PREPARATION COMPLETED"))
    print_separator()

def configure_autofs_in_ipa(nfs_server_ip, nfs_export_path, domain):
    logger.info(generate_banner("AUTOFSD CONFIGURATION IN FREEIPA STARTED"))
    print_separator()

    logger.info(f"Configuring automount for /home from NFS server {nfs_server_ip}:{nfs_export_path}...")

    # 1. Create the automount location if it doesn't exist
    try:
        run_command(["ipa", "automountlocation-add", "default"])
        logger.info("Automount location 'default' created.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e.stderr):
            logger.warning("Automount location 'default' already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount location 'default': {e.stderr}")
            # This is a critical error, so we might want to exit
            # For now, we continue to allow verification steps to run

    # 2. Create the auto.home map within the default location
    try:
        run_command(["ipa", "automountmap-add", "default", "auto.home"])
        logger.info("Automount map 'auto.home' created in location 'default'.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e.stderr):
            logger.warning("Automount map 'auto.home' already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add automount map 'auto.home': {e.stderr}")

    # 3. Link /home to the auto.home map in auto.master
    try:
        run_command([
            "ipa", "automountkey-add", "default", "auto.master", 
            "--key=/home", "--info=auto.home"
        ])
        logger.info("Linked /home to auto.home map in auto.master.")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e.stderr):
            logger.warning("Automount key for /home in auto.master already exists. Skipping creation.")
        else:
            logger.error(f"Failed to link /home to auto.home map: {e.stderr}")

    # 4. Add the wildcard key for user home directories to the auto.home map
    nfs_options = f"-fstype=nfs,rw,hard,intr"
    nfs_full_path = f"{nfs_options} {nfs_server_ip}:{nfs_export_path}/&"
    try:
        run_command([
            "ipa", "automountkey-add", "default", "auto.home", 
            "--key=*", f"--info={nfs_full_path}"
        ])
        logger.info(f"Added wildcard automount key to auto.home: {nfs_full_path}")
    except subprocess.CalledProcessError as e:
        if "already exists" in str(e.stderr):
            logger.warning("Wildcard automount key in auto.home already exists. Skipping creation.")
        else:
            logger.error(f"Failed to add wildcard key to auto.home: {e.stderr}")

    # 5. Verification steps
    logger.info("Verifying automount configuration...")
    run_command(["ipa", "automountlocation-show", "default"], check=False)
    run_command(["ipa", "automountmap-show", "default", "auto.master"], check=False)
    run_command(["ipa", "automountkey-find", "default", "auto.master"], check=False)
    run_command(["ipa", "automountmap-show", "default", "auto.home"], check=False)
    run_command(["ipa", "automountkey-find", "default", "auto.home"], check=False)

    logger.info("Automount configuration in FreeIPA complete.")
    logger.info(generate_banner("AUTOFSD CONFIGURATION IN FREEIPA COMPLETED"))
    print_separator()

def install_freeipa_server(prefs, hostname_short, ip_address, domain):
    logger.info(generate_banner("FREEIPA SERVER INSTALLATION & CONFIGURATION STARTED"))
    print_separator()

    logger.info("Downloading the FreeIPA software...")
    print_separator()
    try:
        run_command([
            "dnf", "install", "-y", "--assumeyes", "--nogpgcheck", 
            "--setopt=timeout=300", "freeipa-server", "freeipa-server-dns"
        ], timeout=900)
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
    print("\n" + "="*60)
    print("STARTING FREEIPA INSTALLATION - THIS WILL TAKE 10-30 MINUTES")
    print("You will see live output below...")
    print("="*60)
    
    try:
        # Run the installation command with live output display
        run_command(ipa_install_cmd, interactive=False, show_live_output=True, timeout=1800)  # 30 minutes timeout
        logger.info("FreeIPA server installed and configured.")
        print("\n" + "="*60)
        print("FREEIPA INSTALLATION COMPLETED SUCCESSFULLY!")
        print("="*60)
    except subprocess.CalledProcessError as e:
        logger.error("FreeIPA installation failed. Check the logs for details.")
        print(f"\n>>> FREEIPA INSTALLATION FAILED with return code: {e.returncode}")
        print(">>> Check /var/log/ipaserver-install.log for detailed error information")
        sys.exit(1)
    except subprocess.TimeoutExpired:
        logger.error("FreeIPA installation timed out. This may indicate network issues or insufficient resources.")
        print("\n>>> FREEIPA INSTALLATION TIMED OUT")
        print(">>> This may be due to network issues or insufficient system resources")
        print(">>> You can try running the installation manually with the same parameters")
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