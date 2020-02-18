import socket
import time


if __name__ == '__main__':
	host = ("192.168.1.2", 8081)  # 服务端地址
	socketClient = socket.socket()  # 默认基于tcp协议
	socketClient.connect(host)
	while True:
		msg = input("（客户端）请输入：")
		socketClient.sendall(msg.encode("utf-8"))  # 只能传输byte类型
		print(msg)
		if msg.lower() == "q":
			break
		informationFromServer = socketClient.recv(1024).decode("utf-8")  # 接收服务端的数据,接受到的字节数据解码为字符串
		print(informationFromServer)
		if informationFromServer.lower()=="q":
			break
		
	socketClient.close()
