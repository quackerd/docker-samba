#!/bin/sh
set +xe
echo "====== Configuring users and groups ====="
python3 /opt/add-user-group.py "$GROUPS" "$USERS"
echo ""
echo "====== Starting Samba Daemon ====="
exec smbd -S -F -d 2 --no-process-group -s /samba/smb.conf
