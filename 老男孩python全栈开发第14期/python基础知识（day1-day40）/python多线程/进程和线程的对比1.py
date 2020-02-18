from multiprocessing import Process
from threading import Thread
import time

'''
多线程开启时间远小于多进程
'''
def func():
	pass


if __name__ == '__main__':
	start = time.time()
	for i in range(50):
		p = Process(target=func)
		p.start()
	print('开50个进程的时间:', time.time() - start)
	
	start = time.time()
	for i in range(50):
		p = Thread(target=func)
		p.start()
	print('开50个线程的时间:', time.time() - start)
