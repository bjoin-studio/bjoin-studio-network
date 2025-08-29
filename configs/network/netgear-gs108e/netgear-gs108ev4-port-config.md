# Netgear GS108Ev4 Switch Port Configuration Design

This document outlines the intended port configuration for the Netgear GS108Ev4 managed switch. This design aims to support the defined VLAN segmentation and connect various network devices appropriately.

## 1. Switch Overview

*   **Model:** Netgear GS108Ev4 (8-Port Gigabit Smart Managed Plus Switch)
*   **Location:** (To be specified, e.g., Studio Rack)
*   **Purpose:** Edge switch for connecting workstations, servers, and other devices to the network, providing VLAN segmentation at the access layer.

## 2. Port Configuration Table

| Port | Type    | PVID | Egress VLAN(s) (Tagged) | Ingress Filtering | Description                                     | Connected Device (Example) |
| :--- | :------ | :--- | :---------------------- | :---------------- | :---------------------------------------------- | :------------------------- |
| **1**| Access  | 11   | -                       | Enabled           | Production Workstation Access                   | Workstation 1              |
| **2**| Access  | 21   | -                       | Enabled           | Stage Device Access                             | Stage Device 1             |
| **3**| Access  | 31   | -                       | Enabled           | Studio Workstation Access                       | Workstation 2              |
| **4**| Access  | 41   | -                       | Enabled           | Workshop Device Access                          | Workshop Device 1          |
| **5**| Access  | 51   | -                       | Enabled           | Uplink to Netgear GS105 (Unmanaged)             | Netgear GS105              |
| **6**| Access  | 61   | -                       | Enabled           | Guest Device Access                             | Guest Device 1             |
| **7**| Access  | 1    | -                       | Enabled           | Default VLAN Access                             | Unassigned / Default       |
| **8**| Trunk   | 1    | 11-15,21-25,31-35,41-45,51-55,61-65 | Enabled           | Uplink to Sodola Switch                         | Sodola Switch              |

### Notes:

*   **PVID (Port VLAN ID):** For an access port, the PVID determines which VLAN the port belongs to. Untagged traffic arriving on this port will be assigned to this VLAN.
*   **Trunk Ports:** Ports configured as Trunk will carry tagged traffic for all specified VLANs. The connected device must be VLAN-aware and configured to handle these tags.
*   **Access Ports:** Ports configured as Access will carry untagged traffic for a single specified VLAN. The connected device does not need to be VLAN-aware.
*   **Ingress Filtering:** This should be enabled on all ports to ensure that only traffic belonging to the allowed VLANs is accepted.
*   **VLAN IDs:** For the full VLAN list, see the `bjoin-studio-network-design.md` document.

## 3. Configuration Strategy

Due to the limitations of the Netgear GS108Ev4 (v1.0.1.3 firmware) which does not provide a command-line interface (CLI) for configuration, all settings for this switch must be applied manually via its web-based graphical user interface (GUI).

This document serves as the blueprint for the desired configuration. A separate runbook (`docs/operational/runbooks/netgear-gs108ev4-manual-vlan-config.md`) will provide step-by-step instructions for applying these settings.

The configuration tasks involve:

*   **VLAN Creation:** Ensuring all necessary VLANs are created on the switch.
*   **Port Configuration:** Setting each port to its designated type (Access/Trunk) and assigning the correct VLANs, including PVID and egress/ingress settings.
*   **Saving Configuration:** Persisting the configuration to the switch's startup configuration.