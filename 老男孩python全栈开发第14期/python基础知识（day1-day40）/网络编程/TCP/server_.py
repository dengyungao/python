import socket


if __name__ == '__main__':
	
	host = ("192.168.1.2", 8081)#服务端地址
	socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 基于tcp协议的传输
	socketServer.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #加入一条socket配置，重用ip和端口
	socketServer.bind(host)  # 端口的范围是1024-65535
	socketServer.listen()  # 监听连接
	conn, addr = socketServer.accept()  # 等待接受客户端的连接，此时会停在这里，等待客户端的连接。
	# print("conn:", conn, "\n", "addr:", addr)
	while True:
		#接受客户端消息
		informationFromClient = conn.recv(1024).decode("utf-8")  # 接收客户端的数据,接受到的字节数据解码为字符串
		print(informationFromClient)
		if informationFromClient.lower()=="q":
			break
		
		#给客户端回消息
		msg=input("（服务端）请输入：")
		conn.sendall(msg.encode("utf-8"))#只能传输字节数据
		print(msg)
		if msg.lower()=="q":
			break
		
	conn.close()
	socketServer.close()
