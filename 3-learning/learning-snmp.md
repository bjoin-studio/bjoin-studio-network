# Understanding SNMP (Simple Network Management Protocol)

**Simple Network Management Protocol (SNMP)** is a standard internet protocol for collecting and organizing information about managed devices on IP networks. It is widely used in network management for monitoring network-attached devices for conditions that warrant administrative attention. SNMP allows network administrators to manage network performance, find and solve network problems, and plan for network growth. It is a fundamental component of most network management systems (NMS).

## Core Components of SNMP

An SNMP-managed network consists of three key components:

*   **SNMP Manager:** A centralized system that monitors and controls the managed devices. It is typically a computer running a network management application. The manager queries agents, gets responses from agents, sets variables in agents, and acknowledges asynchronous events from agents.
*   **SNMP Agent:** A software module that runs on a managed device (e.g., a router, switch, or server). The agent has local knowledge of management information and translates that information into a form compatible with SNMP.
*   **Managed Device:** A network node that contains an SNMP agent and resides on a managed network. These devices collect and store management information and make it available via SNMP.
*   **Management Information Base (MIB):** A hierarchical database of objects that can be managed on a device. The MIB defines the properties of the managed object within the device. Each managed object has a unique Object Identifier (OID).

## SNMP Operations and Versions

SNMP works by sending messages, called Protocol Data Units (PDUs), to managed devices. The most common operations are `GET`, `GETNEXT`, and `GETBULK` (to retrieve data), `SET` (to modify data), and `TRAPS` (for agents to asynchronously inform the manager of a significant event).

There are three major versions of SNMP:

*   **SNMPv1:** The original version, which is now considered obsolete due to its poor security. It uses community strings for authentication, which are sent in clear text.
*   **SNMPv2c:** An enhancement of v1 that introduced the `GETBULK` operation for more efficient data retrieval. However, it still uses the insecure community-based authentication model of v1.
*   **SNMPv3:** The current standard, which provides significant security enhancements. SNMPv3 offers authentication, encryption, and message integrity, making it the recommended version for modern networks. It uses a user-based security model (USM) and a view-based access control model (VACM) to ensure that only authorized users can access and modify management information.
