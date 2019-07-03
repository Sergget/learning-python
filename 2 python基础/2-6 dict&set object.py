# dict 
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储
print("dict对象")
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
#取值
print("d['Michael']=",d['Michael'])
# 判断一个dict表内有没有某个值
print("判断一个dict表内有没有某个值")
print("'Thomas' in d:",'Thomas' in d)
print("d.get('Thomas'):",d.get('Thomas'))
print("d.get('Thomas',-1):",d.get('Thomas',-1))

# 删除键值
print("删除键值")
d.pop('Bob')
print("d.pop('Bob'):",d)

# set
#set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。且内部元素无顺序之分。
#创建一个set，需要提供一个list作为输入集合,重复元素在set中自动被过滤
print("\nset对象")
s = set([1, 1, 2, 2, 3, 3])
print(s)
#添加元素
s.add(4)
print("添加元素  s.add(4):",s)
#移除元素
s.remove(4)
print("移除元素  s.remove(4)",s)
