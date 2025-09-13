# Insights for Working with MikroTik RouterOS

This document consolidates key learnings, best practices, and configuration patterns discovered while implementing MikroTik devices in the bjoin.studio network.

## 1. L3 Routing and IP Configuration

### Insight: Avoid IP Conflicts on a Single Subnet

A router cannot have two distinct interfaces with IP addresses in the same subnet. This creates routing ambiguity, where the router has two equal-cost paths to the same network, leading to unpredictable behavior like failed ARP requests and intermittent connectivity.

**Best Practice:** Ensure every IP subnet on a router is reachable through only one logical interface.

### Insight: Use Dedicated Transit Networks for Inter-Switch Links

For routed links between core network devices (like a switch-to-switch link), creating a dedicated "transit" network is the most stable and secure approach.

**Best Practice:**
1.  Create a new, dedicated VLAN (e.g., VLAN 4090).
2.  Use a small, dedicated subnet (e.g., a `/30` subnet like `10.254.254.0/30`) exclusively for this link.
3.  This isolates the critical link from other networks (like the main management VLAN) and provides clarity and stability.

### Insight: Assign IPs to VLAN Interfaces, Not Physical Ports

On MikroTik devices (and other L3 switches), IP addresses for tagged traffic are not assigned directly to physical ports or LACP bond interfaces.

**Correct Procedure:**
1.  Create the LACP bond or identify the physical interface.
2.  Create a virtual "VLAN Interface" on top of that bond/physical interface.
3.  Assign the gateway IP address to the virtual VLAN interface.

**Example:**
```
# Create a VLAN interface for VLAN 51 on the main bond
/interface vlan
add name=vlan51-mgmt vlan-id=51 interface=bond-to-SG3428X

# Assign the gateway IP to that VLAN interface
/ip address
add address=10.20.51.1/24 interface=vlan51-mgmt
```

## 2. LACP Bond (LAG) Configuration

### Insight: Use 'arp' for Reliable Link Monitoring

The default `link-monitoring=mii` setting on a MikroTik bond is not always reliable. It only checks for a physical carrier signal and can report a link as "RUNNING" even if LACP negotiation has failed.

**Best Practice:** Use `link-monitoring=arp`. This provides robust Layer 3 monitoring by sending ARP requests to a target IP on the other side of the link, ensuring the link is actually capable of passing traffic.

**Example:**
```
/interface bonding
# Set monitoring to ARP and specify the target IP
set [find name=bond-to-SG3428X] link-monitoring=arp arp-ip-targets=10.254.254.2
```

### Insight: Start with a Clean Slate for Bond Members

Before adding physical interfaces to a bond, ensure they are not part of any other configuration, such as the default bridge.

**Correct Procedure:**
1.  Identify the interfaces to be bonded (e.g., `qsfp28-1-1`, `qsfp28-1-2`).
2.  Remove them from the default bridge.
3.  Create the bond using these now-free interfaces.

**Example:**
```
/interface bridge port
remove [find interface=qsfp28-1-1]
remove [find interface=qsfp28-1-2]

/interface bonding
add name=my-bond mode=802.3ad slaves=qsfp28-1-1,qsfp28-1-2
```

## 3. Physical Layer Considerations

### Insight: Match Interface Settings to Cable Type

When using breakout cables, you must know whether you are using Direct Attach Copper (DAC) or Active Optical Cables (AOC) and configure the MikroTik port accordingly.

*   **DAC (Copper):** Use the `10G-baseCR` setting.
*   **AOC (Fiber):** Use the `10G-baseSR/LR` setting.

**Lesson:** Mismatched physical layer settings can prevent a link from coming up. Always verify the cable type.
