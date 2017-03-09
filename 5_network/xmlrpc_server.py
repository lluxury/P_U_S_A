#!/usr/bin/env python

#import SimpleXMLRPCServer
import xmlrpc.server
import os

def ls(directory):
    try:
        return os.listdir(directory)
    except OSError:
        return []

def ls_boom(directory):
    return os.listdir(directory)

def cb(obj):
    print("OBJECT::", obj)
    print("OBJECT.__class__::", obj.__class__)
    return obj.cb()

if __name__ == '__main__':
    #s = SimpleXMLRPCServer.SimpleXMLRPCServer(('127.0.0.1', 8765))
    s = xmlrpc.server.SimpleXMLRPCServer(('127.0.0.1', 8765))
    s.register_function(ls)
    s.register_function(ls_boom)
    s.register_function(cb)
    s.serve_forever()

#import xmlrpc.client
#x = xmlrpc.client.ServerProxy('http://localhost:8765')

#建一个新的xmlrpc.server对象,绑在local的8765端口,注册 ls(),ls_boom(),cd() 函数 
# ls()会列出os.listdir()传来的目录内容, 列表方式,屏蔽错误, ls_boom()返回异常.
#从字典的xml版本中提取数据?