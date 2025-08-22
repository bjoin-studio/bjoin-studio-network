# Physical Network Diagram

This document provides a visual representation of the physical connections between the network devices in the bjoin.studio network.

## Core Infrastructure

```
+-------------+      +----------------------+      +---------------------------+      +-----------------------+
| ISP Modem   |      | Protectli FW4B       |      | Sodola KT-NOS SL-SWTGW2C8F|      |   Cisco NEXUS 9236c   |
| (Unknown)   |      | (opnsense-fw)        |      | (8-port 10G Switch)       |      | (36-port 100G Switch) |
+------+------+      +---------+------------+      +----------+----------------+      +----------+------------+
       |             |         |                   |          |                |      |          |
       |             | WAN     | LAN               | Port 8   | Ports 1-4 (LAG)|      | Port 1   |
       |             +---------+                   | (Trunk)  | (Trunk)        |      | (Trunk)  |
       |                   |                       |          |                |      |          |
       +-------------------+-----------------------+          |                +------+          |
                                                            |
                                                            |
                                                            v
                                                      +-----------------------+
                                                      | QNAP TS-h1290FX       |
                                                      | (qnap.bjoin.studio)   |
                                                      +----------+------------+
                                                                 | Ports 1-2 (LAG)
                                                                 |
                                                                 +------------------+
```

## Access Layer

```
+---------------------------+      +-----------------------+      +-----------------------+
| Sodola KT-NOS SL-SWTGW2C8F|      | Netgear GS108Ev4      |      |   Netgear GS105       |
| (8-port 10G Switch)       |      | (8-port 1G Switch)    |      | (5-port 1G Unmanaged) |
+----------+----------------+      +----------+------------+      +----------+------------+
           | Port 7 (Trunk) |      | Port 8   | Port 5 (Access) |      | Port 5   |
           +----------------+------+----------+               +------+----------+
           | Port 5 (Access)|      
           +----------------+
                 |
                 v
+-----------------------+
| Mac Pro 6,1           |
| (pmx-01.bjoin.studio) |
+-----------------------+
```

## End Devices

```
+-----------------------+      +---------------------------+
|   Cisco NEXUS 9236c   |      | SuperMicro Workstation    |
| (36-port 100G Switch) |      | (jupiter.bjoin.studio)    |
+----------+------------+      +----------+----------------+
           | Ports 3-4 (LAG)+------+ Ports 1-2 (LAG)
           |

+-----------------------+      +---------------------------+
|   Bitengine SW08XM    |      | Mac Studio M3 Ultra       |
| (8-port 1G Switch)    |      | (mercury.bjoin.studio)    |
+----------+------------+      +----------+----------------+
           | Port 1         +------+ Port 1
           |

+-----------------------+      +---------------------------+
|   Netgear GS108Ev4    |      | iMac 27"                  |
| (8-port 1G Switch)    |      | (venus.bjoin.studio)      |
+----------+------------+      +----------+----------------+
           | Port 1         +------+ Port 1
           |

+-----------------------+      +---------------------------+
|   Netgear GS108Ev4    |      | iMac Pro                  |
| (8-port 1G Switch)    |      | (mars.bjoin.studio)       |
+----------+------------+      +----------+----------------+
           | Port 2         +------+ Port 1
```
