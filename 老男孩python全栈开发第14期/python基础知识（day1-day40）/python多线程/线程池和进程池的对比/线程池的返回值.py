from concurrent.futures import ThreadPoolExecutor


def func(num):
	sum = 0
	for i in range(num):
		sum += i ** 2
	return sum


if __name__ == '__main__':
	
	# 下列代码是用map的方式提交多个任务，对应拿结果的方法是__next__()  返回的是一个生成器对象
	t = ThreadPoolExecutor(20)#线程池中存放20个线程
	res = t.map(func, range(100))
	t.shutdown()
	print(res.__next__())
	print(res.__next__())
	print(res.__next__())
	
	# 下列代码是用for循环 + submit提交多个任务，对应拿结果的方法是result()
	t1 = ThreadPoolExecutor(20)
	res_l = []
	for i in range(100):
		re = t1.submit(func, i)
		res_l.append(re)
	t1.shutdown()
	print([i.result() for i in res_l])  # 在Pool进程池中拿结果，是用get方法。在ThreadPoolExecutor里边拿结果是用result()方法
