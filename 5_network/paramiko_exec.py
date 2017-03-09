#!/usr/bin/env python

import paramiko

hostname = '192.168.1.15'
port = 22
username = 'jmjones'
password = 'xxxYYYxxx'

if __name__ == "__main__":
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print (stdout.read())
    s.close()


#写脚本使用ssh协议, 除了使用ssh协议的全部功能,还能使用python的全部功能
# /usr/local/Python3/bin/python3 paramiko_exec.py
#故障
#paramiko.ssh_exception.SSHException: Server 'localhost' not found in known_hosts