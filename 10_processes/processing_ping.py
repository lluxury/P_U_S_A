#!/usr/bin/env python
from multiprocessing import Process, Queue, Pool
import time
import subprocess
from IPy import IP
import sys

q = Queue()
ips = IP("10.0.1.0/24")
def f(i,q):
    while True:
        if q.empty():
            sys.exit()
        print("Process Number: %s" % i)
        ip = q.get()
        ret = subprocess.call("ping -c 1 %s" % ip,
                        shell=True,
                        stdout=open('/dev/null', 'w'),
                        stderr=subprocess.STDOUT)
        if ret == 0:
            print("%s: is alive" % ip)
        else:
            print("Process Number: %s didn't find a response for %s " % (i, ip))
            pass

for ip in ips:
    q.put(ip)

#q.put("192.168.1.1")

for i in range(50):
    p = Process(target=f, args=[i,q])
    p.start()

print("main process joins on queue")
p.join()
print("Main Program finished")

#队列为空,使用sys.exit让自己退出,主程序使用了join,将队列进行添加,队列为空,程序继续
