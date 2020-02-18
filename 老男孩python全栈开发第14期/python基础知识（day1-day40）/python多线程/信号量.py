from threading import Semaphore, Thread
import time


def func(sem, i):
	sem.acquire()
	print('第%s个人进入屋子' % i)
	time.sleep(2)
	print('第%s个人离开屋子' % i)
	sem.release()


sem = Semaphore(5)
for i in range(20):
	t = Thread(target=func, args=(sem, i))
	t.start()