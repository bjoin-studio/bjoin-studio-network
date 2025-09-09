**Layer 1: Physical Layer**

The Physical Layer focuses on the physical transmission of raw bit streams over a communication medium. It defines electrical and physical specifications for devices, including cabling, connectors, voltage levels, and data rates. This layer is concerned with how data is actually transmitted as electrical signals, light pulses, or radio waves, without any regard for their meaning or structure. Examples include Ethernet cables, USB, and Wi-Fi physical components.

**Layer 2: Data Link Layer**

The Data Link Layer provides reliable data transfer across a physical link. It handles error detection and correction from the physical layer, and manages flow control to prevent fast senders from overwhelming slow receivers. This layer is divided into two sublayers: Logical Link Control (LLC) for managing communication between devices, and Media Access Control (MAC) for controlling access to the physical medium. MAC addresses operate at this layer. Examples include Ethernet (frames), PPP, and Wi-Fi (frames).

**Layer 3: Network Layer**

The Network Layer is responsible for logical addressing and routing of packets across different networks. It determines the best path for data to travel from source to destination, potentially across multiple intermediate devices. IP addresses, which are logical addresses, are defined at this layer. Routers operate primarily at the network layer to forward packets between networks. Examples include IP (Internet Protocol) and ICMP.

**Layer 4: Transport Layer**

The Transport Layer provides end-to-end communication between applications on different hosts. It handles segmenting data from the application layer, ensuring reliable delivery, and managing flow control and error recovery. This layer can provide connection-oriented services (like TCP, ensuring delivery and ordering) or connectionless services (like UDP, for faster but less reliable delivery). Port numbers are used at this layer to identify specific applications.

**Layer 5: Session Layer**

The Session Layer establishes, manages, and terminates communication sessions between applications. It handles dialogue control, allowing applications to communicate in either half-duplex or full-duplex mode, and provides synchronization points for long conversations. This layer ensures that applications can maintain a persistent connection and resume communication from a specific point if interrupted. Examples include NetBIOS and RPC.

**Layer 6: Presentation Layer**

The Presentation Layer is responsible for data translation, encryption, and compression. It ensures that data is presented in a format that the application layer can understand, regardless of the underlying system's data representation. This layer handles character code translation (e.g., ASCII to EBCDIC), data encryption/decryption, and data compression/decompression, effectively acting as a data translator for the application layer. Examples include JPEG, MPEG, and SSL/TLS encryption.

**Layer 7: Application Layer**

The Application Layer is the closest layer to the end-user, providing network services directly to user applications. It enables software applications to communicate over the network and provides common application services. This layer interacts with software applications that implement a communicating component. Examples include HTTP, FTP, SMTP, DNS, and web browsers.