# 普通参数调用，计算x的平方

def pow(x):
    return x*x

print("pow(5)",pow(5))

# 参数默认值
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print("power(5):",power(5),"\npower(5,3):",power(5,3))

# 默认参数必须指向不可变对象，否则在重复调用时参数指向的对象内容会发生变化
def add_end(L=[]):
    L.append('END')
    print(L)
    return L
add_end()
add_end()

# 可变参数

# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
# 因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print("calc(1,2,3,4,5,6):",calc(1,2,3,4,5,6))

#传入已有的list或tuple参数时，可按如下调用
listA=[2,3,4,5,6]
print("calc(*listA):",calc())

# 关键字参数

# 键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

# 调用时，关键字参数可以传入任意个（包括0个）
print("person('Adam', 45, gender='M', job='Engineer'):")
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city': 'Beijing', 'job': 'Engineer'}
print("person('Jack', 24, **extra):")
#注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
person('Jack', 24, **extra)

# 命名关键字参数
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查，
# 如果要限制关键字参数的名字，就可以用命名关键字参数，和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，
# *后面的参数被视为命名关键字参数

def person2(name, age, *, city, job):
    print(name, age, city, job)


print("命名关键字参数\nperson2('Jack', 24, city='Beijing', job='Engineer'):")
person2('Jack', 24, city='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
# def person(name, age, *args, city, job):
#    print(name, age, args, city, job)

# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
# 命名关键字参数可以有缺省值，从而简化调用：
# def person(name, age, *, city='Beijing', job):
#    print(name, age, city, job)

# 参数组合

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

