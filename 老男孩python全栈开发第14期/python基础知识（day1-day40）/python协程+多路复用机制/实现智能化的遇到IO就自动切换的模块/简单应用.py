import gevent
import time


# gevent 可以实现当函数中遇到io操作时，就自动的切换到另一个函数
# g1 = gevent.spawn(func,参数)
# gevent.join(g1) 让func执行完毕
# gevent.joinall([g1,g2,g3,g4])
# func停止的原因: 1 func执行完了     2 遇到IO操作了

def 第一种写法():
	def func1():
		print('1 2 3 4')
		# gevent.sleep(1)
		time.sleep(1)
		print('3 2 3 4')
		
	def func2():
		print('2 2 3 4')
		# gevent.sleep(1)
		time.sleep(1)  # gevent不能识别其他的IO操作，只能识别自己认识的IO
		print('再来一次')
	
	g1 = gevent.spawn(func1)
	g2 = gevent.spawn(func2)
	g1.join()  # 等待g1指向的任务执行结束


def 第二种写法():
	from gevent import monkey
	monkey.patch_all()  # 可以让gevent识别大部分常用的IO操作
	import time
	def func1():
		print('1 2 3 4')
		time.sleep(1)
		print('3 2 3 4')
	
	def func2():
		print('2 2 3 4')
		time.sleep(1)
		print('再来一次')
	
	g1 = gevent.spawn(func1)
	g2 = gevent.spawn(func2)
	g1.join()  # 等待g1指向的任务执行结束
	g2.join()


if __name__ == '__main__':
	第一种写法()
	# 以下解决gevent不能识别其他IO操作的事情
	第二种写法()
