import socket
sk=socket.socket()
sk.connect(("127.0.0.1",8071))
while 1 :
	cmd=input("（客户端）请输入要执行的命令：")
	if str(cmd)=="quit":
		print(str(cmd))
		break
	else:
		sk.send(cmd.encode("utf-8"))
		result=sk.recv(1024).decode("gbk")
		print(result)
sk.close()
