import hashlib
import socket
import sys


if __name__ == '__main__':
	sk = socket.socket()
	hostName = ("127.0.0.1", 8989)
	sk.connect(hostName)
	for i in range(3):#设置客户端验证次数为3次，超过则关闭连接
		# salt=b"alex"
		salt = input("请输入盐：").encode("utf-8")
		msgFromServer = sk.recv(1024).decode("utf-8")
		md5Obj = hashlib.md5(salt)
		md5Obj.update(msgFromServer.encode('utf-8'))
		result = md5Obj.hexdigest()
		sk.send(result.encode("utf-8"))
		
		msgFromServer2 = sk.recv(1024).decode("utf-8")
		# print(msgFromServer2)
		if msgFromServer2 == "success":
			print("校验成功")
			sys.exit(0)
		else:
			print("校验失败,你还有%d次机会" % (2 - i))
	sk.close()
