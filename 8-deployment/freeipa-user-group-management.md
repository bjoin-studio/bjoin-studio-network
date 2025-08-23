# FreeIPA User and Group Management Runbook

This document outlines the standards and procedures for managing users and groups within the `bjoin.studio` FreeIPA domain.

## 1. Naming Conventions

- **Usernames:** `firstname.lastname` (e.g., `john.doe`). All lowercase.
- **Groups:** `grp-<domain>` for primary groups (e.g., `grp-studio`). All lowercase.

## 2. Group ID (GID) Strategy

To create a clear and scalable identity management system, the Group IDs (GIDs) for the core access groups are aligned with the network's VLAN schema. This provides a predictable link between a user's group and their network zone.

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

Here is an example of how to create a new user. The command will prompt for a password.

```bash
# Example for creating a user named Jane Smith
ipa user-add jane.smith --first=Jane --last=Smith --email=jane.smith@bjoin.studio --shell=/bin/bash
```

### Add a User to a Group

This is how you grant a user access to a specific environment.

```bash
# Example: Add Jane Smith to the 'grp-studio' and 'grp-management' groups
ipa group-add-member grp-studio --users=jane.smith
ipa group-add-member grp-management --users=jane.smith
```

### Remove a User from a Group

```bash
# Example: Remove Jane Smith from the 'grp-management' group
ipa group-remove-member grp-management --users=jane.smith
```

## 5. Verification

### Show User Information

You can verify a user's details and group memberships.

```bash
# See details for jane.smith, including group membership
ipa user-show jane.smith
```

### Show Group Information

You can see the members of a specific group.

```bash
# See all members of the 'grp-studio' group
ipa group-show grp-studio
```