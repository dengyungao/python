import time
from multiprocessing import Process, Event


def tra(e):
	'''信号灯函数'''
	# e.set()
	# print('\033[32m 绿灯亮! \033[0m')
	while 1:  # 红绿灯得一直亮着，要么是红灯要么是绿灯
		if e.is_set():  # True,代表绿灯亮,那么此时代表可以过车
			time.sleep(5)  # 所以在这让灯等5秒钟，这段时间让车过
			print('\033[31m 红灯亮! \033[0m')  # 绿灯亮了5秒后应该提示到红灯亮
			e.clear()  # 把is_set设置为False
		else:
			time.sleep(5)  # 此时代表红灯亮了，此时应该红灯亮5秒，在此等5秒
			print('\033[32m 绿灯亮! \033[0m')  # 红的亮够5秒后，该绿灯亮了
			e.set()  # 将is_set设置为True


def Car(i, e):
	e.wait()  # 车等在红绿灯，此时要看是红灯还是绿灯，如果is_set为True就是绿灯，此时可以过车
	print('第%s辆车过去了' % i)


if __name__ == '__main__':
	e = Event()
	triff_light = Process(target=tra, args=(e,))  # 信号灯的进程
	triff_light.start()
	for i in range(50):  # 描述50辆车的进程
		if i % 3 == 0:
			time.sleep(2)
		car = Process(target=Car, args=(i + 1, e,))
		car.start()
