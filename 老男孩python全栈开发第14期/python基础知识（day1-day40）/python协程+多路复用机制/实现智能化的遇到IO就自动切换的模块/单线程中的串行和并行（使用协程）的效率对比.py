from gevent import monkey


monkey.patch_all()
import gevent
import time


def func1(num):
	time.sleep(1)
	print(num)


def 串行效率():
	start = time.time()
	for i in range(10):
		func1(i)
	print(time.time() - start)


def 使用协程实现的并行效率():
	start = time.time()
	l = []
	for i in range(10):
		g = gevent.spawn(func1, i)
		l.append(g)
	gevent.joinall(l)
	print(time.time() - start)


if __name__ == '__main__':
	串行效率()
	使用协程实现的并行效率()
