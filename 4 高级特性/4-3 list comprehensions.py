# 列表生成式
# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

print("list(range(1, 11)):", list(range(1, 11)))

# 生成[1x1, 2x2, 3x3, ..., 10x10]
print("[x * x for x in range(1, 11)]:", [x * x for x in range(1, 11)])

# 列表生成式也可以使用两个变量来生成list
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print("[k + '=' + v for k, v in d.items()]:",[k + '=' + v for k, v in d.items()])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print("[x * x for x in range(1, 11) if x % 2 == 0]:", [x * x for x in range(1, 11) if x % 2 == 0])

# 可以使用两层循环，可以生成全排列
print("[m + n for m in 'ABC' for n in 'XYZ']", [m + n for m in 'ABC' for n in 'XYZ'])

# 练习
# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：

# >>> L = ['Hello', 'World', 18, 'Apple', None]
# >>> [s.lower() for s in L]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 1, in <listcomp>
# AttributeError: 'int' object has no attribute 'lower'
# 使用内建的isinstance函数可以判断一个变量是不是字符串：

# >>> x = 'abc'
# >>> y = 123
# >>> isinstance(x, str)
# True
# >>> isinstance(y, str)
# False
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')