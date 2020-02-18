"""
os模块
os.mkdir()      创建单个目录
os.makedirs()   创建多级目录

os.remove()             删除单个目录
os.removedirs()         删除多级目录

os.rename(“old”,“new”)  重命名文件、目录

os.listdir(path)        列出目录下的所有文件，返回列表。
os.stat(file_path)      查看某个文件的详细信息
os.name()               指明当前使用的平台是windows(返回值为nt)还是linux（返回值为posix）

os.system(command)  只执行命令，不关心返回值。
os.popen(command).readlines() 执行命令并获取结果
"""
import os

print(os.path.abspath("hash()方法.py"))#返回文件的绝对路径
print(os.path.split("E:/Projects_to_github(python)/python/python/hash()方法.py"))#以元祖形式返回文件所在路径和文件名
print(os.path.dirname("E:/Projects_to_github(python)/python/python/hash()方法.py"))#返回文件所在路径，E:/Projects_to_github(python)/python/python
print(os.path.basename("E:/Projects_to_github(python)/python/python/hash()方法.py"))#返回文件名，hash()方法.py

print(os.path.exists("E:/Projects_to_github(python)/python/python/hash()方法.py"))#文件是否存在
print(os.path.isfile("E:/Projects_to_github(python)/python/python/hash()方法.py"))#判断是否是文件
print(os.path.isdir("E:/Projects_to_github(python)/python/python/"))#判断是否是目录

print(os.path.join("E:/Projects_to_github(python)/python/","hash()方法.py"))#拼接目录和文件
print(os.path.getsize("E:/Projects_to_github(python)/python/python/hash()方法.py"))#获取文件大小

#注意，所有文件夹的大小都是固定的，都是4096KB
print(os.path.getsize("E:/Projects_to_github(python)/python/python/"))#获取文件夹大小
print(os.path.getsize("E:/Projects_to_github(python)/"))

print(os.path.dirname(__file__))#当前目录
print(os.path.dirname(os.path.dirname(__file__)))#当前目录的上级目录

#面试题：统计某个文件夹中的所有文件的总大小

