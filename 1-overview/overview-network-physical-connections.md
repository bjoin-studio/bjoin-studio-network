The internet connection enters the building via a cable modem. This modem connects to the internal network infrastructure using RJ45 plugs and CAT6 plenum-rated cable, suitable for installation in flame-retardant ceiling spaces.

The internet connection is specifically routed to a 1Gb Ethernet port on a 4x 1Gb Ethernet PCIe Host Bus Adapter (HBA) installed in an HP Z620 workstation. This port is managed by an OPNsense virtual machine running on the HP Z620, and it is configured for DHCPv4 to automatically negotiate network settings with the internet modem.

The remaining three 1Gb Ethernet ports on this HBA are currently available for future network expansion or for multiplexing additional internet connections.

From the OPNsense virtual machine, internal network traffic is routed through a 10Gb Ethernet port on a Solarflare 10Gb Ethernet PCIe Host Bus Adapter (HBA) to port sfp28-1 of the core network switch. This port acts as the LAN interface for the OPNsense virtual machine, providing a 10Gb firewall capability. This connection utilizes appropriate cabling for 10Gb Ethernet.

The core network switch, a Mikrotik CRS520-4XS-16XQ-RM, features 16 x 100Gb Ethernet ports, four 25Gb SFP28 ports, a single RJ45 console port, and two RJ45 management ports.

One of the 100Gb Ethernet ports on the core switch (specifically `qsfp28-1`) is broken out into four 10Gb SFP+ connections (`qsfp28-1-1`, `qsfp28-1-2`, `qsfp28-1-3`, and `qsfp28-1-4`) using a QSFP to 4x 10Gb SFP+ breakout cable. These four 10Gb SFP+ connections are then connected to the four 10Gb SFP+ ports on a TP-Link SG3428X switch.

Another 100Gb Ethernet port on the core switch (specifically `qsfp28-2`) is similarly broken out into four 10Gb SFP+ connections (`qsfp28-2-1`, `qsfp28-2-2`, `qsfp28-2-3`, and `qsfp28-2-4`) using a QSFP to 4x 10Gb SFP+ breakout cable. These four 10Gb SFP+ connections are then connected to the first four 10Gb SFP+ ports on a Sodola KT-NOS SL-SWTGW2C8F 8-port 10Gb Ethernet managed switch.