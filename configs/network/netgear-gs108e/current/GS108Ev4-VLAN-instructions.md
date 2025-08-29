4
Use VLANS for Traffic Segmentation
This chapter describes how you can use virtual LANS (VLANs) to segment traffic on the
switch. It contains these sections:
• Types of supported VLANs
• Manage basic port-based VLANs
• Manage advanced port-based VLANs
• Manage basic 802.1Q VLANs
• Manage advanced 802.1Q VLANs
• Deactivate a port-based or 802.1Q VLAN mode and delete configured VLANs
32
Gigabit Ethernet Plus Switch Model GS108Ev4
Types of supported VLANs
VLANs offer many benefits, such as enhanced security, improved load balancing, better
use of shared resources, and more efficient network management. You can set up one
or more VLANs (virtual local area networks) on your switch to group networked member
devices together as an isolated network.
To start, choose which VLAN mode you want to enable for all the VLANs that you want
to set up on the switch. Select one of the following port-based or tag-based VLAN
modes, listed in order from the simplest to the most advanced:
• Port-based VLANs: For each port-based VLAN, you select the switch ports that you
want to be members of the VLAN, which creates a virtual network consisting of all
the devices connected to the member ports.
You can use port-based VLANs when this is the only switch in your network that
supports VLANs, and the VLAN does not need to function across multiple network
devices such as a router, a WiFi AP, or other network device that supports VLANs.
The switch supports the following port-based VLAN modes:
○ Basic Port-Based VLAN: If each port (except the uplink port) only needs to belong
to a single VLAN, you can use basic port-based VLANs. The number of basic
port-based VLANs can be equal to, or less than, the number of ports on the switch.
To set up a basic port-based VLAN, you assign the same VLAN ID to one or more
ports.
○ Advanced Port-Based VLAN: If you want a port to belong to multiple VLANs,
you can use the advanced port-based VLAN mode. To set up an advanced
port-based VLAN, you assign the same VLAN ID to one or more ports to make
them members of this VLAN. You can also assign other VLAN IDs to these ports
to make them members of other VLANs.
• 802.1Q VLANs (tag-based): Tagged VLANs are more powerful than port-based
VLANs, and the switch can support many more tagged VLANs than port-based
VLANs. The switch supports the IEEE 802.1Q standard, and tags Ethernet frames to
route VLAN traffic. When a port receives an Ethernet frame tagged for a specific
VLAN, the port accepts the data if the port is a member of that VLAN. If not, then it
discards the data.
You can also use 802.1Q VLANs to route traffic from the switch to another network
device on your LAN (or even outside your LAN) by configuring 802.1Q VLANs on
both network devices and using the same VLAN ID. If you need a VLAN to function
across multiple network devices (such as a router, another switch, a WiFi AP), we
recommend that you use an 802.1Q VLAN.
The switch supports the following 802.1Q VLAN modes:
Use VLANS for Traffic
Segmentation
33
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
○ Basic 802.1Q VLAN: If you do not need custom tagging on a port, you can use
the basic 802.1Q VLAN mode. When you enable basic 802.1Q VLAN mode,
VLAN 1 is added to the switch and all ports are assigned as access members of
VLAN 1. A port that functions in access mode can belong to a single VLAN only,
and does not tag the traffic that it processes. You can assign access ports to
different VLANs, or change a port to trunk mode so that it automatically belongs
to all VLANs on the switch and tags the traffic that it processes.
○ Advanced 802.1Q VLAN: If you need custom tagging on a port, or want to set
up a voice VLAN, you must use advanced 802.1Q VLAN mode. When you enable
advanced 802.1Q VLAN mode, VLAN 1 is added to the switch and all ports are
assigned as untagged members of VLAN 1. You can tag or untag ports, remove
ports, add more VLANs, assign ports to different VLANs, and manage port PVIDs.
The following table provides an overview of VLAN features that are supported on the
switch.
Table 3. Supported VLAN modes
VLAN Feature
Basic
Port-Based VLAN
Advanced
Port-Based VLAN
Basic
802.1Q VLAN
Advanced
802.1Q VLAN
Total number of
VLANs
Egress tagging
Multiple VLANs on a
single port
Voice VLAN
8
No
No
No
8
No
Yes
No
8
Yes (trunk port only)
Yes (trunk port only)
No
64
Yes
Yes
Yes
Manage basic port-based VLANs
By default, VLANs are disabled on the switch. When you activate Basic Port-Based VLAN
mode, VLANs are added to the switch, and all ports are made members of VLAN 1. This
is the default VLAN in the Basic Port-Based VLAN mode.
In the Basic Port-Based VLAN mode, you can assign each port (other than the uplink
port) to a single VLAN only.
To activate the Basic Port-Based VLAN mode and assign VLANs:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
Use VLANS for Traffic
Segmentation
34
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QOS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the Basic Port-Based VLAN section, click the ACTIVATE MODE button.
A pop-up window opens, informing you that the current VLAN settings will be lost.
7. Click the CONTINUE button.
Your settings are saved and the pop-up window closes. By default, all VLANs are
added and each port is a member of VLAN 1.
8. To assign one or more ports to other VLANs, do the following:
a. For each port that you want to assign to another VLAN, select a VLAN ID from
the VLAN menu for the individual port.
Each port can be assigned to a single VLAN only. However, for the port that you
want to use as the uplink port to the Internet connection or a server, select All
from the VLAN menu for the individual port.
b. Click the APPLY button.
Your settings are saved.
Manage advanced port-based
VLANs
In an advanced port-based VLAN configuration, ports with the same VLAN ID are placed
into the same VLAN, but you can assign a single port to multiple VLANs.
For more information about port-based VLANs, see the following sections:
• Activate the Advanced Port-Based VLAN mode
• Create an advanced port-based VLAN
• Change an advanced port-based VLAN
• Delete an advanced port-based VLAN
Use VLANS for Traffic
Segmentation
35
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Activate the Advanced Port-Based VLAN
mode
By default, all types of VLANs are disabled on the switch.
When you activate the Advanced Port-Based VLAN mode, VLAN 1 is added to the switch
and all ports are made members of VLAN 1. This is the default VLAN in the Advanced
Port-Based VLAN mode.
To activate the Advanced Port-Based VLAN mode:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the Advanced Port-Based VLAN section, click the ACTIVATE MODE button.
A pop-up window opens, informing you that the current VLAN settings will be lost.
7. Click the CONTINUE button.
Your settings are saved and the pop-up window closes. By default, VLAN 1 is added
and all ports are members of VLAN 1.
Create an advanced port-based VLAN
An advanced port-based VLAN configuration lets you create VLANs and assign ports
on the switch to a VLAN. The number of VLANs is limited to the number of ports on the
switch. In an advanced port-based VLAN configuration, one port can be a member of
multiple VLANs.
By default, all ports are members of VLAN 1, but you can change the VLAN assignment.
Use VLANS for Traffic
Segmentation
36
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To create an advanced port-based VLAN and assign ports as members:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
If you did not yet activate the Advanced Port-Based VLAN mode, see Activate the
Advanced Port-Based VLAN mode on page 36.
6. 7. In the Advanced Port-Based VLAN section, click the ADD VLAN button.
Specify the settings for the new VLAN:
• VLAN Name: Enter a name from 1 to 14 characters.
• VLAN ID: Enter a number from 1 to the total number of ports on the switch.
• Ports: Select the ports that you want to include in the VLAN through a combination
of the following actions:
○ Click the icon for an unselected port to add the port to the VLAN.
○ Click the icon for a selected port to remove the port from the VLAN.
○ Click the Select All link to add all ports to the VLAN.
○ Click the Remove All link to remove all selected ports from the VLAN.
The icon for a selected port displays purple.
NOTE: If ports are members of the same link aggregation group (LAG), you
must assign them to the same VLAN. For more information, see Set up static
link aggregation on page 57.
8. Click the APPLY button.
Your settings are saved. The new VLAN is added to the VLAN table, which shows
the port members for each VLAN.
Use VLANS for Traffic
Segmentation
37
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Change an advanced port-based VLAN
You can change the settings for an existing advanced port-based VLAN.
To change an advanced port-based VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the Advanced Port-Based VLAN section, click the VLAN that you want to change
(you can click anywhere in the row for the VLAN) and click the EDIT button.
The Advanced Port-Based VLAN pane displays.
7. Change the settings for the VLAN:
• VLAN Name: Enter a name from 1 to 14 characters.
You cannot change the VLAN ID. If you need to change the VLAN ID, delete the
VLAN and create a new VLAN with another VLAN ID.
• Ports: Select the ports that you want to include in the VLAN through a combination
of the following actions:
○ Click the icon for an unselected port to add the port to the VLAN.
○ Click the icon for a selected port to remove the port from the VLAN.
○ Click the Select All link to add all ports to the VLAN.
○ Click the Remove All link to remove all selected ports from the VLAN.
The icon for a selected port displays purple.
NOTE: If ports are members of the same LAG, you must assign them to the
same VLAN.
8. Click the APPLY button.
Your settings are saved. The modified VLAN shows in the VLAN table.
Use VLANS for Traffic
Segmentation
38
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Delete an advanced port-based VLAN
You can delete an advanced port-based VLAN that you no longer need. You cannot
delete the default VLAN.
NOTE: If you deactivate the basic or advanced port-based VLAN mode, all
port-based VLANs are deleted.
To delete an advanced port-based VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the Advanced Port-Based VLAN section, click the VLAN that you want to delete
(you can click anywhere in the row for the VLAN).
7. Click the DELETE button.
Your settings are saved. The VLAN is deleted.
Manage basic 802.1Q VLANs
In a basic 802.1Q VLAN configuration, VLAN 1 is added to the switch and all ports
function in access mode as members of VLAN 1. You can change the mode for a port
to trunk mode, you can add more VLANs, and you can assign a different VLAN to a port.
After you activate the Basic 802.1Q VLAN mode, you can create VLANs, assign the
VLANs to ports that function in access mode, and assign the trunk mode, which carries
traffic for all VLANs.
For more information about basic 802.1Q VLANs, see the following sections:
• Activate the Basic 802.1Q VLAN mode
Use VLANS for Traffic
Segmentation
39
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
• Create a basic 802.1Q VLAN and assign ports as members
• Assign the port mode in a basic 802.1Q VLAN configuration
• Change a basic 802.1Q VLAN
• Delete a basic 802.1Q VLAN
Activate the Basic 802.1Q VLAN mode
By default, all types of VLANs are disabled on the switch.
When you activate the Basic 802.1Q VLAN mode, VLAN 1 is added to the switch and
all ports function in access mode (rather than trunk mode) as untagged members of
VLAN 1. This is the default VLAN in the Basic 802.1Q VLAN mode.
To activate the Basic 802.1Q VLAN mode:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The QOS page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the Basic 802.1Q VLAN section, click the ACTIVATE MODE button.
A pop-up window opens, informing you that the current VLAN settings will be lost.
7. Click the CONTINUE button.
Your settings are saved and the pop-up window closes. By default, VLAN 1 is added.
For information about adding VLANs, see Change a basic 802.1Q VLAN on page
44.
For all ports, the default selection from the Mode menu is Access. For more
information about access mode and trunk mode, see Assign the port mode in a basic
802.1Q VLAN configuration on page 42.
Use VLANS for Traffic
Segmentation
40
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
8. If you already determined which ports must function in trunk mode, for those ports,
select Trunk (uplink) from the Mode menu.
9. Click the SAVE button.
Your settings are saved.
Create a basic 802.1Q VLAN and assign
ports as members
A basic 802.1Q VLAN configuration lets you create VLANs and assign ports on the switch
to a VLAN. A port that functions in access mode can be a member of a single VLAN
only. The number of VLANs is limited to the number of ports on the switch. You can
assign a VLAN ID number in the range of 1–4093.
To create a basic 802.1Q VLAN and assign ports as members:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
If you did not yet activate the Basic 802.1Q VLAN mode, see Activate the Basic
802.1Q VLAN mode on page 40.
By default, the Port Configuration tab is selected and the 802.1Q-BASED PORT
CONFIGURATION pane displays.
6. To add a VLAN and then assign ports as members of the VLAN, do the following:
a. Click the Edit VLAN button.
The 802.1Q-BASED VLAN CONFIGURATIONS (BASIC MODE) pane displays.
Click the ADD VLAN button.
The BASIC 802.1Q VLAN pop-up window opens.
c. In the VLAN Name field, enter a name from 1 to 14 characters.
Use VLANS for Traffic
Segmentation
41
b. User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
d. In the VLAN ID field, enter a number from 1 to 4093.
e. Click the APPLY button.
Your settings are saved. The new VLAN shows in the 802.1Q-BASED VLAN
CONFIGURATIONS (BASIC MODE) pane.
f. Click the Port Configuration tab.
The 802.1Q PORT CONFIGURATIONS pane displays
g. For each port that you want to make a member of the new VLAN, select the VLAN
from the VLAN menu for the individual port.
7. NOTE: If ports are members of the same LAG, you must assign them to
the same VLAN.
For a port that functions in access mode, to add a VLAN by using the VLAN menu
for the individual port, do the following:
a. From the VLAN menu for the individual port, select Add VLAN.
The BASIC 802.1Q VLAN pop-up window opens.
b. c. In the VLAN Name field, enter a name from 1 to 14 characters.
In the VLAN ID field, enter a number from 1 to 4093.
d. Click the APPLY button.
The pop-up window closes. The VLAN is added as a possible selection in the
VLAN menu for each individual port.
e. For each port that you want to make a member of the new VLAN, select the VLAN
from the VLAN menu for the individual port.
NOTE: the same VLAN.
8. Click the SAVE button.
Your settings are saved.
If ports are members of the same LAG, you must assign them to
NOTE: For information about assigning the port mode, see Assign the port
mode in a basic 802.1Q VLAN configuration on page 42.
Assign the port mode in a basic 802.1Q
VLAN configuration
In an 802.1Q VLAN configuration, you can assign one of the following port modes:
• Access mode: A port that functions in access mode can belong to a single VLAN
only, and does not tag the traffic that it processes. You would typically use access
Use VLANS for Traffic
Segmentation
42
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
mode for a port that is connected to an end device such as a gaming device, media
device, or computer. When a port that functions in access mode receives data that
is untagged, the data is delivered normally. When a port that functions in access
mode receives data that is tagged for a VLAN other than the one the port belongs
to, the data is discarded.
• Trunk mode: A port that functions in trunk mode automatically belongs to all VLANs
on the switch and tags the traffic that it processes. You would typically use trunk
mode for a port that is connected to another network device. For example, you
would assign trunk mode for an uplink to another switch or router and for a downlink
to a WiFi access point.
To assign the port mode:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
If you did not yet activate the Basic 802.1Q VLAN mode, see Activate the Basic
802.1Q VLAN mode on page 40.
By default, the Port Configuration tab is selected and the 802.1Q-BASED PORT
CONFIGURATION pane displays.
6. For each individual port that you want to change, from the Mode menu, select either
Trunk (uplink) to let the port function in trunk mode or Access to let the port function
in access mode.
If you place a port in trunk mode, the selection from the VLAN menu changes to All
because all VLANs must be supported on a trunk port.
7. Click the SAVE button.
Your settings are saved.
Use VLANS for Traffic
Segmentation
43
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Change a basic 802.1Q VLAN
You can change an existing basic 802.1Q VLAN.
To change a basic 802.1Q VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
By default, the Port Configuration tab is selected and the 802.1Q-BASED PORT
CONFIGURATION pane displays.
6. To change the name for the VLAN, do the following:
a. Click the Edit VLAN button.
The 802.1Q-BASED VLAN CONFIGURATIONS (BASIC MODE) pane displays.
b. Click the VLAN that you want to change (you can click anywhere in the row for
the VLAN).
c. Click the EDIT button.
The BASIC 802.1Q VLAN pop-up window opens.
d. Change the VLAN name.
You cannot change the VLAN ID. If you need to change the VLAN ID, delete the
VLAN and create a new VLAN with another VLAN ID.
e. Click the APPLY button.
Your settings are saved. The modified VLAN shows in the 802.1Q-BASED VLAN
CONFIGURATIONS (BASIC MODE) pane.
7. To change the membership of the VLAN, for each port that you want to make a
member, select the VLAN from the VLAN menu for the individual port in the
802.1Q-BASED PORT CONFIGURATION pane.
8. Click the SAVE button.
Use VLANS for Traffic
Segmentation
44
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Your settings are saved.
Delete a basic 802.1Q VLAN
You can delete a basic 802.1Q VLAN that you no longer need. You cannot delete the
default VLAN.
NOTE: If you deactivate the Basic 802.1Q VLAN mode, all 802.1Q VLANs are
deleted.
To delete a basic 802.1Q VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. Click the Edit VLAN button.
The 802.1Q-BASED VLAN CONFIGURATIONS (BASIC MODE) pane displays.
7. Click the VLAN that you want to delete.
You can click anywhere in the row for the VLAN
8. Click the DELETE button.
Your settings are saved. The VLAN is deleted.
Manage advanced 802.1Q VLANs
Advanced 802.1Q VLANs provide many options. You can tag ports, untag ports, exclude
ports, add more VLANs, assign a different VLAN to a port, manage port PVIDs. When
you enable advanced 802.1Q VLAN, VLAN 1 is created on the switch, and all ports
become untagged members of VLAN 1.
Use VLANS for Traffic
Segmentation
45
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
You can set up special-purpose VLANs like a voice VLAN. When you create a
special-purpose VLAN, the default Organizationally Unique Identifiers (OUI) table lists
OUI values associated with devices from specific manufacturers. When the switch detects
a known OUI in network traffic traffic on a port that belongs to a special-purpose VLAN,
it routes traffic coming from the device to the appropriate VLAN.
For more information about setting up advanced 802.1Q VLANs, see the following
sections:
• Activate the advanced 802.1Q VLAN mode
• Create an advanced 802.1Q VLAN
• Change an advanced 802.1Q VLAN
• Specify a port PVID for an advanced 802.1Q VLAN
• Set an existing advanced 802.1Q VLAN as the voice VLAN and adjust the CoS value
• Edit the OUI table for the voice VLAN
• Delete an advanced 802.1Q VLAN
Activate the advanced 802.1Q VLAN mode
By default, all types of VLANs are disabled on the switch.
When you activate the Advanced 802.1Q VLAN mode, VLAN 1 is added to the switch
and all ports function as untagged members of VLAN 1. This is the default VLAN in the
Advanced 802.1Q VLAN mode.
In an advanced 802.1Q VLAN configuration, you can set up VLANs to which you can
add tagged or untagged ports. Port tagging allows a port to be associated with a
particular VLAN and allows the VLAN ID tag to be added to data packets that are sent
through the port. The tag identifies the VLAN that must receive the data. You can also
manage the VLAN IDs (PVIDs) of the ports (see Specify a port PVID for an advanced
802.1Q VLAN on page 50).
To activate the Advanced 802.1Q VLAN mode and manage port tagging for the
default VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
3. Use VLANS for Traffic
Segmentation
46
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The QOS page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the Advanced 802.1Q VLAN section, click the ACTIVATE MODE button.
A pop-up window opens, informing you that the current VLAN settings will be lost.
7. Click the CONTINUE button.
Your settings are saved and the pop-up window closes. By default, VLAN 1 is added
and all ports are made untagged members of VLAN 1.
For information about creating an advanced 802.1Q VLAN, see Create an advanced
802.1Q VLAN on page 47.
8. To change the port tagging for a VLAN, do the following:
a. In the table, click the VLAN that you want to edit (you can click anywhere in the
row).
b. Click the EDIT button.
c. Select the port tags and whether ports are members of the VLAN through a
combination of the following actions:
• T: Make the port a tagged member of the VLAN.
• U: Make the port an untagged member of the VLAN.
• E: Exclude the port from the VLAN.
• Tag All: Make all ports tagged members of the VLAN.
• Untag All: Make all ports untagged members of the VLAN.
• Exclude All: Exclude ports from the VLAN.
d. Click the APPLY button.
Your settings are saved.
Create an advanced 802.1Q VLAN
In an advanced 802.1Q VLAN configuration, you can set up VLANs to which you can
add tagged or untagged ports. Port tagging allows a port to be associated with a
particular VLAN and allows the VLAN ID tag to be added to data packets that are sent
through the port. You can create a total of 64 advanced 802.1Q VLANs for these switches.
Use VLANS for Traffic
Segmentation
47
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To create an advanced 802.1Q VLAN and assign ports as tagged or untagged
members:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
If you did not yet activate the Advanced 802.1Q VLAN mode, see Activate the
advanced 802.1Q VLAN mode on page 46.
6. In the right pane, click the ADD VLAN button.
The Advanced 802.1Q VLAN pane displays.
7. Specify the VLAN settings and assign ports as tagged or untagged members:
a. In the VLAN Name field, enter a name from 1 to 14 characters.
b. In the VLAN ID field, enter a number from 1 to 4093.
c. Use a combination of the following options to select port tags and set whether
ports are members of the VLAN:
• T: Make the port a tagged member of the VLAN.
• U: Make the port an untagged member of the VLAN.
• E: Exclude the port from the VLAN.
• Tag All: Make all ports tagged members of the VLAN.
• Untag All: Make all ports untagged members of the VLAN.
• Exclude All: Exclude ports from the VLAN.
NOTE: If ports are members of the same LAG, you must assign them to
the same VLAN.
8. Click the APPLY button.
Your settings are saved. The new VLAN shows in the Advanced 802.1Q VLAN pane.
Use VLANS for Traffic
Segmentation
48
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Change an advanced 802.1Q VLAN
You can change the settings for an existing advanced 802.1Q VLAN.
To change an advanced 802.1Q VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the table in the right pane, click the VLAN that you want to change (you can click
anywhere in the row for the VLAN).
7. Click the EDIT button.
8. Change the VLAN settings as needed:
• In the VLAN Name field, enter a name from 1 to 14 characters.
You cannot change the VLAN ID. If you need to change the VLAN ID, delete the
VLAN and create a new VLAN with another VLAN ID.
• Use a combination of the following options to select port tags and set whether
ports are members of the VLAN:
○ T: Make the port a tagged member of the VLAN.
○ U: Make the port an untagged member of the VLAN.
○ E: Exclude the port from the VLAN.
○ Tag All: Make all ports tagged members of the VLAN.
○ Untag All: Make all ports untagged members of the VLAN.
○ Exclude All: Exclude ports from the VLAN.
9. Click the APPLY button.
Your settings are saved. The modified VLAN shows in the Advanced 802.1Q VLAN
pane.
Use VLANS for Traffic
Segmentation
49
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Specify a port PVID for an advanced 802.1Q
VLAN
A default port VLAN ID (PVID) is a VLAN ID tag that the switch assigns to incoming data
packets that are not already addressed (tagged) for a particular VLAN. For example, if
you connect a computer to port 6 of the switch and you want it to be a part of VLAN 2,
add port 6 as a member of VLAN 2 and set the PVID of port 6 to 2. This configuration
automatically adds a PVID of 2 to all data that the switch receives from the computer
and makes sure that the data from the computer on port 6 can be seen only by other
members of VLAN 2. You can assign only one PVID to a port.
NOTE: If you did not yet create an advanced 802.1Q VLAN, all ports are assigned
PVID 1 and you cannot assign another PVID to a port. In this situation, first create
an advanced 802.1Q VLAN (see Create an advanced 802.1Q VLAN on page 47).
To assign a PVID to a port:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
If you did not yet activate the Advanced 802.1Q VLAN mode, see Activate the
advanced 802.1Q VLAN mode on page 46.
6. In PVID Table section in the right pane, click the PVID Table link.
The Port and VLAN IDs pane displays.
7. Click the icon for a port.
A menu displays. The menu lets you select a PVID for the port.
8. From the menu, select a VLAN ID and name.
You can select only a VLAN that the selected port is a member of.
9. Click the APPLY button.
Use VLANS for Traffic
Segmentation
50
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Your settings are saved. The Port and VLAN IDs pane displays again. The VLAN ID
that is assigned as the PVID displays with an asterisk (*) next to the port.
10. Click the BACK button.
The Advanced 802.1Q VLAN pane displays.
Set an existing advanced 802.1Q VLAN as
the voice VLAN and adjust the CoS value
The switch can support a single advanced 802.1Q VLAN as the voice VLAN to facilitate
voice over IP (VoIP) traffic. Because a voice VLAN might require a single port to join to
multiple VLANs as an untagged member, you can set up a voice VLAN only as an
advanced 802.1Q VLAN. For information about creating an advanced 802.1Q VLAN,
see Create an advanced 802.1Q VLAN on page 47.
A port that is a member of the voice VLAN sends any packet with the first 3 bytes of the
MAC addresses listed in the OUI table through the voice VLAN. Other types of packets
(for example, data packets) that enter the port are forwarded according to the 802.1Q
VLAN ID in the packet and the PVID setting on the port.
The default Class of Service (CoS) value for the voice VLAN is 6, which you can adjust
to any value from 0 (the lowest priority) to 7 (the highest priority). The voice VLAN CoS
value applies to all traffic on the voice VLAN. You can set the default VLAN (VLAN 1) as
the voice VLAN if you want.
To set an existing advanced 802.1Q VLAN as the voice VLAN and adjust the CoS
value for the voice VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
Use VLANS for Traffic
Segmentation
51
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
If you did not yet activate the Advanced 802.1Q VLAN mode, see Activate the
advanced 802.1Q VLAN mode on page 46.
6. In the Advanced 802.1Q VLAN table in the right pane, click the VLAN that you want
to make the voice VLAN.
You can click anywhere in the row to select the VLAN.
7. Click the EDIT button.
8. In the Voice VLAN section, turn on the voice VLAN toggle.
When the voice VLAN is enabled, the toggle displays green and is positioned on
the right.
9. From the Class of Service menu, select a CoS value.
A value of 0 is the lowest priority and a value of 7 is the highest priority. The default
value is 6.
10. View the OUI values to verify that your voice over IP (VoIP) device manufacturers are
listed.
For information about viewing and changing the OUI settings, see Edit the OUI table
for the voice VLAN on page 52.
11. Click the APPLY button.
Your settings are saved. The voice VLAN shows in the Advanced 802.1Q VLAN pane
with a telephone icon.
Edit the OUI table for the voice VLAN
The voice VLAN is a specialized advanced 802.1Q VLAN that uses a configurable list of
Organizationally Unique Identifiers (OUI) to recognize VoIP phones from specific
manufacturers. When a switch port that is a member of the voice VLAN receives a packet,
it searches the voice VLAN's OUI table to see whether the originating device is listed,
and if so, the port forwards the packet to the voice VLAN. In this way, the OUI table
helps voice VLAN member ports forward all voice traffic from VoIP phones to the voice
VLAN.
You can add, edit, and remove OUIs from the table, including default OUIs. The maximum
number of OUI entries in the table is 15. The first 3 bytes of the MAC address contain
the manufacturer identifier, and the last 3 bytes contain a unique station identifier. The
OUI prefix must use the format AA:BB:CC.
To edit the OUI table for the voice VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
Use VLANS for Traffic
Segmentation
52
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. 8. In the table in the right pane, click Advanced 802.1Q VLAN.
7. Click the EDIT button.
In the OUI Table section, click the OUI Settings link.
The Voice VLAN pane displays and shows the OUI table.
9. To add a new OUI, do the following:
a. Click the ADD OUI button.
The OUI Entry page displays.
b. Enter the new OUI and description.
c. Click the APPLY button.
Your settings are saved.
10. To change an existing OUI, do the following:
a. Select the OUI that you want to change and click the EDIT button.
b. Change the OUI, the description, or both.
c. Click the APPLY button.
Your settings are saved.
11. To delete an OUI that you no longer need, select the OUI and click the DELETE
button.
Your settings are saved and the OUI is deleted.
12. Click the BACK button.
The Advanced 802.1Q VLAN pane displays and shows the voice VLAN settings.
13. Click the APPLY button.
Your settings are saved.
Use VLANS for Traffic
Segmentation
53
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Delete an advanced 802.1Q VLAN
You can delete an advanced 802.1Q VLAN that you no longer need. You cannot delete
the default VLAN. You cannot delete a VLAN that is in use as the PVID for a port either.
You must first remove the VLAN as the PVID for the port before you can delete the VLAN.
NOTE: If you deactivate the Advanced 802.1Q VLAN mode, all 802.1Q VLANs
are deleted.
To delete an advanced 802.1Q VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the table in the right pane, click the VLAN that you want to delete (you can click
anywhere in the row for the VLAN).
7. Click the DELETE button.
Your settings are saved. The VLAN is deleted.
Deactivate a port-based or 802.1Q
VLAN mode and delete configured
VLANs
If you activated any of the VLAN modes, such as the Basic Port-Based VLAN mode,
Advanced Port-Based VLAN mode, Basic 802.1Q VLAN mode, or Advanced 802.1Q
VLAN mode, you can deactivate the VLAN mode and delete all VLANs.
Use VLANS for Traffic
Segmentation
54
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To deactivate VLAN mode and delete all VLANs:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select VLAN.
The VLAN page displays.
6. In the NO VLANs section, click the ACTIVATE MODE button.
A pop-up window opens, informing you that the current VLAN configuration settings
will be lost.
7. Click the CONTINUE button.
Your settings are saved, the pop-up window closes, and all VLANs are deleted.