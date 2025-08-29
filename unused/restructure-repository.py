#!/usr/bin/env python3

"""
Repository Restructuring Script for bjoin-studio-network
This script uses git mv to reorganize the repository structure
"""

import os
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple

class RepoRestructurer:
    def __init__(self):
        self.repo_root = Path.cwd()
        self.moves_completed = []
        self.moves_failed = []
        self.dirs_created = []
        
    def run_git_command(self, command: List[str]) -> bool:
        """Execute a git command and return success status"""
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"Git command failed: {' '.join(command)}")
            print(f"Error: {e.stderr.strip()}")
            return False
    
    def create_directory(self, path: str) -> bool:
        """Create directory structure"""
        dir_path = self.repo_root / path
        try:
            dir_path.mkdir(parents=True, exist_ok=True)
            self.dirs_created.append(path)
            return True
        except Exception as e:
            print(f"Failed to create directory {path}: {e}")
            return False
    
    def git_mv(self, source: str, destination: str) -> bool:
        """Move file/directory using git mv"""
        source_path = self.repo_root / source
        dest_path = self.repo_root / destination
        
        # Check if source exists
        if not source_path.exists():
            print(f"Source doesn't exist: {source}")
            self.moves_failed.append((source, destination, "Source not found"))
            return False
        
        # Ensure destination directory exists
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Perform git mv
        if self.run_git_command(["git", "mv", source, destination]):
            print(f"✓ Moved: {source} → {destination}")
            self.moves_completed.append((source, destination))
            return True
        else:
            self.moves_failed.append((source, destination, "Git mv failed"))
            return False
    
    def fs_mv(self, source: str, destination: str) -> bool:
        """Move file/directory using file system mv (os.rename)"""
        source_path = self.repo_root / source
        dest_path = self.repo_root / destination

        if not source_path.exists():
            print(f"Source doesn't exist for fs_mv: {source}")
            self.moves_failed.append((source, destination, "Source not found for fs_mv"))
            return False

        dest_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            os.rename(source_path, dest_path)
            print(f"✓ File System Moved: {source} → {destination}")
            self.moves_completed.append((source, destination))
            return True
        except OSError as e:
            print(f"File system move failed: {source} → {destination}")
            print(f"Error: {e}")
            self.moves_failed.append((source, destination, f"FS mv failed: {e}"))
            return False

    def create_directory_structure(self):
        """Create the new directory structure"""
        print("Creating new directory structure...")
        
        directories = [
            "docs/design",
            "docs/equipment", 
            "docs/guides/deployment/initial-setup",
            "docs/guides/deployment/network-configuration",
            "docs/guides/deployment/services",
            "docs/guides/operations",
            "docs/guides/security",
            "docs/reference",
            "configs/network/cisco-nexus/archived",
            "configs/network/netgear-gs108e/current",
            "configs/network/sodola/archived", 
            "configs/network/opnsense/current",
            "configs/network/opnsense/archived",
            "configs/servers/proxmox",
            "configs/servers/truenas",
            "configs/servers/freeipa",
            "configs/monitoring",
            "configs/templates",
            "automation/ansible/inventories/production",
            "automation/ansible/inventories/staging",
            "automation/ansible/group_vars",
            "automation/ansible/host_vars",
            "automation/ansible/roles",
            "automation/ansible/playbooks",
            "automation/scripts/system-info",
            "automation/scripts/backup",
            "automation/scripts/maintenance",
            "inventory",
            "logs/installation",
            "logs/changes", 
            "logs/incidents",
            "plans",
            "temp/scratch"
        ]
        
        for directory in directories:
            self.create_directory(directory)
    
    def move_documentation(self):
        """Move documentation files"""
        print("\nMoving documentation files...")
        
        moves = [
            # Design documents
            ("1-overview/bjoin-studio-network-design.md", "docs/design/overview.md"),
            ("4-insights/network-design-considerations.md", "docs/design/network-design-considerations.md"),
            ("5-physical-layout/physical-diagram.md", "docs/design/physical-diagram.md"),
            ("5-physical-layout/logical-diagram.md", "docs/design/logical-diagram.md"),
            ("5-physical-layout/physical-cabling-guide.md", "docs/design/physical-cabling-guide.md"),
            ("5-physical-layout/data-flow-diagrams.md", "docs/design/data-flow-diagrams.md"),
            
            # Equipment documentation
            ("2-equipment-list/equipment-list.md", "docs/equipment/equipment-list.md"), 
            ("3-learning/network-device-role-optimization.md", "docs/equipment/network-device-optimization.md"),
            
            # Reference documentation
            ("3-learning/key-concepts.md", "docs/reference/key-concepts.md"),
            ("12-appendix/host-naming-conventions.md", "docs/reference/naming-conventions.md"),
            ("6-configuration/ip-address-management.md", "docs/reference/ip-addressing.md"),
            ("11-references/references.md", "docs/reference/external-references.md"),
            
            # Security documentation
            ("12-appendix/firewall-rule-policy.md", "docs/guides/security/firewall-policies.md"),
            ("12-appendix/security/credential-management-best-practices.md", "docs/guides/security/credential-management.md"),
            ("12-appendix/vpn-access-policy.md", "docs/guides/security/vpn-access.md"),
            ("12-appendix/acceptable-use-policy.md", "docs/guides/security/acceptable-use.md"),
        ]
        
        for source, dest in moves:
            self.git_mv(source, dest)
    
    def move_deployment_guides(self):
        """Move deployment guides"""
        print("\nMoving deployment guides...")
        
        # Initial setup guides
        initial_setup_moves = [
            ("8-deployment/cisco-nexus-9236c-initial-setup.md", "docs/guides/deployment/initial-setup/cisco-nexus-setup.md"),
            ("8-deployment/opnsense-initial-setup-guide.md", "docs/guides/deployment/initial-setup/opnsense-setup.md"),
            ("8-deployment/proxmox-host-setup-guide.md", "docs/guides/deployment/initial-setup/proxmox-setup.md"),
            ("8-deployment/truenas-server-setup-guide.md", "docs/guides/deployment/initial-setup/truenas-setup.md"),
            ("8-deployment/bootstrapping-managed-switch-guide.md", "docs/guides/deployment/initial-setup/bootstrapping-managed-switch-guide.md"), # Added
        ]
        
        for source, dest in initial_setup_moves:
            self.git_mv(source, dest)
        
        # Network configuration guides - use glob patterns
        network_config_files = [
            "opnsense-vlan-config-1x-production.md",
            "opnsense-vlan-config-2x-stage.md", 
            "opnsense-vlan-config-3x-studio.md",
            "opnsense-vlan-config-4x-workshop.md",
            "opnsense-vlan-config-5x-management.md",
            "opnsense-vlan-config-6x-guest.md",
            "netgear-gs108ev4-manual-vlan-config.md",
            "netgear-gs108ev4-switch-vlan-configuration.md",
            "sodola-switch-vlan-configuration.md",
            "vlan-and-snmp-monitoring-guide.md",
            "vlan-testing-procedure.md",
            "network-monitoring-setup.md",
            "network-physical-logical-connections.md"
        ]
        
        for filename in network_config_files:
            source = f"8-deployment/{filename}"
            dest = f"docs/guides/deployment/network-configuration/{filename}"
            self.git_mv(source, dest)
        
        # Service deployment guides
        service_files = [
            "freeipa-server-setup-guide.md",
            "freeipa-monitoring-setup.md",
            "grafana-docker-setup.md", 
            "docker-https-setup.md",
            "client-automount-configuration.md",
            "freeipa-user-and-group-management.md", # Added
            "cisco-nexus-9236c-snmp-grafana-setup.md",
            "opnsense-monitoring-setup.md",
            "proxmox-monitoring-setup.md",
            "qnap-monitoring-setup.md",
            "truenas-monitoring-setup.md"
        ]
        
        for filename in service_files:
            source = f"8-deployment/{filename}"
            dest = f"docs/guides/deployment/services/{filename}"
            self.git_mv(source, dest)
    
    def move_operations_guides(self):
        """Move operations guides"""
        print("\nMoving operations guides...")
        
        moves = [
            ("9-maintenance/backup-and-recovery-plan.md", "docs/guides/operations/backup-recovery.md"),
            ("8-deployment/proxmox-host-backup.md", "docs/guides/operations/proxmox-host-backup.md"),
            ("8-deployment/macos-freeipa-client-troubleshooting.md", "docs/guides/operations/troubleshooting.md"),
            ("docs/operational/guest-vlan-monitoring.md", "docs/guides/operations/guest-vlan-monitoring.md"), 
            ("8-deployment/server-onboarding.md", "docs/guides/operations/server-onboarding.md"),
            ("8-deployment/firewall-firmware-updates.md", "docs/guides/operations/firewall-firmware-updates.md"), # Added
        ]
        
        for source, dest in moves:
            self.git_mv(source, dest)
    
    def move_configurations(self):
        """Move configuration files"""
        print("\nMoving configuration files...")
        
        # Network device configs
        network_moves = [
            ("6-configuration/cfg/cisco_NEXUS9236c", "configs/network/cisco-nexus/archived/cisco_NEXUS9236c"),
            ("6-configuration/cfg/sodola", "configs/network/sodola/archived/sodola"),
        ]
        
        for source, dest in network_moves:
            self.git_mv(source, dest)
        
        # Individual files that need specific handling
        gs108e_files = [
            "2025-08-15-15-34-22-GS108Ev4.cfg",
            "GS108Ev4.cfg",
            "GS108Ev4_UM_EN.md", 
            "GS108Ev4_UM_EN.pdf",
            "GS108Ev4-VLAN-instructions.md"
        ]
        
        for filename in gs108e_files:
            source = f"6-configuration/cfg/gs108e/{filename}"
            dest = f"configs/network/netgear-gs108e/current/{filename}"
            self.git_mv(source, dest)
        
        # OpnSense configs - move all files
        opnsense_source = Path("6-configuration/cfg/opnsense")
        if opnsense_source.exists():
            for config_file in opnsense_source.iterdir(): # Use iterdir() to get Path objects directly
                if config_file.is_file() and config_file.suffix == ".xml":
                    # Construct absolute path for relative_to
                    abs_config_file = config_file.resolve()
                    print(f"DEBUG: repo_root={self.repo_root}, abs_config_file={abs_config_file}") # Debug print
                    self.git_mv(str(abs_config_file.relative_to(self.repo_root)), f"configs/network/opnsense/archived/{config_file.name}")
            
            # Move the markdown file
            opnsense_md = "6-configuration/cfg/opnsense/opnsense-firewall-rules.md"
            self.git_mv(opnsense_md, "configs/network/opnsense/archived/opnsense-firewall-rules.md")
        
        # Server configs
        server_moves = [
            ("6-configuration/cfg/proxmox", "configs/servers/proxmox"), # Corrected source path
            ("6-configuration/truenas", "configs/servers/truenas"),
            ("6-configuration/freeipa", "configs/servers/freeipa"),
            ("6-configuration/prometheus", "configs/monitoring/prometheus"),
            ("6-configuration/netgear-gs108e-port-config.md", "configs/templates/netgear-gs108e-port-config.md"),
        ]
        
        for source, dest in server_moves:
            if Path(source).exists(): 
                self.git_mv(source, dest)
    
    def move_automation_files(self):
        """Move automation files"""
        print("\nMoving automation files...\n")
        
        # Ansible files
        ansible_moves = [
            ("6-configuration/ansible/group_vars", "automation/ansible/group_vars"),
            ("6-configuration/ansible/inventory/hosts.ini", "automation/ansible/inventories/production/hosts.ini"),
            ("6-configuration/ansible/playbooks/configure_switches.yml", "automation/ansible/playbooks/configure_switches.yml"),
        ]
        
        for source, dest in ansible_moves:
            self.git_mv(source, dest)
        
        # Scripts from src/
        script_moves = [
            ("src/raspberry-pi-sys-info.sh", "automation/scripts/system-info/raspberry-pi-sys-info.sh"),
            ("src/system_info.txt", "automation/scripts/system-info/system_info.txt"),
            ("src/mac_pro_6_1_IOMMU_config.sh", "automation/scripts/system-info/mac_pro_6_1_IOMMU_config.sh"),
            ("src/modules/firewall/firewall_rules-freeipa.sh", "automation/scripts/backup/firewall_rules-freeipa.sh"),
            ("8-deployment/freeipa-user-and-group-management.sh", "automation/scripts/maintenance/freeipa-user-and-group-management.sh"),
        ]
        
        for source, dest in script_moves:
            self.git_mv(source, dest)
        
        # FreeIPA setup files from src/modules/identity-management/freeipa/
        freeipa_files = [
            ("src/modules/identity-management/freeipa/setup-freeipa-server.py", "automation/scripts/backup/setup-freeipa-server.py"),
            ("src/modules/identity-management/freeipa/setup-freeipa-server.txt", "automation/scripts/backup/setup-freeipa-server.txt"),
        ]
        
        for source, dest in freeipa_files:
            self.git_mv(source, dest)
    
    def move_inventory_and_logs(self):
        """Move inventory and log files"""
        print("\nMoving inventory and log files...")
        
        moves = [
            ("inventory/network_data/network_inventory.json", "inventory/assets.json"),
            ("12-appendix/asset-management.md", "inventory/asset-management.md"),
            ("7-testing/ipaserver-install.log", "logs/installation/ipaserver-install.log"),
            ("install_freeipa.yml", "logs/installation/install_freeipa.yml"), 
            ("9-maintenance/change-management-log.md", "logs/changes/change-management-log.md"),
        ]
        
        for source, dest in moves:
            self.git_mv(source, dest)
    
    def move_planning_documents(self):
        """Move planning documents"""
        print("\nMoving planning documents...")
        
        moves = [
            ("10-future-plans/roadmap.md", "plans/roadmap.md"),
            ("9-maintenance/disaster-recovery-plan.md", "plans/disaster-recovery.md"),
            ("9-maintenance/incident-response-plan.md", "plans/incident-response.md"),
            ("9-maintenance/vulnerability-management-plan.md", "plans/vulnerability-management.md"),
        ]
        
        for source, dest in moves:
            self.git_mv(source, dest)
    
    def move_remaining_files(self):
        """Move remaining files and clean up empty directories"""
        print("\nMoving remaining files...")
        
        # Move insights that are not explicitly moved elsewhere
        # These were previously in 4-insights/ and should go to docs/reference/
        insights_to_move = [
            "apc-ups-network-integration-insight.md",
            "centralized-logging-server-insight.md",
            "freeipa-and-zfs-insights.md",
            "freeipa-groups-ideas.md",
            "repository-insights.md",
            "vlan-monitoring-considerations.md",
        ]
        for insight_file in insights_to_move:
            source = f"4-insights/{insight_file}"
            dest = f"docs/reference/{insight_file}"
            self.git_mv(source, dest)
        
        # Move GEMINI.md
        self.git_mv("12-appendix/GEMINI.md", "docs/reference/GEMINI.md")
        
        # Move scratch files if they exist
        scratch_dir = self.repo_root / "scratch"
        if scratch_dir.exists():
            for item in scratch_dir.iterdir():
                dest = f"temp/scratch/{item.name}"
                self.fs_mv(str(item.relative_to(self.repo_root)), dest)

        # Move repo-tree.md (using fs_mv as it's untracked)
        self.fs_mv("repo-tree.md", "docs/reference/repo-tree.md") 

        print("\nCleaning up empty directories...")
        # List of directories that should be empty after moves
        dirs_to_clean = [
            "1-overview",
            "2-equipment",
            "3-learning",
            "4-insights",
            "5-physical-layout",
            "6-configuration/cfg/cisco_NEXUS9236C/2025/08/20",
            "6-configuration/cfg/cisco_NEXUS9236C/2025/08/21",
            "6-configuration/cfg/cisco_NEXUS9236C/2025/08",
            "6-configuration/cfg/cisco_NEXUS9236C",
            "6-configuration/cfg/gs108e",
            "6-configuration/cfg/opnsense",
            "6-configuration/cfg/proxmox",
            "6-configuration/cfg/sodola/2025/08/21",
            "6-configuration/cfg/sodola/2025/08",
            "6-configuration/cfg/sodola/2025",
            "6-configuration/cfg/sodola",
            "6-configuration/cfg",
            "6-configuration/ansible/group_vars",
            "6-configuration/ansible/inventory",
            "6-configuration/ansible/playbooks",
            "6-configuration/ansible",
            "6-configuration/freeipa",
            "6-configuration/prometheus",
            "6-configuration/truenas",
            "6-configuration",
            "7-testing",
            "8-deployment",
            "9-maintenance",
            "10-future-plans",
            "11-references",
            "12-appendix/security",
            "12-appendix",
            "docs/operational",
            "inventory/network_data",
            "src/modules/firewall",
            "src/modules/identity-management/freeipa",
            "src/modules/identity-management",
            "src/modules",
            "src",
            "scratch"
        ]

        for d in sorted(dirs_to_clean, reverse=True): # Sort reverse to delete subdirs first
            path_to_delete = self.repo_root / d
            if path_to_delete.is_dir() and not any(path_to_delete.iterdir()): # Check if directory exists and is empty
                try:
                    os.rmdir(path_to_delete)
                    print(f"✓ Removed empty directory: {d}")
                except OSError as e:
                    print(f"✗ Failed to remove directory {d}: {e}")
            elif path_to_delete.is_dir():
                print(f"  Skipping non-empty directory: {d}")

    def print_summary(self):
        """Print summary of operations"""
        print("\n--- Restructuring Summary ---")
        print(f"Directories created: {len(self.dirs_created)}")
        print(f"Files/Directories moved: {len(self.moves_completed)}")
        print(f"Operations failed: {len(self.moves_failed)}")
        if self.moves_failed:
            print("Failed operations details:")
            for src, dest, reason in self.moves_failed:
                print(f"  - {src} -> {dest}: {reason}")
        print("---------------------------")

def main():
    """Main execution function"""
    print("Starting repository restructuring...")
    print("This script will reorganize your repository using git mv operations.")
    
    # Verify we're in a git repository
    if not Path(".git").exists():
        print("Error: Not in a git repository!")
        sys.exit(1)
    
    # Create restructurer instance
    restructurer = RepoRestructurer()
    
    try:
        # Execute restructuring steps
        restructurer.create_directory_structure()
        restructurer.move_documentation()
        restructurer.move_deployment_guides()
        restructurer.move_operations_guides()
        restructurer.move_configurations()
        restructurer.move_automation_files()
        restructurer.move_inventory_and_logs()
        restructurer.move_planning_documents()
        restructurer.move_remaining_files()
        
        # Print summary
        restructurer.print_summary()
        
    except KeyboardInterrupt:
        print("\nRestructuring interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()