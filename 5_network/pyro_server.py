#!/usr/bin/env python

import Pyro.core
import os
from xmlrpc_pyro_diff import PSACB

class PSAExample(Pyro.core.ObjBase):

    def ls(self, directory):
        try:
            return os.listdir(directory)
        except OSError:
            return []

    def ls_boom(self, directory):
        return os.listdir(directory)

    def cb(self, obj):
        print("OBJECT:", obj)
        print("OBJECT.__class__:", obj.__class__)
        return obj.cb()

if __name__ == '__main__':
    Pyro.core.initServer()
    daemon=Pyro.core.Daemon()
    uri=daemon.connect(PSAExample(),"psaexample")

    print("The daemon runs on port:",daemon.port)
    print("The object's uri is:",uri)

    daemon.requestLoop()


#Python Remote Objects
#不需要对象字典化, 独立安装, 只能python使用
#3.0 安装包有故障,尚未解决

#import Pyro.core
#psa = Pyro.core.getProxyForURI("PYROLOC://localhost:7766/psaexample")
#psa.ls(".")
#psa.ls_boom('.')
