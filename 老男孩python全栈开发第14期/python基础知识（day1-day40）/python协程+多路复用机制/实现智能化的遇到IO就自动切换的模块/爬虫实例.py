from gevent import monkey
monkey.patch_all()
import gevent
import time
import requests


def get_result(url):  # 任务函数
	res = requests.get(url)
	print(url, res.status_code, len(res.text))


url_l = ['http://www.baidu.com',
         'https://www.jd.com',
         'http://www.apache.com',
         'http://www.taobao.com',
         'http://www.qq.com',
         'http://www.mi.com',
         'http://www.cnblogs.com']


def sync_func(url_l):
	'''同步调用'''
	for url in url_l:  # 串行执行任务函数
		get_result(url)


def async_func(url_l):
	'''异步'''
	l = []
	for url in url_l:
		g = gevent.spawn(get_result, url)  # 使用gevent，协程去并发实现执行任务函数
		# 当遇见请求某个网页发生比较大的网络延迟（IO），马上会切换到其他的任务函数
		l.append(g)
	gevent.joinall(l)  # 等待所有任务函数执行结束


start = time.time()
sync_func(url_l)
print('sync:', time.time() - start)

start = time.time()
async_func(url_l)
print('async:', time.time() - start)
