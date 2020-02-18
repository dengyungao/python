import random
import time
from threading import Thread, Event


def conn_mysql(e, i):
	count = 1
	while count <= 3:
		if e.is_set():
			print('第%s个人连接成功!' % i)
			break
		print('正在尝试第%s次重新连接...' % (count))
		e.wait(0.5)
		count += 1


def check_mysql(e):
	print('\033[42m 数据库正在维护 \033[0m')
	time.sleep(random.randint(1, 2))
	e.set()#将e.is_set()设置为true


if __name__ == '__main__':
	e = Event()
	t_check = Thread(target=check_mysql, args=(e,))
	t_check.start()
	
	for i in range(10):
		t_conn = Thread(target=conn_mysql, args=(e, i))
		t_conn.start()
