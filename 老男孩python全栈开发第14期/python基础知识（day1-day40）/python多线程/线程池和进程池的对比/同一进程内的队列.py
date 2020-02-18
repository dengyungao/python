from multiprocessing import Queue  # 是用于多进程的队列，就是专门用来做进程间通信（IPC）。
import queue  # 是用于同一进程内的队列，不能做多进程之间的通信


def 先进先出队列():
	q = queue.Queue()
	# 先进先出的队列
	q.put(1)
	q.put(2)
	q.put(3)
	print(q.get())
	print(q.get())


def 后进先出队列():
	q = queue.LifoQueue()
	# 后进先出的队列
	q.put(11)
	q.put(22)
	q.put(33)
	print(q.get())
	print(q.get())


def 优先级队列():
	'''
	# 优先级队列，put()方法接收的是一个元组（），第一个位置是优先级，第二个位置是数据
	# 优先级如果是数字，直接比较数值，如果是字符串，是按照 ASCII 码比较的。当ASCII码相同时，会按照先进先出的原则
	:return:
	'''
	q = queue.PriorityQueue()
	q.put((1, 'abc'))
	q.put((5, 'qwe'))
	q.put((-5, 'zxc'))
	print(q.get())
	print(q.get())


if __name__ == '__main__':
	先进先出队列()
	后进先出队列()
	优先级队列()
