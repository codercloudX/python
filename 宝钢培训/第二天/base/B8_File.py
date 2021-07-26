import pickle # 读写文件处理python序列化对象
import datetime
import sys

'''file读写文件'''
# 写文件
file=open("c:/sample.txt","w") # 创建sample.txt文件如果没有的话
file.write("添加新的内容1\r\n")
file.write("添加新的内容2\r\n")
file.close()

# 读文件
file=open("c:/sample.txt","r") # 等同于file=open("c:/sample.txt")
fileStr=file.read() # 读取所有内容
# file.readline() # 读取一行
# fileStr=fileStr.rstrip() # 去除末尾终止符\n \r
file.close()
print(fileStr)
# 更多文件类工具 pipes,fifos,sockets,keyed-access files...

birthday=datetime.datetime.strptime("1929-05-04","%Y-%m-%d").date()
person={"name":{"firstName":"Audrey","lastName":"Hepburn"},
        "three_dimensional":{" chest":"88","waist":"20"," hip":"89"},
        "birthday":birthday}
#将person字典保存到文件
file=open("c:/person.txt","wb") # python3必须以二进制写入模式
pickle.dump(person,file) # 将字典序列化写入文件
file.close()
#将person字典从文件中读取
file=open("c:/person.txt","rb")
personFromFile=pickle.load(file) # 从文件中将字典序列化读取出来
print(personFromFile["name"]) # {'firstName': 'Audrey', 'lastName': 'Hepburn'}