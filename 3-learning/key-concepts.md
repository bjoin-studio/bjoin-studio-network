# Key Network Concepts

This document explains some of the key concepts and architectural decisions behind the bjoin.studio network design.

## Key Architectural Decision: "Router-on-a-Stick"

A core principle of this network design is the use of a "Router-on-a-Stick" configuration. You might notice that even though the Protectli firewall has four ports, we are only using two: one for `WAN` (internet) and one for `LAN` (internal network). This is intentional and is a standard practice for building secure, scalable networks.

Here’s why we do it this way:

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

The only time you might see a spike in FreeIPA traffic is during a "login storm" – for example, if everyone in the studio logs in at exactly the same time on a Monday morning. Even in this worst-case scenario, the traffic is highly unlikely to saturate a 1Gbps link.

## Host-Based Access Control (HBAC) with FreeIPA

Host-Based Access Control (HBAC) is one of the most powerful features of FreeIPA. It allows you to create very specific, fine-grained rules about who can access what services on which machines.

Think of it as a centralized firewall for user access. Instead of managing access lists on every single server, you define all the rules in one place: the FreeIPA server.

An HBAC rule has three main components:
*   **Who:** The users and user groups the rule applies to (e.g., `sysadmins`, `vfx_artists`).
*   **Accessing:** The target hosts and host groups the rule applies to (e.g., `web_servers`, `render_nodes`).
*   **Via:** The services the user is allowed to access on those hosts (e.g., `sshd` for SSH, `sudo`).

By default, FreeIPA has a rule called `allow_all` which is enabled. For a secure environment, the first step is to disable this rule and then build your own specific rules from the ground up. This enforces a "deny by default" policy, which is a security best practice.

## Understanding Digital Certificates

Digital certificates are the foundation of trust and security on modern networks. They are electronic credentials that prove the identity of a person, server, or device, and they are essential for enabling encrypted communication (HTTPS, TLS).

A certificate contains several key pieces of information:
*   **Subject:** The identity of the certificate holder (e.g., the domain name of a website like `grafana.bjoin.studio`).
*   **Public Key:** A cryptographic key that can be shared with anyone. Its corresponding private key is kept secret by the subject.
*   **Issuer (Certificate Authority - CA):** The trusted entity that signed and issued the certificate, verifying that the subject is who they say they are.
*   **Validity Period:** The dates for which the certificate is valid.

When your browser connects to a secure website, the website presents its certificate. Your browser checks if it trusts the "Issuer" (the CA). If the CA is in your browser's built-in list of trusted authorities (like Let's Encrypt or DigiCert), the connection is trusted.

## Managing Trust with a Self-Signed Certificate Authority (CA)

For an internal network like `bjoin.studio`, buying public certificates for every internal service is impractical and unnecessary. Instead, we become our own Certificate Authority. This is known as creating a "self-signed" or "private" CA.

The process involves two main stages:

### Stage 1: Create Your Own Internal CA

First, you generate a special root certificate that acts as the ultimate source of trust for your entire internal network. This is your "bjoin.studio Internal Root CA". This CA has its own private key (which must be kept extremely secure) and a public certificate.

### Stage 2: Issue and Trust Certificates

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
