#!/usr/bin/python3

import os
import sys
import subprocess
import shlex

def main():
    if (len(sys.argv) < 3):
        print("No users/groups to configure.")
        return

    groups = sys.argv[1].split(';')
    users = sys.argv[2].split(';')

    # group,groupid
    for group in groups:
        elements = group.split(',')
        if (len(elements) != 2):
            print("Skipping invalid group config string \"" + group + "\"")
            continue
        subprocess.check_call(shlex.join(["addgroup", "-g", elements[1], elements[0]]), shell=True)
        print("Added group " + elements[0] + " with gid " + elements[1])
        

    # username,uid,password,[group]
    for user in users:
        elements = user.split(',')
        if (len(elements) != 3 and len(elements) != 4):
            print("Skipping invalid user config string \"" + user + "\"")
            continue
        subprocess.check_call(shlex.join(["adduser", "-D", "-H", "-u", elements[1], elements[0]]), shell=True)
        print("Added user " + elements[0] + " with uid " + elements[1])
        if (len(elements) == 4):
            subprocess.check_call(shlex.join(["addgroup", elements[0], elements[3]]), shell=True)
            print("Added user " + elements[0] + " to group " + elements[3])
        # set passwd
        subprocess.check_call(shlex.join(["echo", "-ne", "\"" + elements[2] + "\n" + elements[2] + "\n\""]) + " | " + shlex.join(["smbpasswd", "-a", "-U", elements[0]])), shell=True)
        print("Set user " + elements[0] + " password to " + elements[2])

main()