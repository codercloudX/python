# 引入模块
import sys

'''
多行注释
'''

'''字符串'''
print('hello world')  # 等同于print("hello world")
sys.stdout.write("hello world\n")  # 等同于print("Hello world",end="")
print('hello ladies', 'and gentlemen', file=sys.stdout)  # 重定向输出
f = open('abc.txt', 'w')
print('hello ladies', 'and gentlemen', file=f)  # 重定向输出
# 单引号和双引号交替使用可方便用于显示引号本身
print("我是'隔壁老王'")
print('我是"隔壁老王"')
print('a join b' + ' is c')  # +号可以连接字符串

systemType = sys.platform  # 变量定义
print(systemType)  # 打印系统类型

myStr = "abcdefg"
print(len(myStr))  # 打印myStr长度 7
print(myStr[2])  # 显示myStr正向第三位字符 c
print(myStr[-3])  # 显示myStr反向第三位字符 e
print(myStr[len(myStr) - 3])  # 等同于print(myStr[-3]) e
print(myStr[:3])  # 从头开始剪切myStr3位 abc
print(myStr[1:3])  # 剪切myStr从第二位开始取2位 bc
print(myStr[:])  # 全部剪切，等同于显示myStr abcdefg
print(myStr[:-1])  # 从倒数第二位开始剪切 abcdef
print(myStr * 2)  # 打印2次myStr abcdefgabcdefg
print(myStr[::2])  # aceg 从头到尾间隔获取
print(myStr[1:6:2])  # bdf 从第2位b开始取到g,间隔获取
print(myStr[::-1])  # gfedcba 反转
print(myStr[5:1:-1])  # fedc

'''字符串不可变性'''
crossLineStr = '''
11111
22222
33333
'''
print(crossLineStr)  # 字符串很长希望多行定义完成可用三个单引号处理
otherStr = '123456789'
# otherStr[0]=2 # 一旦定义了字符串则不能改变某个索引位置的字符
otherStr = '2' + otherStr[1:len(otherStr)]  # 重新对字符串赋值是可以的
print(otherStr)

'''字符串函数方法'''
print(otherStr.find('456'))  # 查找出456的索引位置 3
print(otherStr.replace('456', '000'))  # 将所有的456全部替换成000 22300078
print(otherStr.join("join"))  # j22345678o22345678i22345678n
print("join".join(otherStr))  # 2join2join3join4join5join6join7join8
word = "hello world"
print(word.upper())  # HELLO WORLD
print(word.isalpha())  # False
print(word.endswith("rld"))  # True

token = "111,222,333,444"
tokenList = token.split(',')  # 以逗号分隔返回字符串列表 ['111', '222', '333', '444']
print(tokenList)
print(len(tokenList))  # 列表长度=4

'''
回车换行在不同系统中是不一样的
windows \r\n
linix \n
mac \r
'''
print(ord('\n'))  # 显示回车不可见字符的ascii 10
print(ord('\r'))  # 显示换行不可见字符的ascii 13
print(ord('A'))  # 65
print(chr(65))  # A


# mystr = 'abcde'
# print(mystr[:1])