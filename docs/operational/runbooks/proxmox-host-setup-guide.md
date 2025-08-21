# Proxmox VE Host Installation and Network Configuration

This guide provides step-by-step instructions for installing Proxmox VE on the Mac Pro 6,1 and configuring its network interfaces to integrate with the bjoin.studio network design.

## 1. Proxmox VE Installation

1.  Create a bootable Proxmox VE USB stick from the official ISO.
2.  Install Proxmox onto the Mac Pro's internal storage, following the standard on-screen instructions.
3.  During the installation wizard, you will be asked for initial network configuration. Use the following details:
    -   **Hostname:** `pmx-01.bjoin.studio`
    -   **IP Address:** `10.20.51.20/24`
    -   **Gateway:** `10.20.51.1`
    -   **DNS Server:** `10.20.51.10` (the planned IP for your FreeIPA server)

## 2. Network Configuration (The Proxmox Way)

Proxmox uses a `interfaces` file located at `/etc/network/interfaces` to manage its networking. This setup separates the hypervisor's management network from the guest VM networks.

> **Important:** The physical network interface names (`enp11s0`, `enp12s0`) in this guide are examples. Run `ip a` on your Proxmox host to find the correct names for your hardware and substitute them in the configuration below.

**Create a timestamped backup of /etc/network/interfaces:**
```
cp /etc/network/interfaces /etc/network/interfaces.bak.$(date +%F-%H-%M-%S)
```

**Connect the Mac Pro's physical Ethernet ports as follows:**
*   **First Ethernet Port (`enp11s0`):** Connect to a switch port configured for ACCESS on VLAN 51 (Management).
*   **Second Ethernet Port (`enp12s0`):** Connect to a switch port configured as a TRUNK that carries all the VLANs you want your VMs to be able to access.

Here is the recommended content for your `/etc/network/interfaces` file. You can edit this from the Proxmox host's shell.


```
# /etc/network/interfaces

auto lo
iface lo inet loopback

# Management Interface on VLAN 51
# The first physical ethernet port on the Mac Pro
iface enp11s0 inet manual

auto vmbr0
iface vmbr0 inet static
    address 10.20.51.20/24
    gateway 10.20.51.1
    bridge-ports enp11s0
    bridge-stp off
    bridge-fd 0
# This is the Proxmox Management Bridge. The host is accessible at https://10.20.51.20:8006

# Trunk Interface for Guest VMs
# The second physical ethernet port on the Mac Pro
iface enp12s0 inet manual

# --- Guest VLAN Bridges --- #
# The format 'enp12s0.XX' creates a VLAN-aware sub-interface.

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
```

### Explanation:

*   `vmbr0` is the main management bridge. It is physically connected to `enp11s0` (the first ethernet port) and has the static IP of the Proxmox host itself. You connect this port to a switch port that is an access port for VLAN 51.
*   `vmbr11`, `vmbr21`, etc., are bridges for your guest VMs. They are attached to VLAN sub-interfaces on `enp12s0` (the second ethernet port). You connect this port to a trunk port on your switch.
*   When you create a VM (like a render node), you will attach its virtual network card to the corresponding bridge (e.g., `vmbr11`) to place it in that VLAN.

---

## 3. Post-Installation: Enabling IOMMU for PCI Passthrough

To enable IOMMU for passing through hardware like GPUs or network cards directly to your virtual machines, you can use the provided utility script. This is often necessary for high-performance VMs.

For instructions and the script itself, see here: [mac_pro_6_1_IOMMU_config.sh](../../../src/mac_pro_6_1_IOMMU_config.sh)