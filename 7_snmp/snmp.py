#!/usr/bin/env python
import netsnmp

class Snmp(object):
    """A basic SNMP session"""
    def __init__(self,
                oid = "sysDescr",
                Version = 2,
                DestHost = "localhost",
                Community = "public"):
        self.oid = oid
        self.version = Version
        self.destHost = DestHost
        self.community = Community

    def query(self):
        """Creates SNMP query session"""
        try:
            result = netsnmp.snmpwalk(self.oid,
                                    Version = self.version,
                                    DestHost = self.destHost,
                                    Community = self.community)
        except Exception, as err:
            print (err)
            result = None
        return result


#测试 ipython
#who
s = snmp()
s.query()
result = s.query()
len(result)
s.oid
s.oid = ".1.3.6.1.2.1.1"
result = s.query()
print result

bg s.query()
jobs[0].status
jobs[0].result

