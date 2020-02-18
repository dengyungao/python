import os
from multiprocessing import Pool, Process
import time


def func(num):
	num += 1
	# print(num)


def poolMethod():
	# global start
	p = Pool(os.cpu_count() + 1)
	start = time.time()
	p.map(func, [i for i in range(100)])
	p.close()  # 指不允许在向进程池中添加任务
	p.join()  # 等待进程池中所有进程执行完所有任务
	return ('进程池做任务的效率：', time.time() - start)


def multiProcess():
	# global start
	start = time.time()
	p_l = []
	for i in range(100):
		p1 = Process(target=func, args=(i,))
		p1.start()
		p_l.append(p1)
	[p1.join() for p1 in p_l]
	return ('多进程直接做任务的效率', time.time() - start)


if __name__ == '__main__':
	print(poolMethod())
	print(multiProcess())

