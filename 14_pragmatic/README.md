
sudo easy_install dnspython

import dns.resolver
ip = dns.resolver.query("oreilly.com","A")
mail = dns.resolver.query("oreilly.com","MX")
for i,p in ip,mail:
    print i,p


python-ldap
#https://www.python-ldap.org/download.html

import ldap
l = ldap.open("ldap.itd.umich.edu")
l.simple_bind()
#失败
try:
     l = ldap.open("127.0.0.1")
 except Exception,err:
 print err
 l.simple_bind()
#有ldap服务器在运行,代码良好

加载LDIF文件


