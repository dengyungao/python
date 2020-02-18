import json
import os
import socket


LIMIT_FILE_SIZE = 9090  # 单次接受文件大小的最大值
sk = socket.socket()

sk.connect(("127.0.0.1", 8099))
# 选择操作类型
meun = {"1": "upload", "2": "download", }
choiceNumber = input("请输入功能选项（1/2）: ")
if choiceNumber == "1":
	# 创建一个与被上传文件相关的字典
	dic = {"opt": meun.get(choiceNumber),
	       "filename": None,
	       "content": None,
	       }
	file_path = input("输入需上传文件的绝对路径：")#如E:/Projects_to_github(python)/python/python/网络编程/文件的上传和下载/client.py
	dic["filename"] = os.path.basename(file_path)  # 获取需上传文件的名称
	with open(file_path, "r", encoding="utf-8") as f:#获取需上传文件的内容
		content = f.read()
	dic["content"] = content
	str_dic = json.dumps(dic)  # 字典序列化为字符串
	sk.send(str_dic.encode("utf-8"))
elif choiceNumber == "2":
	# 下载
	pass
else:
	# 报错
	pass
