"""
内容：
	双端队列deque
	
"""
import queue
from collections import deque


if __name__ == '__main__':
	# 队列,先进先出
	q = queue.Queue()
	q.put(1)
	q.put("string")
	q.put((1, 2, 3, 4))
	q.put({"name": "dengyungao"})
	while  q.qsize():  # 循环读取队列中的值
		print(q.get())
	
