#内置函数
#python内置函数可见官网：https://docs.python.org/3/library/functions.html
#也可以在交互式命令行通过help(abs)查看abs函数的帮助信息
print("abs(100)=",abs(100))
print("max(2, 3, 1, -5)=",max(2, 3, 1, -5))

#数据类型转换
print("int('123')=",int('123'))
print("int(12.34)=",int(12.34))
print("str(1.23)=",str(1.23))
print("bool(1)=",bool(1))

#函数的别名：函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”
a = abs # 变量a指向abs函数
print("a = abs:a(-1)=",a(-1))
