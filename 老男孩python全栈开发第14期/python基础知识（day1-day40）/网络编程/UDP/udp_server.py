from My_UDP import MySocket


if __name__ == '__main__':
	serverAddr = ("127.0.0.1", 8080)
	sk = MySocket()
	sk.bind(serverAddr)
	while True:
		msgFromClient, addr = sk.my_recvfrom(1024)  # 客户端的消息和地址
		# print(msgFromClient,addr)
		print("\033[32;m 消息：%s\n 来自：%s \033[0m" % (msgFromClient, addr))  # 带颜色输出（绿色）
		msgSendToClient = input("（服务端）请输入：")
		sk.my_sendto(msgSendToClient, addr)
	sk.close()
