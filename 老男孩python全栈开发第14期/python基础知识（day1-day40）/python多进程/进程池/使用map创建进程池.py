from multiprocessing import Process, Pool


def func(num):
	num += 1
	return num


if __name__ == '__main__':
	p = Pool(5)
	res = p.map(func, [i for i in range(100)])  # map函数返回一个列表
	p.close()
	p.join()
	print(res)
