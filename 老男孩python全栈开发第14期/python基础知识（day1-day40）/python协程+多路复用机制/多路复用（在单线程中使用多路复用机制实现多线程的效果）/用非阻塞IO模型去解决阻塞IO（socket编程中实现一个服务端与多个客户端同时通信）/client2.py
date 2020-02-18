import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

while 1:
	msg_s = input('>>>')
	if not msg_s: continue
	if msg_s == 'q': break
	sk.send(msg_s.encode('utf-8'))
	print(sk.recv(1024).decode('utf-8'))
sk.close()
