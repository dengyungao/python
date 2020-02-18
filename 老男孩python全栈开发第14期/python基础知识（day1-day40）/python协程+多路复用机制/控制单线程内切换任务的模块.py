from greenlet import greenlet
import time


# greenlet 只是可以实现一个简单的切换功能，还是不能做到遇到IO就切换
# g1 = greenlet(func)   实例化一个对象
# g1.switch()  用这种方式去调用func函数
# 当使用switch调用func的时候，什么时候func会停止运行？
#   1 要么return
#   2 要么在func内部又遇到switch

def eat(name):
	print('%s吃炸鸡' % name)
	time.sleep(2)
	f2.switch('小雪2')
	print('%s吃雪糕' % name)
	f2.switch()


def drink(name):
	print('%s喝啤酒' % name)
	f1.switch()
	print('%s喝可乐' % name)


f1 = greenlet(eat)
f2 = greenlet(drink)
f1.switch('小雪')