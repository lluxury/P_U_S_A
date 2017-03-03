import subprocess
res = subprocess.Popen(['uname', '-sv'], stdout=subprocess.PIPE)
uname = res.stdout.read().strip()
#uname.index('Linux')
#uname.find('Linux')
uname.find(b'Linux')
uname.index(b'Linux')

#TypeError: a bytes-like object is required, not 'str'
#3.0中部分函数参数需要bytes，如果使用str会报告TypeError: a bytes-like object is required, not ‘str’的错误
#为避免以上错误，需要在字符串前增加b将str转换为bytes []

smp_index = uname.index(b'SMP')
smp_index
uname[smp_index:]
#SMP 后的值[]
#env PATH+=:/appended
#/appended加在PATH最后
uname[:smp_index]
#SMP 前的值[]


some_string = "Raymond Luxury-Yacht"
some_string.startswith("Raymond")
#AttributeError: 'str' object attribute 'startswith' is read-only
some_string.endswith("Raymond")
some_string[:len("Raymond")]=="Raymond"
#some_string[-len("Luxury-Yacht")]=="Luxury-Yacht" X
some_string[-len("Luxury-Yacht"):]=="Luxury-Yacht"

lstrip() rstrip() strip()
#创建新的字符串然后处理
spacious_string = "\n\t Some Non-Spacious Text\n \t\r"
spacious_string
print(spacious_string)
spacious_string.lstrip()
print(spacious_string.lstrip())


xml_tag="<some_tag>"
xml_tag.lstrip("<")
xml_tag.strip("<").strip(">")
#并不是按输入顺序匹配的

mixed_case_string ="Vorpal Bunny"
mixed_case_string.lower() == "vorpal bunny"

comma_delim_string = "pos1,pos2,pos3"
pip_delim_string = "pipepos1|pipepos2|pipepos3"
comma_delim_string.split(',')
pip_delim_string.split('|')


multiline_string= '''xx'''
lines = multiline_string.splitlines()
#行截取 每一行所组成的列表

some_list= ['one', 'two', 'three', 'four']
','.join(some_list)
''.join(some_list)

some_list = range(10)
#','.join(some_list)  整数元素需要转换为字符串
','.join([str(i) for i in some_list])
','.join(str(i) for i in some_list)

replacable_string = "trancendental hibernational nation"
replacable_string.replace("nation", "natty")

#内建字符串类型 str
#字符串类型 unicod 
unicode_string = u'this is a unicode string'
print(unicode_string)
#unicode('this is a unicode string') v3x
unicode_string = u'abc_\u03a0\u03a3\u03a9_\u0414\u0424\u042F'
print(unicode_string)
#print unicode_string.encode('utf-8') v3x

re
#Mastering Regular Expressions
import re
re_string = "{{(.*?)}}"
some_string = "this is a string with {{words}} embedded in\
{{curly brackets}} to show an {{example}} of {{regular expressions}}"

for match in re.findall(re_string, some_string):
    print( "MATCH->", match)
#{{+任意文本 (.*?) + }} 循环处理

#另一种方法
import re
re_obj = re.compile("{{(.*?)}}")
some_string = "this is a string with {{words}} embedded in\
{{curly brackets}} to show an {{example}} of {{regular expressions}}"
for match in re_obj.findall(some_string):
    print("MATCH->", match)


re_loop_nocomplie
timeit -n 5 re_loop_nocomplie.run_re()
#导入及运行[]
time python3 re_loop_nocomplie.py
re_loop_complie
#性能比较, 编译后性能更好

import re
raw_pattern = r'\b[a-z]+\b'
some_string = 'a few little words'
re.findall(raw_pattern, some_string)
non_raw_pattern = '\b[a-z]+\b'
re.findall(non_raw_pattern, some_string)
#正则 /b 匹配词边界, 原始字符
some_other_string = 'a few \blittle\b words'
re.findall(non_raw_pattern, some_other_string)

findall() #所有可能匹配,包括有空格 返回列表或多元列表
finditer() #返回迭代,不是列表
match() search() #匹配


