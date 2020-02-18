import time
from threading import Thread


# 开启线程的一个比较low的方法
def func(num):
	print(str(num))
	print('低级：我是一个子线程')
	time.sleep(2)

# 装逼的方法
class MyThread(Thread):
	def __init__(self):
		super(MyThread, self).__init__()
	
	def run(self):
		print('\n高级：我是一个子线程')


if __name__ == '__main__':
	t = Thread(target=func, args=(4,))
	t.start()#底层也是调用run()
	
	t1 = MyThread()
	t1.start()









