# Network VLAN Design

This document details the Virtual Local Area Network (VLAN) design for the bjoin.studio network, outlining its purpose, standards, and the definitive VLAN and IP addressing plan.

## Table of Contents

1.  [**Introduction to VLANs**](#1-introduction-to-vlans)
2.  [**VLAN Tagging Standard: 802.1Q**](#2-vlan-tagging-standard-8021q)
3.  [**Definitive VLAN, IP, and Group Plan**](#3-definitive-vlan-ip-and-group-plan)
4.  [**Demilitarized Zone (DMZ) Concept**](#4-demilitarized-zone-dmz-concept)
5.  [**VLANs and Identity Management (FreeIPA)**](#5-vlans-and-identity-management-freeipa)
6.  [**VLAN Routing and Purpose**](#6-vlan-routing-and-purpose)
    *   [Production VLANs (11-15)](#production-vlans-11-15)
    *   [Stage VLANs (21-25)](#stage-vlans-21-25)
    *   [Studio VLANs (31-35)](#studio-vlans-31-35)
    *   [Workshop VLANs (41-45)](#workshop-vlans-41-45)
    *   [Management VLANs (51-55)](#management-vlans-51-55)
    *   [Guest VLANs (61-65)](#guest-vlans-61-65)

## 1. Introduction to VLANs

VLANs are a fundamental component of the bjoin.studio network architecture, providing logical segmentation of the network. This segmentation enhances security, improves performance by reducing broadcast domains, and simplifies network management. By isolating different types of traffic and user groups into distinct VLANs, we can apply granular security policies and optimize resource allocation.

## 2. VLAN Tagging Standard: 802.1Q

For all VLAN configurations within this network, the **802.1Q** standard is used.

*   **802.1Q** is the universal standard for creating VLANs on an internal network. It functions by adding a small tag to Ethernet frames, indicating which VLAN the frame belongs to. This allows a single physical network infrastructure (switches, cables) to carry traffic for multiple logical networks. All network equipment (switches, firewalls, servers) in the bjoin.studio network is configured to utilize this standard.

*   **802.1ad (QinQ)**, a specialized standard for service providers, is not used in this internal network design.

## 3. Definitive VLAN, IP, and Group Plan

The definitive VLAN, IP, and group plan is maintained in a separate document to serve as a single source of truth.

*   [**Definitive VLAN, IP, and Group Plan**](./design-network-ip-plan.md)

## 4. Demilitarized Zone (DMZ) Concept

A DMZ is a small, isolated network segment that sits between the internet and your trusted internal LAN. It acts as a buffer zone for services that need to be accessible from the internet (e.g., public web servers).

*   **Security Principle:** The DMZ is separated from the internal LAN by firewall rules that strictly control traffic flow. The internet can access the DMZ, but the internet cannot directly access the internal LAN, and crucially, the DMZ cannot directly initiate connections to the internal LAN. This design ensures that if a service in the DMZ is compromised, the attacker is contained within the DMZ and cannot easily access sensitive internal resources.

## 5. VLANs and Identity Management (FreeIPA)

VLAN segmentation works hand-in-hand with FreeIPA to provide robust access control and seamless cross-VLAN access for users.

*   **VLANs for Isolation:** VLANs provide the fundamental layer of network security by isolating different network segments.
*   **FreeIPA for Centralized Control:** FreeIPA acts as the central authority for authentication and authorization across all these isolated VLANs, providing a single identity for users and machines.
*   **Firewall for Mediation:** The OPNsense firewall mediates controlled communication between VLANs, enforcing rules that allow specific traffic (e.g., FreeIPA authentication requests) to pass between segments.

## 6. VLAN Routing and Purpose

The detailed routing rules and purpose for each VLAN zone are documented in the main network routing design document.

*   [**Network Routing Design**](./design-network-routing.md)


## 4. Demilitarized Zone (DMZ) Concept

A DMZ is a small, isolated network segment that sits between the internet and your trusted internal LAN. It acts as a buffer zone for services that need to be accessible from the internet (e.g., public web servers).

*   **Security Principle:** The DMZ is separated from the internal LAN by firewall rules that strictly control traffic flow. The internet can access the DMZ, but the internet cannot directly access the internal LAN, and crucially, the DMZ cannot directly initiate connections to the internal LAN. This design ensures that if a service in the DMZ is compromised, the attacker is contained within the DMZ and cannot easily access sensitive internal resources.

## 5. VLANs and Identity Management (FreeIPA)

VLAN segmentation works hand-in-hand with FreeIPA to provide robust access control and seamless cross-VLAN access for users.

*   **VLANs for Isolation:** VLANs provide the fundamental layer of network security by isolating different network segments.
*   **FreeIPA for Centralized Control:** FreeIPA acts as the central authority for authentication and authorization across all these isolated VLANs, providing a single identity for users and machines.
*   **Firewall for Mediation:** The OPNsense firewall mediates controlled communication between VLANs, enforcing rules that allow specific traffic (e.g., FreeIPA authentication requests) to pass between segments.

## 6. VLAN Routing and Purpose

By default, all inter-VLAN traffic is **blocked** by the firewall. Rules must be explicitly created to allow traffic to flow between VLANs. The MikroTik CRS520-4XS-16XQ-RM handles high-speed routing between trusted VLANs.

### Production VLANs (11-15)
*   **Purpose:** For business-critical services, such as contracts, billing, and client records, as well as high-performance rendering.
*   **Routing:** Routed by OPNsense. Has filtered access to the internet. Blocked from initiating traffic to the Studio, Stage, or Workshop VLANs to protect those environments.

### Stage VLANs (21-25)
*   **Purpose:** For devices used during production shoots, such as cameras, lighting, and control systems.
*   **Routing:** Routed by OPNsense. Has very limited, filtered internet access. Can send data *to* the Studio VLANs (e.g., for media ingest) but cannot initiate connections to other zones.

### Studio VLANs (31-35)
*   **Purpose:** The core creative environment for editing, color grading, and VFX.
*   **Routing:** Routed by the MikroTik CRS520-4XS-16XQ-RM for high-speed performance. Has limited, filtered internet access via OPNsense.

### Workshop VLANs (41-45)
*   **Purpose:** For engineering, prototyping, and fabrication.
*   **Routing:** Routed by OPNsense. This zone is **isolated** and has **no internet access**. It cannot initiate connections to any other VLANs.

### Management VLANs (51-55)
*   **Purpose:** For secure access to network hardware and monitoring.
*   **Routing:** Routed by OPNsense. This is a highly privileged zone. Access *to* this VLAN is heavily restricted by firewall rules, only allowing connections from designated admin workstations.

### Guest VLANs (61-65)
*   **Purpose:** For providing internet access to visitors.
*   **Routing:** Routed by OPNsense. This zone is completely isolated from all internal VLANs. It can only access the internet.