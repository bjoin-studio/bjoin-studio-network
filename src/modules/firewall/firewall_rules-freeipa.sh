#!/bin/bash

# -------------------------------------------------------------------------- #

# Program Name:     firewall_rules-freeipa.sh
# Version:          1.0
# Language:         bash script
# Flame Version:    2025.x
# Author:           Phil MAN - phil_man@mac.com
# Toolset:          MAN_MADE_MATERIAL
# Created:          2024-04-10
# Modified:         2024-04-10
# Modifier:         Phil MAN - phil_man@mac.com

# Changelist:       Initial commit.

# -------------------------------------------------------------------------- #

# Description:      This program enables firewall rules.

# -------------------------------------------------------------------------- #

# Prerequisites:    1. Rocky Linux 9.x

# -------------------------------------------------------------------------- #

# Installation:     Copy to '/var/tmp/firewall_rules-freeipa.sh',

# -------------------------------------------------------------------------- #

# Instructions:     1. Log in as root
#                   2. nano /var/tmp/firewall_rules-freeipa.sh
#                   3. chmod +x /var/tmp/firewall_rules-freeipa.sh
#                   4. /var/tmp/firewall_rules-freeipa.sh

# -------------------------------------------------------------------------- #

# ========================================================================== #
# This section enables firewall rules for FreeIPA related services.
# ========================================================================== #

