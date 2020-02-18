import subprocess


'''
执行系统命令并获取结果
'''
if __name__ == '__main__':
	'''
	subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
	cmd 代表系统命令
	shell=True 代表这条命令是系统命令，告诉操作系统，将cmd当成系统命令去执行。
	stdout 是执行完系统命令之后用于保存正确结果的一个管道。
	stderr 是执行完系统命令后用于保存错误结果的一个管道。
	'''
	ret = subprocess.Popen("dir", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	stdout=ret.stdout.read().decode("gbk")#字符串
	print(stdout)  # 正确结果
	stderr=ret.stderr.read().decode("gbk")#字符串
	print(stderr)  # 当发生错误时，该值就能捕获异常信息
	
