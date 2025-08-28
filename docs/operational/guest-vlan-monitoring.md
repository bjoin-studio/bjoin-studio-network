# Guest VLAN Monitoring and Security Runbook

This document outlines key monitoring considerations and security requirements for guest VLANs, specifically focusing on VLAN61 (1Gb passwordless Ethernet LAN) and VLAN64 (passwordless guest WiFi). VLAN65 will serve as the dedicated monitoring VLAN for these guest networks.

## 1. Monitoring Information for Guest VLANs (VLAN61 & VLAN64)

Effective monitoring of guest networks focuses on performance, security, and availability.

### 1.1. Network Performance & Usage

*   **Bandwidth Utilization:**
    *   **Metrics:** Ingress and egress traffic (bits/bytes per second) on interfaces connected to guest VLANs (e.g., firewall interfaces, switch ports, wireless access point SSIDs).
    *   **Tools:** SNMP polling (via VLAN65) of network devices, NetFlow/sFlow analysis if supported.
    *   **Purpose:** Identify peak usage times, potential bottlenecks, and ensure adequate capacity.
*   **Throughput:** Actual data transfer rates to/from the internet.
*   **Number of Connected Devices:**
    *   **Metrics:** Count of active DHCP leases, number of associated wireless clients.
    *   **Tools:** DHCP server logs, wireless access point statistics.
    *   **Purpose:** Understand network load and user density.
*   **DHCP Lease Statistics:**
    *   **Metrics:** Number of active leases, lease duration, lease pool exhaustion, DHCP server errors.
    *   **Tools:** DHCP server logs and statistics.
    *   **Purpose:** Ensure smooth client onboarding and troubleshoot connectivity issues.
*   **DNS Query Volume:**
    *   **Metrics:** Number of DNS requests originating from guest VLANs.
    *   **Tools:** DNS server logs (e.g., Unbound on OPNsense).
    *   **Purpose:** Identify unusual DNS activity or potential malware.

### 1.2. Security & Compliance

*   **Firewall Deny Logs:**
    *   **Metrics:** Count and details of denied connections from guest VLANs to internal network segments.
    *   **Tools:** OPNsense firewall logs (syslog to a central logging server on VLAN65).
    *   **Purpose:** **CRITICAL** for detecting unauthorized access attempts to the internal network. Alerts should be configured for these events.
*   **Intrusion Detection/Prevention System (IDS/IPS) Alerts:**
    *   **Metrics:** Alerts triggered by suspicious patterns or known threats.
    *   **Tools:** Suricata/Snort logs on OPNsense.
    *   **Purpose:** Proactive threat detection.
*   **Unusual Traffic Patterns:**
    *   **Metrics:** High connection counts to unusual ports, unexpected protocols, excessive broadcast traffic.
    *   **Tools:** NetFlow/sFlow analysis, deep packet inspection (if enabled).
    *   **Purpose:** Identify potential compromises or misconfigurations.

### 1.3. Availability & Health

*   **Internet Reachability:**
    *   **Metrics:** Success rate and latency of pings/HTTP requests to external internet targets (e.g., 8.8.8.8, google.com) from a host on a guest VLAN (or simulated from VLAN65).
    *   **Tools:** Monitoring agents (e.g., Prometheus Blackbox Exporter), synthetic transactions.
    *   **Purpose:** Ensure guests can access the internet.
*   **AP/Switch Uptime & Health:**
    *   **Metrics:** Device uptime, CPU/memory utilization, interface status (up/down).
    *   **Tools:** SNMP polling (via VLAN65) of network devices.
    *   **Purpose:** Ensure the underlying infrastructure is stable.
*   **Error Rates:**
    *   **Metrics:** Interface errors, packet discards, CRC errors on switch ports and APs.
    *   **Tools:** SNMP polling.
    *   **Purpose:** Identify physical layer issues or misconfigurations.

## 2. Security Requirements and Firewall Rules

The primary security requirement for VLAN61 and VLAN64 is strict isolation from the internal network while providing full internet access.

### 2.1. Core Principles

*   **Deny by Default:** All traffic from guest VLANs to internal networks must be explicitly denied. Only traffic explicitly allowed (e.g., DNS, DHCP, Internet access) should pass.
*   **No Inbound from Internal:** Internal networks should not be able to initiate connections to guest VLANs.
*   **Internet Only:** Guest VLANs should only be able to reach the internet.

### 2.2. OPNsense Firewall Rules (Example)

Assuming OPNsense is handling inter-VLAN routing and firewalling:

**Interface Rules for Guest VLANs (e.g., on VLAN61 and VLAN64 interfaces):**

1.  **Allow DHCP:**
    *   **Action:** Pass
    *   **Interface:** Guest VLAN (e.g., VLAN61, VLAN64)
    *   **Protocol:** UDP
    *   **Source:** Guest VLAN net
    *   **Source Port:** Any
    *   **Destination:** Any
    *   **Destination Port:** DHCP (67, 68)
    *   **Purpose:** Allow clients to obtain IP addresses.

2.  **Allow DNS:**
    *   **Action:** Pass
    *   **Interface:** Guest VLAN (e.g., VLAN61, VLAN64)
    *   **Protocol:** TCP/UDP
    *   **Source:** Guest VLAN net
    *   **Source Port:** Any
    *   **Destination:** DNS Server IP (e.g., OPNsense LAN IP, or external DNS like 8.8.8.8)
    *   **Destination Port:** DNS (53)
    *   **Purpose:** Allow DNS resolution.

3.  **Allow Internet Access:**
    *   **Action:** Pass
    *   **Interface:** Guest VLAN (e.g., VLAN61, VLAN64)
    *   **Protocol:** Any
    *   **Source:** Guest VLAN net
    *   **Source Port:** Any
    *   **Destination:** WAN net (or "any" if NAT is configured correctly)
    *   **Destination Port:** Any
    *   **Purpose:** Allow all outbound internet traffic. This rule should be placed *after* any explicit deny rules for internal networks.

4.  **Deny Access to Internal Networks:**
    *   **Action:** Block/Reject (Block is preferred for silent drop, Reject sends an ICMP unreachable)
    *   **Interface:** Guest VLAN (e.g., VLAN61, VLAN64)
    *   **Protocol:** Any
    *   **Source:** Guest VLAN net
    *   **Source Port:** Any
    *   **Destination:** Internal Network Aliases (e.g., LAN net, Production VLAN net, Management VLAN net, VLAN65 net)
    *   **Destination Port:** Any
    *   **Purpose:** **CRITICAL** to prevent guest networks from accessing internal resources. Create aliases for all internal subnets and use them here. This rule must be placed *before* the "Allow Internet Access" rule.

**Floating Rules (Optional, for global application):**

*   Consider using floating rules for "Deny Access to Internal Networks" if you have many guest-like VLANs and want to apply the same denial policy globally. Ensure proper rule order and interface selection.

## 3. Monitoring VLAN (VLAN65) Considerations

VLAN65 should be a secure, isolated network for your monitoring infrastructure (e.g., Prometheus, Grafana, syslog server, SNMP trap receiver).

*   **Access:** Only allow necessary management access to devices on VLAN65.
*   **SNMP Polling:** Configure network devices (switches, APs, OPNsense) to allow SNMP polling from the IP address(es) of your monitoring server(s) on VLAN65.
*   **Syslog:** Configure devices to send syslog messages to a syslog server on VLAN65.
*   **Time Synchronization:** Ensure all devices and monitoring servers are synchronized to an NTP server.
