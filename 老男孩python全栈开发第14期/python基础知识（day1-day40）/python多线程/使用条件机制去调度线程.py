from threading import Thread, Condition
'''
 Condition涉及4个方法
	 acquire() 加锁
	 release() 解锁
	 wait()    是指让线程阻塞住
	 notify(int)  是指给wait发一个信号，让wait变成不阻塞，
				   int参数是指，你要给多少个正处于wait状态（阻塞状态）的线程发信号，此时就有多少个线程去执行任务。
	'''


def func(con, i):
	con.acquire()
	con.wait()  # 线程执行到这里，会阻塞住，等待notify发送信号，来唤醒此线程
	con.release()
	print('第%s个线程开始执行了！' % i)


if __name__ == '__main__':
	con = Condition()
	for i in range(10):
		t = Thread(target=func, args=(con, i))
		t.start()
	while 1:
		num = int(input(">>>"))
		con.acquire()
		con.notify(num)  # 发送一个信号给num个正在阻塞在wait状态的线程，让这些线程正常执行
		con.release()
