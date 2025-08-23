# FreeIPA User and Group Management Runbook

This document outlines the standards and procedures for managing users and groups within the `bjoin.studio` FreeIPA domain.

## 1. Naming Conventions

- **Usernames:** `firstname.lastname` (e.g., `john.doe`). All lowercase.
- **Groups:** `grp-<domain>` for primary groups (e.g., `grp-studio`). All lowercase.

## 2. Core Access Groups

These groups represent the primary access tiers that correspond to your network VLANs and resource categories, as defined in the main network design document. A user's membership in these groups will be used to control access to servers and file shares.

### Create the Groups

Run these commands on the FreeIPA server (`ipa-01.bjoin.studio`) to create the core groups.

```bash
# Production Environment Group
ipa group-add grp-production --desc='Access group for the Production environment'

# Stage Environment Group
ipa group-add grp-stage --desc='Access group for the Stage environment'

# Studio Environment Group
ipa group-add grp-studio --desc='Access group for the Studio environment'

# Workshop Environment Group
ipa group-add grp-workshop --desc='Access group for the Workshop environment'

# Management Environment Group
ipa group-add grp-management --desc='Access group for the Management environment'

# Guest Access Group
ipa group-add grp-guest --desc='Limited access for guest users'
```

## 3. User Management

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

## 4. Verification

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