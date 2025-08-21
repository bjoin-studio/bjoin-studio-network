# CORRECTED Commands to Configure Network on pmx-01.bjoin.studio

This file provides the necessary commands to update the network configuration on your Proxmox host using the correct interface names (`enp11s0` and `enp12s0`).

- **Backup:** A new backup of the working configuration will be made.
- **Update:** The `/etc/network/interfaces` file will be overwritten with the correct configuration.
- **Apply:** The networking service will be reloaded.

---

## Commands

Run the following commands in the shell of your `pmx-01` host.

### 1. Back up the current configuration

```bash
sudo cp /etc/network/interfaces /etc/network/interfaces.bak.$(date +%F-%H-%M-%S)
```

### 2. Write the new, corrected network configuration

This command will overwrite the `/etc/network/interfaces` file with the correct bridge configuration.

```bash
sudo tee /etc/network/interfaces > /dev/null <<'EOF'
auto lo
iface lo inet loopback

# Management Interface (ACCESS VLAN 51)
iface enp11s0 inet manual

auto vmbr0
iface vmbr0 inet static
        address 10.20.51.20/24
        gateway 10.20.51.1
        bridge-ports enp11s0
        bridge-stp off
        bridge-fd 0

# Trunk Interface for Guest VMs
iface enp12s0 inet manual

# --- Guest VLAN Bridges --- #

auto vmbr11
iface vmbr11 inet manual
    bridge-ports enp12s0.11
    bridge-stp off
    bridge-fd 0
# Bridge for VMs in VLAN 11 (PROD_SERVERS)

auto vmbr21
iface vmbr21 inet manual
    bridge-ports enp12s0.21
    bridge-stp off
    bridge-fd 0
# Bridge for VMs in VLAN 21 (STAGE_SERVERS)

auto vmbr31
iface vmbr31 inet manual
    bridge-ports enp12s0.31
    bridge-stp off
    bridge-fd 0
# Bridge for VMs in VLAN 31 (STUDIO_GENERAL)

auto vmbr41
iface vmbr41 inet manual
    bridge-ports enp12s0.41
    bridge-stp off
    bridge-fd 0
# Bridge for VMs in VLAN 41 (WORKSHOP_GENERAL)

auto vmbr51
iface vmbr51 inet manual
    bridge-ports enp12s0.51
    bridge-stp off
    bridge-fd 0
# Bridge for VMs in VLAN 51 (MGMT)

source /etc/network/interfaces.d/*
EOF
```

### 3. Apply the new network configuration

This command reloads the network configuration. Your connection should remain active.

```bash
sudo ifreload -a
```