import sys
# python3必须从functools模块中引入reduce
from functools import reduce

# 匿名函数 lambda
# 普通写法
'''
def func(x=1,y=2,z=3):return x+y+z
print(func())
print(func(11,22,33))
'''
# lambda写法
func=lambda x=1,y=2,z=3:x+y+z
print(func()) # 6
print(func(4,5,6)) # 15

# lambda内嵌函数自动从上层函数或模块中得到变量
# 尽量避免使用嵌套lambda，因为不够直观
def appellation():
    action=lambda name:"hello "+name
    return action

act=appellation()
print(act("guy")) # lambda获取传入的guy作为name变量的值

# lambda实现选择逻辑
pickValue=lambda x,y:x if x<y else y

print(pickValue(100,200))
print(pickValue(200,100))

# lambda执行循环操作
# 要在lambda内部实现打印使用sys.stdout.write
showList=lambda l:map(sys.stdout.write,l)

myMap=showList(("animal\n","bird\n","swag\n","eagle\n"))
for x in myMap:x

# 函数式编程工具: filter和reduce
# filter过滤为真的元素
# 在-5至5之间选出大于0的值
myMap=filter((lambda x:x>0),range(-5,6))
myList=[]
for x in myMap:
    myList.append(x)
print(myList,end=" ")
print()

# reduce() 函数会对参数序列中元素进行累积。
# python3必须从functools模块中引入reduce
# from functools import reduce
print(reduce((lambda x,y:x+y),[1,2,3,4])) # 10
print(reduce((lambda x,y:x*y),[1,2,3,4])) # 24

# 生成器函数 yield
# 获取指定位数的斐波那契序列
# 1 1 2 3 5 8 13...
# 1.传统做法将序列值放到list序列中，但随着max的增大，程序内存压力也随之增大
'''
def fab(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n = n + 1
    return L

for n in fab(5):
    print(n)
'''
# 2.yield做法
'''
一个带有 yield 的函数就是一个 generator，它和普通函数不同，
生成一个 generator 看起来像函数调用，但不会执行任何函数代码，
直到对其调用 next()（在 for 循环中会自动调用 next()）才开始执行。
虽然执行流程仍按函数的流程执行，但每执行到一个 yield 语句就会中断，
并返回一个迭代值，下次执行时从 yield 的下一个语句继续执行。
'''
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

for n in fab(5):
    print(n)

