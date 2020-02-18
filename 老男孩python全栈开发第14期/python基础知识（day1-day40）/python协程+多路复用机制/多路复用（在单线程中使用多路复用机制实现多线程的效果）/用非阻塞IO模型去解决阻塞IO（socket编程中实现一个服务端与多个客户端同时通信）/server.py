import socket


def server():
	'''
	服务端允许多个客户端同时与之连接通信
	:return:
	'''
	sk = socket.socket()
	sk.setblocking(False)  # 设置为非阻塞
	sk.bind(('127.0.0.1', 8080))
	sk.listen()
	l = []
	del_l = []
	while 1:
		try:
			conn, addr = sk.accept()  # 如果是阻塞IO模型，在这里程序会一直等待。
			l.append(conn)  # 将每个请求连接的客户端的conn添加到列表中
		except BlockingIOError:
			for conn in l:  # 去遍历所有客户端的conn，看看有没有客户端给我发送数据了
				try:
					info = conn.recv(1024).decode('utf-8')  # 尝试接收，看看有没有客户端给我发数据
					if not info:  # 如果客户端主动关闭了和服务器的连接，服务器会接收到一个空
						del_l.append(conn)  # 将已经结束的客户端的conn，添加到要删除的列表中
						print('客户端正常退出了!')
						conn.close()  # 因为客户端已经主动close，所以服务器端的conn也要close
					else:
						print(info)
						conn.send(info.upper().encode('utf-8'))  # 服务端给客户端回消息
				except BlockingIOError:
					continue  # 是没有接受到客户端发来的数据而报错
				except ConnectionResetError:
					pass  # 是因为客户端强制退出而报错
			if del_l:
				for conn in del_l:
					l.remove(conn)
				del_l = []  # 在删除完主动关闭的客户端的连接之后，应该把此列表清空，否则报错


if __name__ == '__main__':
	server()
