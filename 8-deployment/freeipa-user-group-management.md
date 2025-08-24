# FreeIPA User and Group Management Runbook

This document outlines the standards and procedures for managing users and groups within the `bjoin.studio` FreeIPA domain.

## 1. Naming Conventions

- **Usernames:** `firstname.lastname` (e.g., `john.doe`). All lowercase. **Note:** While periods are allowed, for Kerberos compatibility and to avoid potential issues with some applications, it is recommended to use hyphens (e.g., `john-doe`) or no separators (e.g., `johndoe`) instead of periods.
- **Groups:** `grp-<domain>` for primary groups (e.g., `grp-studio`). All lowercase.

## 2. Group ID (GID) Strategy

**⚠️ IMPORTANT WARNING: Potential Login Issues with Custom UIDs/GIDs ⚠️**

While this GID strategy is logically sound, it has been observed to cause login failures on certain Linux client configurations (e.g., Fedora Workstation/Server) when users are created with explicitly assigned UIDs and GIDs (e.g., using `--uid` and `--gidnumber` with `ipa user-add`). The exact cause is under investigation, but it appears to be related to how Kerberos or PAM interacts with non-default ID ranges.

**Recommendation:** Unless you have thoroughly tested and confirmed compatibility with your specific client operating systems, it is strongly recommended to **omit the `--uid` and `--gidnumber` flags** when creating users. Allow FreeIPA to assign UIDs and GIDs automatically from its default `idstart` range (typically 100000 and above).

The convention is `XZ0000`, where `X` is the VLAN zone prefix (e.g., `3` for the 3x Studio VLANs) and `Z` is a sub-identifier (e.g., `1` for the primary group in that zone).

This GID scheme also allows for a logical UID (User ID) numbering system. For example, users in a group with GID `310000` can be assigned UIDs in the range `310001` to `319999`.

| Group | VLAN Zone | Proposed GID | Example User IDs |
| :--- | :--- | :--- | :--- |
| `grp-production` | 1x | **110000** | `110001`, `110002`, ... |
| `grp-stage` | 2x | **210000** | `210001`, `210002`, ... |
| `grp-studio` | 3x | **310000** | `310001`, `310002`, ... |
| `grp-workshop` | 4x | **410000** | `410001`, `410002`, ... |
| `grp-management` | 5x | **510000** | `510001`, `510002`, ... |
| `grp-guest` | 6x | **610000** | `610001`, `610002`, ... |

## 3. Core Access Groups

These groups represent the primary access tiers that correspond to your network VLANs and resource categories.

### Create the Groups

Run these commands on the FreeIPA server (`ipa-01.bjoin.studio`) to create the core groups with their designated GIDs.

```bash
# Production Environment Group
ipa group-add grp-production --desc='Access group for the Production environment' --gid=110000

# Stage Environment Group
ipa group-add grp-stage --desc='Access group for the Stage environment' --gid=210000

# Studio Environment Group
ipa group-add grp-studio --desc='Access group for the Studio environment' --gid=310000

# Workshop Environment Group
ipa group-add grp-workshop --desc='Access group for the Workshop environment' --gid=410000

# Management Environment Group
ipa group-add grp-management --desc='Access group for the Management environment' --gid=510000

# Guest Access Group
ipa group-add grp-guest --desc='Limited access for guest users' --gid=610000
```

## 4. User Management

### Create a New User

The `ipa user-add` command creates the account but does not set a password. This must be done in a separate step.

```bash
# Example for creating a user named Jane Smith
ipa user-add jane.smith --first=Jane --last=Smith --email=jane.smith@bjoin.studio --shell=/bin/bash
```

### Set Initial Password

As an administrator, you must set an initial password for the new user. FreeIPA will require the user to change this password upon their first login.

```bash
# First, ensure you are authenticated as an IPA admin
kinit admin

# Now, set the initial password for the new user
ipa passwd jane.smith
```
The system will then prompt you to enter and confirm the new temporary password for the user.

### Add a User to a Group

This is how you grant a user access to a specific environment.

```bash
# Example: Add Jane Smith to the 'grp-studio' group
ipa group-add-member grp-studio --users=jane.smith
```

### Example: Creating an Administrator User

This is a real-world example for creating an administrator who needs broad access. It combines all the steps: creating the user with a specific UID/GID, setting their password, and adding them to supplemental groups.

```bash
# Step 1: Create the user with a specific UID and set their primary group to grp-management
echo "Creating user nick_bjoin..."
ipa user-add nick_bjoin --first=Nick --last=Bjoin --email=nick_bjoin@bjoin.studio --shell=/bin/bash --uid=510001 --gidnumber=510000

# Step 2: Set the initial password for the new user
# Ensure you have an active admin ticket (kinit admin)
ipa passwd nick_bjoin

# Step 3: Add the user to their additional access groups
echo "Adding nick_bjoin to supplemental groups..."
ipa group-add-member grp-production --users=nick_bjoin
ipa group-add-member grp-stage --users=nick_bjoin
ipa group-add-member grp-studio --users=nick_bjoin
ipa group-add-member grp-workshop --users=nick_bjoin

echo "User setup complete."
```

### Remove a User from a Group

```bash
# Example: Remove nick_bjoin from the 'grp-workshop' group
ipa group-remove-member grp-workshop --users=nick_bjoin
```

## 5. Verification

### Show User Information

You can verify a user's details and group memberships.

```bash
# See details for nick_bjoin, including group membership
ipa user-show nick_bjoin
```

### Show Group Information

You can see the members of a specific group.

```bash
# See all members of the 'grp-studio' group
ipa group-show grp-studio
```