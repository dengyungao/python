'''
进程：指正在运行的程序
	 由3部分组成：代码段、数据段以及PCB（进程管理控制）
	 
进程4大基本状态：
	就绪状态：已经获取运行需要的所有资源，除了CPU
	执行状态：已经获取所有资源包括CPU，处于正在执行状态
	阻塞状态：进程因某些原因放弃CPU，导致进程无法继续执行，此时进程处于内存中，继续等待获取CPU以便继续执行。
	挂起状态：与阻塞类似，不同的是此时进程已经被踢出内存，无法继续执行。

多进程的模块:
	multiprocessing.Process
	
守护进程：
	当父进程的代码执行结束时间，守护进程的代码也随之结束。
	守护进程不能再开子进程。
'''
import os
from multiprocessing import Process


def func(strTest):
	print(str(strTest))
	print("子进程{0}".format(str(os.getpid())))  # 获取当前进程的进程号
	print("父进程{0}".format(str(os.getppid())))  # 获取当前进程的父进程的进程号


class MyProcess(Process):
	def __init__(self):
		super(MyProcess, self).__init__()
	
	def run(self):
		print("继承的方式开启子进程")


if __name__ == '__main__':
	# 普通方式开启子进程
	p = Process(target=func, args=("test",))#args必须是元组类型
	p.daemon = True  # 如果想将p设置为守护进程，必须在调用start()方法之前设置
	p.start()  # start()底层调用run()方法，开启一个子进程
	print("子进程的状态是{0}".format(p.is_alive()))#判断进程是否存活
	print("子进程的名称是{0}，进程号是{1}".format(p.name,p.pid))
	print("子进程是否是守护进程？{0}".format(p.daemon))
	p.join()  # 加上该句，主进程在此处阻塞，等待子进程全部运行完，主进程再从此处开始运行，一般是主进程需要子进程的返回结果时才加join()，此时主子进程之间是同步关系，不加的话主子进程交替运行，此时是异步关系。
	print("父进程是{}".format(str(os.getpid())))
	
	# 使用类的继承方式开启子进程
	myProcess = MyProcess()
	myProcess.start()  # 等效于myProcess.run()
