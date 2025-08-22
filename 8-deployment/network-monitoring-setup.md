# Network Monitoring Setup Guide

This guide describes how to configure your network infrastructure to enable effective monitoring, leveraging dedicated monitoring VLANs (15, 25, 35, 45, 55, 65).

## 1. Purpose of Dedicated Monitoring VLANs

Dedicated monitoring VLANs provide a secure and isolated segment for your monitoring infrastructure. This separation offers several benefits:

*   **Security:** Monitoring traffic and tools are isolated from production networks, reducing the attack surface.
*   **Performance:** Monitoring traffic (especially mirrored traffic) does not contend with production data on core network segments.
*   **Isolation:** Monitoring tools can operate without impacting critical services.

## 2. VLAN Configuration on Network Devices

Ensure that VLANs 15, 25, 35, 45, 55, and 65 are configured on your core switches and firewall (OPNsense). These VLANs should be treated as highly restricted segments.

*   **VLAN 15:** Production Monitoring (e.g., `PROD_MON`)
*   **VLAN 25:** Stage Monitoring (e.g., `STAGE_MON`)
*   **VLAN 35:** Studio Monitoring (e.g., `STUDIO_MON`)
*   **VLAN 45:** Workshop Monitoring (e.g., `WORKSHOP_MON`)
*   **VLAN 55:** Management Monitoring (e.g., `MGMT_MON`)
*   **VLAN 65:** Guest Monitoring (e.g., `GUEST_MON`)

Your monitoring servers (e.g., Prometheus, Grafana, ELK stack components) should reside in one or more of these monitoring VLANs, typically `VLAN 55` (Management Monitoring) if you have a centralized monitoring solution.

## 3. Traffic Mirroring (SPAN/Port Mirroring)

To capture traffic for analysis, you will configure your managed switches to mirror traffic from production VLANs or specific ports to a port connected to your monitoring infrastructure.

*   **Concept:** A SPAN (Switched Port Analyzer) or Port Mirroring feature duplicates network packets from source ports/VLANs and sends them to a destination (monitor) port.
*   **Configuration:** On your Cisco Nexus or Netgear switches, you will define a monitoring session:
    *   **Source:** Specify the VLANs (e.g., VLAN 11, 21, 31, etc.) or specific ports you want to monitor.
    *   **Destination:** A dedicated port on the switch connected to a network interface on your monitoring server. This port should be configured as an **access port** for the relevant monitoring VLAN (e.g., VLAN 15 for production traffic, or VLAN 55 for centralized monitoring).

**Example (Conceptual Cisco Nexus CLI):
**
```cli
monitor session 1 type ethernet
  source interface ethernet 1/1 - 1/8
  source vlan 11,21,31 rx
  destination interface ethernet 1/24
  no shut
```

## 4. Flow-Based Monitoring (NetFlow/sFlow)

For high-level traffic analysis and identifying top talkers or unusual patterns, configure your switches to export flow data.

*   **NetFlow (Cisco) / sFlow (Multi-vendor):** These protocols collect metadata about network conversations (who talked to whom, when, how much data) and send it to a flow collector (e.g., Elastic Flow, ntopng).
*   **Configuration:** Enable NetFlow/sFlow on your switch interfaces and direct the exports to the IP address of your flow collector, which should be located in a monitoring VLAN.

## 5. Device Health and Performance (SNMP)

Enable SNMP (Simple Network Management Protocol) on all your network devices (switches, firewall, servers, NAS) to collect health metrics, interface statistics, and device status.

*   **SNMP Version:** Prefer SNMPv3 for security, or SNMPv2c with strong community strings.
*   **Configuration:** Configure SNMP agents on devices to send traps/data to your Network Management System (NMS) or monitoring server, typically located in a monitoring VLAN.
*   **Firewall Rules:** Ensure your firewall allows SNMP traffic (UDP 161/162) from your devices to your monitoring server.

## 6. Centralized Monitoring Tools

Your monitoring servers will collect and visualize data from the various sources:

*   **Packet Capture/Analysis:** Tools like Wireshark (for ad-hoc analysis) or dedicated network performance monitoring (NPM) solutions (for continuous capture on SPAN ports).
*   **Metrics Collection:** Prometheus, Telegraf, Zabbix, Nagios for collecting SNMP data, system metrics, and application performance.
*   **Log Management:** ELK Stack (Elasticsearch, Logstash, Kibana) or Graylog for centralizing and analyzing logs from all network devices and servers.
*   **Visualization:** Grafana for creating dashboards to visualize network health, traffic patterns, and device performance.

## 7. Security Considerations for Monitoring VLANs

*   **Strict Firewall Rules:** Implement very strict firewall rules on OPNsense to control access to and from monitoring VLANs. Only allow necessary traffic (e.g., SNMP from devices to collector, SSH to monitoring servers).
*   **No Internet Access:** Monitoring VLANs should generally not have direct internet access.
*   **Dedicated Devices:** Use dedicated monitoring servers and network interfaces for capturing mirrored traffic to prevent interference with production services.
