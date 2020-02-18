##############################小文件的传输
# import socket
# import json
# sk = socket.socket()
# sk.bind(("127.0.0.1",8001))
# sk.listen()
# conn,addr = sk.accept()
# str_dic = conn.recv(9090).decode("utf-8")
# dic = json.loads(str_dic)
# if dic["opt"] == "upload":
#     filename = "1"+ dic["filename"]
#     with open(filename,"w",encoding="utf-8") as f:
#         f.write(dic["content"])
# elif dic["opt"] == "download":
#     pass
#
# conn.close()
# sk.close()


###################大文件的传输
# import socket
# import json
# sk = socket.socket()
# sk.bind(("127.0.0.1",8001))
# sk.listen()
# conn,addr = sk.accept()
# str_dic = conn.recv(100).decode("utf-8")
# conn.send(b'ok')
# # str_dic = {"opt":menu.get(num),"filename":None,"filesize":None}
# dic = json.loads(str_dic)
# if dic["opt"] == "upload":
#     filename = "1"+ dic["filename"]
#     with open(filename,"ab") as f:
#         while dic['filesize']:
#             content = conn.recv(1024)
#             f.write(content)
#             dic['filesize'] -= len(content)
#
# elif dic["opt"] == "download":
#     pass
#
# conn.close()
# sk.close()


########################################优化
import socket
import json
import struct
import time


sk = socket.socket()
sk.bind(("127.0.0.1", 8001))
sk.listen()
conn, addr = sk.accept()
b_len_dic = conn.recv(4)  # 接收字典的长度
len_dic = struct.unpack('i', b_len_dic)[0]  # 获取到int类型字典的长度，unpack得到的是一个元组，要取下标为0的位置
str_dic = conn.recv(len_dic).decode('utf-8')
# str_dic = {"opt":menu.get(num),"filename":None,"filesize":None}
dic = json.loads(str_dic)
if dic["opt"] == "upload":
	date = time.time()
	filename = dic["filename"] + "%s" % date
	with open(filename, "ab") as f:
		while dic['filesize']:
			content = conn.recv(1024)
			f.write(content)
			dic['filesize'] -= len(content)

elif dic["opt"] == "download":
	# 客户端发来一个字典要执行的功能，以及客户端自己的绝对路径
	# 服务器要返回这个绝对路径中所有文件及文件夹
	# 客户端自己选择进入到哪一层目录下
	# 服务器都要返回对应目录下所有文件及文件夹
	# 客户随时选择某一个目录下的某一个文件进行下载
	
	
	# 客户端发送来一个字典，包含了要进行的操作，要下载的文件的绝对路径，
	# 根据绝对路径去读取文件内容
	# 一边读，一遍发
	pass

conn.close()
sk.close()
