# 切片
# 取一个list或tuple的部分元素是非常常见的操作。Python提供了切片（Slice）操作符，能大大简化这种操作。

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# [a:b]表示取索引a到索引b之间的元素，其中包括a但不包括b，若a=0则可省略
print("L[0:3]=",L[0:3])

# 同样支持倒数进行索引,记住倒数第一个元素的索引是-1。
print("L[-2:]=", L[-2:])
print("L[-2:-1]=", L[-2:-1])

# 间隔取值
# 前10个数，每两个取一个：
print("L[:10:2]=",L[:10:2])

# 所有数，每5个取一个
print("L[::5]=", L[::5])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串

# 练习
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(str):
    while str!='' and str[0]==' ':
        str=str[1:]
    while str!='' and str[-1]==' ':
        str=str[:-1]
    return str

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!')
elif trim('  hello') != 'hello':
    print('测试失败2!')
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')