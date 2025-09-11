# Overview bjoin.studio

## Table of Contents
1. [**Introduction**](#introduction)
2. [**Analysis of Existing Infrastructure**](#analysis-of-existing-infrastructure)
3. [**High-Level Plan**](#high-level-plan)
4. [**New Network Design**](#new-network-design)

---

## Introduction

This document outlines the redesign of the bjoin.studio network, including the rationale, strategic goals, and implementation plan. It serves as a living reference that will evolve alongside the infrastructure.

[Back to Table of Contents](#table-of-contents)

---

## Analysis of Existing Infrastructure

The existing network was built around consumer-grade hardware and lacked intentional design. Workstations connected to a single 10Gb NAS operated without a DHCP server or static IP configuration, relying instead on APIPA (Automatic Private IP Addressing) addresses in the `169.254.x.x` range. This setup allowed for basic file sharing but lacked routing, segmentation, and centralized control. Meanwhile, Wi-Fi devices received IP addresses via DHCP from a domestic modem/router using a Class C private address space (typically `192.168.x.x`). 

The network was effectively flat, with no VLANs or traffic isolation. There was no firewall between internal devices, no identity management, and no monitoring or logging. As a result, the infrastructure was difficult to scale, insecure by design, and prone to configuration drift. Troubleshooting was manual and inconsistent, and the lack of a unified management plane made even simple changes risky and error-prone.

[Back to Table of Contents](#table-of-contents)

---

## New Network Design

The new network is called bjoin.studio, a class A network starting at 10.20.x.x

The bjoin.studio network is engineered for scalability, resilience, and security.
It replaces the previous ad hoc setup with a structured, centrally managed architecture.

Built around a 100GbE core, the design incorporates 10GbE and 1GbE access layers to support a diverse range of endpoints.
VLAN segmentation ensures logical separation of traffic, reducing attack surfaces and simplifying policy enforcement.
OPNsense handles routing and firewall duties, while FreeIPA provides identity and access management across services.

This infrastructure underpins all studio operations—from creative workflows to business systems—and positions bjoin.studio for long-term growth. Though the investment is substantial, the benefits in performance, reliability, and security will be transformative.

[Back to Table of Contents](#table-of-contents)

---

## High-Level Plan

The redesigned network is a ground-up rebuild tailored to the demands of a modern, data-intensive creative environment. It emphasizes performance, segmentation, and centralized control.

Key components of the plan:

- **Core Backbone:** A 100GbE core will interconnect all major systems, ensuring low-latency, high-throughput communication.

- **Traffic Segmentation:** VLANs will isolate services and device classes, enhancing both security and manageability.

- **Centralized Control:** OPNsense and FreeIPA will provide unified management for routing, identity, and policy enforcement.

- **Security Architecture:** Firewalls, ACLs, and intrusion detection/prevention systems will form a layered defense strategy.

[Back to Table of Contents](#table-of-contents)
