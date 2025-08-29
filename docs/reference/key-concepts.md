# Key Network Concepts

This document explains some of the key concepts and architectural decisions behind the bjoin.studio network design.

## Table of Contents
*   [The Foundation of Network Security: Identity Management](#the-foundation-of-network-security-identity-management)
*   [Key Architectural Decision: "FreeIPA"](#key-architectural-decision-freeipa)
*   [Key Architectural Decision: "Router-on-a-Stick"](#key-architectural-decision-router-on-a-stick)
*   [A Note on Performance and Bottlenecks](#a-note-on-performance-and-bottlenecks)
*   [VLAN Tagging Standard: 802.1Q](#vlan-tagging-standard-8021q)
*   [What is a DMZ (Demilitarized Zone)?](#what-is-a-dmz-demilitarized-zone)
*   [Enabling Seamless Cross-VLAN Access with FreeIPA](#enabling-seamless-cross-vlan-access-with-freeipa)
*   [A Note on FreeIPA Network Traffic](#a-note-on-freeipa-network-traffic)
*   [Host-Based Access Control (HBAC) with FreeIPA](#host-based-access-control-hbac-with-freeipa)
*   [Digital Certificates and Certificate Authorities](#digital-certificates-and-certificate-authorities)
    *   [Understanding Digital Certificates](#understanding-digital-certificates)
    *   [Managing Trust with a Self-Signed Certificate Authority (CA)](#managing-trust-with-a-self-signed-certificate-authority-ca)
    *   [Do You Need a Dedicated CA Server?](#do-you-need-a-dedicated-ca-server)
*   [Simple Network Management Protocol (SNMP)](#simple-network-management-protocol-snmp)
*   [Commonly Used Naming Convention for Cable Labels](#commonly-used-naming-convention-for-cable-labels)
*   [Glossary](#glossary)

---

## The Foundation of Network Security: Identity Management

In any multi-user network environment, one of the most critical challenges is managing user identities and access controls consistently across all systems. Without centralized identity management, you quickly fall into the trap of maintaining separate user accounts, passwords, and permissions on every server, workstation, and network device. This creates a security nightmare: users tend to reuse weak passwords, administrators struggle to revoke access when employees leave, and auditing who has access to what becomes nearly impossible.

Modern identity management systems solve this by providing a single source of truth for user authentication and authorization. They enable single sign-on (SSO), centralized password policies, role-based access control, and comprehensive audit trails. For Linux-centric environments like the bjoin.studio network, FreeIPA emerges as the clear choice because it seamlessly integrates multiple essential services: LDAP for directory services, Kerberos for authentication, DNS for service discovery, and a Certificate Authority for PKI infrastructure. Unlike proprietary solutions that require per-user licensing or cloud-based systems that introduce latency and dependency concerns, FreeIPA provides enterprise-grade identity management that's completely self-hosted and designed specifically for mixed Linux/Unix environments.

## Key Architectural Decision: "FreeIPA"

The choice of FreeIPA as the central identity management system for the bjoin.studio network represents a strategic architectural decision that affects virtually every aspect of network operations. FreeIPA is not merely an authentication service—it's a comprehensive identity platform that forms the backbone of network security, user management, and system integration.

**Why FreeIPA Over Alternatives:**

*   **Integrated Architecture:** FreeIPA combines four critical services into a single, cohesive system: 389 Directory Server (LDAP), MIT Kerberos (authentication), BIND DNS (service discovery), and Dogtag Certificate Authority (PKI). This eliminates the complexity of managing separate systems and ensures they work together seamlessly.

*   **Linux-Native Design:** Unlike Windows Active Directory, which requires complex compatibility layers for Linux systems, FreeIPA is built specifically for Unix-like environments. This means native SSH key management, sudo rule distribution, and seamless integration with standard Linux authentication mechanisms.

*   **Zero Licensing Costs:** FreeIPA is completely open source with no per-user licensing fees. For a growing studio, this represents significant long-term cost savings compared to proprietary identity solutions.

*   **Self-Hosted Control:** By running FreeIPA internally, the bjoin.studio network maintains complete control over identity data, authentication policies, and service availability. There's no dependency on external cloud services or internet connectivity for basic authentication operations.

**FreeIPA's Role in Network Architecture:**

FreeIPA serves as the central nervous system for the bjoin.studio network, enabling several key architectural patterns:

*   **Cross-VLAN Identity:** Users authenticated by FreeIPA can access resources across different VLANs based on centralized policies, rather than maintaining separate accounts on each system.

*   **Certificate Management:** FreeIPA's integrated CA automatically handles certificate lifecycle management for all domain-joined systems, enabling encrypted communication throughout the network.

*   **Automated Configuration:** Through integration with tools like Ansible, FreeIPA can automatically provision and configure new systems based on their role assignments and group memberships.

*   **Audit and Compliance:** All authentication events, permission changes, and access attempts are centrally logged, providing comprehensive audit trails for security and compliance purposes.

This architectural decision creates a foundation where security, scalability, and operational efficiency are built-in rather than added on as afterthoughts.

## Key Architectural Decision: "Router-on-a-Stick"

A core principle of this network design is the use of a "Router-on-a-Stick" configuration. You might notice that even though the Protectli firewall has four ports, we are only using two: one for `WAN` (internet) and one for `LAN` (internal network). This is intentional and is a standard practice for building secure, scalable networks.

Here's why we do it this way:

*   **Centralized Control:** By forcing all traffic between VLANs to go up the "stick" to the OPNsense firewall through a single port, we guarantee that every packet is inspected. This gives us a single, powerful point of control for all security policies.
*   **Specialized Roles:** It lets the switches do what they do best (handle high-speed VLAN traffic) and lets the firewall do what it does best (deep packet inspection, routing, and security).
*   **Flexibility:** We can add dozens of new VLANs in the future without ever needing to change the physical cabling on the firewall.

The spare ports on the firewall give us great options for the future, like a dedicated high-security DMZ or a redundant link to the core switch.

## A Note on Performance and Bottlenecks

It's fair to ask: "If we have a 100Gb/s switch, won't the 1Gb/s firewall be a bottleneck?" The answer is **no** for the most important traffic, and it highlights the power of this design. The key is understanding the two types of traffic on our network.

### 1. Traffic *Inside* a VLAN (East-West)
This is your high-speed lane. When a 100Gb/s editing workstation needs to pull a huge file from a 100Gb/s media server in the same VLAN, that traffic goes directly to the Cisco 100G switch and is handled there. It **never touches the firewall**. This is where the heavy lifting is done, at full speed.

### 2. Traffic *Between* VLANs (North-South)
When a device from one VLAN needs to talk to another (e.g., a 1G office workstation accessing a server), that traffic *must* go through the firewall to be inspected and routed. This traffic **is limited to the 1Gb/s speed of the firewall's port**.

This is an intentional trade-off. We are using the expensive, high-speed switch for the bulk data transfers *within* our performance-critical zones, while using the firewall to apply security and control to the lower-speed traffic that needs to cross between those zones.

### Upgrading Firewall Performance
If, in the future, the 1Gb/s speed for traffic *between* VLANs becomes a limitation, the solution is to upgrade the firewall hardware. To achieve true 10Gb/s firewalling, you would need a new machine with:

*   **10Gb Ports:** This raises the maximum physical speed of the connection to the network.
*   **A Powerful CPU:** This is the "engine" of the firewall. A faster CPU is critical for processing packets, inspecting traffic, and handling routing at high speeds.
*   **Sufficient RAM:** More memory is needed to handle the state table for a larger number of connections.
*   **Awareness of Services:** Performance-intensive services like Intrusion Detection (IDS/IPS) and VPNs will always require a more powerful CPU to maintain high throughput.

## VLAN Tagging Standard: 802.1Q

When configuring VLANs, you will see references to different tagging standards. For this entire network, we will be using the **802.1Q** standard.

*   **802.1Q** is the universal standard for creating VLANs on an internal network. It's like putting colored labels on your internal office mail to send it to the right department. All of your equipment (OPNsense, switches) uses this standard.

*   You may also see an option for **802.1ad (QinQ)**. This is a specialized standard for service providers to "stack" customer VLANs inside their own. It's like FedEx putting your entire box of labeled mail inside a larger FedEx box. We are the office, not FedEx, so we will not use this.

A frame tagged for VLAN 11 (Production) will have a 4-byte 802.1Q header inserted with VLAN ID 11, allowing the switch to route it to the correct VLAN.

**In short: For all VLAN configuration, 802.1Q is the correct and only standard you need to use.**

## What is a DMZ (Demilitarized Zone)?

The concept of a DMZ can seem a bit confusing, but it's a simple and very powerful security tool. Think of your network like a secure office building.

*   Your **Internal LAN** (e.g., Production Wired VLAN 11, Studio Wired VLAN 32) is the secure main office where all your trusted employees and sensitive documents are. You don't want random people from the street wandering in.
*   The **Internet** is the public street outside.
*   A **DMZ** is like the **lobby** of your building.

Visitors from the street (the internet) are allowed into the lobby (the DMZ) to talk to a receptionist or drop off a package (e.g., access your public web server). However, the lobby is separated from the main office by locked, secure doors (the firewall). A visitor in the lobby can't get into the main office.

In network terms, a DMZ is a small, isolated network that sits between the internet and your trusted internal LAN. It's where you place any services that need to be accessible from the internet.

The firewall rules are simple and strict:
*   The **Internet** can talk to servers in the **DMZ**.
*   The **Internet** can **NOT** talk to your **Internal LAN**.
*   The **DMZ** can **NOT** talk to your **Internal LAN**. This is the most important rule. If a server in your DMZ is compromised, the attacker is still trapped in the lobby and can't access your secure internal network.

One of the spare ports on the Protectli firewall is the perfect tool to create a dedicated, physical DMZ if you ever decide to host a public-facing service.

## Enabling Seamless Cross-VLAN Access with FreeIPA

Your network design is indeed on target for building a FreeIPA environment that allows users to seamlessly cross VLANs and access resources in a controlled and secure manner. This is achieved through the powerful combination of:

*   **VLANs for Isolation:** Your VLAN segmentation provides a fundamental layer of security by isolating different network segments. This is a strength, not a limitation.
*   **FreeIPA for Centralized Control:** FreeIPA acts as the central authority for authentication and authorization across all these isolated VLANs. It provides a single identity for users and machines.
*   **The Firewall for Mediation:** Your OPNsense firewall is the critical component that mediates controlled communication between VLANs. It enforces the rules that allow specific traffic (e.g., FreeIPA authentication requests) to pass between segments.

This architecture ensures that users can access resources across VLANs using their single FreeIPA identity, while maintaining granular control over what they can access and from where. For example, a lead flame artist who is also a system administrator can be granted broad access through FreeIPA group memberships and `sudo` rules, allowing them to manage storage, networks, servers, and production systems from any authorized workstation, regardless of its VLAN.

## A Note on FreeIPA Network Traffic

FreeIPA traffic is generally not heavy. A 1Gbps connection is more than sufficient for the FreeIPA server. Here's a breakdown of why:

*   **Lightweight Traffic:** FreeIPA traffic mostly consists of small, quick transactions like DNS lookups, Kerberos authentication tickets, and LDAP queries. These are very small packets and don't consume much bandwidth.
*   **Not a File Server:** You won't be transferring large files to or from the FreeIPA server. It's purely for authentication and identity management.
*   **The Real Bottleneck:** If you were to experience performance issues with FreeIPA, the bottleneck would almost certainly be the CPU or the disk I/O on the Proxmox host, not the network connection.

### When Could it Spike?

The only time you might see a spike in FreeIPA traffic is during a "login storm" — for example, if everyone in the studio logs in at exactly the same time on a Monday morning. When we say 'login storm,' we're talking about 50-100 simultaneous authentications. Even in this worst-case scenario, the traffic is highly unlikely to saturate a 1Gbps link. FreeIPA typically uses less than 10Mbps even during peak usage.

## Host-Based Access Control (HBAC) with FreeIPA

Host-Based Access Control (HBAC) is one of the most powerful features of FreeIPA. It allows you to create very specific, fine-grained rules about who can access what services on which machines.

Think of it as a centralized firewall for user access. Instead of managing access lists on every single server, you define all the rules in one place: the FreeIPA server.

An HBAC rule has three main components:
*   **Who:** The users and user groups the rule applies to (e.g., `sysadmins`, `vfx_artists`).
*   **Accessing:** The target hosts and host groups the rule applies to (e.g., `web_servers`, `render_nodes`).
*   **Via:** The services the user is allowed to access on those hosts (e.g., `sshd` for SSH, `sudo`).

By default, FreeIPA has a rule called `allow_all` which is enabled. For a secure environment, the first step is to disable this rule and then build your own specific rules from the ground up. This enforces a "deny by default" policy, which is a security best practice.

## Digital Certificates and Certificate Authorities

### Understanding Digital Certificates

Digital certificates are the foundation of trust and security on modern networks. They are electronic credentials that prove the identity of a person, server, or device, and they are essential for enabling encrypted communication (HTTPS, TLS).

A certificate contains several key pieces of information:
*   **Subject:** The identity of the certificate holder (e.g., the domain name of a website like `grafana.bjoin.studio`).
*   **Public Key:** A cryptographic key that can be shared with anyone. Its corresponding private key is kept secret by the subject.
*   **Issuer (Certificate Authority - CA):** The trusted entity that signed and issued the certificate, verifying that the subject is who they say they are.
*   **Validity Period:** The dates for which the certificate is valid.

When your browser connects to a secure website, the website presents its certificate. Your browser checks if it trusts the "Issuer" (CA). If the CA is in your browser's built-in list of trusted authorities (like Let's Encrypt or DigiCert), the connection is trusted.

### Managing Trust with a Self-Signed Certificate Authority (CA)

For an internal network like `bjoin.studio`, buying public certificates for every internal service is impractical and unnecessary. Instead, we become our own Certificate Authority. This is known as creating a "self-signed" or "private" CA.

The process involves two main stages:

#### Stage 1: Create Your Own Internal CA

First, you generate a special root certificate that acts as the ultimate source of trust for your entire internal network. This is your "bjoin.studio Internal Root CA". This CA has its own private key (which must be kept extremely secure) and a public certificate.

#### Stage 2: Issue and Trust Certificates

Once you have your internal CA, you can use it to sign and issue certificates for all of your internal services (e.g., `prometheus.bjoin.studio`, `opnsense.bjoin.studio`, etc.).

The crucial final step is to **distribute the public certificate of your "bjoin.studio Internal Root CA" to all client devices on your network**. By installing this CA certificate into the "Trusted Root Certification Authorities" store on your computers (Windows, macOS, Linux), you are telling them: "Any certificate signed by this internal CA should be trusted completely."

This provides several benefits:
*   **Full Encryption:** All internal traffic can be encrypted.
*   **No More Errors:** You get the green padlock in your browser for all internal sites without any security warnings.
*   **Enhanced Security:** It allows services like the Docker daemon to be configured for secure, encrypted remote access (TLS).

Setting up a private CA is a foundational step for building a secure and professional internal network environment.

### Do You Need a Dedicated CA Server?

This is an excellent question. A Certificate Authority is not necessarily a server. It's more accurate to say a CA is a **trusted entity that is represented by a root certificate and its corresponding private key**. These are, fundamentally, files.

The *process* of signing certificates can be done on any machine that has the CA's private key. For high-security environments, this is often done on a completely offline computer.

**For the `bjoin.studio` network, you do not need a dedicated CA server.** You already have two powerful CA management systems built into your key infrastructure:

1.  **FreeIPA:** Your FreeIPA server has its own built-in CA. It automatically creates and manages certificates for all the servers and services that are enrolled in your FreeIPA domain. This is the most convenient option for domain-joined machines.
2.  **OPNsense:** Your OPNsense firewall also has a full-featured Certificate Authority manager. This is perfect for creating certificates for devices or services that are *not* part of your FreeIPA domain, or for things like user VPN certificates.

**Recommendation:** Use the FreeIPA CA for everything related to your IPA domain, and use the OPNsense CA for everything else.

## Simple Network Management Protocol (SNMP)

SNMP is an Internet Standard protocol for collecting and organizing information about managed devices on IP networks and for modifying that information to change device behavior. Devices that typically support SNMP include routers, switches, servers, workstations, printers, and more.

### How SNMP Works:
*   **Managed Devices:** Network devices that run an SNMP agent.
*   **SNMP Agent:** Software that runs on a managed device and translates local management information into a format compatible with SNMP.
*   **Network Management Station (NMS):** A console or set of applications used to monitor and manage network devices. Grafana, when integrated with a data source like Prometheus or InfluxDB, can act as an NMS for visualizing SNMP data.
*   **Management Information Base (MIB):** A hierarchical database of network device objects that can be managed using SNMP. Each object in the MIB has a unique Object Identifier (OID).

### Enabling SNMP on Switches:
Enabling SNMP on a switch typically involves:
1.  **Enabling the SNMP service:** Turning on the SNMP agent on the device.
2.  **Configuring SNMP communities:** These are essentially passwords that allow access to the SNMP agent.
    *   **Read-only (RO) community:** Allows an NMS to retrieve information from the device.
    *   **Read-write (RW) community:** Allows an NMS to retrieve and modify information on the device (use with extreme caution).
3.  **Defining SNMP views:** Limiting the MIB objects that can be accessed by certain communities.
4.  **Configuring SNMP traps/informs:** Setting up the switch to send notifications (traps) to the NMS when specific events occur (e.g., a port going down).
5.  **Specifying NMS hosts:** Limiting which IP addresses are allowed to query the SNMP agent.

## Commonly Used Naming Convention for Cable Labels

Adhering to a consistent naming convention for cable labels is crucial for efficient network management, troubleshooting, and documentation. The goal is to provide clear, concise, and actionable information at a glance.

### Key Elements of a Good Cable Labeling Convention:

1.  **Source (From):** Where the cable originates.
2.  **Destination (To):** Where the cable terminates.
3.  **Port/Interface:** The specific port number on the device.
4.  **Device Identifier:** A unique name or ID for the device (e.g., switch name, server name).
5.  **Cable Type (Optional but Recommended):** Especially useful for mixed environments (e.g., Cat6a, Fiber, Coax).
6.  **VLAN (Optional but Recommended):** If the port is assigned to a specific VLAN.

### Common Naming Convention Approaches/Examples:

The most common and highly recommended approach is a **"From-To"** or **"Source-Destination"** format, applied at *both ends* of the cable. This means each end of the cable has a label indicating where it's coming from and where it's going.

**Example Format:** `[Source_Device]-[Source_Port] -> [Destination_Device]-[Destination_Port]`

Let's break down some variations:

**1. Simple Device-Port (Most Common):**
This is the most fundamental and widely adopted.
*   **Label on End A:** `SW1-G0/1 -> SRV-NIC0`
*   **Label on End B:** `SRV-NIC0 -> SW1-G0/1`
    *   **Explanation:** Cable connects Switch 1, Gigabit Ethernet port 0/1, to Server's Network Interface Card 0.

**2. Including Location/Rack (for larger environments):**
Useful in data centers or multi-floor buildings.
*   **Label on End A:** `RACK1-SW1-G0/1 -> RACK2-SRV-NIC0`
*   **Label on End B:** `RACK2-SRV-NIC0 -> RACK1-SW1-G0/1`
    *   **Explanation:** Adds rack or location identifier.

**3. Including VLAN (for clarity on trunk/access ports):**
Especially helpful when troubleshooting VLAN issues.
*   **Label on End A:** `SW1-G0/1(VLAN10) -> AP1-ETH0`
*   **Label on End B:** `AP1-ETH0 -> SW1-G0/1(VLAN10)`
    *   **Explanation:** Indicates the port is associated with VLAN 10. For trunk ports, you might list multiple VLANs or just indicate "TRUNK".

**4. Including Cable Type (for quick identification):**
*   **Label on End A:** `SW1-G0/1 -> SRV-NIC0 (C6A)`
*   **Label on End B:** `SRV-NIC0 -> SW1-G0/1 (C6A)`
    *   **Explanation:** "C6A" for Cat6a.

**5. Using a Unique Cable ID (for complex tracing):**
Some organizations assign a unique ID to each physical cable run, which is then referenced in documentation.
*   **Label on End A:** `CBL-001-A` (with `SW1-G0/1` written below or on the other side)
*   **Label on End B:** `CBL-001-B` (with `SRV-NIC0` written below or on the other side)
    *   **Explanation:** `CBL-001` is the unique identifier for that specific cable. Details are in a database.

### Best Practices for Cable Labeling:

*   **Label Both Ends:** Always label both ends of the cable with the same information, just reversed (source on one end, destination on the other). This is the single most important rule.
*   **Consistency:** Once you choose a convention, stick to it rigorously across your entire network.
*   **Conciseness:** Keep labels as short as possible while still being informative. Use abbreviations where clear.
*   **Durability:** Use high-quality, durable labels that are resistant to fading, smudging, and peeling. Heat-shrink labels are excellent.
*   **Readability:** Use a clear font and ensure the label is positioned so it can be easily read without disconnecting the cable.
*   **Logical Order:** Typically, `FROM -> TO` is the most intuitive flow.
*   **Documentation:** Maintain a separate, centralized document (like a spreadsheet or network diagram) that maps out all cable runs and their corresponding labels. This is your ultimate source of truth.

## Glossary

*   **802.1Q:** The IEEE standard for VLAN tagging on Ethernet networks, allowing multiple VLANs to share a single physical network interface.
*   **DMZ (Demilitarized Zone):** A perimeter network that protects and adds an extra layer of security to an organization's internal local area network (LAN) from untrusted traffic, usually from the internet.
*   **FreeIPA:** An integrated security information management solution that combines Linux (Fedora) and open source identity management components like 389 Directory Server, MIT Kerberos, NTP, DNS, Dogtag certificate system, and SSSD.
*   **HBAC (Host-Based Access Control):** A FreeIPA feature that allows administrators to define granular rules for who can access what services on which machines, centralizing access control policies.
*   **IDS/IPS (Intrusion Detection System/Intrusion Prevention System):** Security tools that monitor network or system activities for malicious activity or policy violations. IDS detects and alerts, while IPS can also block detected threats.
*   **Kerberos:** A network authentication protocol that works on the basis of "tickets" to allow nodes communicating over a non-secure network to prove their identity to one another in a secure manner.
*   **LDAP (Lightweight Directory Access Protocol):** An open, vendor-neutral, industry standard application protocol for accessing and maintaining distributed directory information services.
*   **MIB (Management Information Base):** A hierarchical database of network device objects that can be managed using SNMP.
*   **NAT (Network Address Translation):** A method of remapping one IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device.
*   **NMS (Network Management Station):** A console or set of applications used to monitor and manage network devices, often collecting data via SNMP.
*   **NTP (Network Time Protocol):** A networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks.
*   **OID (Object Identifier):** A unique identifier used in SNMP to name objects in a Management Information Base (MIB) hierarchy.
*   **Router-on-a-Stick:** A configuration where a single physical router interface is used to route traffic between multiple VLANs by using sub-interfaces, each configured for a different VLAN.
*   **SNMP (Simple Network Management Protocol):** An Internet Standard protocol for collecting and organizing information about managed devices on IP networks and for modifying that information to change device behavior.
*   **SSSD (System Security Services Daemon):** A service that provides access to identity and authentication remote services and caches the information locally to improve performance and provide offline support.
*   **TLS (Transport Layer Security):** A cryptographic protocol designed to provide communications security over a computer network. It is widely used in applications like web browsing (HTTPS), email, and instant messaging.
*   **VLAN (Virtual Local Area Network):** A logical grouping of network devices that allows them to communicate as if they were on the same physical network segment, regardless of their actual physical location.
*   **ZFS:** A combined file system and logical volume manager designed by Sun Microsystems. It is known for its data integrity features, snapshot capabilities, and scalability.