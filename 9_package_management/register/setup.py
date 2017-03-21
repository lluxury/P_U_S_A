#!/usr/bin/env python
# liten 0.1.4.2 -- deduplication command-line tool
#
# Author: Noah Gift
try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import os,sys

version = '0.1.4.2'
f = open(os.path.join(os.path.dirname(__file__), 'docs', 'index.txt'))
long_description = f.read().strip()
f.close()

setup(
    name='liten',
    version='0.1.4.2',
    description='a de-duplication command line tool',
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
    ],
    author='Noah Gift',
    author_email='noah.gift@gmail.com',
    url='http://pypi.python.org/pypi/liten',
    download_url="http://code.google.com/p/liten/downloads/list",
    license='MIT',
    py_modules=['virtualenv'],
    zip_safe=False,
    py_modules=['liten'],
    entry_points="""
    [console_scripts]
    liten = liten:main
    """,
    )   

#未测试,待研究
#python setup.py register
#添加的额外字段 description long_description classifiers author download_url
#Easy install
#http://peak.telecommunity.com/DevCenter/EasyInstall
#Python eggs
#http://peak.telecommunity.com/DevCenter/PythonEggs
#The setuptools module
#http://peak.telecommunity.com/DevCenter/setuptools
#The package resources module
#http://peak.telecommunity.com/DevCenter/PkgResources
#Architectural overview of pkg_resources and Python eggs in general
#mailing list 
#http://mail.python.org/pipermail/distutilssig/.