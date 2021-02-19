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
        gid = elements[1]
        gname = elements[0]
        subprocess.check_call("addgroup -g" + shlex.quote(gid) + " " + shlex.quote(gname), shell=True)
        print("Added group " + gname + " with gid " + gid)
        

    # username,uid,password,[group]
    for user in users:
        elements = user.split(',')
        if (len(elements) != 3 and len(elements) != 4):
            print("Skipping invalid user config string \"" + user + "\"")
            continue
        uname = elements[0]
        uid = elements[1]
        passwd = elements[2]
        subprocess.check_call("adduser -D -H -u ", shlex.quote(uid), shlex.quote(uname), shell=True)
        print("Added user " + uname + " with uid " + uid)
        if (len(elements) == 4):
            gname = elements[3]
            subprocess.check_call("addgroup " + shlex.quote(uname) + " " + shlex.quote(gname), shell=True)
            print("Added user " + uname + " to group " + gname)
        # set passwd
        subprocess.check_call("echo -ne " + shlex.quote("\n" + passwd + "\n" + passwd + "\n") + " | smbpasswd -a -U " + shlex.quote(uname), shell=True)
        print("Set user " + uname + " password to " + passwd)

main()