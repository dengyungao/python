if __name__ == '__main__':
	lst = [1, 1, 4, 5, 6, 7, 2, 6, 8, 5, 7, 6]
	# 无顺序去重
	print(list(set(lst)))
	
	# 原顺序去重
	print({key: None for key in lst}.keys())
	print({lst[i]: None for i in range(len(lst))}.keys())
