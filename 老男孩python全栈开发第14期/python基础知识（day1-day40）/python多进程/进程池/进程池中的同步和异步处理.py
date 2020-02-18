from multiprocessing import Pool
import time


def func(num):
	num += 1
	return num


def poolAsync():
	p = Pool(5)
	start = time.time()
	lst = []
	for i in range(100):
		res = p.apply_async(func, args=(i,))  # 异步处理这100个任务，异步是指，进程中有5个进程，一下就处理5个任务，接下来哪个进程处理完任务了，就马上去接收下一个任务
		lst.append(res)  # res是一个对象，获取其内容必须使用res.get()
	p.close()
	p.join()
	[print(i.get()) for i in lst]  # 打印
	return (time.time() - start)


def poolSynchronization():
	p = Pool(5)
	start = time.time()
	for i in range(100):
		res = p.apply(func, args=(i,))  # 同步处理这100个任务，同步是指，哪怕我进程池中有5个进程，也依旧是1个进程1个进程的去执行任务
		print(res)
	return (time.time() - start)


if __name__ == '__main__':
	time1 = poolAsync()
	time2 = poolSynchronization()
	print('同步时间为{0}，异步时间为{1}'.format(time1, time2))
