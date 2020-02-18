import os
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import current_thread


def func(num):
	sum = 0
	for i in range(num):
		sum += i ** 2
	return sum


def call_back_fun(sum):
	'''
	函数func(num)的返回结果sum会自动给回调函数
	:param sum:
	:return:
	'''
	print('回调函数的进程号：', os.getpid(), 'func()执行结果', sum.result())


def funcThread(i):
	sum = 0
	sum += i
	time.sleep(1)
	print('这是在子线程中', current_thread())
	return sum


def call_back_funcThread(sum):
	'''
	函数funcThread(i)的返回结果sum会自动给回调函数
	:param sum:
	:return:
	'''
	time.sleep(1)
	print('这是在回调函数中', sum.result(), current_thread())


def 测试进程中的回调函数():
	print('父进程的进程号', os.getpid())
	t = ProcessPoolExecutor(20)
	for i in range(10):
		t.submit(func, i).add_done_callback(call_back_fun)
	t.shutdown()


def 测试线程中的回调函数():
	print('这是在父线程', current_thread())
	t = ThreadPoolExecutor(5)
	for i in range(20):
		t.submit(funcThread, i).add_done_callback(call_back_funcThread)
	t.shutdown()


if __name__ == '__main__':
	测试进程中的回调函数()
	print("****************************")
	测试线程中的回调函数()

'''
结论
不管是ProcessPoolExecutor的进程池还是Pool的进程池，回调函数都是父进程调用的。与子进程无关系！
与进程池不同，不管是ThreadPoolExecutor的线程池还是Thread的线程池，线程池中的回调函数都是由子线程调用的，与父线程无关系！
'''
