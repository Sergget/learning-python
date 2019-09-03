# 练习1
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2
# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools  import reduce
def prod(L):
    def times(x,y):
        return x*y
    return reduce(times,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习3
# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
from functools import reduce

def str2float(s):
    digits = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9
    }
    char=s.split('.')
    s = char[0]+char[1]
    dotp = len(char[1])
    def char2num(str):
        return digits[str]
    def num2float(x,y):
        return x*10+y
    return reduce(num2float,map(char2num,s))/(10**dotp)

print('str2float(\'1595.365\') =', str2float('1595.365'))
if abs(str2float('1595.365') - 1595.365) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')