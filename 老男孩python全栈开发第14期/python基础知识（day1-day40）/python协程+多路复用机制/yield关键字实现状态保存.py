'''
结论：
	程序每遇到带yield关键的行时就会返回yield后面的参数（返回值），并停留在该行代码处，
	继续运行代码的话，程序就会从该行的下一行继续执行。所以说yield能实现状态保存和程序切换。
'''
def func():
	sum = 0
	print(1)
	print(2)
	yield sum
	print(3)
	yield sum+1
	print(4)
	print(5)
	yield sum+2

def ffff():
	g = func()#此时不会执行func函数
	print('这是在ffff函数中')
	print(next(g))#此时才开始执行func函数到第10行（第一个yield），返回结果sum并停留在此处
	print('这是在ffff函数中')
	print(next(g))#此时func函数从第11行开始执行到第12行(第二个yield)，返回结果sum+1并停留在此处
	print('这是在ffff函数中')
	print(next(g))#此时func函数从第13行开始执行到第15行（第三个yield），返回结果sum+2,此时func函数运行结束。

if __name__ == '__main__':
	ffff()
