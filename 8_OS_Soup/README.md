#根据ip读配置文件,执行命令,独立纯种池中执行分发

osx
import subprocess
p = subprocess.Popen("dscl . read /Users/ngift", shell=True,stdout=subprocess.PIPE)
out = p.stdout.readlines()
for line in out:
    line.strip().split()

dscl命令
https://developer.apple.com/library/prerelease/content/releasenotes/OpenSource/PerlExtensionsRelNotes/
py-appscript

from appscript import appscript
sysevents = app('System Events')
processnames = sysevents.application_processes.name.get()
processnames.sort(lambda x, y: cmp(x.lower(), y.lower()))
print('\n' .join(processnames))


Libvert
Cobbler
Virt-Factory
FUNC


Amazon web
import boto
sdb = boto.connect_sdb()
domain = sdb.create_domain('my_domain')
item = domain.new_item('item')



