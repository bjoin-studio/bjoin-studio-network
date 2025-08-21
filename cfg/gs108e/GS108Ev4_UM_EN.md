User Manual
Gigabit Ethernet Plus Switch
Model GS108Ev4
November 2024
202-12710-03
NETGEAR, Inc.
350 E. Plumeria Drive
San Jose, CA 95134, USA
Gigabit Ethernet Plus Switch Model GS108Ev4
Support and Community
Visit netgear.com/support to get your questions answered and access the latest
downloads.
You can also check out our NETGEAR Community for helpful advice at
community.netgear.com.
Regulatory and Legal
Si ce produit est vendu au Canada, vous pouvez accéder à ce document en français
canadien à https://www.netgear.com/support/download/.
(If this product is sold in Canada, you can access this document in Canadian French at
https://www.netgear.com/support/download/.)
For regulatory compliance information including the EU Declaration of Conformity, visit
https://www.netgear.com/about/regulatory/.
See the regulatory compliance document before connecting the power supply.
For NETGEAR’s Privacy Policy, visit https://www.netgear.com/about/privacy-policy.
By using this device, you are agreeing to NETGEAR’s Terms and Conditions at
https://www.netgear.com/about/terms-and-conditions. If you do not agree, return the
device to your place of purchase within your return period.
Do not use this device outdoors.
Applicable to 6 GHz devices only: Only use the device indoors. The operation of 6 GHz
devices is prohibited on oil platforms, cars, trains, boats, and aircraft, except that
operation of this device is permitted in large aircraft while flying above 10,000 feet.
Operation of transmitters in the 5.925-7.125 GHz band is prohibited for control of or
communications with unmanned aircraft systems.
Trademarks
© NETGEAR, Inc., NETGEAR, and the NETGEAR Logo are trademarks of NETGEAR, Inc.
Any non-NETGEAR trademarks are used for reference purposes only.
2
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Revision History
Publication Part
Number
202-12710-03
202-12710-02
Publish Date
Comments
November 2024
September 2024
202-12710-01
April 2024
We made some corrections.
• Updated Types of supported VLANs on page 33 to change the number
of Basic 8021.Q VLANs.
• Updated Use the NETGEAR Discovery Tool to discover the switch’s IP
address and access the device UI on page 15.
• Changed the NETGEAR Switch Discovery Tool to NETGEAR Discovery
Tool.
First publication.
3
User Manual
Contents
Chapter 1 Hardware
Related documentation...................................................................... 8
Switch package contents.................................................................... 8
LEDs...................................................................................................... 8
Front panel........................................................................................... 9
Back panel............................................................................................ 9
Switch label.......................................................................................... 9
Safety instructions and warnings....................................................... 9
Chapter 2 Install and Access the Switch in Your Network
Set up the switch in your network and power on the switch....... 14
Discover the switch’s IP address to access its device UI.............. 14
Use the NETGEAR Discovery Tool to discover the switch’s IP
address and access the device UI.............................................. 15
Assign a fixed IP address to the switch.......................................... 16
Set a fixed IP address for the switch through a network
connection..................................................................................... 17
Assign a fixed IP address by connecting directly to the switch
off-network.................................................................................... 18
Register the switch....................................................................... 19
Chapter 3 Optimize the Switch Performance
Set the quality of service mode and port rate limits..................... 22
Use port-based quality of service and set port priorities........ 22
Use 802.1P/DSCP quality of service........................................... 24
Manage broadcast filtering and set port storm control rate
limits............................................................................................... 25
Manage individual port settings..................................................... 26
Set rate limits for a port............................................................... 27
Set the priority for a port............................................................. 28
Manage flow control for a port................................................... 29
Change the speed for a port or disable a port......................... 29
Add or change the name label for a port.................................. 30
Chapter 4 Use VLANS for Traffic Segmentation
Types of supported VLANs.............................................................. 33
Manage basic port-based VLANs................................................... 34
Manage advanced port-based VLANs........................................... 35
Activate the Advanced Port-Based VLAN mode...................... 36
4
Gigabit Ethernet Plus Switch Model GS108Ev4
Create an advanced port-based VLAN...................................... 36
Change an advanced port-based VLAN................................... 38
Delete an advanced port-based VLAN...................................... 39
Manage basic 802.1Q VLANs.......................................................... 39
Activate the Basic 802.1Q VLAN mode..................................... 40
Create a basic 802.1Q VLAN and assign ports as members... 41
Assign the port mode in a basic 802.1Q VLAN configuration. 42
Change a basic 802.1Q VLAN.................................................... 44
Delete a basic 802.1Q VLAN...................................................... 45
Manage advanced 802.1Q VLANs................................................. 45
Activate the advanced 802.1Q VLAN mode............................. 46
Create an advanced 802.1Q VLAN............................................ 47
Change an advanced 802.1Q VLAN.......................................... 49
Specify a port PVID for an advanced 802.1Q VLAN................ 50
Set an existing advanced 802.1Q VLAN as the voice VLAN and
adjust the CoS value.................................................................... 51
Edit the OUI table for the voice VLAN....................................... 52
Delete an advanced 802.1Q VLAN............................................ 54
Deactivate a port-based or 802.1Q VLAN mode and delete
configured VLANs............................................................................. 54
Chapter 5 Manage the Switch in Your Network
Set up static link aggregation.......................................................... 57
Set up a link aggregation group................................................ 57
Make a link aggregation connection......................................... 58
Enable a link aggregation group............................................... 59
Manage multicast.............................................................................. 59
Manage IGMP snooping.............................................................. 60
Enable a VLAN for IGMP snooping............................................ 60
Manage blocking of unknown multicast addresses................. 61
Manage IGMPv3 IP header validation....................................... 62
Set up a static router port for IGMP snooping.......................... 63
Change the IP address of the switch.............................................. 63
Reenable the DHCP client of the switch......................................... 64
Chapter 6 Maintain and Monitor the Switch
Update the firmware on the switch................................................. 67
Manage the configuration file......................................................... 68
Back up the switch configuration............................................... 68
Restore the switch configuration................................................ 69
Return the switch to its factory default settings............................. 70
Use the RESET button to reset the switch................................. 70
Use the device UI to reset the switch......................................... 70
Control access to the device UI....................................................... 71
5
Gigabit Ethernet Plus Switch Model GS108Ev4
Change or lift access restrictions to the switch............................. 72
Manage the DoS prevention mode................................................ 73
Manage the power saving mode.................................................... 74
Control the port LEDs....................................................................... 75
Change the device management password................................. 75
Change the switch device name..................................................... 76
View system information.................................................................. 77
View switch connections.................................................................. 77
View the status of a port................................................................... 78
Manage NETGEAR Discovery Protocol.......................................... 78
Enable loop prevention................................................................... 79
View or clear the port statistics........................................................ 80
Enable port mirroring....................................................................... 81
Chapter 7 Diagnostics and Troubleshooting
Test cable connections..................................................................... 83
Resolve a subnet conflict to access the switch.............................. 83
Chapter 8 Additional Switch Discovery and Access Information
Access the switch from any computer............................................ 86
Appendix A Factory Default Settings and Technical Specifications
Factory default settings.................................................................... 88
Technical specifications................................................................... 88
6
1
Hardware
This user manual is for the NETGEAR Gigabit Ethernet Plus Switch model GS108Ev4.
This chapter covers the following topics:
• Related documentation
• Switch package contents
• LEDs
• Front panel
• Back panel
• Switch label
• Safety instructions and warnings
NOTE: This user manual complements the installation guide that came with
your switch. You can also download the installation guide by visiting
netgear.com/support/download/.
NOTE: For more information about the topics covered in this manual, visit the
support website at netgear.com/support.
NOTE: Firmware updates with new features and bug fixes are made available
from time to time at netgear.com/support/download/. You can manually check
for, and download, new firmware. If the features or behavior of your product do
not match what is described in this guide, see the latest firmware release notes
for your switch model.
7
Gigabit Ethernet Plus Switch Model GS108Ev4
Related documentation
The following related documentation is available at netgear.com/support/download/:
• Installation guide
• Data sheet
Switch package contents
The package contains the switch, power adapter (power cable localized to the country
of sale), wall-mount kit, and installation guide.
LEDs
This section describes the LED designations. The port LEDs are located above the ports.
Figure 1. GS108Ev4 LEDs
Table 1. Front Panel System LED
LED
Description
Power LED
Solid green: The switch is powered on and operating normally.
Solid amber: The switch is starting.
Off: Power is not supplied to the switch.
Table 2. Front Panel Port LEDs
Left port LED
Right port LED
Description
Solid green
Blinking green
Solid green
Blinking green
Off
Solid green
Blinking green
Off
Off
Solid green
1000 Mbps link on this port.
The port is transmitting or receiving packets at 1000 Mbps.
100 Mbps link is established.
The port is transmitting or receiving packets at 100 Mbps.
10 Mbps link is established.
Hardware
8
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Table 2. Front Panel Port LEDs (Continued)
Left port LED
Right port LED
Description
Off
Off
Blinking green
Off
The port is transmitting or receiving packets at 10 Mbps.
No link is established.
Front panel
The switch provides eight 10/100/1000BASE-T RJ-45 copper ports and a recessed
Factory Defaults button is provided to reset the switch back to the factory default
configuration.
Figure 2. Front panel model GS108Ev4
Back panel
The back panel provides a Kensington lock and AC power receptacle (an AC power
adapter is provided localized to the country of sale).
Switch label
The switch label on the bottom panel of the switch shows the serial number, MAC
address, and default login information of the switch.
Safety instructions and warnings
Use the following safety guidelines to ensure your own personal safety and to help
protect your system from potential damage.
Hardware
9
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To reduce the risk of bodily injury, electrical shock, fire, and damage to the equipment,
observe the following precautions:
• This product is designed for indoor use only in a temperature-controlled and
humidity-controlled environment. Note the following:
○ For more information about the environment in which this product must operate,
see the environmental specifications in the appendix or the data sheet.
○ If you want to connect the product to a device located outdoors, the outdoor
device must be properly grounded and surge protected, and you must install an
Ethernet surge protector inline between the indoor product and the outdoor
device. Failure to do so can damage the product.
○ Before connecting the product to outdoor cables or devices, see
https://kb.netgear.com/000057103 for additional safety and warranty information.
Failure to follow these guidelines can result in damage to your NETGEAR product,
which might not be covered by NETGEAR’s warranty, to the extent permissible by
applicable law.
• Observe and follow service markings:
○
Do not service any product except as explained in your product documentation.
Some devices should never be opened.
○ If applicable to your product, opening or removing covers that are marked with
the triangular symbol with a lightning bolt can expose you to electrical shock.
We recommend that only a trained technician services components inside these
compartments.
• If any of the following conditions occur, unplug the product from the power outlet,
and then replace the part or contact your trained service provider:
○ Depending on your product, the power adapter, power adapter cable, power
cable, extension cable, or plug is damaged.
○ An object fell into the product.
○ The product was exposed to water.
○ The product was dropped or damaged.
○ The product does not operate correctly when you follow the operating
instructions.
• Keep the product away from radiators and heat sources. Also, do not block cooling
vents.
• Do not spill food or liquids on your product components, and never operate the
product in a wet environment. If the product gets wet, see the appropriate section
in your troubleshooting guide, or contact your trained service provider.
• Do not push any objects into the openings of your product. Doing so can cause fire
or electric shock by shorting out interior components.
Hardware
10
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
• Use the product only with approved equipment.
• If applicable to your product, allow the product to cool before removing covers or
touching internal components.
• Operate the product only from the type of external power source indicated on the
electrical ratings label. If you are not sure of the type of power source required,
consult your service provider or local power company.
• To avoid damaging your system, if your product uses a power supply with a voltage
selector, be sure that the selector is set to match the power at your location:
○ 115V, 60 Hz in most of North and South America and some Far Eastern countries
such as South Korea and Taiwan
○ 100V, 50 Hz in eastern Japan and 100V, 60 Hz in western Japan
○ 230V, 50 Hz in most of Europe, the Middle East, and the Far East
• Be sure that attached devices are electrically rated to operate with the power available
in your location.
• Depending on your product, use only a supplied power adapter or approved power
cable:
If your product uses a power adapter:
○ If you were not provided with a power adapter, contact your local NETGEAR
reseller.
○ The power adapter must be rated for the product and for the voltage and current
marked on the product electrical ratings label.
If your product uses a power cable:
○ If you were not provided with a power cable for your system or for any
AC-powered option intended for your system, purchase a power cable approved
for your country.
○ The power cable must be rated for the product and for the voltage and current
marked on the product electrical ratings label. The voltage and current rating of
the cable must be greater than the ratings marked on the product.
• To help prevent electric shock, plug the system and peripheral power cables into
properly grounded power outlets.
• If applicable to your product, the peripheral power cables are equipped with
three-prong plugs to help ensure proper grounding. Do not use adapter plugs or
remove the grounding prong from a cable. If you must use an extension cable, use
a three-wire cable with properly grounded plugs.
• Observe extension cable and power strip ratings. Make sure that the total ampere
rating of all products plugged into the extension cable or power strip does not
exceed 80 percent of the ampere ratings limit for the extension cable or power strip.
Hardware
11
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
• To help protect your system from sudden, transient increases and decreases in
electrical power, use a surge suppressor, line conditioner, or uninterruptible power
supply (UPS).
• Position system cables, power adapter cables, or power cables carefully. Route
cables so that they cannot be stepped on or tripped over. Be sure that nothing rests
on any cables.
• Do not modify power adapters, power adapter cables, power cables or plugs. Consult
a licensed electrician or your power company for site modifications.
• Always follow your local and national wiring rules.
Hardware
12
User Manual
2
Install and Access the Switch in Your
Network
This chapter describes how you can install the switch in your network, get an IP address
for the switch, and use the IP address to access the switch's device UI so you can set up,
manage, and monitor the switch.
The chapter contains the following sections:
• Set up the switch in your network and power on the switch
• Discover the switch’s IP address to access its device UI
• Assign a fixed IP address to the switch
13
Gigabit Ethernet Plus Switch Model GS108Ev4
Set up the switch in your network
and power on the switch
Figure 3. Example connections
To set up the switch in your network and power on the switch:
1. Connect any port on the switch to a LAN port on a router that is connected to the
Internet.
2. On the switch, connect your devices to the lowest number ports, starting with port
1.
If you connect an Access Point to the switch, you must use a power adapter. The
switch does not provide Power over Ethernet (PoE).
3. Connect the power adapter to the switch and plug the power adapter into an
electrical outlet.
The power LED lights, and the port LEDs for connected devices light.
Discover the switch’s IP address to
access its device UI
By default, the switch is configured to receive an IP address from a DHCP server (or a
router that functions as a DHCP server) in your network.
Install and Access the Switch in
Your Network
14
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Use a computer and a web browser to access the device UI so you can configure and
manage the switch. Choose one of the following methods to discover the switch's IP
address in your network, and then use the IP address to access the device UI of the
switch:
• Use the NETGEAR Discovery Tool to discover the switch’s IP address and access the
device UI on page 15.
• Set a fixed IP address for the switch through a network connection on page 17
• Assign a fixed IP address by connecting directly to the switch off-network on page
18
Use the NETGEAR Discovery Tool to discover
the switch’s IP address and access the device
UI
The NETGEAR Discovery Tool (NDT, formerly referred to as NSDT) discovers the switch
in your network so you can access the device UI of the switch from a web browser.
To install the NDT, discover the switch in your network, access the switch, and
discover the switch IP address:
1. Download the NDT by visiting
netgear.com/support/product/netgear-discovery-tool.aspx.
Download the version for your operating system.
2. Temporarily disable the firewall, Internet security, antivirus programs, or all of these
on the computer that you are using to configure the switch.
3. Unzip the NDT file (which might be labeled NSDT), and double-click the .exe file (for
example, NETGEAR Discovery Tool x.x.xxx.exe) to install the program on your
computer.
Depending on your computer setup, the installation process might add the NETGEAR
Discovery Tool icon to the dock of your Mac or the desktop of your Windows-based
computer.
4. Reenable the security services on your computer.
5. Power on the switch.
The DHCP server assigns the switch an IP address.
6. Connect your computer to the same network as the switch.
You can use a WiFi or wired connection. The computer and the switch must be on
the same Layer 2 network.
7. Open the NDT.
Install and Access the Switch in
Your Network
15
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
If the NETGEAR Discovery Tool icon is in the dock of your Mac or on the desktop
of your Windows-based computer, click or double-click the icon to open the program.
The initial page displays a menu and a button.
8. From the Choose a connection menu, select the network connection that allows
the NDT to access the switch.
9. Click the Start Searching button.
The NDT displays a list of switches that it discovers on the selected network.
For each switch, the tool displays the IP address.
10. To access the device UI of the switch, click the ADMIN PAGE button.
The login page of the device UI opens.
11. Enter the device management password.
The default password to access the switch is password. The first time that you log
in to the switch, you must change the default password. The password is
case-sensitive.
The HOME page displays.
The right pane (or, depending on the size of your browser window, the middle pane)
shows the IP address that is assigned to the switch.
NOTE: You can copy and paste the IP address into a new shortcut or
bookmark it for quick access on your computer or mobile device. However,
if you restart the switch, a dynamic IP address (assigned by a DHCP server)
might change the IP address, and the bookmark might no longer link to the
login page for the switch. When you restart the switch, you must repeat this
procedure so that you can discover the new IP address of the switch in the
network and update your bookmark accordingly. You can also set up a fixed
(static) IP address for the switch (see Assign a fixed IP address to the switch
on page 16) to make sure that the new bookmark always links to the login
page for the switch, even after you restart the switch.
Assign a fixed IP address to the
switch
By default, the switch is configured to automatically receive an IP address from a DHCP
server (or a router that functions as a DHCP server) in your network. However, certain
events can cause the DHCP server to issue a new IP address to the switch, so if you need
the switch to persistently have the same IP address, you can assign a fixed (static) IP
address to the switch. For example, you may want to attach a shared device such as a
Install and Access the Switch in
Your Network
16
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
printer or file server, configure port forwarding, or set up the switch so you can connect
remotely from a mobile device.
To change the IP address of the switch, use one of the following methods:
• Connect to the switch through the network: If the switch and your computer are
connected to the same network, you can change the IP address of the switch through
a network connection (see Set a fixed IP address for the switch through a network
connection on page 17).
• Connect directly to the switch: If you cannot connect to the switch over a network
connection, you can change the IP address of the switch by using an Ethernet cable
to connect a directly to the switch (see Assign a fixed IP address by connecting
directly to the switch off-network on page 18).
Set a fixed IP address for the switch through
a network connection
If the switch and your computer are connected to the same network, you can set a fixed
IP address on the switch through a network connection.
To disable the DHCP client of the switch and change the IP address of the switch
to a fixed IP address by using a network connection:
1. Open a web browser from a computer that is connected to the same network as the
switch.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The default password to access the switch is password. The first time that you log
in to the switch, you must change the default password. The password is
case-sensitive.
The HOME page displays.
The right pane (or, depending on the size of your browser window, the middle pane)
shows the IP address that is assigned to the switch.
4. Select IP Address (DHCP On).
The toggle in the DHCP section displays green because the DHCP client of the switch
is enabled.
5. In the DHCP section, turn off the toggle.
The toggle in the DHCP section displays gray because the DHCP client of the switch
is disabled. The IP address fields become editable.
Install and Access the Switch in
Your Network
17
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
6. Enter the fixed (static) IP address that you want to assign to the switch and the
associated subnet mask and gateway IP address.
You can also either leave the address in the IP Address field as it is (with the IP
address that was issued by the DHCP server) or change the last three digits of the
IP address to an unused IP address.
7. Write down the complete fixed IP address.
You can bookmark it later.
8. Click the APPLY button.
Your settings are saved. Your switch web session is disconnected when you change
the IP address.
9. If the login page does not display, enter the new IP address of the switch in the
address field of your web browser.
The login page displays.
10. For easy access to the device UI, bookmark the page on your computer.
Assign a fixed IP address by connecting
directly to the switch off-network
If you cannot connect to the switch over a network connection, you can use an Ethernet
cable to connect your computer directly to the switch, and then you can set the IP
address of the switch.
To disable the switch's DHCP client and change the IP address of the switch to a
fixed IP address through a direct connection:
1. Connect an Ethernet cable from your computer to an Ethernet port on the switch.
2. Change the IP address of your computer to be in the same subnet as the default IP
address of the switch.
The default IP address of the switch is 192.168.0.239 and, to connect to it, your
computer's IP address must be on the same subnet (192.168.0.x).
The method to change your computer's IP address depends on the operating system
of your computer.
3. 4. Open a web browser from your computer.
Enter 192.168.0.239 as the IP address of the switch.
The login page displays.
5. Enter the device management password.
Install and Access the Switch in
Your Network
18
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The default password to access the switch is password. The first time that you log
in to the switch, you must change the default password. The password is
case-sensitive.
The HOME page displays.
The right pane (or, depending on the size of your browser window, the middle pane)
shows the IP address that is assigned to the switch.
6. Select IP Address (DHCP On).
The toggle in the DHCP section displays green because the DHCP client of the switch
is enabled.
7. Turn off the toggle in the DHCP section.
The toggle in the DHCP section displays gray because the DHCP client of the switch
is disabled. The IP address fields become editable.
8. Enter the fixed (static) IP address that you want to assign to the switch and the
associated subnet mask and gateway IP address.
9. Write down the complete fixed IP address.
You can bookmark it later.
10. Click the APPLY button.
Your settings are saved. Your switch web session disconnects when you change the
IP address.
11. Disconnect the switch from your computer and install the switch in your network.
12. Restore your computer to its original IP address.
13. Verify that you can connect to the switch with its new IP address:
a. Open a web browser from a computer that is connected to the same network as
the switch.
b. Enter the new IP address that you assigned to the switch.
The login page displays.
Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
Register the switch
1. 2. From a computer or mobile device that is connected to the Internet, visit
my.netgear.com.
Log in to your NETGEAR account.
Install and Access the Switch in
Your Network
19
User Manual
c. 
Gigabit Ethernet Plus Switch Model GS108Ev4
NOTE: If you don't have a free NETGEAR account, you can create one.
The My Products page displays.
3. 4. 5. From the menu on the left, select Register a Product.
In the Serial Number field, type the serial number of your switch.
From the Date of Purchase menu, select the date that you purchased the switch.
6. Click the REGISTER button.
Your switch is registerd to your NETGEAR account.
A confirmation email is sent to your NETGEAR account email address.
Install and Access the Switch in
Your Network
20
User Manual
3
Optimize the Switch Performance
This chapter describes how you can optimize the performance of the switch and contains
the following sections:
• Set the quality of service mode and port rate limits
• Manage individual port settings
21
Gigabit Ethernet Plus Switch Model GS108Ev4
Set the quality of service mode and
port rate limits
You can manually set the Quality of Service (QoS) modes to manage traffic:
• Port-based QoS mode: Lets you set the priority (low, normal, medium, high, or
critical) for individual port numbers and lets you set rate limits for incoming and
outgoing traffic for individual ports. If broadcast filtering is enabled, you can also
set the storm control rate for incoming traffic for individual ports.
• 802.1P/DSCP QoS mode: Applies pass-through prioritization that is based on
tagged packets and lets you set rate limits for incoming and outgoing traffic for
individual ports. If broadcast filtering is enabled, you can also set the storm control
rate for incoming traffic for individual ports.
This QoS mode applies only to devices that support 802.1P and Differentiated
Services Code Point (DSCP) tagging. For devices that do not support 802.1P and
DSCP tagging, ports are not prioritized, but the configured rate limit is still applied.
You can limit the rate of traffic on a port, including incoming or outgoing traffic, or both,
to prevent the port and the device that is attached to it from taking up too much
bandwidth on the switch. Rate limiting, which you can set for individual ports in either
of these QoS modes, means that the switch ensures that traffic does not exceed the
limit that you set for that port. If you set the rate limit on a port too low, you might notice
degraded video stream quality, sluggish response times during online activity, and
other problems.
Use port-based quality of service and set
port priorities
802.1P/DSCP is the default QoS mode on the switch, but you can also set port-based
QoS. For each port, you can set the priority and the rate limits for both incoming and
outgoing traffic:
• Port priority: The switch services traffic from ports with a critical priority before traffic
from ports with a high, medium, or low priority. Similarly, the switch services traffic
from ports with a high priority before traffic from ports with a medium or low priority.
If severe network congestion occurs, the switch might drop packets from ports with
a low priority.
• Port rate limits: The switch accepts traffic on a port at the rate (the speed of the
data transfer) that you set for incoming traffic on that port. The switch transmits traffic
Optimize the Switch
Performance
22
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
from a port at the rate that you set for outgoing traffic on that port. You can select
each rate limit as a predefined data transfer threshold from 512 Kbps to 512 Mbps.
NOTE: If you set a port rate limit, the actual rate might fluctuate, depending on
the type of traffic that the port is processing.
To use the port-based QoS mode and set the priority and rate limits for ports:
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
5. If the selection from the QoS Mode menu is 802.1P/DSCP, do the following to
change the selection to Port-Based:
a. From the QoS Mode menu, select Port-Based.
A pop-up warning window opens.
b. Click the CONTINUE button.
The pop-up window closes.
6. 7. NOTE: For information about broadcast filtering, see Manage broadcast
filtering and set port storm control rate limits on page 25.
To set the port priorities, do the following:
a. Click the PRIORITY tab.
b. Click the purple pencil icon.
The EDIT PRIORITY page displays.
c. For each port for which you want to set the priority, select Low, Medium, High,
or Critical from the individual menu for the port.
The default selection is High.
d. Click the APPLY button.
Your settings are saved and the EDIT PRIORITY page closes.
To set rate limits, do the following:
Optimize the Switch
Performance
23
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
a. b. Click the RATE LIMITS tab.
Click the purple pencil icon.
The EDIT RATE LIMITS page displays.
c. For each port for which you want to set rate limits, select the rate in Kbps or Mbps
from the individual In Limits and Out Limits menus for the port.
The default selection is No Limit.
d. Click the APPLY button.
Your settings are saved and the EDIT RATE LIMITS page closes.
Use 802.1P/DSCP quality of service
In the 802.1P/DSCP QoS mode, the switch uses the 802.1P or DSCP information in the
header of an incoming packet to prioritize the packet. With this type of QoS, you cannot
control the port prioritization on the switch because the device that sends the traffic
(that is, the packets) to the switch prioritizes the traffic. However, you can set the rate
limits for individual ports on the switch.
The switch accepts traffic on a port at the rate (the speed of the data transfer) that you
set for incoming traffic on that port. The switch transmits traffic from a port at the rate
that you set for outgoing traffic on that port. You can select each rate limit as a predefined
data transfer threshold from 512 Kbps to 512 Mbps.
To use 802.1P/DSCP QoS mode and set the rate limits for ports:
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
5. If the selection from the QoS Mode menu is Port-Based, do the following to change
the selection to 802.1P/DSCP:
a. From the QoS Mode menu, select 802.1P/DSCP.
A pop-up warning window opens.
b. Click the CONTINUE button.
Optimize the Switch
Performance
24
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
6. The pop-up window closes.
NOTE: For information about broadcast filtering, see Manage broadcast
filtering and set port storm control rate limits on page 25.
To set rate limits, do the following:
a. b. Click the RATE LIMITS tab.
Click the purple pencil icon.
The EDIT RATE LIMITS page displays.
c. For each port for which you want to set rate limits, select the rate in Kbps or Mbps
from the individual In Limits and Out Limits menus for the port.
The default selection is No Limit.
d. Click the APPLY button.
Your settings are saved and the EDIT RATE LIMITS page closes.
Manage broadcast filtering and set port
storm control rate limits
A broadcast storm is a massive transmission of broadcast packets that are forwarded
to every port on the switch. If they are not blocked, broadcast storm packets can delay
or halt the transmission of other data and cause problems. However, you can block
broadcast storms on the switch.
You can also set storm control rate limits for each port. Storm control measures the
incoming broadcast, multicast, and unknown unicast frame rates separately on each
port, and discards the frames if the rate that you set for the port is exceeded. By default,
no storm control rate limit is set for a port. You can select each storm control rate limit
as a predefined data transfer threshold from 512 Kbps to 512 Mbps.
To manage broadcast filtering and set the storm control rate limits for ports:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING.
Optimize the Switch
Performance
25
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The Quality of Service (QoS) page displays.
5. If the selection from the QoS Mode menu is Port-Based, do the following to change
the selection to 802.1P/DSCP:
a. From the QoS Mode menu, select 802.1P/DSCP.
A pop-up warning window opens.
b. Click the CONTINUE button.
The pop-up window closes.
NOTE: For information about broadcast filtering, see Manage broadcast
filtering and set port storm control rate limits on page 25.
6. Turn on the Broadcast Filtering toggle.
When broadcast filtering is enabled, the toggle displays green.
7. Click the APPLY button.
Broadcast filtering is enabled. The STORM CONTROL RATE tab displays next to
the RATE LIMITS tab.
8. To set storm control rate limits, do the following:
a. Click the STORM CONTROL RATE tab.
b. Click the purple pencil icon.
The EDIT STORM CONTROL RATE options display.
c. For each port for which you want to set storm control rate limits, select the rate
in Kbps or Mbps from the individual menu for the port.
The default selection is No Limit.
d. Click the APPLY button.
Your settings are saved, and the Storm Control Rate column displays the limit
that you set.
Manage individual port settings
For each individual port, you can set the port priority, set rate limits for incoming and
outgoing traffic, set the port speed (by default, the speed is set automatically), enable
flow control, and change the port name label.
Optimize the Switch
Performance
26
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Set rate limits for a port
You can limit the rate of incoming (ingress) traffic, outgoing (egress) traffic, or both on
a port to prevent the port (and the device that is attached to it) from taking up too much
bandwidth on the switch. Rate limiting simply means that the switch slows down all
traffic on a port so that traffic does not exceed the limit that you set for that port. If you
set the rate limit on a port too low, you might, for example, see degraded video stream
quality, sluggish response times during online activity, and other problems.
You also can set port rate limits (the same feature) as part of the Quality of Service
configuration on the switch (see Set the quality of service mode and port rate limits on
page 22).
To set rate limits for incoming and outgoing traffic on a port:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
The PORT STATUS pane displays on the right or the bottom of the HOME page,
depending on the size of your browser window.
A port that is in use shows as UP. A port that is not in use shows as AVAILABLE.
4. Select the port.
The pane displays detailed information about the port.
5. Click the EDIT button.
The EDIT PORT page displays for the selected port.
If the QoS mode on the switch is Port-Based (the default setting), the Priority menu
displays on the page. If the QoS mode is 802.1P/DSCP, the Priority menu does not
display.
6. From the In Rate Limit menu, Out Rate Limit menu, or both, select the rate in Kbps
or Mbps.
The default selection is No Limit.
7. Click the APPLY button.
Your settings are saved.
Optimize the Switch
Performance
27
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Set the priority for a port
If the QoS mode on the switch is Port-Based (the default setting), you can set the priority
for a port.
The switch services traffic from ports with a critical priority before traffic from ports with
a high, medium, or low priority. Similarly, the switch services traffic from ports with a
high priority before traffic from ports with a medium or low priority. If severe network
congestion occurs, the switch might drop packets with a low priority.
You also can set the priority for a port (the same feature) as part of the Quality of Service
configuration on the switch (see Use port-based quality of service and set port priorities
on page 22).
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The user
name and password are case-sensitive.
The HOME page displays.
The PORT STATUS pane displays on the right or the bottom of the HOME page,
depending on the size of your browser window.
A port that is in use shows as UP. A port that is not in use shows as AVAILABLE.
4. Select the port.
The pane displays detailed information about the port.
5. Click the EDIT button.
The EDIT PORT page displays for the selected port.
If the QoS mode on the switch is Port-Based (the default setting), the Priority menu
displays on the page. If the QoS mode is 802.1P/DSCP, the Priority menu does not
display.
6. From the Priority menu, select Low, Medium, High, or Critical.
The default selection is Low.
7. Click the APPLY button.
Your settings are saved.
Optimize the Switch
Performance
28
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Manage flow control for a port
IEEE 802.3x flow control works by pausing a port if the port becomes oversubscribed
(that is, the port receives more traffic than it can process) and dropping all traffic for
small bursts of time during the congestion condition.
You can enable or disable flow control for an individual port. By default, flow control is
disabled for all ports.
To manage flow control for a port:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The user
name and password are case-sensitive.
The HOME page displays.
The PORT STATUS pane displays on the right or the bottom of the HOME page,
depending on the size of your browser window.
A port that is in use shows as CONNECTED. A port that is not in use shows as
AVAILABLE.
4. Select the port.
The pane displays detailed information about the port.
5. Select the port.
The pane displays port settings.
6. In the Flow Control section, turn on or off the Flow Control toggle to enable or disable
flow control.
When flow control is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
Change the speed for a port or disable a
port
By default, the port speed on all ports is set automatically (that is, the setting is Auto)
after the switch determines the speed using autonegotiation with the linked device. We
Optimize the Switch
Performance
29
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
recommend that you leave the Auto setting for the ports. However, you can select a
specific port speed for each port, or disable a port by shutting it down manually.
To change the speed for a port or disable a port:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
The PORT STATUS pane displays on the right or the bottom of the HOME page,
depending on the size of your browser window.
A port that is in use shows as UP. A port that is not in use shows as AVAILABLE.
4. Select the port.
The pane displays port settings.
5. Click the EDIT button.
6. Select one of the following options from the Speed menu:
• Auto: The port speed is set automatically after the switch determines the speed
using autonegotiation with the linked device. This is the default setting.
• Disable: The port is shut down (blocked).
• 10M Full: The port is forced to function at 10 Mbps with full-duplex.
• 100M Full: The port is forced to function at 100 Mbps with full-duplex.
7. Click the APPLY button.
Your settings are saved.
Add or change the name label for a port
You can add or change a name label for a port. Name labels are for your reference only,
and do not affect port behavior.
To add or change a name label for a port:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
Optimize the Switch
Performance
30
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
The PORT STATUS pane displays on the right or the bottom of the HOME page,
depending on the size of your browser window.
A port that is in use shows as CONNECTED. A port that is not in use shows as
AVAILABLE.
4. Select the port.
The pane displays detailed information about the port.
5. In the Port Name field, type a name label for the port.
The name label can be from 1 to 16 characters.
6. Click the APPLY button.
Your settings are saved.
Optimize the Switch
Performance
31
User Manual
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
Use VLANS for Traffic
Segmentation
55
User Manual
5
Manage the Switch in Your Network
This chapter describes how you can manage the switch in your network.
The chapter contains the following sections:
• Set up static link aggregation
• Manage multicast
• Change the IP address of the switch
• Reenable the DHCP client of the switch
56
Gigabit Ethernet Plus Switch Model GS108Ev4
Set up static link aggregation
Static link aggregation on the switch allows you to combine multiple Ethernet ports into
a single logical link. Network devices treat the link aggregation group (LAG) as a single
link, which increases throughput, fault tolerance, or both, between devices. Depending
on how link aggregation is set up in your network, the link supports either increased
bandwidth (a larger pipe) or fault tolerance (if one port fails, another one takes over).
The switch supports two static LAGs with up to four ports each, which means that one
static LAG can support a link of up to 4 Gbps.
NOTE: The switch does not support Link Aggregation Control Protocol (LACP).
Set up static link aggregation on the switch by performing this series of tasks:
1. 2. Set up the LAG on the switch (see Set up a link aggregation group on page 57).
Physically connect the ports that must be members of the LAG on the switch to the
ports that must be members of the LAG on another device in your network (see Make
a link aggregation connection on page 58).
3. Enable the LAG on the switch (see Make a link aggregation connection on page 58)
and on the other device.
Set up a link aggregation group
You can set up one or more link aggregation groups (LAGs) on the switch. When you
set up a LAG on the switch, you must:
• Ensure that all ports on both devices that are to participate in the LAG use the same
speed, duplex mode, and flow control settings. For more information, see Manage
individual port settings on page 26.
• Select the ports on the switch that will participate in the LAG, as described in this
task.
To set up a LAG on the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
Manage the Switch in Your
Network
57
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
4. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select LINK AGGREGATION.
The LINK AGGREGATION page displays.
6. To add ports to a LAG, click the port numbers that you want to add.
A selected port displays purple.
A LAG must consist of at least two ports, but can consist of all ports.
The number of LAGs that the switch supports depends on the model.
7. Click the APPLY button.
Your settings are saved.
Now that the LAG ports are selected, you must set up the physical link aggregation
connection. For more information, see Make a link aggregation connection on page
58.
Make a link aggregation connection
Before you make a physical link aggregation connection to another network device
(usually a router or another switch) that also supports link aggregation, you must first
set up a LAG on the switch (see Set up a link aggregation group on page 57). If you do
not, the LAG cannot take effect. Whether a LAG on the switch functions to support
increased bandwidth or fault tolerance depends on the LAG configuration on the other
network device.
All ports that participate in a LAG (that is, the ports on both devices) must use the same
speed, full duplex mode, and flow control setting. For information about changing these
settings on the switch, see Manage individual port settings on page 26.
To make link aggregation connections between the switch and another network
device:
Using Ethernet cables, connect each port that must be a member of the LAG on the
switch to each port that must be a member of the same LAG on another network
device.
The port numbers on the other network device do not matter as long as:
• The ports on the other network device are members of the same LAG.
• The LAG consists of the same total number of ports.
• The ports use the same speed, full duplex mode, and flow control setting as the
ports in the LAG on the switch.
Manage the Switch in Your
Network
58
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
1. 2. Enable a link aggregation group
After you set up a link aggregation group (see Set up a link aggregation group on page
57) and make a physical link aggregation connection (see Make a link aggregation
connection on page 58), you can enable the link aggregation group.
NOTE: You must also enable the LAG on the other network device.
To enable a LAG on the switch:
Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
Enter the IP address that is assigned to the switch.
A login window opens.
Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
From the menu at the top of the page, select SWITCHING > QOS.
The Quality of Service (QoS) page displays.
From the menu on the left, select LINK AGGREGATION.
The LINK AGGREGATION page displays.
Under the LAG that you want to enable, turn on the toggle.
The toggle for a LAG that is enabled displays green.
7. Click the APPLY button.
Your settings are saved.
3. 4. 5. 6. Manage multicast
Multicast IP traffic is traffic that is destined to a host group. Host groups are identified
by Class D IP addresses, which range from 224.0.0.0 to 239.255.255.255.
Internet Group Management Protocol (IGMP) snooping allows the switch to forward
multicast traffic intelligently. Based on the IGMP query and report messages, the switch
forwards traffic only to the ports that request multicast traffic, rather than to all ports,
which could affect network performance.
Manage the Switch in Your
Network
59
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
IGMP snooping helps to optimize multicast performance and is especially useful for
bandwidth-intensive IP multicast applications such as online media streaming
applications.
Manage IGMP snooping
IGMP snooping is enabled by default. Under some circumstances you might want to
temporarily disable IGMP snooping.
To manage IGMP snooping:
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
5. From the menu on the left, select MULTICAST.
The MULTICAST page displays.
6. In the IGMP Snooping section, turn on or off the toggle to enable or disable IGMP
snooping.
When IGMP snooping is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
Enable a VLAN for IGMP snooping
You can enable IGMP for a VLAN only if you enabled a port-based VLAN mode or an
802.1Q VLAN mode (see Use VLANS for Traffic Segmentation on page 32).
To enable IGMP snooping for a VLAN:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
Manage the Switch in Your
Network
60
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SWITCHING > QOS.
The Quality of Service (QoS) page displays.
5. From the menu on the left, select MULTICAST.
The MULTICAST page displays.
6. In the VLAN ID Enabled for IGMP Snooping section, enter a VLAN ID in the field.
If you enabled either a port-based VLAN mode or an 802.1Q VLAN mode, the default
VLAN for IGMP snooping is VLAN 1.
7. Click the APPLY button.
Your settings are saved.
Manage blocking of unknown multicast
addresses
As a way to limit unnecessary multicast traffic, you can block multicast traffic from
unknown multicast addresses. If you do this, the switch forwards multicast traffic only
to ports in the multicast group that the switch learned through IGMP snooping. By
default, multicast traffic from unknown addresses is allowed.
To manage blocking of unknown multicast addresses:
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
5. From the menu on the left, select MULTICAST.
Manage the Switch in Your
Network
61
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The MULTICAST page displays.
6. In the Block Unknown Multicast Address section, turn on or off the toggle to enable
or disable blocking of unknown multicast traffic.
When blocking of unknown multicast traffic is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
Manage IGMPv3 IP header validation
You can enable IGMPv3 IP header validation so that the switch inspects whether IGMPv3
packets conform to the IGMPv3 standard. By default, IGMPv3 IP header validation is
disabled. If IGMPv3 IP header validation is enabled, IGMPv3 messages must include a
time-to-live (TTL) value of 1 and a type of service (ToS) byte of 0xC0 (Internetwork
Control). In addition, the router alert IP option (9404) must be set.
NOTE: If IGMPv3 IP header validation is enabled, the switch does not drop
IGMPv1 and IGMPv2 traffic, but processes this traffic normally.
To manage IGMPv3 IP header validation:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. From the menu on the left, select MULTICAST.
The MULTICAST page displays.
4. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
5. From the menu at the top of the page, select SWITCHING.
The Quality of Service (QoS) page displays.
6. In the Validate IGMPv3 IP Header section, turn on or off the toggle to enable or
disable IGMPv3 IP header validation.
When IGMPv3 IP header validation is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
Manage the Switch in Your
Network
62
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Set up a static router port for IGMP snooping
If your network does not include a device that sends IGMP queries, the switch cannot
discover the router port dynamically. (The router port is a port on a device in the network
that performs IGMP snooping in the network.) In this situation, select one port on the
switch as the dedicated static router port for IGMP snooping, allowing all IGMP Join
and Leave messages in the network to be forwarded to this port.
To set up a static router port for IGMP snooping:
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
5. From the menu on the left, select MULTICAST.
The MULTICAST page displays.
6. From the menu in the IGMP Snooping Static Router Port section, select a specific
port as the router port or select Any to let IGMP Join and Leave messages be sent
to every port on the switch.
Typically, the uplink port (that is, the port that is connected to your router or to the
device that provides your Internet connection) serves as the router port.
7. Click the APPLY button.
Your settings are saved.
Change the IP address of the switch
By default, the switch receives an IP address from a DHCP server (or a router that
functions as a DHCP server) in your network.
Manage the Switch in Your
Network
63
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To disable the DHCP client of the switch and change the IP address of the switch
to a fixed IP address:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. Select IP Address (DHCP On).
The IP address fields display, but you cannot change them yet. The toggle in the
DHCP section displays green because the DHCP client of the switch is enabled.
5. Turn off the toggle in the DHCP section.
The toggle displays gray, indicating that the DHCP client of the switch is disabled,
and you can now change the IP address fields.
6. Enter the fixed (static) IP address that you want to assign to the switch and the
associated subnet mask and gateway IP address.
7. Click the APPLY button.
A message displays to confirm that the IP address changed.
If the IP address of the switch changes, you web session disconnects, and you must
log back in to the device UI.
Reenable the DHCP client of the
switch
If you disabled the DHCP client of the switch and changed the IP address of the switch
to a fixed (static) IP address, you can reverse the situation.
To reenable the DHCP client on the switch:
1. 2. 3. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
Enter the IP address that is assigned to the switch.
A login window opens.
Enter the device management password.
Manage the Switch in Your
Network
64
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. Select IP Address (Fixed IP).
The toggle in the DHCP section displays gray because the DHCP client of the switch
is disabled.
5. Click the button in the DHCP section.
The toggle displays green, indicating that the DHCP client of the switch is enabled.
You can no longer change the IP address fields.
6. Click the APPLY button.
A message displays to confirm that the IP address settings changed.
The switch receives an IP address from a DHCP server (or a router that functions as
a DHCP server) in your network. If the IP address of the switch changes, you web
session disconnects, and you must log back in to the device UI.
Manage the Switch in Your
Network
65
User Manual
6
Maintain and Monitor the Switch
This chapter describes how you can maintain and monitor the switch, and contains these
sections:
• Update the firmware on the switch
• Manage the configuration file
• Return the switch to its factory default settings
• Control access to the device UI
• Change or lift access restrictions to the switch
• Manage the DoS prevention mode
• Manage the power saving mode
• Control the port LEDs
• Change the device management password
• Change the switch device name
• View system information
• View switch connections
• View the status of a port
• Manage NETGEAR Discovery Protocol
• Enable loop prevention
• View or clear the port statistics
• Enable port mirroring
66
Gigabit Ethernet Plus Switch Model GS108Ev4
Update the firmware on the switch
The switch firmware does not update automatically, so you must update it manually.
You can manually check for the latest firmware version, download the firmware, and
upload it to the switch.
CAUTION: We recommend that you read the release notes before updating
the switch’s firmware.
To manually check for new switch firmware and update the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The CONFIGURATION FILE page displays.
5. From the menu on the left, select FIRMWARE.
The FIRMWARE page displays. The page also shows the UPDATE FIRMWARE section.
The FIRMWARE VERSION displays the current firmware version of the switch.
6. To check if new firmware is available, click the netgear.com link in the FIRMWARE
section.
A NETGEAR web page opens.
7. Click the Downloads button.
8. If new firmware is available, download the firmware file to your computer.
If the file does not end in .binor .image, you might need to unzip the file. For
example, if the file ends in .rar, you must unzip the file.
9. In the FIRMWARE UPDATE section, click the purple file icon, navigate to the firmware
file that you just downloaded, and select the file.
10. Click the UPDATE button.
A pop-up window displays a warning and the firmware update process starts.
Maintain and Monitor the Switch
67
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
WARNING: Do not interrupt the network connection or power to the switch
during the firmware update process. Do not disconnect any Ethernet cables
or power off the switch until the firmware update process and switch reboot
are complete. Doing so can damage the switch.
Your switch web session is disconnected and you must log back in to the device UI.
Manage the configuration file
The switch stores its configuration settings in a configuration file. You can back up your
switch’s configuration settings by saving the configuration file to your computer. Later,
if you need to restore your settings, you can load the saved configuration file from your
computer to the switch.
Back up the switch configuration
You can save a copy of the switch's current configuration settings to your computer so
that you can restore the configuration settings from this backup file later if needed.
To back up the configuration settings switch of the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. Click the BACKUP tab.
The BACKUP CONFIGURATION page displays.
6. Click the BACKUP button.
7. Follow the directions in your browser to save the file.
The default name of the backup file is based on the switch model with a .cfg
extension.
Maintain and Monitor the Switch
68
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Restore the switch configuration
If you saved a back up of the switch's configuration file, you can load this file from your
computer on to the switch to restore the configuration.
To restore the configuration settings of the switch from a back up file:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. Click the purple file icon, navigate to the saved configuration file, and select it.
The name of the saved configuration file is based on the switch model with a .cfg
extension.
The RESTORE button changes to the APPLY CONFIGURATION button.
6. Click the APPLY CONFIGURATION button.
A pop-up window displays a warning.
7. Click the CONTINUE button.
The configuration is uploaded to the switch.
WARNING: Do not interrupt the network connection or power to the switch
during the restoration process. Do not disconnect any Ethernet cables or
power off the switch until the restoration process and switch reboot are
complete. Doing so can damage the switch.
Your switch web session is disconnected and you must log back in to the device UI.
Maintain and Monitor the Switch
69
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Return the switch to its factory
default settings
You can reset the switch to return it to factory default settings, using either the Factory
Defaults button on the front of the switch, or the reset function in the device UI. If you
have lost the password and cannot access the switch, you must use the Factory Defaults
button.
After you reset the switch to factory default settings, the password is password and the
switch’s DHCP client is enabled. For more information, see Factory default settings on
page 88.
Use the RESET button to reset the switch
You can use the RESET button to return the switch to its factory default settings.
CAUTION: This process erases all settings that you configured on the switch.
To reset the switch to factory default settings:
1. 2. On the front of the switch, locate the recessed RESET button.
Using a straightened paper clip, press and hold the RESET button for more than
5 seconds.
3. Release the RESET button.
The switch resets. When the reset is complete, the switch reboots. This process takes
about one minute.
WARNING: Do not interrupt the network connection or power to the switch
during the reset process. Do not disconnect any Ethernet cables or power
off the switch until the reset process and switch reboot are complete. Doing
so can damage the switch.
Use the device UI to reset the switch
CAUTION: This process erases all settings that you configured on the switch.
Maintain and Monitor the Switch
70
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To reset the switch to factory default settings using the device UI:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select FACTORY DEFAULT.
The FACTORY DEFAULT page displays.
6. Click the RESTORE DEFAULT SETTINGS button.
A warning pop-up window opens.
7. Click the CONTINUE button.
The switch is reset to factory default settings and reboots.
WARNING: Do not interrupt the network connection or power to the switch
during the reset process. Do not disconnect any Ethernet cables or power
off the switch until the reset process and switch reboot are complete. Doing
so can damage the switch.
Control access to the device UI
You can control which IP address or IP addresses are allowed to access the switch
through the device UI for management purposes.
To control management access to the device UI:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
Maintain and Monitor the Switch
71
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select ACCESS CONTROL.
The ACCESS CONTROL page displays any allowed IP addresses.
6. Click the ADD button.
7. Specify the IP address or IP addresses to allow:
• IP Address: Enter a single IP address or a network IP address.
Enter a network IP address in the format x.x.x.0, for example, 192.168.100.0.
• Mask: If you enter a single IP address, enter 255.255.255.255 as the mask. If
you enter a network IP address, enter 255.255.255.0 as the mask.
NOTE: First add the IP address of the computing device that you are using
to configure the switch so you can ensure your own access to the switch UI.
8. Click the APPLY button.
Your settings are saved.
9. To enter more IP addresses, repeat the previous three steps.
Change or lift access restrictions to
the switch
If you set up IP addresses that are allowed to access the switch through the device UI
for management purposes, you can remove one or more IP addresses, or you can
remove all IP addresses to lift the access restrictions.
If you lift access restrictions, any IP address can access the device UI of the switch. (The
user still must enter a password to access the device UI.)
To change or lift access restrictions to the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
Maintain and Monitor the Switch
72
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select ACCESS CONTROL.
The ACCESS CONTROL page displays.
6. Click the IP address that you want to remove.
The DELETE button displays.
7. Click the DELETE button.
The IP address is removed from the list, and access to the switch's device UI from
the IP address is blocked.
8. To remove more IP addresses, repeat steps 6 and 7.
CAUTION: If you remove all IP addresses, all access restrictions are removed
and any IP address can access the device UI of the switch.
Manage the DoS prevention mode
You can enable the Denial of Service (DoS) prevention mode so that the switch
automatically blocks malicious packets. By default, this mode is disabled.
To manage the DoS prevention mode:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select DOS PREVENTION.
The DOS PREVENTION page displays.
6. Turn on or off the toggle to enable or disable the DoS prevention mode.
Maintain and Monitor the Switch
73
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
When the DoS prevention mode is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
Manage the power saving mode
The power saving mode enables the IEEE 802.3az Energy Efficient Ethernet (EEE)
function, cable length power saving, and link-up and link-down power saving:
• IEEE 802.3az: Combines the Energy Efficient Ethernet (EEE) 802.3 MAC sublayer
with the 100BASE-TX and 1000BASE-T physical layers to support operation in Low
Power Idle (LPI) mode. When LPI mode is enabled, systems on both sides of the link
can disable portions of their functionality and save power during periods of low link
utilization.
• Short cable power saving: Dynamically detects and adjusts power that is required
for the detected cable length.
• Link-down power saving: Reduces the power consumption considerably when the
network cable is disconnected. When the network cable is reconnected, the switch
detects an incoming signal and restores normal power.
By default, the power saving mode is disabled.
To manage the power saving mode on the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select POWER SAVING.
The POWER SAVING page displays.
6. Turn on or off the toggle to enable or disable the power saving mode.
When the power saving mode is enabled, the toggle displays green.
7. Click the APPLY button.
Maintain and Monitor the Switch
74
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Your settings are saved.
Control the port LEDs
You can turn the port LEDs on the switch on and off by using the device UI.
By default, a port LED lights when you connect a powered-on device to the port. When
the switch functions with its LEDs off, we refer to it as Stealth Mode.
To control the port LEDs through the device UI:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. Select Port LEDs.
The Port LEDs button displays.
5. Turn on or off the toggle to enable or disable the port LEDs.
When the port LEDs are enabled, the toggle displays green. When the ports LEDs
are disabled (Stealth Mode), the toggle displays gray.
6. Click the APPLY button.
Your settings are saved.
Change the device management
password
The default password to access the device UI of the switch is password. The first time
that you log in to the switch, you must change the default password. In this manual, we
call the password to access the device UI the device management password.
You can change the password again. The ideal password contains no dictionary words
from any language and contains uppercase and lowercase letters, numbers, and symbols.
It can be up to 20 characters.
Maintain and Monitor the Switch
75
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
To change the device management password:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select CHANGE PASSWORD.
The CHANGE PASSWORD page displays.
6. 7. In the Current Password field, type the current password for the switch.
Type the new password in the New Password field and in the Retype New Password
field.
8. Click the APPLY button.
Your settings are saved. Keep the new password in a secure location so that you can
access the switch in the future.
Change the switch device name
By default, the device name of the switch is the same as the model number. This device
name shows in, for example, in Windows Explorer and Bonjour. You can change the
device name, which can be up to 20 characters.
To change the device name of the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
Maintain and Monitor the Switch
76
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
4. Select System Info.
The System Info fields display.
5. In the Switch Name field, enter a new name for the switch.
6. Click the APPLY button.
Your settings are saved.
View system information
You can view basic information about the switch, such as the firmware version, switch
name, MAC address, serial number, and model number.
To view basic information about the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. Select System Info.
The system information fields display.
View switch connections
You can see the number of connections that are established on the switch.
To see the number of connections on the switch:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The user
name and password are case-sensitive.
Maintain and Monitor the Switch
77
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The HOME page displays.
The switch connections show in the upper left of the page.
View the status of a port
You can view the port status and drill down for details about the port.
To view the status of a port:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
The PORT STATUS pane displays on the right or the bottom of the HOME page,
depending on the size of your browser window.
A port that is in use shows as UP. A port that is not in use shows as AVAILABLE.
4. To view details about a port, select the port.
The pane displays detailed information about the port.
If the QoS mode on the switch is port-based (the default setting), the Priority field
displays on the page. If the QoS mode is 802.1P/DSCP, the Priority field does not
display.
For information about setting rate limits for incoming and outgoing traffic, setting
the port priority (if the QoS mode on the switch is port-based), setting the port speed
(by default, the speed is set automatically), enabling flow control, and changing the
port name label, see Manage individual port settings on page 26
Manage NETGEAR Discovery
Protocol
A NETGEAR device or application that supports NETGEAR Discovery Protocol (NDP,
formerly referred to as NSDP) can discover the switch in the network so that you can
Maintain and Monitor the Switch
78
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
find the switch IP address and log in to the device UI of the switch. NDP is enabled by
default. You can disable NDP for security reasons.
To manage NDP:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select SETTINGS.
The RESTORE CONFIGURATION page displays.
5. From the menu on the left, select SWITCH DISCOVERY.
The SWITCH DISCOVERY page displays.
6. In the NSDP section, turn on or off the toggle to enable or disable NDP.
When NDP is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
Enable loop prevention
If loop prevention is enabled and the switch detects a loop, both LEDs of a port blink
at a constant speed.
To enable loop detection:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select DIAGNOSTICS.
Maintain and Monitor the Switch
79
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The CABLE TEST page displays.
5. From the menu on the left, select LOOP PREVENTION.
The LOOP PREVENTION page displays.
6. Turn on the toggle to enable LOOP PREVENTION.
When loop prevention is enabled, the toggle displays green.
7. Click the APPLY button.
Your settings are saved.
View or clear the port statistics
For each switch port, you can view the bytes received, bytes sent, and cyclic redundancy
check (CRC) error packets.
To view or clear the port statistics:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select DIAGNOSTICS.
The CABLE TEST page displays.
5. From the menu on the left, select PORT STATISTICS.
The PORT STATISTICS page displays.
For each port, the page lists the bytes received, bytes sent, and cyclic redundancy
check (CRC) error packets, which are packets with errors or corrupt packets.
6. To clear the port statistics, click the CLEAR button.
All statistics counters change to 0.
Maintain and Monitor the Switch
80
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Enable port mirroring
Port mirroring lets you mirror the incoming (ingress) and outgoing (egress) traffic of
one or more ports (the source ports) to a single predefined destination port.
To enable port mirroring:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select DIAGNOSTICS.
The CABLE TEST page displays.
5. From the menu on the left, select PORT MIRRORING.
The PORT MIRRORING page displays.
6. Turn on the toggle to enable PORT MIRRORING.
When port mirroring is enabled, the toggle displays green.
7. In the source port section, select one or more source ports by selecting the port
number associated with the port.
The port number displays solid purple when enabled.
You can select more than one source port. You cannot select a source port that is a
member of a LAG.
8. In the destination port section, select the destination port.
The port number displays solid purple when enabled.
You can select a single destination port only. You cannot select a destination port
that is a member of a LAG.
9. Click the APPLY button.
Your settings are saved.
Maintain and Monitor the Switch
81
User Manual
7
Diagnostics and Troubleshooting
This chapter covers the following topics:
• Test cable connections
• Resolve a subnet conflict to access the switch
82
Gigabit Ethernet Plus Switch Model GS108Ev4
Test cable connections
You can use the cable diagnostic feature to easily find out the health status of network
cables. If any problems exist, this feature helps quickly locate the point where the cabling
fails, allowing connectivity issues to be fixed much faster, potentially saving technicians
hours of troubleshooting.
If an error is detected, the distance at which the fault is detected is stated in meters.
(This is the distance from the port.)
To test cable connections:
1. Open a web browser from a computer that is connected to the same network as the
switch, or connected directly to the switch through an Ethernet cable.
2. Enter the IP address that is assigned to the switch.
A login window opens.
3. Enter the device management password.
The password is the one that you specified the first time that you logged in. The
password is case-sensitive.
The HOME page displays.
4. From the menu at the top of the page, select DIAGNOSTICS.
The CABLE TEST page displays.
5. Select one or more ports for which you want to test the cable that is attached to the
port.
6. Click the NEXT button.
The switch tests cable connections for the selected ports and displays the results.
This process might take up to a few minutes.
7. Click the DONE button to dismiss the test results.
You can run another cable test if desired.
Resolve a subnet conflict to access
the switch
If you power on the switch before you connect it to a network that includes a DHCP
server, the switch uses its own default IP address of 192.168.0.239. This subnet might
be different from the subnet used in your network. You might see the following message
if you try to access the switch:
Diagnostics and
Troubleshooting
83
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
The switch and manager IP address are not in the same subnet.
To resolve this subnet conflict:
1. 2. 3. 4. Disconnect the Ethernet cable between the switch and your network.
Shut down power to the switch.
Reconnect the Ethernet cable between the switch and your network.
Reapply power to the switch.
The switch powers on. The network DHCP server discovers the switch and assigns
it an IP address that is in the correct subnet for the network.
Diagnostics and
Troubleshooting
84
User Manual
8
Additional Switch Discovery and
Access Information
This appendix provides additional information about how you can discover and access
the switch in your network.
The appendix contains the following section:
• Access the switch from any computer
85
Gigabit Ethernet Plus Switch Model GS108Ev4
Access the switch from any
computer
This procedure requires you to use an IP scanner application. Such applications are
available on the Internet, and some of them are free of charge.
To discover the switch IP address and access the switch from a computer:
1. From a computer that is connected to your network, run the IP scanner application
in your network.
The IP address that is assigned to the switch displays in the IP scanner application.
2. 3. NOTE: You can also access the DHCP server (or the router that functions as
a DHCP server) in your network and determine the IP address that is assigned
to the switch.
Open a web browser, and in the address bar, type the IP address of the switch.
The login page of the device UI opens.
Enter the device management password.
The default password to access the switch is password. The first time that you log
in to the switch, you must change the default password. The password is
case-sensitive.
The HOME page displays.
The right pane (or, depending on the size of your browser window, the middle pane)
shows the IP address that is assigned to the switch.
NOTE: You can copy and paste the IP address into a new shortcut or
bookmark it for quick access on your computer or mobile device. However,
if you reboot the switch, a dynamic IP address (assigned by a DHCP server)
might change and the bookmark might no longer link to the login page for
the switch. In this case, you must repeat these steps so that you can discover
the new IP address of the switch in the network and update your bookmark
accordingly. You can also set up a fixed (static) IP address for the switch (see
Assign a fixed IP address to the switch on page 16) to make sure that the new
bookmark always links to the login page for the switch, even after you reboot
the switch.
Additional Switch Discovery and
Access Information
86
User Manual
A
Factory Default Settings and
Technical Specifications
This appendix contains the following sections:
• Factory default settings
• Technical specifications
87
Gigabit Ethernet Plus Switch Model GS108Ev4
Factory default settings
You can return the switch to its factory settings. For more information, see Return the
switch to its factory default settings on page 70.
The switch resets and returns to the factory settings shown in the following table.
Table 4. Factory default settings
Feature
Setting
Device management
password
IP address
Subnet mask
DHCP mode
IGMP snooping
LAGs
VLANs
802.1p/DSCP-based QoS
Port-based QoS
Rate limiting
Broadcast filtering
Loop prevention
Port speed
Flow control
Port mirroring
password
192.168.0.239 (if the switch is not connected to a network with a DHCP server)
255.255.255.0
Enabled
Disabled
None configured
Disabled. If enabled, by default, all ports are members of VLAN 1.
Enabled
Disabled
Disabled
Disabled
Enabled
Autonegotiation
Disabled
Disabled
Technical specifications
The following table shows the technical specifications.
Factory Default Settings and
Technical Specifications
88
User Manual
Gigabit Ethernet Plus Switch Model GS108Ev4
Table 5. Technical specifications
Feature
Description
Network interface
Network cable
Ethernet ports
Power input
Power consumption
Dimensions (W x D x H)
Weight
Operating temperature
Operating humidity
Electromagnetic
compliance
RJ-45 connector for 10BASE-T, 100BASE-TX, or 1000BASE-T
Category 5e (Cat 5e) or higher-rated Ethernet cable
8
12V, 1.5A DC input
3.7W maximum
6.2 x 4.0 x 1.14 in. (158 x 101 x 29 mm)
1.12 lb (0.508 kg)
32º to 104ºF (0° to 40°C)
10–90% maximum relative humidity, noncondensing
KC Class B, FCC part 15 Class B, RCM Class B, CE Class B, VCCI Class B, BSMI,
CAN ICES-3 (B)/NMB-3(B)
Safety agency approvals
CB, CE LVD, BSMI
Factory Default Settings and
Technical Specifications
89
User Manual