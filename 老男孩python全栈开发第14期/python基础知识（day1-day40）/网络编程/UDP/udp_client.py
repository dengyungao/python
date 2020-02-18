from My_UDP import MySocket


if __name__ == '__main__':
	serverAddr = ("127.0.0.1", 8080)  # 服务端的地址和端口
	sk = MySocket()
	while True:
		msgSendToServer = input("（客户端）请输入：")
		sk.my_sendto(msgSendToServer, serverAddr)
		msgReceivedFromServer, addr = sk.my_recvfrom(1024)
		print("消息：%s\n 来自：%s"%(msgReceivedFromServer,addr))
	
	sk.close()
