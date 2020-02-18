import os
from multiprocessing import Pool

import requests


def func(url):
	res = requests.get(url)
	print('子进程的pid:%s,父进程的pid：%s' % (os.getpid(), os.getppid()))
	# print(res.text)
	if res.status_code == 200:
		return url, res.text


def cal_back(sta):
	url, text = sta
	print('回调函数的pid', os.getpid())
	with open('a.txt', 'a', encoding='utf-8') as f:
		f.write(url + text)


if __name__ == '__main__':
	p = Pool(5)
	l = ['https://www.baidu.com',
	     'http://www.jd.com',
	     'http://www.taobao.com',
	     'http://www.mi.com',
	     'http://www.cnblogs.com',
	     'https://www.bilibili.com',
	     ]
	print('主进程的pid', os.getpid())
	for i in l:
		p.apply_async(func, args=(i,),
		              callback=cal_back)  # 异步执行任务func，每有一个进程执行完任务后，在func中return一个结果，结果会自动的被callback指定的函数当成形式参数来接收到
	p.close()
	p.join()
