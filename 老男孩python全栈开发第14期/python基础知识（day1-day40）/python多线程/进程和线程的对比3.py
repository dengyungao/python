from threading import Thread


'''
在同一个进程内，所有线程共享该进程中的全局变量
'''

def func():
	global num
	num -= 1

if __name__ == '__main__':
	
	# 主进程中的num变量被在主进程中创建的多个子线程共享，能被子进程改变数值大小。
	num = 100#全局变量
	t_l = []
	for i in range(50):
		t = Thread(target=func)
		t.start()
		t_l.append(t)
	[t.join() for t in t_l]
	print(num)
