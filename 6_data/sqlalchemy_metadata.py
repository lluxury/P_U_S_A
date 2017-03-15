#!/usr/bin/env python
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
import os

#path
path = "/tmp"

#Part 1:  create engine
engine = create_engine('sqlite:///:memory:', echo=False)

#Part 2:  metadata
metadata = MetaData()

filesystem_table = Table('filesystem', metadata,
   Column('id', Integer, primary_key=True),
     Column('path', String(500)),
     Column('file', String(255)),
)

metadata.create_all(engine)

#Part 3:  mapped class
class Filesystem(object):

    def __init__(self, path, file):
        self.path = path
        self.file = file

    def __repr__(self):
        return "[Filesystem('%s','%s')]" % (self.path, self.file)

#Part 4:  mapper function
mapper(Filesystem,filesystem_table)

#Part 5:  create session
Session = sessionmaker(bind=engine, autoflush=True, transactional=True)
session = Session()

#Part 6:  crawl file system and populate database with results
for dirpath, dirnames, filenames in os.walk(path):
    for file in filenames:
        fullpath = os.path.join(dirpath, file)
        record = Filesystem(fullpath, file)
        session.save(record)

#Part 7:  commit to the database
session.commit()

#Part 8:  query
for record in session.query(Filesystem):
    print ("Database Record Number: %s, Path: %s , File: %s " \
        % (record.id,record.path, record.file))

#/usr/local/Python3/bin/python3 sqlalchemy_metadata.py
#from pysqlite2 import dbapi2 as sqlite   #修改为sqlite3
#ImportError: No module named '_sqlite3'
#yum install sqlite-devel  貌似要重新编译python 先跳过

#创建引擎,定义实例,建表,创建类,放入ORM映射函数,创建数据库会话
#遍历目录树,提交,查询
