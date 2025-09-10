# QNAP TS-h1290FX

## Description
High-performance NVMe NAS designed for intensive workloads, media editing, and virtualization.  
Equipped with AMD EPYC processor, PCIe Gen4 architecture, and dual 100GbE via ConnectX-6 SmartNIC.

- **System Details**
    - <details>
        <summary>Hardware Inventory</summary>

        <details>
        <summary>CPU</summary>

            - AMD EPYC™ 7232P / 7302P  
            - Up to 16 cores, 32 threads  
            - 64-bit x86 architecture with AES-NI

        </details>

        <details>
        <summary>Memory</summary>

            - 64GB DDR4 ECC RDIMM (8×8GB)  
            - Max supported: 1TB (8×128GB)

        </details>

        <details>
        <summary>Storage</summary>

            - 12× 2.5" U.2 NVMe PCIe Gen4 x4 / SATA SSD bays  
            - Hot-swappable  
            - SSD cache acceleration supported  
            - Dual boot OS protection (5GB flash)

        </details>

        <details>
        <summary>Network Interfaces</summary>

            - 2× 100GbE via [ConnectX-6 SmartNIC](https://www.nvidia.com/en-us/networking/ethernet-adapters/connectx-6-dx/)  
            - 2× 25GbE SFP28  
            - 2× 2.5GbE RJ45  
            - Jumbo frame support

        </details>

        <details>
        <summary>PCIe Expansion</summary>

            - 4× PCIe Gen4 slots (3× x16, 1× x8)  
            - GPU pass-through and SR-IOV supported

        </details>

        <details>
        <summary>Power & Cooling</summary>

            - 750W PSU  
            - 2× 92mm fans  
            - Typical consumption: ~134W

        </details>

        <details>
        <summary>Form Factor</summary>

            - Tower chassis  
            - Dimensions: 150 × 368 × 362 mm  
            - Weight: 10.4 kg

        </details>

        <details>
        <summary>Operating System</summary>

            - QTS Hero (ZFS-based)  
            - [Manual](https://docs.qnap.com/operating-system/quts-hero/5.0.x/en-us/)

        </details>

    </details>

## Role
- **Primary Storage Node**
    - <details>
        <summary>Functions</summary>

        - High-speed NVMe storage for VMs and media workflows  
        - ZFS snapshots, deduplication, and compression  
        - iSCSI, NFS, SMB, and S3-compatible object storage  
        - Backup target for infrastructure servers

        </details>
    </details>

## Identification

| Hostname(s)         | IP Address(es)   | VLAN  | Cable ID   |
|---------------------|------------------|-------|------------|
| `qnap.bjoin.studio` | `10.20.51.80`    | `51`  | `----/----` |
