#!/bin/bash

# FreeIPA User and Group Management Scripts
# Make sure you're authenticated with kinit admin before running

#=============================================================================
# CONFIGURATION - Modify these variables for your environment
#=============================================================================

IPA_DOMAIN="example.com"
DEFAULT_PASSWORD="TempPass123!"
LOG_FILE="/var/log/ipa-management.log"

#=============================================================================
# LOGGING FUNCTION
#=============================================================================

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOG_FILE"
}

#=============================================================================
# USER MANAGEMENT FUNCTIONS
#=============================================================================

# Create a single user
create_user() {
    local username="$1"
    local firstname="$2"
    local lastname="$3"
    local email="$4"
    local password="${5:-$DEFAULT_PASSWORD}"
    
    if [[ -z "$username" || -z "$firstname" || -z "$lastname" ]]; then
        log_message "ERROR: Missing required parameters for user creation"
        echo "Usage: create_user <username> <firstname> <lastname> [email] [password]"
        return 1
    fi
    
    # Set email if not provided
    email="${email:-${username}@${IPA_DOMAIN}}"
    
    log_message "Creating user: $username ($firstname $lastname)"
    
    ipa user-add "$username" \
        --first="$firstname" \
        --last="$lastname" \
        --email="$email" \
        --password="$password" \
        --shell=/bin/bash \
        --homedir="/home/$username"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: User $username created successfully"
    else
        log_message "ERROR: Failed to create user $username"
        return 1
    fi
}

# Create users from CSV file
# CSV format: username,firstname,lastname,email,password
create_users_from_csv() {
    local csv_file="$1"
    
    if [[ ! -f "$csv_file" ]]; then
        log_message "ERROR: CSV file $csv_file not found"
        return 1
    fi
    
    log_message "Creating users from CSV file: $csv_file"
    
    # Skip header line if present
    tail -n +2 "$csv_file" | while IFS=, read -r username firstname lastname email password; do
        # Skip empty lines
        [[ -z "$username" ]] && continue
        
        create_user "$username" "$firstname" "$lastname" "$email" "$password"
        sleep 1  # Small delay to avoid overwhelming the server
    done
}

# Bulk create users with a pattern
create_bulk_users() {
    local prefix="$1"
    local count="$2"
    local start_num="${3:-1}"
    
    if [[ -z "$prefix" || -z "$count" ]]; then
        echo "Usage: create_bulk_users <prefix> <count> [start_number]"
        return 1
    fi
    
    log_message "Creating $count users with prefix $prefix"
    
    for ((i=start_num; i<start_num+count; i++)); do
        local username="${prefix}$(printf "%03d" $i)"
        create_user "$username" "User" "$username" "${username}@${IPA_DOMAIN}"
    done
}

# Delete a user
delete_user() {
    local username="$1"
    
    if [[ -z "$username" ]]; then
        echo "Usage: delete_user <username>"
        return 1
    fi
    
    log_message "Deleting user: $username"
    
    ipa user-del "$username"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: User $username deleted successfully"
    else
        log_message "ERROR: Failed to delete user $username"
        return 1
    fi
}

#=============================================================================
# GROUP MANAGEMENT FUNCTIONS
#=============================================================================

# Create a group
create_group() {
    local groupname="$1"
    local description="$2"
    
    if [[ -z "$groupname" ]]; then
        echo "Usage: create_group <groupname> [description]"
        return 1
    fi
    
    description="${description:-Group $groupname}"
    
    log_message "Creating group: $groupname"
    
    ipa group-add "$groupname" --desc="$description"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: Group $groupname created successfully"
    else
        log_message "ERROR: Failed to create group $groupname"
        return 1
    fi
}

# Add user to group
add_user_to_group() {
    local username="$1"
    local groupname="$2"
    
    if [[ -z "$username" || -z "$groupname" ]]; then
        echo "Usage: add_user_to_group <username> <groupname>"
        return 1
    fi
    
    log_message "Adding user $username to group $groupname"
    
    ipa group-add-member "$groupname" --users="$username"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: User $username added to group $groupname"
    else
        log_message "ERROR: Failed to add user $username to group $groupname"
        return 1
    fi
}

# Remove user from group
remove_user_from_group() {
    local username="$1"
    local groupname="$2"
    
    if [[ -z "$username" || -z "$groupname" ]]; then
        echo "Usage: remove_user_from_group <username> <groupname>"
        return 1
    fi
    
    log_message "Removing user $username from group $groupname"
    
    ipa group-remove-member "$groupname" --users="$username"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: User $username removed from group $groupname"
    else
        log_message "ERROR: Failed to remove user $username from group $groupname"
        return 1
    fi
}

