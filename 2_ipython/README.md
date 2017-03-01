 class DoubleRep(object):
     def __str__(self):
         return "Hi, I'm a __str__"
     def __repr__(self):
         return "Hi, I'm a __str__"

#貌似3.0 非正式字符串改掉了,待确认


 type(In)
 list
#使用列表,可以省略保存位置
 type(Out)
 dict
#每行都有输入,但不一定都有输出,所以用字典的方式保存,不用考虑null


~.ipython 定制用文件

In [31]: %cd Navicat/
In [33]: lsmagic
#魔力函数?

In [41]: alias nss netstat -lptn

In [42]: alias achoo echo "%1"
In [55]: alias achoo echo first: "|%s|", second: "|%s|"
In [56]: achoo foo bar
#别名跟参数,参数不足会报错
In [57]: store achoo

#执行shell
In [62]: !netstat - lptn

In [62]: user = 'yann'
In [63]: process = 'bash'
In [64]: !ps aux |grep $user |grep $process
#变量传递
l = !ps aux |grep $user |grep $process
#保存结果

In [66]: __IP.alias_table
In [67]: rehash
In [68]: __IP.alias_table['transcode']

In [69]: rehashx

In [72]: os.chdir('C:\\Users\\yann\\Documents')
In [79]: cd -1

In [81]: bookmark t
In [82]: bookmark -l
In [83]: cd -b t

In [84]: dhist
In [86]: cd - [tab]


 [88]: for i in range(10):
  ...:     !date >${i}.txt

#可变扩展[]


ps = !ps aux
ps.grep('sshd')
ps.grep('Mar07', prune=True)
# 符合正则的都删掉[]

import os
file_list = !ls
file_list
file_list.grep(os.path.isfile)
file_list.grep(os.path.isdir)

In [99]: ps.grep('Mar07', prune=True).fields(0, 1, 8)
#列选取例子[]


ps.fields(0, 1).grep('root').fields(1)
ps.fields(0, 1).grep('root').fields(1).s
#结果集[]

ps = !ps aux
ps.grep('root', field=0)
ps.grep('root', field=0).fields(1)
#列过滤[]

ipython3 -p sh
import os
os.environ['PATH']
env PATH+=:/appended
env PATH-=:/appended:
env -d PATH
#环境,貌似不可用[]

mglob rec:*.py
mglob dir:*
#sh profile[]

p = !ps aux
page p
#分页[]

def myfunc(a, b, c, d):
    '''abcd '''
pdef myfunc
hist
#打印函数声明部分[]
pdoc myfunc
#打印函数注释[]

import os
pfile os
#能够运行的对象文件[]

import xx
pinfo xx
pinfo xx.yy
#类,基础类,命名空间[]

f = xx.yy()
?? myfunc
#信息及源码

import myfunc
psource myfunc
#源代码[]

psearch a*
psearch -e builtin a*
#搜索[]


who
#列出交互对象


who_ls
who_ls int
who_ls str
whos

CTRL-s CTRL-r
hist
_  a=_  历史结果

alias
macro
store  -d -z -r
#储存变量

reset 
#删变量


run
save

rep
def format_str(s):
    return "str(%s)" % s
format_str(1)
rep
str(1)
#混合generators 和宏 输出放输入


