enable_firewall_rules_for_freeipa_services() {

    # Add a separator to the shell output
    echo -e "\n$separator_hash\n"
    echo -e "  Enabling firewall rules for FreeIPA services."
    echo -e "\n$separator_hash\n"

    # ---------------------------------------------------------------------- #

    # Service: AUDITD (system logs)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: AUDITD"
    echo -e "\n               purpose: generation / maintenance of system logs"

    firewall-cmd --permanent --zone=public --add-service=audit | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: COCKPIT (remote system administration)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule."
    echo -e "\n  service name / port#: COCKPIT"
    echo -e "\n               purpose: remote system administration"

    firewall-cmd --permanent --zone=public --add-service=cockpit | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=9090/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: Dynamic Host Configuration Protocol (DHCP)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: DHCP port 67 (server) & 68 (client)"
    echo -e "\n               purpose: dynamic ipv4 allocation"

    firewall-cmd --permanent --zone=public --add-service=dhcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=67/udp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=68/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: DHCPv6 port 547 (server) & 546 (client)"
    echo -e "\n               purpose: dynamic ipv6 allocation"

    firewall-cmd --permanent --zone=public --add-service=dhcpv6 | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=dhcpv6-client | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=547/udp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=546/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: Domain Name Services (DNS)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: DNS port 53"
    echo -e "\n               purpose: domain name services"

    firewall-cmd --permanent --zone=public --add-service=dns | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=53/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=53/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: DNS port 853"
    echo -e "\n               purpose: domain name services over TLS"

    firewall-cmd --permanent --zone=public --add-service=dns-over-tls | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=853/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: FreeIPA (Identity, Policy, Audit services)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: FREEIPA"
    echo -e "\n               purpose: Identity, Policy, Audit services"

    firewall-cmd --permanent --zone=public --add-service=freeipa-4 | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=freeipa-ldap | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=freeipa-ldaps | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=freeipa-replication | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=freeipa-trust | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: HTTP & HTTPS (web traffic)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: HTTP port 80"
    echo -e "\n               purpose: web traffic"

    firewall-cmd --permanent --zone=public --add-service=http | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=80/tcp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: HTTPS port 443"
    echo -e "\n               purpose: secure web traffic"

    firewall-cmd --permanent --zone=public --add-service=https | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=443/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: IPSEC (secure network communication)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: IPSEC"

    firewall-cmd --permanent --zone=public --add-service=ipsec | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: Kerberos (authentication)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: KADMIN port 749"
    echo -e "\n               purpose: kerberos admin services"

    firewall-cmd --permanent --zone=public --add-service=kadmin | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=749/tcp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: KERBEROS port 88"
    echo -e "\n               purpose: authentication"

    firewall-cmd --permanent --zone=public --add-service=kerberos | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=88/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=88/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: KLOGIN port 543"
    echo -e "\n               purpose: kerberos login services"

    firewall-cmd --permanent --zone=public --add-service=klogin | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=543/tcp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: KPASSWD port 464"
    echo -e "\n               purpose: password change"

    firewall-cmd --permanent --zone=public --add-service=kpasswd | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=464/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=464/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: KSHELL port 544"
    echo -e "\n               purpose: kerberos remote shell services"

    firewall-cmd --permanent --zone=public --add-service=kshell | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=544/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: LDAP (directory services)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: LDAP port 389"
    echo -e "\n               purpose: directory services"

    firewall-cmd --permanent --zone=public --add-service=ldap | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=389/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=389/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: LDAPS port 636"
    echo -e "\n               purpose: secure LDAP communication"

    firewall-cmd --permanent --zone=public --add-service=ldaps | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=636/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: LLMNR (link-local multicast name resolution)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: LLMNR port 5355"
    echo -e "\n               purpose: link-local multicast name resolution"

    firewall-cmd --permanent --zone=public --add-service=llmnr | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=llmnr-tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-service=llmnr-udp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=5355/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=5355/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: MDNS (multicast domain name services)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: MDNS port 5353"
    echo -e "\n               purpose: multicast domain name services"

    firewall-cmd --permanent --zone=public --add-service=mdns | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=5353/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: Microsoft RPC (Remote Procedure Call)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: MS-RPC port 135"
    echo -e "\n               purpose: Microsoft remote procedure call"

    # firewall-cmd --permanent --zone=public --add-service=msrpc | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=135/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=135/udp | sed 's/^/  /'

    # --------------------------------------------------------------------- #

    # Service: Microsoft SMB (Server Message Block)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: MS-SMB port 445"
    echo -e "\n               purpose: Microsoft server message block"

    firewall-cmd --permanent --zone=public --add-port=445/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=445/udp | sed 's/^/  /'

    # --------------------------------------------------------------------- #

    # Service: mountd Service

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: MOUNTD port 20048"
    echo -e "\n               purpose: mountd service"

    firewall-cmd --permanent --zone=public --add-service=mntd | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=20048/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=20048/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #


    # Service: NetBIOS Datagram Service

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: NETBIOS-DATAGRAM port 138"
    echo -e "\n               purpose: NetBIOS datagram service"

    firewall-cmd --permanent --zone=public --add-port=138/udp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=138/tcp | sed 's/^/  /'

    # --------------------------------------------------------------------- #

    # Service: NetBIOS Session Service
    
    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: NETBIOS-SESSION port 139"
    echo -e "\n               purpose: NetBIOS session service"

    firewall-cmd --permanent --zone=public --add-port=139/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=139/udp | sed 's/^/  /'

    # --------------------------------------------------------------------- #

    # Service: NIS (Network Information Service)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: NIS port 111"
    echo -e "\n               purpose: network information services"

    firewall-cmd --permanent --zone=public --add-service=nis | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=111/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=111/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: NFS (Network File System)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: NFS port 2049"
    echo -e "\n               purpose: network file services"

    firewall-cmd --permanent --zone=public --add-service=nfs | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=2049/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=2049/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: NFS3 port 2049"
    echo -e "\n               purpose: network file services v3"

    firewall-cmd --permanent --zone=public --add-service=nfs3 | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=2049/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=2049/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: NTP (Network Time Protocol)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: NTP port 123"
    echo -e "\n               purpose: time synchronization"

    firewall-cmd --permanent --zone=public --add-service=ntp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=123/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=123/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: Port Range 1024-1300

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: Port Range 1024-1300"
    echo -e "\n               purpose: FreeIPA services"

    firewall-cmd --permanent --zone=public --add-port=1024-1300/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=1024-1300/udp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: statd (NFS status monitor)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: STATD port 32765"
    echo -e "\n               purpose: NFS status monitor"

    firewall-cmd --permanent --zone=public --add-service=statd | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=32765/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=32765/udp | sed 's/^/  /'    

    # Service: SSH (secure shell)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: SSH port 22"
    echo -e "\n               purpose: secure shell"

    firewall-cmd --permanent --zone=public --add-service=ssh | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=22/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: SYSLOG (system logging)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: SYSLOG port 514"
    echo -e "\n               purpose: system logging services"

    firewall-cmd --permanent --zone=public --add-service=syslog | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=514/tcp | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=514/udp | sed 's/^/  /'

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: SYSLOG-TLS port 6514"
    echo -e "\n               purpose: secure system logging services"

    firewall-cmd --permanent --zone=public --add-service=syslog-tls | sed 's/^/  /'
    firewall-cmd --permanent --zone=public --add-port=6514/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #

    # Service: WEBMIN (web administration)

    # Add a new firewall rule
    echo -e "\n  Adding firewall rule:"
    echo -e "\n  service name / port#: WEBMIN port 10000"
    echo -e "\n               purpose: Web Administration"
    # firewall-cmd --permanent --zone=public --add-service=webmin
    firewall-cmd --permanent --zone=public --add-port=10000/tcp | sed 's/^/  /'

    # ---------------------------------------------------------------------- #
}

# ========================================================================== #
# This section defines how to handle the main script function.
# ========================================================================== #

# Call the function if this script is executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    enable_firewall_rules_for_freeipa_services
fi

# ========================================================================== #
# C2 A9 32 30 32 34 2D 4D 41 4E 2D 4D 41 44 45 2D 4D 45 4B 41 4E 59 5A 4D 53 #
# ========================================================================== #
