"""

反射
定义：
在做程序开发中，我们常常会遇到这样的需求：需要执行对象里的某个方法，或需要调用对象中的某个变量，但是由于种种原因我们无法确定这个方法或变量是否存在，这是我们需要用一个特殊的方法或机制要访问和操作这个未知的方法或变量，这种机制就称之为反射。
实质：用变量名的字符串形式来访问这个变量的值。

常用内置函数：hasattr()  getattr()   setattr()  delattr()
通用反射转换方式：
                针对变量：命名空间.XXX   == getattr(命名空间,"XXX")   命名空间如：类，类的对象，模块，包，XXX一般为变量或方法
                针对方法：命名空间.XXX() == getattr(命名空间,"XXX")()
使用场景：
1）类调用它的静态属性,类方法,静态方法,
    格式：getattr(类名，"类方法名")  == 类名.类方法名，
    如getattr(className，"classmethodName")() == className.classmethodName()

2）对象调用它的对象属性和方法,
    格式：getattr(对象名，"对象属性名") == 对象名.对象属性名，
    如getattr(obj,"attr_name")  == obj.attr_name

3）反射模块中的变量、方法或类,
    格式：getattr(模块名，"模块中的方法名") == 模块名.模块中的方法名,
    如 getattr(os,"rename")("new_name","old_name") == os.rename("new_name","old_name")

4)反射当前模块中的变量、方法或类，
    格式：getattr(sys.modules["__main__"],"当前模块中的方法名")()  == 当前模块中的方法名()
"""
import sys


if __name__ == '__main__':
	def test():
		print("test func")
	
	
	class Test():
		def __init__(self, name):
			self.name = name
		
		def function(self):
			print(self.name)
	
	
	
	my = sys.modules["__main__"]  # 当期文件所在的命名空间
	my.test()  # 调用方法
	obj = getattr(sys.modules["__main__"], "Test")('邓云高')  # 实例化类Test的对象
	obj.function()  # 调用对象的方法
