# 练习
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：
# class Screen(object):
#     pass

class Screen(object):
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self,width):
        self.__width = width
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self,height):
        self.__height = height
    
    @property
    def resolution(self):
        return self.__width*self.__height    

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')