#!/usr/bin/env python

from twisted.internet import reactor, protocol
import sys

class PortCheckerProtocol(protocol.Protocol):
    def __init__(self):
        print("Created a new protocol")
    def connectionMade(self):
        print("Connection made")
        reactor.stop()

class PortCheckerClientFactory(protocol.ClientFactory):
    protocol = PortCheckerProtocol
    def clientConnectionFailed(self, connector, reason):
        print("Connection failed because", reason)
        reactor.stop()

if __name__ == '__main__':
    host, port = sys.argv[1].split(':')
    factory = PortCheckerClientFactory()
    print("Testing %s" % sys.argv[1])
    reactor.connectTCP(host, int(port), factory)
    reactor.run()


#twisted pip上没有,待确认
#事件驱动的网络框架
#反应器 reactor, 工厂 factory, 协议和延迟 deferred
