# 1.if语句
job="Serial Killer"
if job=="Thief":
    print\
        ("Hi thief!") # 反斜杠跨行连接
elif job=="Robber":
    print("Hi robber!")
else:
    print("Hi guy!")

# 2.三元表达式
# 一般用来替代2个条件的if...else，从而简化语法
# 类似java的三元表达式 boolean flag=(10<9)?true:false
flag=True if 10<9 else False
print(flag)

# 3.一行写几条语句，也是python唯一用分号的地方
x=1;y=2;z=3

# 4.while语句
# 死循环写法
'''
while True:
    print("see u again!")
'''
# 标准while
i=0;j=10
while i<10:
    if j>5:pass # 占用语句不做任何事情
    i += 1
    if i==5:break
    #if i == 5:continue
    print("current i="+str(i))

# while else
x=2
while x<5:
    print("x=" + str(x) + " x<5")
    x+=1
else:
    print("x="+str(x)+" x>=5")

# 5.for
sum=0
list=[1,2,3,4,5] # 这里用字符串、元组均可
for x in list:
    sum+=x
print("total="+str(sum))

# for嵌套
sumI=sumJ=0
# range第一位默认0可以不写，最后一位步长默认1可以不写
# 等同于for i in range(5): 标识0到5之间不包括5，步长为1
for i in range(0,5,1):
    sumI+=i
    for j in range(5):
        sumJ+=sumI+j
print("sumI="+str(sumI)+" sumJ="+str(sumJ))

# 文件内容循环读取
file=open("c:/sample.txt")
while True:
    char=file.read(1) #以字母方式逐个读取，file.read()一次性读取整个文件内容[如果文件很大性能差]
    if not char:break
    print(char,end="") # 打印不换行
file.close()

file=open("c:/sample.txt")
for char in file.read():
    print(char,end="")
file.close()

file=open("c:/sample.txt")
# 最快读取方式
for line in file.readlines():
    print(line.strip()) # 去除每行换行符，因为readlines()会为line再加换行符，这样行与行之间就会有空行
file.close()

# 循环技巧:for的执行速度比while快

# 6.并行遍历：zip和map
# zip合并列表元素生成元组列表
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]
tupleList=zip(l1,l2,l3) # [(1,5,9),(2,6,10),(3,7,11),(4,8,12)]
for (x,y,z) in tupleList:
    print("x="+str(x)+" y="+str(y)+" z="+str(z)+" x+y+z="+(str(x+y+z)))

# zip构建字段
keysList=["id","name","department"]
valsList=["001","jeffrey","sales"]
zipDict=dict(zip(keysList,valsList)) # dict函数构造字典
print(zipDict) # {'id': '001', 'name': 'jeffrey', 'department': 'sales'}

# map 根据提供的函数对指定序列做映射
myMap=map(lambda x: pow(x,3), [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
myList=[]
for x in myMap:
    myList.append(x)
print(myList,end=" ")
print()

# enumerate 得到元素和索引下标
word="sandra"
for (offset,item) in enumerate(word):
    print(item + " at "+ str(offset))

# 小结: python通过缩进分几行完成while、for等语句块