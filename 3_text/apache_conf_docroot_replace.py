#!/usr/bin/env python
#replace host v3

#from cStringIO import StringIO
#for 2.7
from io import StringIO
import re

vhost_start = re.compile(r'<VirtualHost\s+(.*?)>')
vhost_end = re.compile(r'</VirtualHost')
docroot_re = re.compile(r'(DocumentRoot\s+)(\S+)')

def replace_docroot(conf_string, vhost, new_docroot):
    '''yield new lines of an httpd.conf file where docroot lines matching
        the specified vhost are replaced with the new_docroot
    '''
    conf_file = StringIO(conf_string)
    in_vhost = False
    curr_vhost = None
    for line in conf_file:
        vhost_start_match = vhost_start.search(line)
        if vhost_start_match:
            curr_vhost = vhost_start_match.groups()[0]
            in_vhost = True

        if in_vhost and (curr_vhost == vhost):
            docroot_match = docroot_re.search(line)
            if docroot_match:
                sub_line = docroot_re.sub(r'\1%s' % new_docroot, line)
                line = sub_line
        vhost_end_match = vhost_end.search(line)

        if vhost_end_match:
            in_vhost = False
        yield line

if __name__ == '__main__':
    import sys
    conf_file = sys.argv[1]
    vhost = sys.argv[2]
    docroot = sys.argv[3]
    conf_string = open(conf_file).read()
    for line in replace_docroot(conf_string, vhost, docroot):
        print (line),

#   /usr/local/Python3/bin/python3 apache_conf_docroot_replace.py /etc/apache2/sites-available/psa local2:80 /tmp

#Python3 没有cStringIO, 改为io

#找到VirtualHost 替换DocumentRoot,打印输出而不是替换文件
#遍历配置文件里的行,建立3个编译后的正则: 开头有定义, 遍历,找开始,找到赋值curr_vhost,in_vhost为真
#开始,true,替换,结束, flase ;3种情况判断; 在vhost块 and 匹配==参数, 赋值docroot_match,为真,赋值suub_line, 换回行,找块尾

#一个匹配VirtualHost开始 ,一个匹配VirtualHost结尾 一个匹配DocumentRoot

#docroot_re.sub(r'\1%s' % new_docroot, line)   
#\1 对应的第一个匹配组, 值,替换值, 所在行

#yield 迭代 生成generator
# http://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/
