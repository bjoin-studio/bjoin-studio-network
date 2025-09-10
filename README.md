# Bjoin Studio Network

This repository contains the documentation, configuration, and automation for the bjoin.studio network.

## How to Use This Repository

This repository is designed to be a living document that can be used by both technical and non-technical people to understand and recreate the bjoin.studio network.

The repository is organized into the following sections:

**01. Overview:** Start here for a high-level overview of the project.

**02. Inventory:** A list of all the hardware used in the network.

**03. Research:** Explanations of key concepts and considerations for the network design.

**04. Insights:** Interesting findings and ideas related to the network.

**05. Plans:** Documents related to network planning and future development.

**07. Physical Layout:** Diagrams and guides for the physical setup of the network.

**06. Configuration:** The nitty-gritty details of the network configuration, including VLANs, IP addresses, and device settings.

**08. Deployment:** Step-by-step guides for setting up and configuring the network devices.

**09. Maintenance:** How to keep the network running smoothly, including backup and disaster recovery plans.

**10. Future Plans:** The roadmap for the future of the network.

**11. References:** Links to external resources.

**12. Appendix:** Additional information, such as naming conventions and security policies.

## Table of Contents

### 1. Overview
*   [README.md](1-overview/README.md)
*   [Network Physical Connections Overview](1-overview/overview-network-physical-connections.md)
*   [Network Data Paths Overview](1-overview/overview-network-data-paths.md)

### 2. Inventory
*   [Overall Inventory](02-inventory/inventory.md)
*   [Network Switches Inventory](02-inventory/inventory-switches.md)
*   [Server Inventory](02-inventory/inventory-servers.md)
*   [Software Inventory](02-inventory/inventory-software.md)
*   [Storage Inventory](02-inventory/inventory-storage.md)

### 3. Learning
*   [Key Concepts](3-learning/key-concepts.md)
*   [Network Device Role Optimization](3-learning/network-device-role-optimization.md)

### 4. Insights
*   [FreeIPA and ZFS Insights](4-insights/freeipa-and-zfs-insights.md)
*   [FreeIPA Groups Ideas](4-insights/freeipa-groups-ideas.md)
*   [Network Design Considerations](4-insights/network-design-considerations.md)
*   [Repository Insights](4-insights/repository-insights.md)

### 7. Physical Layout
*   [Data Flow Diagrams](5-physical-layout/data-flow-diagrams.md)
*   [Logical Diagram](5-physical-layout/logical-diagram.md)
*   [Physical Cabling Guide](5-physical-layout/physical-c cabling-guide.md)
*   [Physical Diagram](5-physical-layout/physical-diagram.md)

### 6. Configuration
*   [Network Design](6-configuration/bjoin-studio-network-design.md)
*   [Netgear GS108Ev4 Port Config](6-configuration/netgear-gs108ev4-port-config.md)
*   [IP Address Management](6-configuration/ip-address-management.md)
*   [Ansible](6-configuration/ansible)
*   [Device Configurations](6-configuration/cfg)

### 5. Plans
*   [Network Plan](05-plans/plan-network.md)
*   [VLAN Testing Procedure](05-plans/vlan-testing-procedure.md)

### 8. Operational
*   [Proxmox Bridge STP Configuration](docs/operational/runbooks/proxmox-bridge-stp-configuration.md)

### 9. Deployment
*   [Bootstrapping Managed Switch Guide](8-deployment/bootstrapping-managed-switch-guide.md)
*   [Cisco Nexus 9236c Initial Setup](8-deployment/cisco-nexus-9236c-initial-setup.md)
*   [Firewall Firmware Updates](8-deployment/firewall-firmware-updates.md)
*   [FreeIPA Server Setup Guide](8-deployment/freeipa-server-setup-guide.md)
*   [FreeIPA User Group Management](8-deployment/freeipa-user-group-management.md)
*   [Monitoring VM Setup Proxmox](8-deployment/monitoring-vm-setup-proxmox.md)
*   [Netgear GS108Ev4 Manual VLAN Config](8-deployment/netgear-gs108ev4-manual-vlan-config.md)
*   [Netgear GS108Ev4 Switch VLAN Configuration](8-deployment/netgear-gs108ev4-switch-vlan-configuration.md)
*   [Network Monitoring Setup](8-deployment/network-monitoring-setup.md)
*   [Network Physical Logical Connections](8-deployment/network-physical-logical-connections.md)
*   [OPNsense Initial Setup Guide](8-deployment/opnsense-initial-setup-guide.md)
*   [OPNsense VLAN Config 1x Production](8-deployment/opnsense-vlan-config-1x-production.md)
*   [OPNsense VLAN Config 2x Stage](8-deployment/opnsense-vlan-config-2x-stage.md)
*   [OPNsense VLAN Config 3x Studio](8-deployment/opnsense-vlan-config-3x-studio.md)
*   [OPNsense VLAN Config 4x Workshop](8-deployment/opnsense-vlan-config-4x-workshop.md)
*   [OPNsense VLAN Config 5x Management](8-deployment/opnsense-vlan-config-5x-management.md)
*   [OPNsense VLAN Config 6x Guest](8-deployment/opnsense-vlan-config-6x-guest.md)
*   [Proxmox Host Backup](8-deployment/proxmox-host-backup.md)
*   [Proxmox Host Setup Guide](8-deployment/proxmox-host-setup-guide.md)
*   [Server Onboarding](8-deployment/server-onboarding.md)
*   [Sodola Switch VLAN Configuration](8-deployment/sodola-switch-vlan-configuration.md)

### 10. Maintenance
*   [Backup and Recovery Plan](9-maintenance/backup-and-recovery-plan.md)
*   [Disaster Recovery Plan](9-maintenance/disaster-recovery-plan.md)
*   [Change Management Log](9-maintenance/change-management-log.md)
*   [Incident Response Plan](9-maintenance/incident-response-plan.md)
*   [Vulnerability Management Plan](9-maintenance/vulnerability-management-plan.md)

### 11. Future Plans
*   [Roadmap](10-future-plans/roadmap.md)

### 12. References
*   [References](11-references/references.md)

### 13. Appendix
*   [GEMINI.md](12-appendix/GEMINI.md)
*   [Asset Management](12-appendix/asset-management.md)
*   [Host Naming Conventions](12-appendix/host-naming-conventions.md)
*   [Acceptable Use Policy](12-appendix/acceptable-use-policy.md)
*   [Firewall Rule Policy](12-appendix/firewall-rule-policy.md)
*   [VPN Access Policy](12-appendix/vpn-access-policy.md)
