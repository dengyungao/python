from multiprocessing import Process, Lock
import time


def check(i):
	with open('余票') as f:
		con = f.read()
	print('第%s个人查到余票还剩%s张' % (i, con))


def buy_ticket(i, l):
	l.acquire()  # 拿钥匙，锁门
	with open('余票') as f:
		con = int(f.read())
		time.sleep(0.1)
	if con > 0:
		print('\033[31m 第%s个人买到票了\033[0m' % i)
		con -= 1
	else:
		print('\033[32m 第%s个人没有买到票\033[0m' % i)
	time.sleep(0.1)  # 是指 买完票后，把余票数量重写写入数据库的时间延迟
	with open('余票', 'w') as f:
		f.write(str(con))
	l.release()  # 还钥匙，开门


if __name__ == '__main__':
	l = Lock()
	for i in range(10):
		p_ch = Process(target=check, args=(i + 1,))
		p_ch.start()
	for i in range(10):
		p_buy = Process(target=buy_ticket, args=(i + 1, l))
		p_buy.start()
