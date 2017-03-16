#snmp 也可以监控软件, RMON MIB
#MIB 名称翻译为数字, 像dns. 包含名称,类型,话音未落
#OID对象标识 数字或文本
snmpwalk -v 2c -c public localhost .1.3.6.1.2.1.1.1.0
snmpwalk -v 2c -c public localhost sysDescr


Net-SNMP
PySNMP (TwistedSnmp,Zenoss)

ldconfig -v /usr/local/lib


import netsnmp
oid = netsnmp.Varbind('sysDescr')
result = netsnmp.snmpwalk(oid, Version =2, DestHost="localhost", Community="public")
#sysDescr是一个重要的OID查询

#在IPython内部切换到vim, who来查看?


