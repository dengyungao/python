from multiprocessing import JoinableQueue


q = JoinableQueue()

'''
q.join()# 用于生产者。等待 q.task_done的返回结果，通过返回结果，生产者就能获得消费者当前消费了多少个数据
q.task_done() # 用于消费者，是指每消费队列中一个数据，就给join返回一个标识。
详细解释：
	假设生产者生产了100个数据，join就能记录下100这个数字。每次消费者消费一个数据，
	就必须要task_done返回一个标识，当生产者（join）接收到100个消费者返回来的标识的时候，
	生产者就能知道消费者已经把所有数据都消费完了。
'''

from multiprocessing import Process


def consumer(q, name, color):
	while 1:
		info = q.get()
		print('%s %s 拿走了%s \033[0m' % (color, name, info))
		q.task_done()


def producer(q, product):
	for i in range(20):
		info = product + '的娃娃%s号' % str(i)
		q.put(info)
	q.join()  # 记录了生产了20个数据在队列中,此时会阻塞等待消费者消费完队列中所有数据
	


if __name__ == '__main__':
	q = JoinableQueue(10)
	p_pro1 = Process(target=producer, args=(q, '岛国米饭保你爱'))
	p_con1 = Process(target=consumer, args=(q, 'alex', '\033[31m'))
	p_con1.daemon = True  # 把消费者进程设为守护进程
	p_con1.start()
	p_pro1.start()
	p_pro1.join()  # 主进程等待生产者进程结束
'''
上面程序的详细解释：
程序有3个进程，主进程和生产者进程和消费者进程。
当主进程执行到35行代码时，主进程会等待生产进程结束,
而生产进程中（第26行）会等待消费者进程把所有数据消费完，生产者进程才结束。
现在的状态就是主进程等待生产者进程结束，生产者进程等待消费者消费完所有数据，
所以，把消费者设置为守护进程。当主进程执行完，就代表生产进程已经结束，
也就代表消费者进程已经把队列中数据消费完,此时，主进程一旦结束，守护进程也就是消费者进程也就跟着结束。 整个程序也就能正常结束了。
'''

