import os
path = "/tmp"

def enumeratepaths(path=path):
    """Returns the path to all the files in a directory as a list"""
    path_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            path_collection.append(fullpath)

    return path_collection

def enumeratefiles(path=path):
    """Returns all the files in a directory as a list"""
    file_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            file_collection.append(file)

    return file_collection

def enumeratedir(path=path):
    """Returns all the directories in a directory as a list"""
    dir_collection = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            dir_collection.append(dir)

    return dir_collection

if __name__ == "__main__":
    print("\nRecursive listing of all paths in a dir:")
    for path in enumeratepaths():
        print(path)
    print("\nRecursive listing of all files in dir:")
    for file in enumeratefiles():
        print(file)
    print("\nRecursive listing of all dirs in dir:")
    for dir in enumeratedir():
        print(dir)


#os.walk返回的是一个 generator对象

#generator 对象
# In [1]: import os
# In [2]: os.walk("/tmp")
# Out[2]: <generator object walk at 0x7ff0e25b0938>
# In [8]: path.next()
# AttributeError: 'generator' object has no attribute 'next'
# 在python 3.x中 generator（有yield关键字的函数则会被识别为generator函数）中的next变为__next__了,next是python 3.x以前版本中的方法