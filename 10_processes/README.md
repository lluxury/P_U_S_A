import subprocess
subprocess.call('df -k', shell=True)

#python3 /usr/bin/easy_install envoy
/usr/local/Python3/bin/pip3 install envoy
import envoy
r = envoy.run('git config', data='data to pipe in', timeout=2)
r.status_code
r.std_out
r.std_err
#之前没有注意环境的问题,结果出现3套配置

subprocess.call('du -hs $HOME', shell=True)

import subprocess
ret = subprocess.call("ping -c 1 10.0.1.1", shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
#subprocess.call会封锁响应,subprocess.Popen不会

subprocess.call("ls /foo", shell=True)

ret = subprocess.call("ls /foo", shell=True)
if ret == 0:
    print("success")
else:
    print("failure")

subprocess.call("rsync /foo /bar", shell=True)
#命令未发现, 127

import subprocess
subprocess.call("rsync", shell=True)

import subprocess
p = subprocess.Popen("df -h", shell=True, stdout=subprocess.PIPE)
out = p.stdout.readlines()
for line in out:
    print line.strip()


def multi(*args):
    for cmd in args:
        p = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE)
        out = p.stdout.read()
        print out

multi("df -h", "ls -l /tmp", "tail /var/log/system.log")



machines = ['homer', 'marge','lisa', 'bart']
for machine in machines:
    r = Runner("ssh " + machine + "df -h", "ssh " + machine + "du -h /tmp")
    r.run()


results = fc.Client("*").service.status("httpd")
for (host, returns) in results.iteritems():
if returns == 0:
fc.Client(host).reboot.reboot()
#发布脚本

p = subprocess.Popen("wc -c", shell=True, stdin=subprocess.PIPE)
p.communicate("charactersinword")

echo charactersinword | wc -c

from __future__ import with_statement
with open('temp.txt', 'w') as file:
    file.write('charactersinword')
file = open('temp.txt')
f = file.read()
p = subprocess.Popen("wc -c", shell=True, stdin=subprocess.PIPE)
p.communicate(f)
p.communicate(f)

#写入数据,读出,重定向到进程
echo charactersinword > temp.txt
wc -c < temp.txt

cat /etc/passwd | grep 0:0 | cut -d ':' -f 7

p1 = subprocess.Popen("cat /etc/passwd", shell=True, stdout=subprocess.PIPE)
p2 = subprocess.Popen("grep 0:0", shell=True, stdin=p1.stdout, stdout=subprocess.PIPE)
p3 = subprocess.Popen("cut -d ': ' -f 7", shell=True, stdin=p2.stdout, stdout=subprocess.PIPE)
print p3.stdout.read()
#子进程协同工作,注意stdin stdout搭配

import pwd
pwd.getpwnam('root')
#('root', '********', 0, 0, 'System Administrator', '/var/root', '/bin/sh')
shell = pwd.getpwnam('root')[-1]
shell
#使用pwd代替subprocess


ed upper.py
import subprocess
p = subprocess.Popen("tr a-z A-Z", shell=True,stdin=subprocess.PIPE,
stdout=subprocess.PIPE)
output, error = p.communicate("translatetoupper")
print outpu
#ipython中使用



#python3 /usr/bin/easy_install supervisor
#Supervisor requires Python 2.4 or later ?
https://github.com/Supervisor/supervisor


supervisor1.py
vi supervisord.conf
supervisord
supervisorctl

stop daemon
start daemon
tail -f daemon



screen python2.4 /usr/bin/tracd --hostname=trac.example.com --port 8888
-r --single-env --auth=*, /home/noahgift/trac-instance/conf/password, tracadminaccount /home/example/trac-instance/

screen -r
screen [-d] -r [pid.]tty.host


#线程,在同一个进程内共享状态及内存,不会要IPC或进程间通信
#调试困难,追踪库

thread1.py
nothread.py
 python3 /usr/bin/easy_install common
#ImportError: cannot import name 'IP_LIST'

ping_thread_basic.py
ping_thread_arp.py

thread_folder_watch.py


进程
#GIL 全局解释器锁, 某一时刻只有一个线程可以运行
#有些库不能和线程一起工作,比如net-snmp ?
# https://pypi.python.org/pypi/processing
# https://www.python.org/dev/peps/pep-0324/

processing1.py

python3 /usr/bin/easy_install ipy
processing_ping.py

# http://www.cnblogs.com/s380774061/p/4693066.html



/etc/cron.daily, /etc/cron.hourly, /etc/cron.monthly, /etc/cron.weekly
df -h | mail -s "Nightly Disk Usage Report" staff@example.com
cron_email.py

daemonize.py
use_daemonize.py
http://mojijs.com/2014/04/134219/index.html


#还有一些代码不知道归哪一块, 保留原位置待后续处理