import struct

'''struct读写文件'''
# struct模块打包二进制数据存储与解析
'''
数据格式为
姓名 年龄 性别   职业
lily 18  female teacher
'''
fp = open('c:/teacher.bin','wb')
# 按照上面的格式将数据写入文件中
# 这里如果string类型的话，在pack函数中就需要encode('utf-8')
name = b'lily' # b代表bytes类型
age = 18
sex = b'female'
job = b'teacher'
# int类型占4个字节
fp.write(struct.pack('4si6s7s', name,age,sex,job))
fp.flush()
fp.close()
# 将文件中写入的数据按照格式读取出来
fd = open('c:/teacher.bin','rb')
name1,age1,sex1,job1=struct.unpack('4si6s7s',fd.read(21))
fd.close()
print(str(name1) + "," + str(age1) +","+str(sex1)+","+str(job1))
