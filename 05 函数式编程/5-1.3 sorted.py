# sorted
# Python内置的sorted()函数就可以对list进行排序

# ython内置的sorted()函数就可以对list进行排序：
print("sorted([36, 5, -12, 9, -21]):", sorted([36, 5, -12, 9, -21]))

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print("sorted([36, 5, -12, 9, -21], key=abs)", sorted([36, 5, -12, 9, -21], key=abs))

# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序

# 我们再看一个字符串排序的例子：

print("sorted(['bob', 'about', 'Zoo', 'Credit'])",
      sorted(['bob', 'about', 'Zoo', 'Credit']))
# ['Credit', 'Zoo', 'about', 'bob']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
# 只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，
# 实际上就是先把字符串都变成大写（或者都变成小写），再比较。这样，我们给sorted传入key函数，即可实现忽略大小写的排序：

print("sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower):",
      sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
# ['about', 'bob', 'Credit', 'Zoo']

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

print(
    "sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True):",
    sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# ['Zoo', 'Credit', 'bob', 'about']

# 练习
# 假设我们用一组tuple表示学生名字和成绩：

# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字、成绩排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0]

L2 = sorted(L, key=by_name)
print(L2)
# 按成绩
def by_score(t):
    return -t[1]

L2 = sorted(L, key=by_score)
print(L2)