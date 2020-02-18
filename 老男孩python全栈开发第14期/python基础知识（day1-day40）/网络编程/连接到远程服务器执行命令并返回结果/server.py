"""
客户端发送要执行的命令到服务器，服务器执行完后将结果返回给客户端，
客户端拿到结果后呈现给用户。
"""
import socket
import subprocess


sk = socket.socket()#默认tcp传输
sk.bind(("127.0.0.1", 8071))
sk.listen()
conn, addr = sk.accept()
while 1:
	cmd = conn.recv(1024).decode("utf-8")
	r = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout = r.stdout.read()  # 正确结果,byte类型
	stderr = r.stderr.read()  # 错误结果，byte类型
	if not stderr:
		conn.send(stdout)
	else:
		conn.send(stderr)
conn.close()
sk.close()