import re
re_obj = re.compile('F00')
search_string = ' F00'
re_obj.search(search_string)
re_obj.match(search_string)
#match无法从开始搜索?
re_obj.search(search_string, pos=1)
re_obj.match(search_string, pos=1)
re_obj.search(search_string, pos=1, endpos=3)
re_obj.match(search_string, pos=1, endpos=3)
#start(), end(), span(), group(), groupdict() match方法

#修改vhost

infile = open("foo.txt", "r")
print(infile.read())
outputfile = open("foo_out.txt", "w")
outputfile.write("This is \nSome\nRandom\nOutput Text\n")
outputfile.close()
#读写文件
try:
    f = open("writeable.txt", "w")
    f.write("quick line here\n")
finally:
    f.close()


frome __future__ import with_statement
from __future__ import with_statement
with open('writeable.txt', 'w') as f:
    f.write('this is a writeable file\n')
f
#with 语句,使用上下文管理器,有__enter__() __exit__()方法
#Python Library Reference


f = open("foo.txt", "r")
f.read(5)
f = open("foo.txt", "r")
f.readline(7)
f = open("foo.txt", "r")
lines = f.readlines(1024)
len(lines)              #读取行数
len("".join(lines))     #读取字节
lenes = f.readlines()
len(lines)
len("".join(lines))
#注意检测,期望值与现实值,期望值1024字节
#读文件



f=open("some_writeable_file.txt", "w")
f.write("Test\nFile\n")
f.close()
g = open("some_writeable_file.txt", "r")
g.read()


f=open("writelines_outfile.txt", "w")
f.writelines("%s\n" % i for i in range(10))
f.close()
g = open("writelines_outfile.txt", "r")
g.read()
#序列写入


def myRange(r):
    i = 0
    while i < r:
        yield "%s\n" % i
        i += 1
f = open("writelines_generator_function_outfile", "w")
f.writelines(myRange(10))
f.close()
g = open("writelines_generator_function_outfile", "r")
g.read()
#函数的方法


import sys
f = open("foo.txt", "r")
sys.stdin
f
type(sys.stdin)== type(f)
#标准输入输出


import sys
f = open('foo.txt', 'w')
sys.stdout
f
type(sys.stdout)== type(f)



readable_file = open('foo.txt', 'r')
writable_file = open('foo_writeable.txt', 'w')
readable_file
writable_file
type(readable_file) == type(writable_file)
#sys.stdout 采用处理文件相同的方法

#from StringIO import StringIO
from io import StringIO
file_like_string = StringIO("This is a\nmultiline string. \n readline() should see\nmultiple lines of\ninput")
file_like_string.readline()
file_like_string.readline()
file_like_string.readline()
file_like_string.readline()
file_like_string.readline()
#StringIO对象 ,依次的读出来
dir(file_link_string)

f = open("foo.txt", "r")
#from sets import Set
sio_set = set(dir(file_like_string))
file_set = set(dir(f))
sio_set.difference(file_set)
sio_set.difference(sio_set)
#不明 StringIO


import urllib.request
#url_file = urllib.request("http://docs.python.org/lib/module-urllib.html")
url_file = urllib.request.urlopen("https://docs.python.org/3/library/index.html")
urllib_docs = url_file.read()
url_file.close()
len(urllib_docs)
urllib_docs[:80]
urllib_docs[-80:]
#打开,读,结束,前后80个字符 3.0发生了变化

#日志解析
apache_log_parser_split.py
/usr/local/Python3/bin/python3 test_apache_log_parser_split.py


vi test_apache_log_parser_regex.py
/usr/local/Python3/bin/python3   test_apache_log_parser_regex.py


#xml解析
from xml.etree import ElementTree as ET
tcusers = ET.parse('/etc/tomcat5.5/tomcat-users.xml')
tcusers
#first_user = tcusers.find('/user')  bug
first_user = tcusers.find('./user')
first_user
first_user.attrib
first_user.get('name')
first_user.get('foo')
first_user.tag
first_user.text
#find(), findall(), *所有子 .当前 //起点子孙, 
#attrib, find(), findall(), get(), tag ,text
