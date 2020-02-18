"""
参考 ：https://www.cnblogs.com/yang-wei/p/9985099.html
"""
import hashlib
def encrypt(s):
	'''
	md5加密字符串
	:param s:被加密字符串
	:return:
	'''
	md5 = hashlib.md5()
	md5.update(s.encode("utf-8"))#只能加密字节数据
	return md5.hexdigest()


if __name__ == '__main__':
	# 加密单个字符串
	print(encrypt("deng"))
	# 加密多个字符串
	strList = ["deng", "yun", "gao"]
	code = ""
	for key in strList:
		code += encrypt(key)
	print(code)
