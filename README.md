# Bjoin Studio Network

This document is designed to help you understand the bjoin.studio network designed for the creative photography studio of Bjoin Films. This repository contains comprehensive details about the design, construction and maintainmaintenanceof this infrastructure.

## What You'll Find Here

This network uses enterprise-grade security with Linux-based systems, centralized identity management, and segmented VLANs for different work areas. Whether you're learning networking concepts or building your own studio network, this documentation provides both educational content and practical implementation guides.

## Choose Your Path

### 🎯 **New to Networking?** → [Start with Fundamentals](3-learning/)
Learn the core concepts behind modern network design, including VLANs, firewalls, and identity management. No prior experience required.

- [Key Network Concepts](3-learning/key-concepts.md) - Essential concepts explained simply
- [Network Design Philosophy](4-insights/network-design-considerations.md) - Why we made these choices

### 🛠️ **Ready to Build?** → [Implementation Guides](8-deployment/)
Step-by-step instructions for setting up each component. Start with the basics and work your way up.

**Essential Setup (in order):**
1. [Firewall Setup](8-deployment/opnsense-initial-setup-guide.md) - Your network's security foundation
2. [Identity Server Setup](8-deployment/freeipa-server-setup-guide.md) - Centralized user management
3. [Switch Configuration](8-deployment/netgear-gs108ev4-switch-vlan-configuration.md) - Network segmentation
4. [Monitoring Setup](8-deployment/network-monitoring-setup.md) - Keep an eye on everything

### 🔧 **Managing an Existing Network?** → [Operations](9-maintenance/)
Daily tasks, troubleshooting, and maintenance procedures for keeping things running smoothly.

### 📋 **Need Specific Info?** → [Reference Materials](#reference-materials)
Quick access to configurations, equipment lists, and technical details.

---

## Network Overview

This network serves different work areas through isolated VLANs:
- **Production** - Critical creative workstations and render systems
- **Studio** - General creative work and collaboration spaces  
- **Management** - Servers, storage, and infrastructure systems
- **Workshop** - Development, testing, and experimental work
- **Guest** - Visitor access with restricted permissions

All systems use centralized authentication through FreeIPA, providing single sign-on and consistent security policies across the entire network.

## Quick Reference

### Essential Documents
- [Equipment List](2-equipment-list/equipment-list.md) - What hardware you'll need
- [Network Diagrams](5-physical-layout/) - Visual overview of connections
- [IP Address Plan](6-configuration/ip-address-management.md) - How addresses are organized

### Common Tasks
- [Adding New Users](8-deployment/freeipa-user-group-management.md)
- [Configuring New Devices](8-deployment/server-onboarding.md)
- [Backup Procedures](9-maintenance/backup-and-recovery-plan.md)

## Reference Materials

<details>
<summary>📚 Learning Resources</summary>

- [Key Concepts](3-learning/key-concepts.md)
- [Device Optimization](3-learning/network-device-role-optimization.md)
- [Design Insights](4-insights/)
- [ZFS and FreeIPA Best Practices](4-insights/freeipa-and-zfs-insights.md)

</details>

<details>
<summary>🔧 Implementation Guides</summary>

**Core Infrastructure:**
- [Firewall Configuration](8-deployment/opnsense-initial-setup-guide.md)
- [Identity Management](8-deployment/freeipa-server-setup-guide.md)
- [Virtualization Platform](8-deployment/proxmox-host-setup-guide.md)
- [Storage System](8-deployment/truenas-server-setup-guide.md)

**Network Devices:**
- [Cisco Switch Setup](8-deployment/cisco-nexus-9236c-initial-setup.md)
- [Managed Switch Config](8-deployment/netgear-gs108ev4-switch-vlan-configuration.md)

**Monitoring & Management:**
- [Network Monitoring](8-deployment/network-monitoring-setup.md)
- [Grafana Dashboard](8-deployment/grafana-docker-setup.md)

</details>

<details>
<summary>⚙️ Configuration Files</summary>

- [Device Configurations](6-configuration/cfg/)
- [Ansible Automation](6-configuration/ansible/)
- [Prometheus Monitoring](6-configuration/prometheus/)

</details>

<details>
<summary>📋 Policies & Procedures</summary>

- [Security Policies](12-appendix/firewall-rule-policy.md)
- [Naming Conventions](12-appendix/host-naming-conventions.md)
- [Incident Response](9-maintenance/incident-response-plan.md)
- [Disaster Recovery](9-maintenance/disaster-recovery-plan.md)

</details>

## Getting Help

- Check the [troubleshooting guides](9-maintenance/) for common issues
- Review [change logs](9-maintenance/change-management-log.md) for recent modifications
- Consult [reference materials](11-references/references.md) for external documentation

## Contributing

This documentation is designed to evolve. If you find errors, have improvements, or want to add your own insights, contributions are welcome.