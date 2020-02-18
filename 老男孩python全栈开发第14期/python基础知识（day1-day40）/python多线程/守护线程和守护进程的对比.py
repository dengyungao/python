import time
from multiprocessing import Process
from threading import Thread


'''
守护线程：
	守护线程不会随主线程的代码执行结束而结束,而是会在主线程结束后继续执行，所以，一般把不重要的事情设置为守护线程。
	主线程会等待普通线程执行结束后再结束
守护进程
	当主进程的代码执行完毕时，守护进程在同一时间结束
	主进程会等待普通进程执行结束后再结束
'''


def func123():
	time.sleep(4)  # 守护线程（进程）的方法睡眠时间必须大于普通线程（进程）方法，才能显示出守护线程的效果
	print(123)


def func123Abc():
	time.sleep(2)
	print('123Abc')

def 验证守护线程():
	t = Thread(target=func123)
	t.daemon = True
	t.start()
	t1 = Thread(target=func123Abc)
	t1.start()
	print("主线程结束")


def 验证守护进程():
	t = Process(target=func123)
	t.daemon = True
	t.start()
	t1 = Process(target=func123Abc)
	t1.start()
	print("主进程结束")


if __name__ == '__main__':
	验证守护线程()
	time.sleep(5)
	验证守护进程()
	
	

	

'''
结论：守护线程在主线程结束（等普通线程打印了“123Abc”后）后依然执行，打印了“123”，而守护进程则没打印“123”
'''
