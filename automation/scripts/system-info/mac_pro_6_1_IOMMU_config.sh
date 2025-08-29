#!/bin/bash
#
# Title: mac_pro_6_1_IOMMU_config.sh
# Description: Enables IOMMU on a Proxmox VE host for PCI(e) passthrough.
# Adapted for the bjoin.studio project.
#
# This script is intended to be run on the Proxmox host itself.
# It modifies critical boot files. Run with caution and after backing up.
#

set -euo pipefail

echo "--- [Step 1/3] Modifying /etc/kernel/cmdline for IOMMU ---"
# Create a backup first
cp /etc/kernel/cmdline /etc/kernel/cmdline.bak.$(date +%F)
# Add kernel parameters for IOMMU
sed -i '1s/$/ intel_iommu=on iommu=pt/' /etc/kernel/cmdline
echo "Successfully updated /etc/kernel/cmdline."


echo "--- [Step 2/3] Loading required VFIO modules ---"
# Create a backup of /etc/modules first
cp /etc/modules /etc/modules.bak.$(date +%F)
# Append modules required for PCI passthrough
cat <<EOF >> /etc/modules
# Modules for PCI Passthrough (IOMMU)
vfio
vfio_iommu_type1
vfio_pci
vfio_virqfd
EOF
echo "Successfully updated /etc/modules."


echo "--- [Step 3/3] Updating initramfs ---"
echo "Updating the initial RAM filesystem for all kernels. This may take a moment..."
update-initramfs -u -k all
echo "initramfs updated."


echo
echo "--- IOMMU Configuration Complete ---"
echo "A REBOOT IS REQUIRED for these changes to take effect."
echo "Please reboot your Proxmox host now."

exit 0
