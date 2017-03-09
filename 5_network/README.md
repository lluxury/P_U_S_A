
import socket
s = socket.socket()
s.connect(('192.168.0.1', 80))
#s.send("GET / HTTP/1.0\n\n")
s.send(b"GET / HTTP/1.1\n\n")
s.recv(200)
s.close()

#2块, 3.0特性要加b, 设备1.0协议不支付
#创建叫s的socket对象,连web发送请求



#http://old.sebug.net/paper/books/dive-into-python3/porting-code-to-python-3-with-2to3.html
python3 /usr/local/Python3/bin/2to3 -w test3/test2.py
#刷不过的时候,可以对比

