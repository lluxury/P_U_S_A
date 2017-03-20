#!/usr/bin/env python
from fingerprint import fingerprint
from subprocess import call

os = fingerprint()

#Gets epm keyword correct
epm_keyword = {"ubuntu":"dpkg", "redhat":"rpm", "SunOS":"pkg", "osx":"osx"}

#try:
#    epm_keyword[os]
#except Exception, err:
#    print err

#if epm_keyword.has_key(os):
if os in epm_keyword:
        platform_cmd = epm_keyword[os]

subprocess.call("epm -f %s helloEPM hello_epm.list" % platform_cmd, shell=True)