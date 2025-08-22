# Disaster Recovery Plan

## 1. Purpose and Objectives

This document outlines the disaster recovery (DR) plan for the bjoin.studio network. The primary objectives are to:

*   Minimize downtime and data loss in the event of a disaster.
*   Provide a clear and actionable plan for recovering critical network infrastructure.
*   Ensure the safety of all personnel during a disaster.

## 2. Activation Criteria

This DR plan should be activated in the event of any of the following:

*   **Major Hardware Failure:** Failure of a critical network device (e.g., firewall, core switch, Proxmox host) that cannot be resolved through standard troubleshooting.
*   **Natural Disaster:** Fire, flood, earthquake, or other natural disaster that impacts the physical location of the network equipment.
*   **Security Incident:** A major security breach that compromises the integrity of the network.
*   **Power Outage:** A prolonged power outage that exceeds the capacity of the UPS.

## 3. Roles and Responsibilities

*   **DR Lead:** The DR Lead is responsible for declaring a disaster and activating the DR plan. They will coordinate the recovery effort and communicate with stakeholders.
*   **Network Team:** The Network Team is responsible for executing the recovery procedures outlined in this plan and the `backup-and-recovery-plan.md`.
*   **Stakeholders:** All other personnel will be considered stakeholders and will be kept informed of the recovery progress.

## 4. Communication Plan

*   **Initial Notification:** The DR Lead will notify all stakeholders that the DR plan has been activated.
*   **Regular Updates:** The DR Lead will provide regular updates on the recovery progress to all stakeholders.
*   **Communication Channels:** Communication will be conducted via a pre-determined out-of-band channel (e.g., a dedicated Slack channel, a phone tree).

## 5. Recovery Scenarios

### 5.1. Scenario 1: Firewall Failure

1.  **Activate DR Plan:** The DR Lead declares a disaster.
2.  **Procure Replacement Hardware:** Procure a new Protectli Vault or compatible device.
3.  **Restore Configuration:** Follow the OPNsense recovery procedure in the `backup-and-recovery-plan.md`.
4.  **Test Connectivity:** Verify that all VLANs and firewall rules are functioning correctly.

### 5.2. Scenario 2: Proxmox Host Failure

1.  **Activate DR Plan:** The DR Lead declares a disaster.
2.  **Procure Replacement Hardware:** Procure a new server with similar specifications.
3.  **Restore Host:** Follow the Proxmox VE host recovery procedure in the `backup-and-recovery-plan.md`.
4.  **Restore VMs:** Restore critical VMs (starting with FreeIPA) from backup.
5.  **Verify Services:** Verify that all critical services are running.

### 5.3. Scenario 3: Core Switch Failure

1.  **Activate DR Plan:** The DR Lead declares a disaster.
2.  **Procure Replacement Hardware:** Procure a new switch with similar specifications.
3.  **Restore Configuration:** Follow the network switch recovery procedure in the `backup-and-recovery-plan.md`.
4.  **Test Connectivity:** Verify that all VLANs and port configurations are correct.

### 5.4. Scenario 4: Total Site Failure

In the event of a total site failure, the recovery process will be significantly more complex and will require a separate, more detailed plan. This section provides a high-level overview of the steps involved.

1.  **Activate DR Plan:** The DR Lead declares a disaster.
2.  **Secure New Location:** Secure a new physical location for the network equipment.
3.  **Procure New Hardware:** Procure all new network hardware.
4.  **Rebuild Network:** Rebuild the network from scratch, using the documentation in this repository as a guide.
5.  **Restore Data:** Restore all data from off-site backups.

## 6. Plan Maintenance

*   **Review:** This DR plan will be reviewed and updated annually, or after any major change to the network infrastructure.
*   **Testing:** The DR plan will be tested annually by conducting a tabletop exercise of one of the recovery scenarios.
