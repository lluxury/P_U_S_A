import Pyro.core
#import xmlrpclib
import xmlrpc.client

class PSACB:
    def __init__(self):
        self.some_attribute = 1

    def cb(self):
        return "PSA callback"

if __name__ == '__main__':
    cb = PSACB()

    print("PYRO SECTION")
    print("*" * 20)
    psapyro = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/psaexample")
    print("-->>", psapyro.cb(cb))
    print("*" * 20)

    print("XMLRPC SECTION")
    print("*" * 20)
    psaxmlrpc = xmlrpc.client.ServerProxy('http://localhost:8765')
    print("-->>", psaxmlrpc.cb(cb))
    print("*" * 20)

#ImportError: No module named 'Pyro'
#测试自定义对象 pyro可以执行,xml-rpc报错,dict没有cb属性
#字典化xml-rpc客户端创建对象时,some_attribute被转成一个字典关键字,这个属性保留时,cd()不保留
