# APC UPS Network Integration: Insights and Best Practices

Connecting and configuring APC UPS (Uninterruptible Power Supply) devices to your network is a critical step for ensuring power reliability and enabling graceful shutdowns of your infrastructure during power events. The decision of which devices should communicate with the UPS depends on the role of each system and the desired level of automation during power outages.

## 1. Network Connectivity for APC UPS Devices

Most modern APC UPS units offer network connectivity primarily through:

*   **Network Management Card (NMC):** This is the most common and recommended method. The NMC is an accessory card (e.g., APC AP9631, AP9641) that slots into the UPS, providing it with its own IP address, web interface, and SNMP capabilities. This allows the UPS to be a network-managed device.
*   **USB/Serial Connection to a Host:** Some smaller UPS units connect directly to a single server via USB or serial cable. Software on that server (e.g., APC PowerChute Personal Edition, Network UPS Tools - NUT) then monitors the UPS and can initiate shutdowns for that specific host. For network-wide graceful shutdowns, this host would then need to communicate with other systems.

**Recommendation:** For a network of bjoin.studio's complexity, an **APC Network Management Card (NMC)** is highly recommended for each UPS. This provides independent network access to the UPS, enabling centralized monitoring and control.

## 2. Configuration for Network Management (via NMC)

Once the NMC is installed and connected to your network (ideally on your management VLAN, e.g., VLAN55, or a dedicated power management VLAN), you'll configure its basic network settings:

*   **IP Address:** Assign a static IP address.
*   **Subnet Mask & Gateway:** Standard network configuration.
*   **DNS Servers:** For name resolution.
*   **SNMP Settings:** Configure SNMP communities (read-only for monitoring, read-write for control, though read-write should be used with extreme caution and strong security). SNMPv3 is preferred for security.
*   **User Accounts:** Set up secure user accounts for web interface access.
*   **Email/SMS Alerts:** Configure the NMC to send notifications for power events (e.g., power failure, low battery, battery test failure).

## 3. Communication with Other Devices: Who Should Talk to the UPS?

The primary goal of UPS-to-server communication is to initiate **graceful shutdowns** of critical systems before the UPS battery is depleted, preventing data corruption and hardware damage.

### **Crucial Communication:**

*   **`pmx-01` (Proxmox Host):** **Absolutely essential.** The Proxmox host needs to be aware of the UPS status to:
    *   **Gracefully shut down all running Virtual Machines (VMs):** This is paramount to prevent data loss in your VMs.
    *   **Gracefully shut down itself:** Once all VMs are down, the Proxmox host itself needs to shut down cleanly.
    *   **How:** Install APC PowerChute Network Shutdown (PCNS) software on the Proxmox host. PCNS communicates with the UPS NMC via the network (SNMP/proprietary protocols) and orchestrates the shutdown sequence. Alternatively, Network UPS Tools (NUT) can be configured on Proxmox to monitor the UPS.

*   **`truenas-01` (TrueNAS Storage):** **Absolutely essential.** Storage systems are highly susceptible to data corruption during abrupt power loss.
    *   **Graceful shutdown:** TrueNAS needs to be informed to shut down its services and unmount its ZFS pools cleanly.
    *   **How:** Install APC PowerChute Network Shutdown (PCNS) or configure Network UPS Tools (NUT) on the TrueNAS system to communicate with the UPS NMC.

### **Beneficial Communication (for Monitoring/Alerting):**

*   **`opnsense-f1` (OPNsense Firewall):**
    *   **Monitoring:** OPNsense can monitor the UPS via SNMP for status (on battery, battery level, load). This can be integrated into your monitoring system (e.g., Grafana via SNMP exporter).
    *   **Shutdown Control:** Less critical for the firewall itself to initiate a shutdown unless it's running as a VM on `pmx-01` (in which case `pmx-01` handles its shutdown). If OPNsense is on dedicated hardware, it typically has its own power management.
    *   **How:** Configure SNMP monitoring on OPNsense to poll the UPS NMC.

*   **`ipa-01` (FreeIPA Server):**
    *   **Monitoring/Alerting:** `ipa-01` can receive SNMP traps from the UPS NMC for critical events (e.g., "on battery," "low battery"). This allows FreeIPA to potentially trigger alerts or integrate with its own monitoring.
    *   **Graceful shutdown:** While `ipa-01` is a critical service, its graceful shutdown is typically handled by the underlying hypervisor (`pmx-01`) if it's a VM, or by PCNS/NUT if it's a physical server directly connected to a UPS. Direct communication with the UPS for shutdown is less common unless it's the *only* server connected to that UPS.
    *   **How:** Configure the UPS NMC to send SNMP traps to `ipa-01`'s IP address.

## 4. Overall Recommendation

Prioritize **graceful shutdown** for your critical systems:

1.  **Install APC PowerChute Network Shutdown (PCNS) or configure Network UPS Tools (NUT) on `pmx-01` and `truenas-01`.** These are the most critical systems that require clean shutdowns to prevent data loss and corruption.
2.  **Place UPS NMCs on a secure management VLAN (e.g., VLAN55).** This isolates their management traffic.
3.  **Integrate UPS monitoring into your central monitoring system (e.g., Grafana via SNMP).** This provides real-time visibility into power status.
4.  **Configure email/SNMP trap alerts** from the UPS NMC to relevant administrators and potentially to `ipa-01` for broader alerting.

This approach ensures that your most vulnerable systems are protected during power outages, and you have comprehensive visibility into your power infrastructure.
