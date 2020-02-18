"""
random模块
用的最多的：
        random.random() 0-1之间的随机小数
        random.uniform(1,5) 指定范围内的随机小数
        random.randint(1,3)  包含3在内的范围内的随机整数，即[1,3]
        random.randrange(1,3) 不包含3在内的范围内的随机整数，即[1,3)
        random.randrange(1,10,2) 不包含10在内的范围内的随机奇数，即[1,10)

随机抽取（只能在列表上使用）
list=[1,2,3,4,5]
random.choice(list)#随机抽取列表一个值
random.simple(list,3)#随机抽取列表3个值

打乱顺序
random.shuffle(list)#随机打乱列表顺序
"""
import random

if __name__ == '__main__':
	
	# 1 生成随机4位数字验证码：
	
	code = ""
	for i in range(4):
		num = random.randint(0, 9)
		code += str(num)
	print(code)
	
	# 2 生成随机6位数字+字母验证码：
	code = ""
	for i in range(6):
		rand_num = str(random.randint(0, 9))  # 随机数字
		rand_zimu_lower = chr(random.randint(97, 122))  # 随机小写字母
		rand_zimu_upper = chr(random.randint(65, 90))  # 随机大写字母
		auto_code = random.choice([rand_num, rand_zimu_lower, rand_zimu_upper])  # 随机取出一个
		code += auto_code
	print(code)
	
	
	
	
	
