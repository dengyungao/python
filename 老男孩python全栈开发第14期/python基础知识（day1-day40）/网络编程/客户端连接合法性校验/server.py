import hashlib
import socket


if __name__ == '__main__':
	sk = socket.socket()
	hostName = ("127.0.0.1", 8989)
	sk.bind(hostName)
	sk.listen()
	# while 1:
	conn, addr = sk.accept()
	salt = b"alex"
	stringTest = "这是一个测试字符串"
	
	conn.send(stringTest.encode('utf-8'))
	md5Obj = hashlib.md5(salt)
	md5Obj.update(stringTest.encode('utf-8'))
	result = md5Obj.hexdigest()
	msgFromClient = conn.recv(1024).decode("utf-8")
	if msgFromClient == result:
		conn.send("success".encode("utf-8"))
	else:
		conn.send("fail".encode("utf-8"))
	
	conn.send(stringTest.encode('utf-8'))
	md5Obj = hashlib.md5(salt)
	md5Obj.update(stringTest.encode('utf-8'))
	result = md5Obj.hexdigest()
	msgFromClient = conn.recv(1024).decode("utf-8")
	if msgFromClient == result:
		conn.send("success".encode("utf-8"))
	else:
		conn.send("fail".encode("utf-8"))
	
	conn.send(stringTest.encode('utf-8'))
	md5Obj = hashlib.md5(salt)
	md5Obj.update(stringTest.encode('utf-8'))
	result = md5Obj.hexdigest()
	msgFromClient = conn.recv(1024).decode("utf-8")
	if msgFromClient == result:
		conn.send("success".encode("utf-8"))
	else:
		conn.send("fail".encode("utf-8"))
		
	conn.close()
	sk.close()
