# Netgear GS108Ev4 Switch Port Configuration Design

This document outlines the intended port configuration for the Netgear GS108Ev4 managed switch. This design aims to support the defined VLAN segmentation and connect various network devices appropriately.

## 1. Switch Overview

*   **Model:** Netgear GS108Ev4 (8-Port Gigabit Smart Managed Plus Switch)
*   **Location:** (To be specified, e.g., Studio Rack)
*   **Purpose:** Edge switch for connecting workstations, servers, and other devices to the network, providing VLAN segmentation at the access layer.

## 2. Port Configuration Table

| Port | Type    | VLAN(s) | Description                                     | Connected Device (Example) |
| :--- | :------ | :------ | :---------------------------------------------- | :------------------------- |
| **1**| Access  | 11      | Production Workstation Access                   | Workstation 1              |
| **2**| Access  | 21      | Stage Device Access                             | Stage Device 1             |
| **3**| Access  | 31      | Studio Workstation Access                       | Workstation 2              |
| **4**| Access  | 41      | Workshop Device Access                          | Workshop Device 1          |
| **5**| Access  | 51      | Management Device Access                        | Management Laptop / IPMI   |
| **6**| Access  | 61      | Guest Device Access                             | Guest Device 1             |
| **7**| Access  | 1       | Default VLAN Access                             | Unassigned / Default       |
| **8**| Trunk   | 1,11,21,31,41,51,61 | Uplink to Core Switch / Sodola / Proxmox Host | Sodola Switch / pmx-01     |

### Notes:

*   **Trunk Ports:** Ports configured as Trunk will carry tagged traffic for all specified VLANs. The connected device must be VLAN-aware and configured to handle these tags.
*   **Access Ports:** Ports configured as Access will carry untagged traffic for a single specified VLAN. The connected device does not need to be VLAN-aware.
*   **VLAN IDs:**
    *   **1:** Default
    *   **11:** PRODUCTION
    *   **21:** STAGE
    *   **31:** STUDIO
    *   **41:** WORKSHOP
    *   **51:** MANAGEMENT
    *   **61:** GUEST

## 3. Configuration Strategy

Due to the limitations of the Netgear GS108Ev4 (v1.0.1.3 firmware) which does not provide a command-line interface (CLI) for configuration, all settings for this switch must be applied manually via its web-based graphical user interface (GUI).

This document serves as the blueprint for the desired configuration. A separate runbook (`docs/operational/runbooks/netgear-gs108ev4-manual-vlan-config.md`) will provide step-by-step instructions for applying these settings.

The configuration tasks involve:

*   **VLAN Creation:** Ensuring all necessary VLANs (1, 11, 21, 31, 41, 51, 61) are created on the switch.
*   **Port Configuration:** Setting each port to its designated type (Access/Trunk) and assigning the correct VLANs.
*   **Saving Configuration:** Persisting the configuration to the switch's startup configuration.
