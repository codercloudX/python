import decimal
import random
import math

'''内置set函数'''
# set会乱序排序且去除同类型相同的数据
x=set("pythonn") # {'n', 'y', 'h', 'o', 't', 'p'} 无序
print(x)
y=set(['p','y','t','h','o','n'])
print(y)
z=set(['1',1,'t','h','o','n'])
print(z)
# set不支持多层嵌套的list
# z1=set([[1,2,3],[4,5,6],[1,2,3]])
# print(z1)

'''固定精度浮点数'''
# 不用decimal的类库会发生小数精度的偏移丢失的风险
d1=3.14159265358979
d1+=1
print(d1)
# 固定精度浮点数的正确用法
d=decimal.Decimal('3.1415926')
d+=1
print(d) # 4.1415926

'''布尔值'''
bool=1>10
print(bool) # False

'''空占位符'''
param=None
print(param) # None
paramList=[None]*5
print(paramList) # [None, None, None, None, None]
print(type(paramList)) # <class 'list'> 显示变量的类型

'''判断变量类型'''
# 方法1
if type(paramList)==type([]):print("yes")
else:print("no")
# 方法2
if type(paramList)==list:print("yes")
else:print("no")
# 方法3
if isinstance(paramList,list):print("yes")
else:print("no")

# 混合类型自动升级
integer=100 # python3没有long类型，统一为int
integer+=3.64
floatType=integer
print(floatType) # 103.64 升级为float，在java中是不允许的
print(int(floatType)) # 103 强制转换为int，不做四舍五入
oInt=1
print(float(oInt)) # 1.0

# 保留小数位数
num=1/3
print(num)
num1="%.3f" % num #保留3位小数
print(num1)

# 除法：真除法、Floor除法
print(10/3) # 3.3333333333333335
print(10//3) # Floor除法只保留整数

# 位操作—见ppt分析
x=1 # 0001
print(x<<2) # 0100=4
print(x|2) # 0011
print(x&1) # 0001

# 复数—见ppt分析
complexData=2+2j*2 # 2+4j
complexData*=3
print(complexData) # (6+12j)
print(complexData.real) # 6.0
print(complexData.imag) # 12.0
print(complexData.conjugate()) # 共轭复数 (6-12j)

# 八进制和十六进制—见ppt分析
print(0o1) # 1
print(0o11) # 9
print(0o111) # 73
print(0x01) # 1
print(0x1A) # 26
print(0x3E7) # 999
print(oct(64)) # 0o100
print(hex(255)) # 0xff
print(int('0100')) # 100
print(int('0o100',8)) # 64
print(int('0x40',16)) # 64
# eval函数也可以转换，但速度会稍慢些
print(eval('100')) # 100
print(eval('0o100')) # 64
print(eval('0x40')) # 64

# 其他内置数学工具
print(math.pi) # 3.141592653589793
print(math.sin(2*math.pi/180)) # 0.03489949670250097
print(math.sqrt(9)) # 3.0
print(abs(-100)) # 100
print(2**100) # 2的100次方
print(pow(2,4)) # 等同于2**4 16
print(int(7.896)) # 7
print(round(7.896)) # 8
print(round(7.896,3)) #7.9
print(random.random()) # 0-1之间随机数
print(random.randint(1,10)) # 1-10之间随机数包括10
myList=["jack","rose","mike"]
print(random.choice(myList)) # myList序列随机取值

# 小数
myFloat=0.1+0.1+0.1-0.3
print(myFloat) # 5.551115123125783e-17 硬件精度缺陷造成
# 银行金融业必须使用decimal
myFloat=decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1')-decimal.Decimal('0.3')
print(myFloat) # 0.0 Decimal修正精度缺陷

# 集合
collectionX=set("abcde")
collectionY=set("defgh")
print(collectionX) # {'b', 'c', 'a', 'd', 'e'}
print('e' in collectionX) # True
print(collectionX-collectionY) # {'a', 'b', 'c'} 得到collectionX中在collectionY里没有的元素
print(collectionX|collectionY) # {'c', 'd', 'b', 'f', 'h', 'g', 'e', 'a'} 合并collectionX和collectionY的元素并去除重复
print(collectionX&collectionY) # {'d', 'e'} 得到collectionX和collectionY交集部分的元素