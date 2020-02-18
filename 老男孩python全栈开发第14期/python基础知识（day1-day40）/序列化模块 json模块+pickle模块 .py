
"""
字典、列表、数字、对象转化成一个字符串，即序列化，反过来则是反序列化
何时用序列化：
		要把文件写入文件时
		网络传输数据时
		
序列化模块
json    支持数据类型较少（只支持列表或字典），但能跨语言，
pickle  注意，pickle的用法与json完全相同，pickle几乎支持python所有数据类型，但只能在python中用

json模块的限制：
        json格式的字典的key必须是字符串类型，如果不是也会自动转成字符串。
        json格式中的字符串只能用双引号括起来。不能用单引号。
        json不支持元组作为字典的value，会自动转换成列表，也不支持元组作为字典的key。
        json不允许对set类型进行操作，必须转换成列表在操作。
"""
import json
import os
import pickle


if __name__ == '__main__':
    dic={"K":"V"}
    strDic=str(dic)
    print(type(strDic))
    print(type(eval(strDic)))
    
    #json模块
    dic2={'aaa':'bbb','ccc':'ddd'}
    print(dic2)
    print(json.dumps(dic2))#字典转字符串
    print(json.loads(json.dumps(dic2))['aaa'])#字符串转字典
    
    #字典的内容以字符串的形式写入文件
    currentPath=os.path.dirname(__file__)
    with open(currentPath+"/config/json_to_file",'w') as file:
        json.dump(dic2,file)
        
    #从文件中读取字符串形式的字典
    with open(currentPath+"/config/json_to_file",'r')  as file:
        ret=json.load(file)
    print(type(ret))#拿到的值直接就是一个字典
    
    #同时写入和获取多个数据
    dicTest={"name":"邓云高","age":28}
    lst=[1,2,3,4,5,6,7]
    with open(currentPath+"/config/test1","w")  as file:
        strDic=json.dumps(dicTest)
        strLst=json.dumps(lst)
        file.write(strDic+"\n")#按行写入，方便读取
        file.write(strLst+"\n")
        
    with open(currentPath+"/config/test1","r") as file:
        for line in file:#按行读取
            ret=json.loads(line)
            print(ret)
    
    
        
    #pickle模块
    dicTest2={1:(2,3,4),('a','b'):4}
    print(pickle.dumps(dicTest2))#序列化，只能将字典转换成byte类型
    print(pickle.loads(pickle.dumps(dicTest2)))#反序列化，完全返回原字典，支持元组和单引号等，不同于json
    
    class Student():
        def __init__(self,name,age):
            self.name=name
            self.age=age
    student=Student("dengyungao",24)
    print(pickle.dumps(student))#只能将对象转换成byte类型
    print(pickle.loads(pickle.dumps(student)).name)#反序列化对象，访问其name属性
    
    with open(currentPath+"/config/test2",'wb') as file:
        pickle.dump(student,file)#可以将任意类型的数据存入文件
        
    with open(currentPath+"/config/test2",'rb') as file:
        obj=pickle.load(file)#返回student对象
        print(obj.age)
        
        
    
    
    
    
    
    
    
    
    
    
