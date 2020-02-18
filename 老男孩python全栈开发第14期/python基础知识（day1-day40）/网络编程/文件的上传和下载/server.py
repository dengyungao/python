import json
import os
import socket


LIMIT_FILE_SIZE = 9090  # 读取文件内容的最大值
sk = socket.socket()
sk.bind(("127.0.0.1", 8099))
sk.listen()
conn, addr = sk.accept()
str_dic = conn.recv(LIMIT_FILE_SIZE).decode("utf-8")
dic = json.loads(str_dic)
if dic["opt"] == "upload":
	# 上传
	filename = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "/config/upload/" + dic["filename"]
	with open(filename, "w", encoding="utf-8") as f:
		f.write(dic["content"])

elif dic["opt"] == "download":
	# 下载
	pass

else:
	pass

conn.close()
sk.close()
