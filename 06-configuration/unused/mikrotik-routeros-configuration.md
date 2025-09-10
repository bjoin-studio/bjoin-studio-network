# MikroTik RouterOS Configuration for bjoin.studio

This document tracks the configuration of MikroTik devices within the bjoin.studio network. It serves as a log of commands used and decisions made.

## Core Switch (CRS520) L3 Configuration

The following steps were taken to configure the CRS520-4XS-16XQ-RM as the core Layer 3 router for the network.

### 1. LACP Bond Configuration

A 40Gbps LACP bond was created to connect to the TP-Link SG3428X distribution switch. This provides a high-bandwidth, resilient link for all inter-VLAN traffic.

First, the member ports were removed from the default bridge:
```
/interface bridge port
remove [find interface=qsfp28-1-1]
remove [find interface=qsfp28-1-2]
remove [find interface=qsfp28-1-3]
remove [find interface=qsfp28-1-4]
```

Then, the bond was created with the four lanes as slaves:
```
/interface bonding add name=bond-to-SG3428X mode=802.3ad lacp-rate=1sec link-monitoring=mii slaves=qsfp28-1-1,qsfp28-1-2,qsfp28-1-3,qsfp28-1-4
```

### 2. VLAN Interface Creation

Virtual VLAN interfaces were created on top of the main bond. This allows the router to see tagged traffic for each distinct VLAN.

```
/interface vlan
add name=vlan11-prod vlan-id=11 interface=bond-to-SG3428X
add name=vlan12-prod vlan-id=12 interface=bond-to-SG3428X
add name=vlan13-prod-res vlan-id=13 interface=bond-to-SG3428X
add name=vlan14-prod-wifi vlan-id=14 interface=bond-to-SG3428X
add name=vlan15-prod-mon vlan-id=15 interface=bond-to-SG3428X
add name=vlan21-stage vlan-id=21 interface=bond-to-SG3428X
add name=vlan22-stage vlan-id=22 interface=bond-to-SG3428X
add name=vlan23-stage-res vlan-id=23 interface=bond-to-SG3428X
add name=vlan24-stage-wifi vlan-id=24 interface=bond-to-SG3428X
add name=vlan25-stage-mon vlan-id=25 interface=bond-to-SG3428X
add name=vlan31-studio vlan-id=31 interface=bond-to-SG3428X
add name=vlan32-studio vlan-id=32 interface=bond-to-SG3428X
add name=vlan33-studio-srv vlan-id=33 interface=bond-to-SG3428X
add name=vlan34-studio-wifi vlan-id=34 interface=bond-to-SG3428X
add name=vlan35-studio-mon vlan-id=35 interface=bond-to-SG3428X
add name=vlan41-workshop vlan-id=41 interface=bond-to-SG3428X
add name=vlan42-workshop-res vlan-id=42 interface=bond-to-SG3428X
add name=vlan43-workshop-res vlan-id=43 interface=bond-to-SG3428X
add name=vlan44-workshop-wifi vlan-id=44 interface=bond-to-SG3428X
add name=vlan45-workshop-mon vlan-id=45 interface=bond-to-SG3428X
add name=vlan51-mgmt vlan-id=51 interface=bond-to-SG3428X
add name=vlan52-mgmt-res vlan-id=52 interface=bond-to-SG3428X
add name=vlan53-mgmt-mon vlan-id=53 interface=bond-to-SG3428X
add name=vlan54-mgmt-wifi vlan-id=54 interface=bond-to-SG3428X
add name=vlan55-mgmt-mon vlan-id=55 interface=bond-to-SG3428X
add name=vlan61-guest vlan-id=61 interface=bond-to-SG3428X
add name=vlan62-guest-res vlan-id=62 interface=bond-to-SG3428X
add name=vlan63-guest-res vlan-id=63 interface=bond-to-SG3428X
add name=vlan64-guest-wifi vlan-id=64 interface=bond-to-SG3428X
add name=vlan65-guest-mon vlan-id=65 interface=bond-to-SG3428X
```

### 3. Gateway IP Assignment

An IP address was assigned to each VLAN interface, establishing the MikroTik CRS520 as the gateway for each respective network.

```
/ip address
add address=10.20.11.1/24 interface=vlan11-prod
add address=10.20.12.1/24 interface=vlan12-prod
add address=10.20.13.1/24 interface=vlan13-prod-res
add address=10.20.14.1/24 interface=vlan14-prod-wifi
add address=10.20.15.1/24 interface=vlan15-prod-mon
add address=10.20.21.1/24 interface=vlan21-stage
add address=10.20.22.1/24 interface=vlan22-stage
add address=10.20.23.1/24 interface=vlan23-stage-res
add address=10.20.24.1/24 interface=vlan24-stage-wifi
add address=10.20.25.1/24 interface=vlan25-stage-mon
add address=10.20.31.1/24 interface=vlan31-studio
add address=10.20.32.1/24 interface=vlan32-studio
add address=10.20.33.1/24 interface=vlan33-studio-srv
add address=10.20.34.1/24 interface=vlan34-studio-wifi
add address=10.20.35.1/24 interface=vlan35-studio-mon
add address=10.20.41.1/24 interface=vlan41-workshop
add address=10.20.42.1/24 interface=vlan42-workshop-res
add address=10.20.43.1/24 interface=vlan43-workshop-res
add address=10.20.44.1/24 interface=vlan44-workshop-wifi
add address=10.20.45.1/24 interface=vlan45-workshop-mon
add address=10.20.51.1/24 interface=vlan51-mgmt
add address=10.20.52.1/24 interface=vlan52-mgmt-res
add address=10.20.53.1/24 interface=vlan53-mgmt-mon
add address=10.20.54.1/24 interface=vlan54-mgmt-wifi
add address=10.20.55.1/24 interface=vlan55-mgmt-mon
add address=10.20.61.1/24 interface=vlan61-guest
add address=10.20.62.1/24 interface=vlan62-guest-res
add address=10.20.63.1/24 interface=vlan63-guest-res
add address=10.20.64.1/24 interface=vlan64-guest-wifi
add address=10.20.65.1/24 interface=vlan65-guest-mon
```