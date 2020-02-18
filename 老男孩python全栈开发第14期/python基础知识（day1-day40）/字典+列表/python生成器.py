'''
生成器函数让你可以声明行为类似迭代器的函数。它们让程序员能够以快速、简单和简洁的方式生成迭代器。
不妨举例解释这个概念。
假设你需要为前100000000个完美平方数求总和，从1开始。
使用列表推导很容易做到这一点，但问题是输入量很大时容易内存溢出，生成器则不会：
'''
import time


def 使用列表推导式():
	t1 = time.time()
	sum([i * i for i in range(1, 10000000)])
	t2 = time.time()
	time_diff = t2 - t1
	print("It took {0} Secs to execute this method".format(time_diff))


def 使用生成器():
	t1 = time.time()
	sum((i * i for i in range(1, 10000000)))
	t2 = time.time()
	time_diff = t2 - t1
	print("It took {0} Secs to execute this method".format(time_diff))


if __name__ == '__main__':
	使用列表推导式()
	使用生成器()
