if __name__ == '__main__':
	# 列表推导式
	lst = [["deng", "yuneegdeng"], ["gao", "dengyungao"]]
	print([name for first in lst for name in first if name.count('e') >= 2])  # 嵌套列表
	print([(x + 2, y) for x in range(3) for y in range(3)])
	print(["{first}*{second}=".format(first=m, second=n) + str(m * n) for m in range(5) for n in range(5)])
	
	x = {
			'name': 'alex',
			'Values': [{'time': 34, 'value': 100},
			           {'time': 34, 'value': 100},
			           {'time': 34, 'value': 100}]
	}
	listNew = [(el['time'], el['value']) for el in x['Values']]
	print(listNew)
	
	# 假设使用列表推导从两个列表中查找通用数字
	lst1 = [1, 2, 3, 4, 5]
	lst2 = [3, 4, 5, 6, 7, 8]
	lst3 = [a for a in lst1 for b in lst2 if a == b]
	print(lst3)
	
	# 字典推导式
	dic = {
			"age": 12,
			"height": 123,
			"name": "dyg",
	}
	print({key: str(value) + "-NEW" for key, value in dic.items()})
	print({key: str(dic[key]) + "-NEW" for key in dic.keys()})
