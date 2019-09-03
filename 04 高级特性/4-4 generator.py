# 生成器
# 如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，
# 从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
g = (x * x for x in range(10))

# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值，直到计算到没有更多的元素时，抛出StopIteration的错误。
# 当然，这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象

for n in g:
    print(n)

# 基于函数的生成器
# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

# 输出斐波那契数列的前N个数
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 普通函数遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
# 再次执行时从上次返回的yield语句处继续执行。
f = fib(6)
for n in f:
    print("f:",n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

# 练习
# 杨辉三角定义如下：

#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
    L = []
    T = []
    while True:
        L.append(1)
        T.append(1)
        for i,l in enumerate(L):
            if i<len(L)-1 and i>0:
                T[i] = L[i-1] +l
        L = T.copy()
        yield L.copy()

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1],[1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1],[1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1],[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]]:
    print('测试通过!')
else:
    print('测试失败!')
