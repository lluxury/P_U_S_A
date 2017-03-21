curl http://peak.telecommunity.com/dist/ez_setup.py
locate ez_setup.py

/usr/bin/easy_install*
#安装setuptools时,会安装easy_install的脚本用于安装和管理代码
#涉及PyPI,Cheeseshop https://pypi.python.org/pypi
#下载脚本,运行ez_setup.py,指明版本

easy_install ipython
#http://dirtsimple.org/programming/

#搜索
easy_install -f http://code.google.com/p/liten/ liten

#源码安装,可以本地网络安装
easy_install http://superb-west.dl.sourceforge.net/sourceforge/sqlalchemy/SQLAlchemy-0.4.3.tar.gz

#升级
easy_install cherrypy==2.2.1
python3 /usr/bin/easy_install sqlalchemy
#说不定之前的代码可以测试了

easy_install --upgrade cherrypy
#到最新版,不加则不会处理

easy_install
#当前目录
easy_install --editable --build-directory ~/sandbox liten
#指定目录


easy_install liten=0.1.3
#修改包的活动版本(已安装)

easy_install -f "http://svn.colorstudy.com/virtualenv/trunk/virtualenv.py#egg=virtualenv-1.0" virtualenv
easy_install -f "http://svn.colorstudy.com/virtualenv/trunk/virtualenv.py#egg=foofoo-1.0" foofoo
#转化为egg,使用环境或包名

easy_install -f http://uid:passwd@example.com/packages

#配置文件在current_working_directory/setup.cfg或 ~/.pydistutils.cfg
#内容
[easy_install]
#Where to look for packages
find_links = http://code.example.com/downloads
#Restrict searches to these domains
allow_hosts = *.example.com
#Where to install packages. Note, this directory has to be on the PYTHONPATH
install_dir = /src/lib/python

#https://mail.python.org/mailman/listinfo/distutils-sig



#egg是python包的集合
#安装setuptools,创建egg中的文件,创建setup.py文件,运行


cd /tmp
mkdir egg-example
cd egg-example
touch hello-egg.py

vi setup.py
from setuptools import setup, find_packages
setup(
name = "HelloWorld",
version = "0.1",
packages = find_packages(),
)

python3 setup.py bdist_egg
#固定名称
#sudo easy_install HelloWorld-0.1-py2.5.egg
python3 /usr/bin/easy_install dist/HelloWorld-0.1-py3.4.egg

setup.py  
symlinkator.py
python3 setup.py bdist_egg
python3 /usr/bin/easy_install dist/symlinkator-0.1-py3.4.egg

from symlinkator import get_links
get_links('/home/jmjones/logs/')


#控制台脚本
    entry_points = {
        'console_scripts': [
            'linkator = symlinkator.symlinkator:main',
        ],
    },
#脚本执行时,调用symlinkator.symlinkator模块的main函数,用户路径命令行



distutils
#写安装脚本setup.py,基本配置,创建源码包,创建二进制
distutils_ex.py
setup.py
python setup.py sdist
#对比egg的命令
python setup.py install
#解压包并安装

#rpm包,苹果不能用
python setup.py bdist_rpm
python setup.py bdist_pkgtool
python setup.py bdist_sdux

python setup.py build --build-base=/mnt/python_src/a_script.py
#待测试
https://pypi.python.org/pypi/zc.buildout

#plone ? buildout工具
bootstrap.py
buildout.cfg
python bootstrap.py
bin/buildout
bin/mypython
import liten
bin/liten
#liten与进入点一起创建,egg除了本地buildout的bin目录中的模块外,自动安装一个控制台脚本
#buidlout创建独立环境并自动部署项目及环境

bin/buildout -N
#删除配置后运行, 解释器和命令行不见了,只有buildout命令行,egg在但没有激活,没有解释器

virtualenv
#创建虚拟环境,和buildout类似,buildout使用声明的配置文件
#两都都扩展使用了setuptools
# http://www.ianbicking.org/blog/
sudo easy_install virtualenv
curl http://svn.colorstudy.com/virtualenv/trunk/virtualenv.py > virtualenv.py
sudo cp virtualenv.py /usr/local/bin/virtualenv.py
#多环境
alias virtualenv-py24="/usr/bin/python2.4 /usr/local/bin/virtualenv.py"
alias virtualenv-py25="/usr/bin/python2.5 /usr/local/bin/virtualenv.py"
alias virtualenv-py26="/usr/bin/python2.6 /usr/local/bin/virtualenv.py"

virtualenv-py24 /tmp/sandbox/py24ENV
/tmp/sandbox/py24ENV/bin/python

virtualenv-py25 /tmp/sandbox/py25ENV
/tmp/sandbox/py25ENV/bin/python
#分别生成了2个不同环境
#可以使用全路径,也可以使用虚拟目录下bin\下的活动脚本来设置环境使用sandbox,不用全路径
#使用过,待补充
# http://www.doughellmann.com/projects/virtualenvwrapper/


#EMP多环境配置
./configure
make
make install


python hello_epm.py
python hello_epm.py --os RedHat

hello_epm.list

cd /tmp/release/hello_epm
touch README
touch COPYING
mkdir doc
touch doc/hello_epm.html
touch doc/hello_epm.man
#构建需要的文件

#epm -f osx hello_epm hello_epm.list
epm -f osx helloEPM hello_epm.list
ls -la macosx-10.5-intel

which hello_epm
hello_epm
hello_epm -h

scp -r  /tmp/release/hello xx
