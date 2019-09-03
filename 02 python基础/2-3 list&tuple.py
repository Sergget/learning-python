#列表list
print("list列表")
#列表赋值
classmates = ['Michael', 'Bob', 'Tracy']
#长度
print("len(classmates):",len(classmates))
#从列表中取值
print("classmates[0]:",classmates[0])
print("classmates[-1]:",classmates[-1])

#向列表末尾增加值
classmates.append('Adam')
print("classmates.append('Adam'):",classmates)

#向列表中插值
classmates.insert(1, 'Jack')
print("classmates.insert(1, 'Jack'):",classmates)

#要删除list末尾的元素，用pop()方法
classmates.pop()
print("classmates.pop():",classmates)

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1)
print("classmates.pop(1):",classmates)

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print("classmates[1] = 'Sarah':",classmates)

#列表里面的元素的数据类型也可以不同,元素也可以是另一列表


#元组tuple
print("\n 元组tuple")
#tuple和list非常类似，但是tuple一旦初始化就不能修改，它也没有append()，insert()这样的方法。
#其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。

#只有1个元素的tuple定义时必须加一个逗号,来消除歧义
t = (1,)
print(" t = (1,):", t )

#tuple内的元素不可变，但元素内容是可变的
t = ('a', 'b', ['A', 'B'])
print("修改前：",t)
t[2][0] = 'X'
t[2][1] = 'Y'
print("对t内的list列表内元素重新赋值:",t)