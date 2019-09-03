#定义函数
#在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，
#函数的返回值用return语句返回。
def _abs(a):
    if(a>=0):
        return a
    else:
        return -a

a = input("please input a number:")
print(_abs(int(a)))

#空函数
def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

#调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError，但是如果参数类型不对，Python解释器就无法帮我们检查。

#返回多个值

print("返回多个值\n")
#import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print("此处返回值看起来连在一起了：",x, y)
r = move(100, 100, 60, math.pi / 6)
print("实际上是一个tuple类型：",r)
print("可以将tuple内的值依次取出：x=%3f,y=%3f"%r)

#练习
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#  ax2 + bx + c = 0  的两个解
def quadratic(a,b,c):
    delta = b*b -4*a*c
    if delta==0:
        x1=x2=-b/2*a
    elif delta<0:
        print("方程无实数解")
    else:
        x1 = (-b+math.sqrt(delta))/2/a
        x2 = (-b-math.sqrt(delta))/2/a
    return x1,x2

# 测试:
print('\nquadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')