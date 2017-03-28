import pickle
some_dict = {'a': 1, 'b': 2}
#pickle_file = open('some_dict.pkl', 'w')
pickle_file = open('some_dict.pkl', 'wb')
pickle.dump(some_dict, pickle_file)
pickle_file.close()
#open xx wb 以二进制格式打开一个文件只用于写入
#http://www.runoob.com/python3/python3-inputoutput.html

vi some_dict.pkl
#保存结果, 乱码

import pickle
#pickle_file = open('some_dict.pkl', 'r')
pickle_file = open('some_dict.pkl', 'rb')
another_name_for_some_dict = pickle.load(pickle_file)
another_name_for_some_dict
#字典,创建文件,dump导出,关闭


list_of_dicts = [{str(i): i} for i in range(5)]
list_of_dicts
import pickle
pickle_file = open('list_of_dicts.pkl', 'wb')
for d in list_of_dicts:
    pickle.dump(d, pickle_file)
pickle_file.close()

import pickle
pickle_file = open('list_of_dicts.pkl', 'rb')
while 1:
    try:
        print(pickle.load(pickle_file))
    except EOFError:
        print("EOF Error")
        break
#批量序列


custom_class.py
custom_class_pickle.py
custom_class_unpickle.
#模块化


import pickle
default_pickle_file = open('default.pkl', 'wb')
binary_pickle_file = open('binary.pkl', 'wb')
d = {'a': 1}
pickle.dump(d, default_pickle_file)
pickle.dump(d, binary_pickle_file, -1)
default_pickle_file.close()
binary_pickle_file.close()
#hexcat binary.pkl


cPickle
#用c语言实现的序列化,语法相同
#序列化的目的就是为了跨进程传递格式化数据



import shelve
d = shelve.open('example.s')
d
d['key'] = 'some value'
d.close()
d2 = shelve.open('example.s')
#d2
d2['key']
#结果不对啊

import shelve
d = shelve.open('lossy.s')
d['key'] = 'this is a key that will persist'
#d
d['key']
d.close()

import shelve
d = shelve.open('lossy.s')
d
d['another_key'] = 'this is an entry that will not persist'
#不使用close()关闭shelve对象不具有持久性

import shelve
d = shelve.open('lossy.s')
d

import shelve
d = shelve.open('mutable_lossy.s')
d['key'] = []
d['key'].append(1)
d.close()
#修改持久性对象默认不会被pickle,要重新赋值



import shelve
d = shelve.open('mutable_nonlossy.s')
d['key'] = []
temp_list = d['key']
temp_list.append(1)
d['key'] = temp_list
d.close()


import shelve
d = shelve.open('mutable_lossy.s')
d['key']
#后面用到再处理吧


import shelve
d = shelve.open('mutable_nonlossy.s', writeback=True)
d['key'] = []
d['key'].append(1)
d.close()

import shelve
d = shelve.open('mutable_nonlossy.s')
#d
d['key']
#标志位



import yaml
yaml_file = open('test.yaml', 'w')
d = {'foo': 'a', 'bar': 'b', 'bam': [1, 2,3]}
yaml.dump(d, yaml_file, default_flow_style=False)
yaml_file.close()

cat test.yaml

import yaml
yaml_file = open('test.yaml', 'r')
yaml.load(yaml_file)


import yaml
yaml_file = open('nonblock.yaml', 'w')
d = {'foo': 'a', 'bar': 'b', 'bam': [1, 2,3]}
yaml.dump(d, yaml_file)
yaml_file.close()
#序列化字典

import yaml
d = {'first': {'second': {'third': {'fourth': 'a'}}}}
print yaml.dump(d, default_flow_style=False)

print yaml.dump(d)
d2 = [{'a': 'a'}, {'b': 'b'}, {'c': 'c'}]
print yaml.dump(d2, default_flow_style=False)
#非风格化序列
print yaml.dump(d2)
d3 = [{'a': 'a'}, {'b': 'b'}, {'c': [1, 2, 3, 4, 5]}]
print yaml.dump(d3, default_flow_style=False)
print yaml.dump(d3)


#zodb事务处理
python3 zodb_read.py


SQLite
yum install sqlite sqlite-devel
sqlite3 inventory.db < inventory.sql
import sqlite3
conn = sqlite3.connect('inventory.db')
cursor = conn.execute("insert into inventory_operatingsystem (name,
description) values ('Linux', '2.0.34 kernel');")
cursor.fetchall()
conn.commit()
#不提交的话,关闭连接修改清除


import sqlite3
conn = sqlite3.connect('inventory.db')
cursor = conn.execute('select * from inventory_operatingsystem;')
cursor.fetchall()
#name和discription是unicode, id是整型

Storm是一个ORM,开源

