#!/bin/bash
#
# This script configures the Proxmox host for OPNsense and creates the VM.
#
# v4: Corrected to use .img file and qm importdisk method.
#
# Network Configuration:
# - Management NIC 'enp1s0' (Intel 82574L) is NOT modified.
# - WAN Bridge (vmbr1): Uses physical NIC 'enp8s0f0' (from the Intel 4-port card).
# - LAN Bridge (vmbr2): Uses physical NIC 'ens5np0' (10Gb Solarflare).
#
set -e

# --- Configuration Variables ---
VM_ID="101"
VM_NAME="opnsense-fw-10gb"
RAM="16384" # In MB
CORES="2"
DISK_SIZE="128G"
STORAGE_POOL="local-zpool"
WAN_BRIDGE="vmbr1"
WAN_NIC="enp8s0f0"
LAN_BRIDGE="vmbr2"
LAN_NIC="ens5np0"
OPNSENSE_IMG_URL="https://mirror.sfo12.us.leaseweb.net/opnsense/releases/25.7/OPNsense-25.7-vga-amd64.img.bz2"
IMG_FILENAME=$(basename ${OPNSENSE_IMG_URL})
IMG_NAME="${IMG_FILENAME%.bz2}"
DOWNLOAD_PATH="/var/lib/vz/template/iso" # Re-using iso path for downloads

# --- 1. Configure Proxmox Networking (Idempotent) ---
echo ">>> Configuring Proxmox network bridges for OPNsense..."

if ! grep -q "iface ${WAN_BRIDGE} inet manual" /etc/network/interfaces; then
    echo "...Adding ${WAN_BRIDGE} configuration."
    cat >> /etc/network/interfaces <<EOF

# OPNsense WAN Bridge (using a port from the Intel 4-port NIC)
auto ${WAN_BRIDGE}
iface ${WAN_BRIDGE} inet manual
        bridge-ports ${WAN_NIC}
        bridge-stp off
        bridge-fd 0
EOF
else
    echo "...${WAN_BRIDGE} configuration already exists."
fi

if ! grep -q "iface ${LAN_BRIDGE} inet manual" /etc/network/interfaces; then
    echo "...Adding ${LAN_BRIDGE} configuration."
    cat >> /etc/network/interfaces <<EOF

# OPNsense 10Gbps LAN Bridge (using the Solarflare NIC)
auto ${LAN_BRIDGE}
iface ${LAN_BRIDGE} inet manual
        bridge-ports ${LAN_NIC}
        bridge-stp off
        bridge-fd 0
EOF
else
    echo "...${LAN_BRIDGE} configuration already exists."
fi

echo ">>> Applying network changes..."
ifreload -a

# --- 2. Download OPNsense Disk Image ---
if [ ! -f "${DOWNLOAD_PATH}/${IMG_NAME}" ]; then
    echo ">>> Downloading OPNsense disk image..."
    wget -P ${DOWNLOAD_PATH} ${OPNSENSE_IMG_URL}
    echo ">>> Decompressing disk image..."
    bzip2 -d "${DOWNLOAD_PATH}/${IMG_FILENAME}"
else
    echo ">>> OPNsense disk image already exists. Skipping download."
fi

# --- 3. Create and Configure OPNsense VM ---
# Destroy existing VM if it exists, to ensure a clean import
if qm status ${VM_ID} >/dev/null 2>&1; then
    echo ">>> Found existing VM ${VM_ID}. Destroying for clean import..."
    qm stop ${VM_ID} || true # Stop the VM, ignore error if already stopped
    qm destroy ${VM_ID}
fi

echo ">>> Creating new VM ${VM_ID} (${VM_NAME})..."
qm create ${VM_ID} --name "${VM_NAME}" --memory ${RAM} --cores ${CORES} --net0 virtio,bridge=${WAN_BRIDGE} --net1 virtio,bridge=${LAN_BRIDGE} --scsihw virtio-scsi-pci

echo ">>> Importing downloaded disk image..."
qm importdisk ${VM_ID} "${DOWNLOAD_PATH}/${IMG_NAME}" ${STORAGE_POOL}

echo ">>> Attaching imported disk and configuring boot order..."
qm set ${VM_ID} --scsi0 ${STORAGE_POOL}:vm-${VM_ID}-disk-0,iothread=1
qm set ${VM_ID} --boot order=scsi0
qm set ${VM_ID} --onboot 1
qm set ${VM_ID} --description "OPNsense Firewall VM. WAN is on ${WAN_NIC}, LAN is on ${LAN_NIC}."

# Clean up the downloaded image file after successful import
rm "${DOWNLOAD_PATH}/${IMG_NAME}"

echo ""
echo "✅ --- SUCCESS --- ✅"
echo ""
echo "VM ${VM_ID} (${VM_NAME}) has been created with the imported disk."
echo "You can now start the VM from the Proxmox web interface. No installation is needed."
