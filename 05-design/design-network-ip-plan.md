# Network IP Plan

This document contains the definitive VLAN, IP, and group plan. It serves as the single source of truth for VLAN IDs, their associated network zones, purposes, IP addressing schemes, and corresponding FreeIPA groups.

| VLAN ID | Zone         | Purpose                          | Primary FreeIPA Group | Devices / Use Cases              | Subnet          | Gateway IP     | DHCP Range                  |
|:--------|:-------------|:---------------------------------|:----------------------|:---------------------------------|:----------------|:---------------|:----------------------------|
| **11**  | Production   | Business-critical services       | `grp-production`      | Producer, admin staff, finance systems, CRM, secure document storage | `10.20.11.0/24` | `10.20.11.1`   | `10.20.11.100 – 200`        |
| **12**  | Production   | High-performance production      | `grp-production`      | Render nodes, file servers       | `10.20.12.0/24` | `10.20.12.1`   | `10.20.12.100 – 200`        |
| **13**  | Production   | Production Reserved              | `grp-production`      | Future production needs          | `10.20.13.0/24` | `10.20.13.1`   | Static only                 |
| **14**  | Production   | Production Wifi                  | `grp-production`      | Staff laptops, mobile devices    | `10.20.14.0/24` | `10.20.14.1`   | `10.20.14.100 – 200`        |
| **15**  | Production   | Production Monitoring            | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.15.0/24` | `10.20.15.1`   | `10.20.15.100 – 200`        |
| **21**  | Stage        | Physical photography stage       | `grp-stage`           | Robotic rigs, lighting arrays, product movers, control systems, IoT interfaces | `10.20.21.0/24` | `10.20.21.1`   | `10.20.21.100 – 200`        |
| **22**  | Stage        | High-performance stage           | `grp-stage`           | Image servers, preview stations  | `10.20.22.0/24` | `10.20.22.1`   | `10.20.22.100 – 200`        |
| **23**  | Stage        | Stage Reserved                   | `grp-stage`           | Future stage needs               | `10.20.23.0/24` | `10.20.23.1`   | Static only                 |
| **24**  | Stage        | Stage Wifi                       | `grp-stage`           | Tablets, mobile control apps     | `10.20.24.0/24` | `10.20.24.1`   | `10.20.24.100 – 200`        |
| **25**  | Stage        | Stage Monitoring                 | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.25.0/24` | `10.20.25.1`   | `10.20.25.100 – 200`        |
| **31**  | Studio       | Digital photography processing   | `grp-studio`          | Director, editors, retouchers, editing suites, color grading tools | `10.20.31.0/24` | `10.20.31.1`   | `10.20.31.100 – 200`        |
| **32**  | Studio       | High-performance studio          | `grp-studio`          | Color grading, VFX workstations  | `10.20.32.0/24` | `10.20.32.1`   | `10.20.32.100 – 200`        |
| **33**  | Studio       | Ultra-high-performance studio    | `grp-studio`          | SAN/NAS systems, media servers   | `10.20.33.0/24` | `10.20.33.1`   | Static only                 |
| **34**  | Studio       | Studio Wifi                      | `grp-studio`          | Creative team mobile devices     | `10.20.34.0/24` | `10.20.34.1`   | `10.20.34.100 – 200`        |
| **35**  | Studio       | Studio Monitoring                | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.35.0/24` | `10.20.35.1`   | `10.20.35.100 – 200`        |
| **41**  | Workshop     | Fabrication and prototyping      | `grp-workshop`        | Makers, engineers, technicians, CAD stations, equipment controllers | `10.20.41.0/24` | `10.20.41.1`   | `10.20.41.100 – 200`        |
| **42**  | Workshop     | Workshop Reserved                | `grp-workshop`        | Future workshop needs            | `10.20.42.0/24` | `10.20.42.1`   | Static only                 |
| **43**  | Workshop     | Workshop Reserved                | `grp-workshop`        | Future workshop needs            | `10.20.43.0/24` | `10.20.43.1`   | Static only                 |
| **44**  | Workshop     | Workshop Wifi                    | `grp-workshop`        | Tool-connected devices           | `10.20.44.0/24` | `10.20.44.1`   | `10.20.44.100 – 200`        |
| **45**  | Workshop     | Workshop Monitoring              | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.45.0/24` | `10.20.45.1`   | `10.20.45.100 – 200`        |
| **51**  | Management   | IT infrastructure and oversight  | `grp-management`      | IT manager, C-level staff, FreeIPA admin tools, audit logs, network monitoring | `10.20.51.0/24` | `10.20.51.1`   | Static only                 |
| **52**  | Management   | Management Reserved              | `grp-management`      | Future management needs          | `10.20.52.0/24` | `10.20.52.1`   | Static only                 |
| **53**  | Management   | Management Reserved              | `grp-management`      | Future management needs          | `10.20.53.0/24` | `10.20.53.1`   | Static only                 |
| **54**  | Management   | Management Wifi                  | `grp-management`      | Admin mobile devices             | `10.20.54.0/24` | `10.20.54.1`   | `10.20.54.100 – 200`        |
| **55**  | Management   | Management Monitoring            | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.55.0/24` | `10.20.55.1`   | `10.20.55.100 – 200`        |
| **61**  | Guest        | Visitor access                   | `grp-guest`           | Clients, freelancers, visitors, isolated VLAN, no internal resource access | `10.20.61.0/24` | `10.20.61.1`   | `10.20.61.100 – 200`        |
| **62**  | Guest        | Guest Reserved                   | `grp-guest`           | Future guest needs               | `10.20.62.0/24` | `10.20.62.1`   | Static only                 |
| **63**  | Guest        | Guest Reserved                   | `grp-guest`           | Future guest needs               | `10.20.63.0/24` | `10.20.63.1`   | Static only                 |
| **64**  | Guest        | Guest Wifi                       | `grp-guest`           | Visitor laptops, phones          | `10.20.64.0/24` | `10.20.64.1`   | `10.20.64.100 – 200`        |
| **65**  | Guest        | Guest Monitoring                 | `grp-management`      | Syslog, SNMP, NetFlow            | `10.20.65.0/24` | `10.20.65.1`   | `10.20.65.100 – 200`        |
