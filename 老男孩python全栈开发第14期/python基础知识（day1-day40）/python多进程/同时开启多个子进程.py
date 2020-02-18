from multiprocessing import Process


def func(s):
	print(s)


if __name__ == '__main__':
	lst = []
	for i in range(5):
		p = Process(target=func, args=(i,))
		lst.append(p)
	for i in lst:
		print("第{0}个进程".format(i))
		i.start()
		i.join()
	print("这里是主进程")
