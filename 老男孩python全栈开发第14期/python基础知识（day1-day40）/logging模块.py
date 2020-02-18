"""
模块的功能
	日志格式的规范
	操作的简化
	日志的分级管理
	
logging模块的使用
	普通配置型
	对象配置型

日志级别
	日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），
	默认的日志格式为日志级别：Logger名称：用户输出消息。
"""
import logging
import os


if __name__ == '__main__':
	
	# 使用配置形式操作日志文件，不能将日志同时输出到屏幕和文件中。一般输出到文件。
	logging.basicConfig(
			level=logging.DEBUG,  # 最低级别日志
			format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
			datefmt='%a, %d %b %Y %H:%M:%S',
			filename=os.path.dirname(__file__) + '/config/test.log',  # 指定日志输出文件
			filemode='w'
	)
	logging.debug('debug message')
	logging.info('info message')
	logging.warning('warning message')
	logging.error('error message')
	logging.critical('critical message')
	
	strTest = "邓"
	if strTest == "邓":
		logging.info("username is：%s" % strTest)
	
	# 使用logging对象的形式来操作日志文件（推荐！），能同时输出到屏幕和文件中
	'''
	使用步骤：
			第一步：
				创建一个logger对象
			    创建一个文件管理操作符，用以输出到文件
			    创建一个屏幕管理操作符，用以输出到屏幕
			    创建一个日志输出的格式
		    第二步：
			    文件管理操作符  绑定  一个日志输出格式
				屏幕管理操作符  绑定  一个日志输出格式
				logger对象     绑定  文件管理操作符
				logger对象     绑定  屏幕管理操作符
			第三步：
				使用logger对象调用
	'''
	# 创建
	logger = logging.getLogger()
	fh = logging.FileHandler(filename=os.path.dirname(__file__) + "/config/logger.log",
	                         encoding="utf-8")  # 设置日志编码格式，支持中文
	sh = logging.StreamHandler()
	formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")
	# 绑定
	fh.setFormatter(formatter)
	sh.setFormatter(formatter)
	logger.addHandler(fh)
	logger.addHandler(sh)
	# 设置日志级别
	logger.setLevel(logging.DEBUG)  # 设置日志最低级别
	# 调用
	logger.debug('new debug message')
	logger.info('new info message')
	logger.warning('new warning message')
	logger.error('new error message')
	logger.critical('new critical message')
