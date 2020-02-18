'''
该模型的核心思想：
			生产者代码生产消息，放入缓存中，消费者代码从缓存中取出消息并消费。隔断生产者和消费者之间的直接关联。
'''
# from multiprocessing import Queue,Process
# import time
#
# def consumer(q,name):
#     while 1:
#         info = q.get()
#         if info:
#             print('%s 拿走了%s'%(name,info))
#         else:# 当消费者获得队列中数据时，如果获得的是None，就是获得到了生产者不再生产数据的标识
#             break# 此时消费者结束即可
#
# # 消费者如何判断，生产者是没来得及生产数据，还是生产者不再生产数据了？
# # 如果你尝试用get_nowait() + try 的方式去尝试获得生产者不再生产数据，此时是有问题的。
#
# def producer(q,product):
#     for i in range(20):
#         info = product + '的娃娃%s号'%str(i)
#         q.put(info)
#     q.put(None)# 让生产者生产完数据后，给消费者一个不再生产数据的标识
#
# if __name__ == '__main__':
#     q = Queue(10)
#     p_pro = Process(target=producer,args=(q,'岛国米饭保你爱'))
#     p_con = Process(target=consumer,args=(q,'alex'))
#     p_pro.start()
#     p_con.start()

"""
改进代码如下：将生产者生产结束的标识，放到父进程中
"""
from multiprocessing import Queue, Process


def consumer(q, name, color):
	'''
	消费者
	:param q:进程名
	:param name:
	:param color:颜色左侧数值
	:return:
	'''
	while 1:
		info = q.get()
		if info:
			print('%s %s 拿走了%s \033[0m' % (color, name, info))
		else:  # 当消费者获得队列中数据时，如果获得的是None，就是获得到了生产者不再生产数据的标识
			break  # 此时消费者结束即可

def producer(q, product):
	'''
	生产者
	:param q: 进程名
	:param product:
	:return:
	'''
	for i in range(20):
		info = product + '的娃娃%s号' % str(i)
		q.put(info)


if __name__ == '__main__':
	q = Queue(10)
	# 创建多个生产者
	p_pro1 = Process(target=producer, args=(q, '陶国丽版'))
	p_pro2 = Process(target=producer, args=(q, '苍老师版'))
	p_pro3 = Process(target=producer, args=(q, '波多多版'))
	# 创建多个消费者
	p_con1 = Process(target=consumer, args=(q, 'alex', '\033[31m'))
	p_con2 = Process(target=consumer, args=(q, 'wusir', '\033[32m'))
	
	p_l = [p_con1, p_con2, p_pro1, p_pro2, p_pro3]
	[i.start() for i in p_l]
	# 父进程如何感知到生产者子进程不再生产数据了？
	[i.join() for i in [p_pro1, p_pro2, p_pro3]]

	q.put(None)  # 几个消费者就要设置几个结束标识
	q.put(None)
