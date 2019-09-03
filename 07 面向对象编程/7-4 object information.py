# 获取对象信息

# 使用type()
print("type(123):", type(123))
# 但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同
print("type(123)==type(456):", type(123)==type(456))
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
    pass

print("type(fn)==types.FunctionType:", type(fn) == types.FunctionType)
print("type(abs)==types.BuiltinFunctionType:",
      type(abs) == types.BuiltinFunctionType)
print("type(lambda x: x)==types.LambdaType:",
      type(lambda x: x) == types.LambdaType)
print("type((x for x in range(10)))==types.GeneratorType:",
      type((x for x in range(10))) == types.GeneratorType)

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：

class Animal():
    pass

class Dog(Animal):
    pass

class Husky(Dog):
    pass

a = Animal()
d = Dog()
h = Husky()
# 然后，判断：
print("isinstance(h, Husky):", isinstance(h, Husky))
print("isinstance(h, Dog):", isinstance(h, Dog))
print("isinstance(h, Animal):", isinstance(h, Animal))

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print("isinstance([1, 2, 3], (list, tuple)):",
      isinstance([1, 2, 3], (list, tuple)))
