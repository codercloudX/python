# 很多时候，数据读写不一定是文件，也可以在内存中读写。

# StringIO
# 顾名思义就是在内存中读写str。
from io import StringIO
f=StringIO()
f.write("hello")
f.write(" ")
f.write("world")
print(f.getvalue())# getvalue()方法用于获得写入后的str

# 读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s=f.readline()
    if(s==""):
        break
    print(s.strip())
    
# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
from io import BytesIO
f=BytesIO()
f.write("hello,py".encode('utf-8'))
print(f.getvalue())
