import hashlib
import json
import socket


sk = socket.socket()
sk.connect(('127.0.0.1', 8080))

dic = {'status': False, 'username': None, 'password': None}
c = 3
while c:
	username = input('请输入用户名')
	password = input('请输入密码')
	
	md5_obj = hashlib.md5(password.encode('utf-8'))
	md5_obj.update(username.encode('utf-8'))
	pawd_m = md5_obj.hexdigest()
	
	dic['username'] = username
	dic['password'] = pawd_m
	str_dic = json.dumps(dic)#序列化
	sk.send(str_dic.encode('utf-8'))
	
	# 服务器应该回复我一个这样的字典：
	# 是否登录成功，如果没有登录成功是因为什么原因？
	res_dic = sk.recv(1024).decode('utf-8')  # str_dic
	result = json.loads(res_dic)  # dic = {status:False/True ,  username ,   password,   reason}
	if result['status']:
		print('登录成功')
		break
	else:
		print('失败，%s' % result['reason'])
		c -= 1

sk.close()
