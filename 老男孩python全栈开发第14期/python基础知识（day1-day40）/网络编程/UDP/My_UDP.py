import socket


class MySocket(socket.socket):
	'''
	继承socket类，定制传输内容
	'''
	def __init__(self, encodingType="utf-8"):
		self.encoding = encodingType
		super(MySocket, self).__init__(type=socket.SOCK_DGRAM)  # 基于udp协议的传输
	
	def my_sendto(self, msg, addr):
		'''
		发送数据
		:param msg:消息
		:param addr:目标服务器地址
		:return:
		'''
		return self.sendto(msg.encode(self.encoding), addr)
	
	def my_recvfrom(self, num):
		'''
		接受数据  
		:param num: 接受字节数据的大小
		:return:
		'''
		msg_r, addr = self.recvfrom(num)#返回包含接收数据的字符串（客户端消息）和发送数据的套接字地址（客户端地址）
		return msg_r.decode(self.encoding), addr
