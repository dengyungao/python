'''
   信号量。
       一把锁配多把钥匙
       sem = Semaphore（num）
       num代表的是几把钥匙
'''

from multiprocessing import Process, Semaphore
import time
import random


def func(i, sem):
	sem.acquire()  # 加锁
	print('第%s个人进入小黑屋,拿了钥匙锁上门' % i)
	time.sleep(random.randint(3, 5))
	print('第%s个人出去小黑屋,还了钥匙打开门' % i)
	sem.release()  # 解锁


if __name__ == '__main__':
	sem = Semaphore(5)  # 初始化了一把锁5把钥匙，也就是说先允许5个人同时进入小黑屋
	# 之后其他人必须等待，等有人从小黑屋出来，还了钥匙，才能允许后边的人进入
	for i in range(20):
		p = Process(target=func, args=(i, sem,))
		p.start()
