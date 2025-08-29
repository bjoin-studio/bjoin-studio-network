
(
echo "--- Raspberry Pi System Information ---"
echo ""
echo "Hostname and IP:"
hostname -I 2>&1
echo ""
echo "OS Version:"
if [ -f /etc/os-release ]; then
    cat /etc/os-release
else
    echo "OS release info not found."
fi
echo ""
echo "Hardware Model:"
if [ -f /sys/firmware/devicetree/base/model ]; then
    cat /sys/firmware/devicetree/base/model | tr -d '\0'
else
    echo "Hardware model info not found."
fi
echo ""
echo "CPU Info:"
cat /proc/cpuinfo 2>&1
echo ""
echo "Kernel and Architecture:"
uname -a 2>&1
echo ""
echo "Memory Usage:"
free -h 2>&1
echo ""
echo "Disk Space:"
df -h 2>&1
echo ""
echo "CPU Temperature:"
if command -v vcgencmd >/dev/null 2>&1; then
    vcgencmd measure_temp
else
    echo "vcgencmd not available."
fi
echo ""
echo "USB Devices:"
lsusb 2>&1
echo ""
) > system_info.txt

# Docker installation
# curl -sSL https://get.docker.com | sh
# sudo usermod -aG docker $USER
