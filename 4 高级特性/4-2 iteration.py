# 迭代

# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
print("遍历list或tuple")
listA=[1,3,5,7,9,11,12]
for item in listA:
    print(item)

print("遍历dict")
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 在for循环内获取索引
print("在for循环内获取索引")
for i,v in enumerate(listA):
    print(i,v)

# 练习
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

def findMinAndMax(L):
    if L != []:
        min = L[0]
        max = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
    else:
        min = None
        max = None
    return min,max

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')