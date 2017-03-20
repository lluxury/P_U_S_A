import re

"""Returns Hit Count for Firefox"""

def grep(lines,pattern="Firefox"):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line): yield line

def increment(lines):
    num = 0
    for line in lines:
        num += 1
    return num

wwwlog = open("/home/noahgift/logs/noahgift.com-combined-log")
column = (line.rsplit(None,1)[1] for line in wwwlog)
match  = grep(column)
count = increment(match)
print "Total Number of Firefox Hits: %s" % count




#修改conf
syslocation "O'Reilly"
syscontact bofh@oreilly.com
rocommunity public
exec helloworld /usr/bin/python -c "print 'hello world from Python'"
exec .1.3.6.1.5.1.2021.28664.100 FirefoxHits /usr/bin/python /opt/local/snmp_scripts/agent_ext_logs.python

