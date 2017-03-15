import os
os.getcwd()
os.mkdir("/tmp/os_mod_explore")
os.listdir("/tmp/os_mod_explore")
os.mkdir("/tmp/os_mod_explore/test_dir1")
os.listdir("/tmp/os_mod_explore")
os.stat("/tmp/os_mod_explore")
os.rename("/tmp/os_mod_explore/test_dir1/", "/tmp/os_mod_explore/test_dir1_renamed")
os.listdir("/tmp/os_mod_explore")
os.rmdir("/tmp/os_mod_explore/test_dir1_renamed/")
os.rmdir("/tmp/os_mod_explore/")

#可以跨平台

import os
os.chdir("/tmp")
os.makedirs("test/test_subdir1/test_subdir2")
ls -lR
import shutil
shutil.copytree("test", "test-copy")
ls -lR
shutil.move("test-copy", "test-copy-moved")
ls -lR
shutil.rmtree("test-copy-moved/")
shutil.rmtree("test-copy")


import filecmp
filecmp.cmp("file0", "file1")
filecmp.cmp("file0", "file00")
#没有比较文件内容

import filecmp
pwd
filecmp.dircmp("dirA", "dirB").diff_files
#只对文件名相同的进行比较,只在B存在的无视
filecmp.dircmp("dirA", "dirB").same_files
filecmp.dircmp("dirA", "dirB").report()

import os
dirA = set(os.listdir("/tmp/dirA"))
dirA
dirB = set(os.listdir("/tmp/dirB"))
dirB
dirA - dirB
dirB - dirA
#列表转集合再处理,文件同名时会导致错误


from checksum import create_checksum
if create_checksum("foo_out.txt") == create_checksum("foo.txt"):
     print (True)

from checksum import create_checksum
from diskwalk_api import diskwalk
#
from os.path import getsize
#上面一行getsize没有导入,果然是这里的问题
d = diskwalk('/tmp/test/')
files = d.enumeratePaths()
#len(files)
len(b'files')
#无值
dup = []
record = {}
for file in files:
    compound_key = (getsize(file),create_checksum(file))
    if compound_key in record:
        dup.append(file)
    else:
        record[compound_key] = file
print(dup)
#类型不存在
#TypeError: 'method' object is not iterable


import os
os.remove("test.bak")

from find_dupes import findDupes
dupes = findDupes("/tmp/test")
def delete(file):
    import os
print("deleting %s" % file)
os.remove(file)
for dupe in dupes:
    delete(dupe)
#注意输出的处理
#dups等于/tmp带入/findDupes函数,出来的返回值


from diskwalk_api import diskwalk
from shutil import move
from fnmatch import fnmatch
files = diskwalk("/tmp/test/")
for file in files:
    if fnmatch(file, "*.mp3"):
        move(file, "%s.txt" % file)
#批量重命名

f = open("largeFile.txt", "w")
statement = "This is a big line that I intend to write over and over again."
x = 0
#for x in xrange(200):
for x in range(200):
    x +=1
    f.write("%s\n" % statement)
#创建大文件

import tarfile
tar = tarfile.open("largeFile.tar", "w")
tar.add("largeFile.txt")
tar.close()
ll
#压缩


import tarfile
tar = tarfile.open("temp.tar", "w")
import os
for root, dir, files in os.walk("/tmp/test"):
    for file in files:
        fullpath = os.path.join(root, file)
        tar.add(fullpath)
tar.close()
#遍历目录树

tar = tarfile.open("largeFilecompressed.tar.gzip2", "w|bz2")
tar.add("largefile.txt")
tar.close()
#同样是环境问题

tar = tarfile.open("largefile.tar.gzip", "w|gz")
tar.add("largeFile.txt")
tar.close()
#tar.gz

import tarfile
tar = tarfile.open("temp.tar", "r")
tar.list()
tar.name
tar.getnames()
tar.members
tar.extractall()
#检测
