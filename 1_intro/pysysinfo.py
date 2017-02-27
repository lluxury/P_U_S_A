#!/usr/bin/env python
#A System Information Gathering Script
# v 3.0
import subprocess

#Command 1
uname = "uname"
uname_arg = "-a"
print( "Gathering system information with %s command:\n" % uname)
subprocess.call([uname, uname_arg])

#Command 2
diskspace = "df"
diskspace_arg = "-h"
print(subprocess.call([diskspace, diskspace_arg]))

#subprocess.call("df -h", shell=True)