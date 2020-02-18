import select
import socket


def server():
	sk = socket.socket()
	sk.bind(('127.0.0.1', 8080))
	sk.listen()
	del_l = []  # 存放需要删除的客户端连接对象
	rlist = [sk]  # 是用来让select帮忙监听的所有接口，比如sk或者连接对象conn
	# select：windows/linux是监听事件有没有数据到来
	# poll:  linux   也可以做select的工作
	# epoll: linux   也可以做类似的工作
	while 1:
		r, w, x = select.select(rlist, [], [])  # 传参给select，当rlist列表中哪个接口有反应，就返回给列表r
		if r:
			for i in r:  # 循环遍历r，看看有反应的接口到底是sk还是conn
				if i == sk:
					# 如果是sk，那就表示有客户端的连接请求
					'''sk有数据要接收，代表着有客户端要来连接'''
					conn, addr = i.accept()
					rlist.append(conn)  # 把新的客户端的连接，添加到rlist，继续让select帮忙监听
				else:
					# 如果是conn，就表示有客户端给我发数据了
					'''conn有数据要接收，代表要使用recv'''
					try:
						msg_r = i.recv(1024).decode('utf-8')
						if not msg_r:
							'''客户端主动关闭了连接'''
							del_l.append(i)
							i.close()
						else:
							print(msg_r)
							i.send(msg_r.upper().encode('utf-8'))  # 服务端回消息
					except ConnectionResetError:  #
						pass
			if del_l:  # 删除那些主动断开连接的客户端的conn
				for conn in del_l:
					rlist.remove(conn)
				del_l.clear()


if __name__ == '__main__':
	server()
