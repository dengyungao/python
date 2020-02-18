# ############################# 小文件的传输
# import socket
# import os
# import json
# sk = socket.socket()
# sk.connect(("127.0.0.1",8001))
# menu = {"1":"upload","2":"download"}
# for k,v in menu.items():
#     print(k,v)
# num = input("请输入功能选项:")
# if num == "1":
#     dic = {"opt":menu.get(num),"filename":None,"content":None}
#     file_path = input("请输入一个绝对路径:")
#     filename = os.path.basename(file_path)
#     with open(file_path,"r",encoding="utf-8") as f:
#         content = f.read()
#     dic["filename"] = filename
#     dic["content"] = content
#     str_dic = json.dumps(dic)
#     sk.send(str_dic.encode("utf-8"))
#
# elif num == "2":
#     pass


#################################################大文件的传输
# import socket
# import os
# import json
# sk = socket.socket()
# sk.connect(("127.0.0.1",8001))
# menu = {"1":"upload","2":"download"}
# for k,v in menu.items():
#     print(k,v)
# num = input("请输入功能选项:")
# if num == "1":
#     dic = {"opt":menu.get(num),"filename":None,"filesize":None}
#     file_path = input("请输入一个绝对路径:")# 文件的绝对路径
#     filename = os.path.basename(file_path)# 文件名字
#     filesize = os.path.getsize(file_path)# 获取用户输入的路径中文件的大小
#
#     dic["filename"] = filename
#     dic["filesize"] = filesize
#     str_dic = json.dumps(dic)
#     sk.send(str_dic.encode("utf-8"))# 将被填充完成的字典先发送给服务器
#     sk.recv(1024)# 为什么要有一个recv？
#     #  因为上边send字典时，如果程序执行过快，可能会马上执行到下边的send(content)
#     #  此时有可能会发生粘包，所以在此中间加一个recv,为了避免粘包
#     with open(file_path,"rb") as f:
#         while filesize:
#             content = f.read(1024)
#             sk.send(content)
#             filesize -= len(content)
#
# elif num == "2":
#     pass
##########################################优化
import socket
import os
import json
import struct


sk = socket.socket()
sk.connect(("127.0.0.1", 8001))
menu = {"1": "upload", "2": "download"}  # 操作类型
for k, v in menu.items():
	print(k, v)
num = input("请输入功能选项:")
if num == "1":
	dic = {"opt": menu.get(num), "filename": None, "filesize": None}
	file_path = input("请输入一个绝对路径:")  # 文件的绝对路径，E:\Python S14\day32\实现大文件的传输\11.mp4
	filename = os.path.basename(file_path)  # 文件名字
	filesize = os.path.getsize(file_path)  # 获取用户输入的路径中文件的大小
	dic["filename"] = filename
	dic["filesize"] = filesize
	str_dic = json.dumps(dic)
	len_dic = len(str_dic)  # 获取到字典的长度，是一个int类型的数据   46   146
	b_len_dic = struct.pack('i', len_dic)  # 用一个4bytes的数据表示字典的长度
	
	sk.send(b_len_dic + str_dic.encode("utf-8"))  # 将bytes类型的字典的长度 + bytes类型的字典的内容，一起发送给服务器
	
	#  因为上边send字典时，如果程序执行过快，可能会马上执行到下边的send(content)
	#  此时有可能会发生粘包，所以在此中间加一个recv,为了避免粘包
	with open(file_path, "rb") as f:
		while filesize:
			content = f.read(1024)
			sk.send(content)
			filesize -= len(content)

elif num == "2":
	pass
