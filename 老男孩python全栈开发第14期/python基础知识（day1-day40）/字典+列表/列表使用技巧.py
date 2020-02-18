from collections import Counter


if __name__ == '__main__':
	numbers = [30, 42, 28, 50, 15]
	for index, num in enumerate(numbers):  # enumerate()方法为可迭代对象添加一个计数器，并以枚举对象的形式返回
		if num % 3 == 0 and num % 5 == 0:
			numbers[index] = num + 1
		elif num % 3 == 0:
			numbers[index] = num + 2
		elif num % 5 == 0:
			numbers[index] = num + 3
	print(numbers)
	
	# 合并长度相同的多个列表
	countries = ['France', 'Germany', 'Canada']
	capitals = ['Paris', 'Berlin', 'Ottawa']
	for country, capital in zip(countries, capitals):
		print(country, capital)
	
	# 计算可迭代对象的元素出现的次数
	num = Counter(['a', 'b', 'c', 'd', 'b', 'c', 'd', 'b'])
	print(num)
	print(num.get('b'))
	
	# 将两个列表转换成字典
	students = ["Peter", "Julia", "Alex"]
	marks = [84, 65, 77]
	dic = dict(zip(students, marks))
	print(dic)

	