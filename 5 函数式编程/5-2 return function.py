# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
def lazy_sum(*args):
    def suma():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return suma
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

f = lazy_sum(1, 3, 5, 7, 9)
print("f:",f)
# <function lazy_sum.<locals>.sum at 0x101c6ed90>
# 调用函数f时，才真正计算求和的结果：
print("f():",f())

# 在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数.

# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用.
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行
def count():
    fs = []

    for i in range(1, 4):
        def foo():
            return i * i
        fs.append(foo)
    return fs

f1,f2,f3=count()
print("f1():", f1())
print("f2():", f2())
print("f3():", f3())

# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：9,9,9。
# 原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def countA():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

f1, f2, f3 = countA()
print("f1():", f1())
print("f2():", f2())
print("f3():", f3())


# 练习
# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    n=0
    def counter():
        nonlocal n
        n=n+1
        return n
    return counter

# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
