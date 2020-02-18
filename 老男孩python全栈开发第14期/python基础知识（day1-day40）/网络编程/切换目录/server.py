#  切换目录
import os
import socket


sk = socket.socket()
sk.bind(('127.0.0.1', 8080))
sk.listen()
conn, addr = sk.accept()


def send_data(conn, path):
	'''你给我一个目录，我把目录发给client'''
	lis_dir = os.listdir(path)
	str_dir = '--'.join(lis_dir)
	conn.send(str_dir.encode('utf-8'))


abs_path = conn.recv(1024).decode('utf-8')  # 获取用户输入的绝对路径
current_dir = abs_path + '/'  # 以下再处理，都要根据当前路径去处理，无论是返回上一层，还是进入下一层
send_data(conn, current_dir)  # 把用户输入的路径下的所有文件及文件夹返回给客户端

# C:/Program Files (x86)/Common Files
while 1:
	cmd = conn.recv(1024).decode('utf-8')
	if cmd == '..':
		current_dir = current_dir.split('/')[:-2]#获取上一层目录
		current_dir = '/'.join(current_dir) + '/'
		# if 如果当前是C盘：
		#     就返回给客户端告诉说没有上一层了！
		send_data(conn, current_dir)
	else:
		filename = cmd.split(' ')[1]  # 获取用户输入的文件名字
		current_dir += filename + '/'  # 将文件名字添加到当前路径下，组成一个完整的新路径
		if os.path.isdir(current_dir):  # 如果客户输入的文件名字是一个文件夹
			send_data(conn, current_dir)
		else:  # 如果不是一个文件夹
			conn.send(b'bu shi wen jian jia')


# conn.close()
# sk.close()
