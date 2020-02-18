import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

abs_path = input('请输入您的根目录:')
sk.send(abs_path.encode('utf-8'))
current_dir = sk.recv(1024).decode('utf-8')
print(current_dir.split('--'))

while 1:
	cmd = input('请输入>>>')
	# cd + 文件夹      ..
	if cmd == '..':
		sk.send(cmd.encode('utf-8'))
		current_dir = sk.recv(1024).decode('utf-8')
		print(current_dir.split('--'))
	if cmd == 'cd':
		filename = input('请输入一个文件夹名：')
		sk.send((cmd + ' ' + filename).encode('utf-8'))
		current_dir = sk.recv(1024).decode('utf-8')
		print(current_dir.split('--'))

sk.close()