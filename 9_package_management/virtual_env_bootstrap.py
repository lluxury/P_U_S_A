#!/usr/bin/env python
# encoding: utf-8
"""
virtual_env_bootstrap_creator_example.py

Created by ngift on 2008-03-08.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess
def after_install(options, home_dir):
    etc = join(home_dir, 'etc')
    if not os.path.exists(etc):
        os.makedirs(etc)
    subprocess.call([join(home_dir, 'bin', 'easy_install'),
                     'liten'])
"""))
f = open('liten-bootstrap.py', 'w').write(output)


#最后2行注意,告诉after_install在liten-bootstrap.py的工作目录上写入了一个新文件
#加入了一个自定义easy_install,代码创建了一个bootstrap.py文件并执行

#python liten-bootstrap.py --no-site-packages /tmp/liten-ENV
#/tmp/liten-ENV/bin/liten
#用脚本创建独立的启动空间?

#http://groups.google.com/group/python-virtualenv/