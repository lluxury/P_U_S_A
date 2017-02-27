#!/usr/bin/env python

# v 3.0

class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
    def set_ip(self, ip):
        self.ip = ip
    def set_hostname(self, hostname):
        self.hostname = hostname
    def ping(self, ip_addr):
        print ("Pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname))

if __name__ == '__main__':
    server = Server('192.168.1.20', 'bumbly')
    #函数的参数
    server.ping('192.168.1.15')
    #函数的方法