# Add multiple users to a group
add_users_to_group() {
    local groupname="$1"
    shift
    local users=("$@")
    
    if [[ -z "$groupname" || ${#users[@]} -eq 0 ]]; then
        echo "Usage: add_users_to_group <groupname> <user1> [user2] [user3] ..."
        return 1
    fi
    
    log_message "Adding ${#users[@]} users to group $groupname"
    
    # Join array elements with commas
    local user_list=$(IFS=,; echo "${users[*]}")
    
    ipa group-add-member "$groupname" --users="$user_list"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: Users added to group $groupname: ${users[*]}"
    else
        log_message "ERROR: Failed to add some users to group $groupname"
        return 1
    fi
}

# Create group and add users from CSV
# CSV format: username (one per line)
create_group_from_csv() {
    local groupname="$1"
    local csv_file="$2"
    local description="$3"
    
    if [[ -z "$groupname" || -z "$csv_file" ]]; then
        echo "Usage: create_group_from_csv <groupname> <csv_file> [description]"
        return 1
    fi
    
    if [[ ! -f "$csv_file" ]]; then
        log_message "ERROR: CSV file $csv_file not found"
        return 1
    fi
    
    # Create the group first
    create_group "$groupname" "$description"
    
    # Add users from CSV
    log_message "Adding users to group $groupname from CSV file: $csv_file"
    
    while IFS= read -r username; do
        # Skip empty lines and comments
        [[ -z "$username" || "$username" =~ ^#.*$ ]] && continue
        
        add_user_to_group "$username" "$groupname"
    done < "$csv_file"
}

#=============================================================================
# UTILITY FUNCTIONS
#=============================================================================

# List all users
list_users() {
    echo "=== FreeIPA Users ==="
    ipa user-find --all | grep -E "(User login|First name|Last name|Email|UID)"
}

# List all groups
list_groups() {
    echo "=== FreeIPA Groups ==="
    ipa group-find --all | grep -E "(Group name|Description|GID)"
}

# Show group members
show_group_members() {
    local groupname="$1"
    
    if [[ -z "$groupname" ]]; then
        echo "Usage: show_group_members <groupname>"
        return 1
    fi
    
    echo "=== Members of group $groupname ==="
    ipa group-show "$groupname" | grep -A 20 "Member users:"
}

# Reset user password
reset_user_password() {
    local username="$1"
    local new_password="$2"
    
    if [[ -z "$username" ]]; then
        echo "Usage: reset_user_password <username> [new_password]"
        return 1
    fi
    
    new_password="${new_password:-$DEFAULT_PASSWORD}"
    
    log_message "Resetting password for user: $username"
    
    ipa passwd "$username" <<< "$new_password"
    
    if [ $? -eq 0 ]; then
        log_message "SUCCESS: Password reset for user $username"
        echo "New password: $new_password"
    else
        log_message "ERROR: Failed to reset password for user $username"
        return 1
    fi
}

# Check if user exists
user_exists() {
    local username="$1"
    ipa user-show "$username" &>/dev/null
}

# Check if group exists
group_exists() {
    local groupname="$1"
    ipa group-show "$groupname" &>/dev/null
}

#=============================================================================
# EXAMPLE USAGE AND MAIN FUNCTION
#=============================================================================

show_usage() {
    cat << EOF
FreeIPA User and Group Management Script

Usage: $0 <command> [arguments]

User Commands:
  create-user <username> <firstname> <lastname> [email] [password]
  create-users-csv <csv_file>
  create-bulk-users <prefix> <count> [start_number]
  delete-user <username>
  reset-password <username> [new_password]
  list-users

Group Commands:
  create-group <groupname> [description]
  add-user-to-group <username> <groupname>
  remove-user-from-group <username> <groupname>
  add-users-to-group <groupname> <user1> [user2] [user3] ...
  create-group-csv <groupname> <csv_file> [description]
  list-groups
  show-group-members <groupname>

Examples:
  $0 create-user jdoe John Doe john.doe@example.com
  $0 create-bulk-users student 50 1
  $0 create-group developers "Development Team"
  $0 add-user-to-group jdoe developers

Note: Make sure you're authenticated with 'kinit admin' before running commands.
EOF
}

# Main function to handle command-line arguments
main() {
    if [[ $# -eq 0 ]]; then
        show_usage
        exit 1
    fi
    
    # Check if user is authenticated
    klist &>/dev/null
    if [[ $? -ne 0 ]]; then
        echo "ERROR: Not authenticated. Please run 'kinit admin' first."
        exit 1
    fi
    
    command="$1"
    shift
    
    case "$command" in
        create-user)
            create_user "$@"
            ;;
        create-users-csv)
            create_users_from_csv "$@"
            ;;
        create-bulk-users)
            create_bulk_users "$@"
            ;;
        delete-user)
            delete_user "$@"
            ;;
        reset-password)
            reset_user_password "$@"
            ;;
        list-users)
            list_users
            ;;
        create-group)
            create_group "$@"
            ;;
        add-user-to-group)
            add_user_to_group "$@"
            ;;
        remove-user-from-group)
            remove_user_from_group "$@"
            ;;
        add-users-to-group)
            add_users_to_group "$@"
            ;;
        create-group-csv)
            create_group_from_csv "$@"
            ;;
        list-groups)
            list_groups
            ;;
        show-group-members)
            show_group_members "$@"
            ;;
        *)
            echo "Unknown command: $command"
            show_usage
            exit 1
            ;;
    esac
}

# Only run main if script is executed directly (not sourced)
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi