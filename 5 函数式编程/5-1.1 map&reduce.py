#map

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

#             f(x) = x * x
#                   │
#                   │
#   ┌───┬───┬───┬───┼───┬───┬───┬───┐
#   │    │    │    │   │    │    │    │    │
#   ▼    ▼   ▼   ▼   ▼   ▼    ▼   ▼   ▼
#  [ 1    2    3    4   5    6     7    8    9 ]
#   │    │    │    │   │    │    │    │    │
#   │    │    │    │   │    │    │    │    │
#   ▼   ▼    ▼   ▼   ▼   ▼    ▼   ▼   ▼
# [ 1    4    9    16   25   36   49   64   81 ]

def f(x):
    return x * x
r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("list(r):",list(r))

# reduce

# reduce把一个函数作用在一个序列[x1, x2, x3, 上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算.其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比方说对一个序列求和，就可以用reduce实现：

from functools import reduce
def add(x, y):
    return x + y
print("reduce(add, [1, 3, 5, 7, 9]):", reduce(add, [1, 3, 5, 7, 9]))

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str类型的数字转换为int的函数：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))

