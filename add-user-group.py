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
        gid = elements[1].strip()
        gname = elements[0].strip()
        cmd = "addgroup -g" + shlex.quote(gid) + " " + shlex.quote(gname)
        print(cmd)
        subprocess.check_call("addgroup -g" + shlex.quote(gid) + " " + shlex.quote(gname), shell=True, stdout=subprocess.DEVNULL)
        

    # username,uid,password,[group]
    for user in users:
        elements = user.split(',')
        if (len(elements) < 3):
            print("Skipping invalid user config string \"" + user + "\"")
            continue
        uname = elements[0].strip()
        uid = elements[1].strip()
        passwd = elements[2].strip()
        cmd = "adduser -D -H -u " + shlex.quote(uid) + " " + shlex.quote(uname)
        print(cmd)
        subprocess.check_call(cmd, shell=True, stdout=subprocess.DEVNULL)
        if (len(elements) > 3):
            for i in range(3, len(elements)):
                gname = elements[i].strip()
                cmd = "addgroup " + shlex.quote(uname) + " " + shlex.quote(gname)
                print(cmd)
                subprocess.check_call(cmd, shell=True, stdout=subprocess.DEVNULL)
        # set passwd
        cmd = "echo -ne \"" + shlex.quote(passwd) + "\\n" + shlex.quote(passwd) + "\\n\" | smbpasswd -a -U " + shlex.quote(uname)
        print(cmd)
        subprocess.check_call(cmd, shell=True, stdout=subprocess.DEVNULL)

main()