# OPNsense Firewall Rules

This document outlines the firewall rules for the bjoin.studio network. The rules are designed to enforce a default deny policy, meaning that only explicitly allowed traffic is permitted.

## 1. Firewall Aliases

Aliases are used to make the firewall rules easier to read and manage. The following aliases should be created in OPNsense under `Firewall > Aliases`.

| Name                | Type      | Content                                     |
|:--------------------|:----------|:--------------------------------------------|
| `FreeIPA_Servers`   | Host(s)   | `10.20.51.10`, `10.20.51.11`                |
| `FreeIPA_Ports`     | Port(s)   | `53`, `88`, `123`, `389`, `443`, `636`       |
| `Client_VLANs`      | Network(s)| `10.20.11.0/24`, `10.20.12.0/24`, `10.20.14.0/24`, `10.20.21.0/24`, `10.20.22.0/24`, `10.20.24.0/24`, `10.20.31.0/24`, `10.20.32.0/24`, `10.20.34.0/24`, `10.20.41.0/24`, `10.20.44.0/24` |

## 2. Firewall Rules

The following tables outline the firewall rules for each VLAN interface. The rules should be created in OPNsense under `Firewall > Rules`.

### 2.1. Production VLANs (VLANs 11, 12, 14)

| Action | Interface | Source         | Destination       | Port(s)         | Description                                  |
|:-------|:----------|:---------------|:------------------|:----------------|:---------------------------------------------|
| Allow  | Production| `Client_VLANs` | `FreeIPA_Servers` | `FreeIPA_Ports` | Allow clients to access FreeIPA services.    |
| Allow  | Production| `Client_VLANs` | Any               | Any             | Allow clients to access the internet.        |
| Block  | Production| Any            | Any               | Any             | Default deny rule.                           |

### 2.2. Stage VLANs (VLANs 21, 22, 24)

| Action | Interface | Source         | Destination       | Port(s)         | Description                                  |
|:-------|:----------|:---------------|:------------------|:----------------|:---------------------------------------------|
| Allow  | Stage     | `Client_VLANs` | `FreeIPA_Servers` | `FreeIPA_Ports` | Allow clients to access FreeIPA services.    |
| Allow  | Stage     | `Client_VLANs` | `10.20.31.0/24`   | Any             | Allow Stage to send data to the Studio VLAN. |
| Block  | Stage     | Any            | Any               | Any             | Default deny rule.                           |

### 2.3. Studio VLANs (VLANs 31, 32, 33, 34)

| Action | Interface | Source         | Destination       | Port(s)         | Description                                  |
|:-------|:----------|:---------------|:------------------|:----------------|:---------------------------------------------|
| Allow  | Studio    | `Client_VLANs` | `FreeIPA_Servers` | `FreeIPA_Ports` | Allow clients to access FreeIPA services.    |
| Allow  | Studio    | `Client_VLANs` | Any               | Any             | Allow clients to access the internet.        |
| Block  | Studio    | Any            | Any               | Any             | Default deny rule.                           |

### 2.4. Workshop VLANs (VLANs 41, 44)

| Action | Interface | Source         | Destination       | Port(s)         | Description                                  |
|:-------|:----------|:---------------|:------------------|:----------------|:---------------------------------------------|
| Allow  | Workshop  | `Client_VLANs` | `FreeIPA_Servers` | `FreeIPA_Ports` | Allow clients to access FreeIPA services.    |
| Block  | Workshop  | Any            | Any               | Any             | Default deny rule.                           |

### 2.5. Management VLAN (VLAN 51)

| Action | Interface  | Source                  | Destination       | Port(s)         | Description                                  |
|:-------|:-----------|:------------------------|:------------------|:----------------|:---------------------------------------------|
| Allow  | Management | `10.20.11.100`          | `FreeIPA_Servers` | `FreeIPA_Ports` | Allow designated admin workstation to access FreeIPA. |
| Block  | Management | Any                     | Any               | Any             | Default deny rule.                           |

### 2.6. Guest VLAN (VLAN 61)

| Action | Interface | Source         | Destination       | Port(s)         | Description                                  |
|:-------|:----------|:---------------|:------------------|:----------------|:---------------------------------------------|
| Allow  | Guest     | `10.20.61.0/24`| Any               | Any             | Allow guests to access the internet.         |
| Block  | Guest     | Any            | Any               | Any             | Default deny rule.                           |
