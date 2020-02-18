from threading import Lock


def lockTest():
	l = Lock()  # 一把钥匙配一把锁
	l.acquire()
	print('abc')
	l.acquire()  # 程序会阻塞住，并且陷入死锁
	print(123)


if __name__ == '__main__':
	lockTest()
