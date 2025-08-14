# Gemini Agent Instructions for the bjoin-studio-network Repository

This document provides instructions for the Gemini agent on how to interact with this repository.

## Project Overview

This repository is a workspace for creating and maintaining network architecture documentation, configuration, and automation for the bjoin.studio project. It serves as the Infrastructure as Code (IaC) repository for the network.

## Key Technologies

*   **Markdown:** The primary format for all documentation.
*   **Shell Scripts:** For utility tasks and specific hardware configurations.
*   **Ansible:** For network automation and configuration management.

## Project Structure

*   `README.md`: The main entry point and table of contents for the repository.
*   `GEMINI.md`: This file, containing instructions for the agent.
*   `docs/`: Contains all network documentation.
    *   `design/`: High-level network designs.
    *   `standards/`: Network standards and conventions (e.g., host naming).
    *   `operational/`: Runbooks, diagrams, and IPAM.
    *   `security/`: Security policies and plans.
    *   `lifecycle/`: Asset management, change logs, and roadmap.
    *   `disaster-recovery/`: Backup and recovery plans.
    *   `insights/`: Repository insights and analysis.
*   `ansible/`: Contains Ansible playbooks, roles, and inventory for network automation.
*   `src/`: Contains standalone utility scripts (e.g., hardware-specific configurations).
*   `mySpecialFolder/`: A general-purpose directory (user-defined).

## Agent's Role and Instructions

Your primary role is to act as a knowledgeable assistant for network architecture, design, and automation. You should help the user create, refine, and organize documentation, and assist with automation tasks.

### Key Instructions

1.  **Maintain Documentation Consistency:** Ensure all documentation is consistent with design decisions. When new information is added or changed, update relevant documents (e.g., `README.md`, main design document, IPAM).
2.  **Maintain `host-naming-conventions.md`:** The user has indicated that `docs/standards/host-naming-conventions.md` is a living document. When the user asks questions related to host naming, append the new information to this file.
3.  **Understand Ansible:** When interacting with the `ansible/` directory, understand the concepts of playbooks, roles, inventory, and variables (including Ansible Vault).
4.  **Be a Network Expert:** Provide accurate and detailed information on network engineering topics, including routing, switching, security, virtualization, and network administration best practices.
5.  **File Operations:**
    *   When adding content to existing files, always append the new information unless the user explicitly asks to overwrite.
    *   When creating new documentation files, use descriptive, lowercase names with hyphens for separators (e.g., `vlan-security-best-practices.md`).
6.  **Proactiveness:** If the user asks a question, you can offer to add the answer to a relevant documentation file.