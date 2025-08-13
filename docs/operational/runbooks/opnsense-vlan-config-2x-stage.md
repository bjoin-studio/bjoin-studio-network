# OPNsense Stage VLAN Configuration (VLANs 21, 22, 24)

This guide provides step-by-step instructions for configuring the Stage VLANs. These VLANs are for devices used during production shoots, such as cameras, lighting, and control systems.

## 1. VLAN Definitions

| VLAN ID | Name             | Subnet           | Gateway IP     | DHCP Range           | Purpose                                      |
|:--------|:-----------------|:-----------------|:---------------|:---------------------|:---------------------------------------------|
| **21**  | STAGE_CONTROL    | `10.20.21.0/24`  | `10.20.21.1`   | `10.20.21.100 – 200` | For tethered cameras, lighting, and control. |
| **22**  | STAGE_TRANSFER   | `10.20.22.0/24`  | `10.20.22.1`   | `10.20.22.100 – 200` | For high-speed image servers and preview stations. |
| **24**  | STAGE_WIFI       | `10.20.24.0/24`  | `10.20.24.1`   | `10.20.24.100 – 200` | For tablets, mobile control apps, and crew.  |

---

## 2. Step-by-Step Configuration

### Step 2.1: Create, Assign, and Enable Interfaces

Follow the procedures in the previous guides to create the VLANs (21, 22, 24) and assign them to enabled interfaces with static IPs as defined in the table above.

### Step 2.2: Configure DHCP Server

Enable the DHCP server for each Stage VLAN interface and set the correct IP range as defined in the table.

### Step 2.3: Firewall Rules

The key principle for the Stage VLANs is to allow them to send data to the Studio, but otherwise be isolated.

Navigate to **Firewall > Rules** and select the tab for each Stage VLAN.

1.  **Allow DNS:** Allow traffic to your DNS servers (e.g., `10.20.51.10`) on port 53.
2.  **Allow Media Ingest to Studio:** Create a rule to allow traffic *from* the `STAGE_TRANSFER net` *to* the `StudioNet` alias. You can restrict this to specific ports (e.g., for SMB or NFS) if desired.
    -   **Action:** Pass
    -   **Source:** `STAGE_TRANSFER net`
    -   **Destination:** `StudioNet` (You should create an alias for all Studio VLAN subnets)
3.  **Block All Other Internal Traffic:** Add a rule to block traffic from the `StageNet` alias to all other internal networks (`RFC 1918`) to prevent unauthorized access.
4.  **Allow Limited Internet (Optional):** If needed, add a rule at the bottom to allow traffic to `! (RFC 1918)` for internet access.
