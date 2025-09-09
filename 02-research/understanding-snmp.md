# What is SNMP?

**SNMP (Simple Network Management Protocol)** is like a language that network devices use to share information with a central management system. Think of it as a manager asking for status updates from their team. It helps network administrators keep an eye on the health of their network, identify problems, and make sure everything is running smoothly.

## Key Components

An SNMP setup has a few key parts:

*   **SNMP Manager:** This is the central system (usually a computer running special software) that does the monitoring. It's like the manager who asks for updates.
*   **SNMP Agent:** This is a small piece of software that runs on each network device (like a router or switch). It gathers information about the device and sends it to the manager.
*   **Managed Device:** This is any device on the network that has an SNMP agent installed.
*   **Management Information Base (MIB):** This is like a menu of all the information that a device can share. Each item on the menu has a unique code, called an Object Identifier (OID), so the manager can ask for specific information.

## How it Works

SNMP uses a few basic commands:

*   **GET:** The manager asks for a specific piece of information (e.g., "How much traffic is going through this port?").
*   **SET:** The manager can change a setting on the device.
*   **TRAP:** The device can send an alert to the manager if something important happens (e.g., "I'm about to run out of memory!").

There are a few versions of SNMP, but the most important thing to know is that **SNMPv3 is the most secure** and should be used whenever possible. Older versions have security weaknesses that can put your network at risk.