import time
from threading import Thread, Lock

'''
背景：男的只拿到厕所资源，女的只拿到纸资源
'''
def man(l_tot, l_pap):
	l_tot.acquire()  # 是男的获得厕所资源，把厕所锁上了
	print('alex在厕所上厕所')
	time.sleep(1)
	l_pap.acquire()  # 男的拿纸资源
	print('alex拿到卫生纸了！')
	time.sleep(0.5)
	print('alex完事了!')
	l_pap.release()  # 男的先还纸
	l_tot.release()  # 男的再还厕所


def woman(l_tot, l_pap):
	l_pap.acquire()  # 女的拿纸资源
	print('小雪拿到卫生纸了！')
	time.sleep(1)
	l_tot.acquire()  # 女的拿厕所资源，此时拿不到，因为被男的占用了
	print('小雪在厕所上厕所')
	time.sleep(0.5)
	print('小雪完事了!')
	l_tot.release()  # 女的先还厕所
	l_pap.release()  # 女的再还纸


if __name__ == '__main__':
	l_tot = Lock()
	l_pap = Lock()
	t_man = Thread(target=man, args=(l_tot, l_pap))
	t_woman = Thread(target=woman, args=(l_tot, l_pap))
	t_man.start()
	t_woman.start()