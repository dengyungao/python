
from multiprocessing import Process
from threading import Thread
import time, os

'''
在同一个进程内，所有线程共享这个进程的pid，也就是说所有线程共享所属进程的所有资源和内存地址
'''
def func(name):
	print('我是一个%s，我的pid是%s' % (name, os.getpid()))


if __name__ == '__main__':
	
	print('我是main，我的pid是%s' % (os.getpid()))
	for i in range(10):
		p = Process(target=func, args=('进程',))
		p.start()
	
	for i in range(10):
		p = Thread(target=func, args=('线程',))
		p.start()
