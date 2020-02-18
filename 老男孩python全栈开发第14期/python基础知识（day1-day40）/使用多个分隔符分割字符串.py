import re


if __name__ == '__main__':
	line = "asdf fjdk  ;    afed, fjek, asdf   ,               foo"  # 同时有多个分隔符
	lineToList = re.split(r"\s*[;,\s]\s*", line)
	print(lineToList)
	lineToList2 = re.split(r"\s[;|,|\s]\s*", line)
	print(lineToList2)
	
	line2 = "asdf  fjdk          afed   fjek asdf                     foo"  # 同时有多个分隔符
	print(re.split(r"\s*[\s]\s*", line2))  # 去掉多个空格
	print(re.split(r"\s*(\s)\s*", line2))  # 保留一个空格
	print(list(filter(None, line2.split(" "))))  # 去掉多个空格
