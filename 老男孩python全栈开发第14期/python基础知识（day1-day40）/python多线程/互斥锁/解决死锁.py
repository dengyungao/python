import time
from threading import Thread, RLock


# RLock是递归锁 --- 是无止尽的锁，但是所有锁都有一个共同的钥匙
# 想解决死锁，配一把公共的钥匙就可以了。


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
	l_tot.release()  # 男的还厕所


def woman(l_tot, l_pap):
	l_pap.acquire()  # 女的拿纸资源
	print('小雪拿到卫生纸了！')
	time.sleep(1)
	l_tot.acquire()  # 是女的获得厕所资源，把厕所锁上了
	print('小雪在厕所上厕所')
	time.sleep(0.5)
	print('小雪完事了!')
	l_tot.release()  # 女的还厕所
	l_pap.release()  # 女的先还纸


if __name__ == '__main__':
	l_tot = l_pap = RLock()
	t_man = Thread(target=man, args=(l_tot, l_pap))
	t_woman = Thread(target=woman, args=(l_tot, l_pap))
	t_man.start()
	t_woman.start() 