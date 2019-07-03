# 练习

# 利用os模块编写一个能实现dir -l输出的程序。
# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。

import os

#dir -l
# for i in os.listdir('.'):
#     print(i)

# 查找
def dir_list(pathname='.'):
    abspath = os.path.abspath(pathname)
    try:
        for i in os.listdir(pathname):
            i = os.path.join(abspath, i)
            if os.path.isdir(i):
                for file in dir_list(i):    # 在生成器中递归调用自身的时候不能直接调用，需要使用for进行循环才能正常调用自身
                    yield file
            else:
                yield i
    except IOError as e:
        print(e, ". Please make sure you have the access to this directory/file")

text = input("search for:")
dir = input("in directory(default: this directory):")
DIRLIST = dir_list(dir)

for x in DIRLIST:
    try:
        x.index(text)
        print(x)
    except ValueError as e:
        continue
