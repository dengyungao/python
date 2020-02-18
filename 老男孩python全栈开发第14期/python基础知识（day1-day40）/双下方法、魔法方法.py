"""
双下方法、魔术方法
谨记：所有的魔术方法都没有需要你在外部直接调用的场景，而是总有一个其他的方法（对应的内置函数、特殊的语法）来调用这些魔术方法。
__call__(): 特殊语法 调用格式：”对象()“


__len__(): len()内部调用了__len__(),len()是内置函数，__len__()是内置方法

__str__(): str()内部调用了__str__()
__repr__() : 带引号输出字符串  %r


__new__()： 类的构造方法（一般不写），默认调用object.__new__(cls)，实例化类时在__init__()之前调用
__init__()：类的初始化方法，实例化类时在__new__()之后调用
在实例化一个类时分三步：
第一，使用__new__()方法开辟一个属于对象的空间，
第二，把上述空间传给self，再执行__init__()方法初始化，
第三，再将这个对象的空间返回给调用者。
面试题：写一个单例类（类有且只有一个对象）
class Single():
	__instance=None
	def __new__(cls, *args, **kwargs):
		if  cls.__instance==None:#如果__instance为空证明是第一次创建实例
			cls.__instance=object.__new__(cls) #通过父类的__new__(cls)创建实例
			return cls.__instance
		else:
			return cls.__instance#直接返回上一个对象的引用
	def __init__(self):pass
a=Single()
b=Single()
print("True" if id(a) == id(b) else "False") #结果为True

__iter__(): iter()内部调用了__iter__()
__next__(): next()内部调用了__next__()

__eg__(): “==”内部调用了__eq__()
"""
if __name__ == '__main__':
	lst=[1,2,3,4]
	for key in lst:
		print(key)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  