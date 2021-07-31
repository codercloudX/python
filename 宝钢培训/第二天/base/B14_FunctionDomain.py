import base.B14_1_OutsideGlobal as b14og
import sys

X=100 # 全局变量一般都定义成大写
def func():
    X=88
    return X

print(X) # 全局100
print(func()) # 局部88
print(X) #100

X1=100
def func1():
    global X1 # global用于在函数内部声明全局变量，不能出现在X1=100的顶层位置
    X1=101
    return X1
print(X1) # 全局100
print(func1()) # 101
print(X1) # 全局修改后的值101

# 引用外部base.B14_1_OutsideGlobal.py的全局变量
# 方法1:import base.B14_1_OutsideGlobal as b14og
print(b14og.PI) # 3.14
print(b14og.R) # 100
# 方法2:import sys
sys_b14og=sys.modules["base.B14_1_OutsideGlobal"]
print(sys_b14og.PI)
print(sys_b14og.R)

# 工厂函数：能够记住嵌套作用域变量值的函数
# 后续用类来替换工厂函数
def myPow(n):
    def doPow(x):
        return pow(x,n);
    return doPow

mp=myPow(3) # 初始化myPow并设置n指数=3
print(mp(2)) #将底数x传入已被初始化myPow的实例mp计算

# python函数返回多值
def getStuffFund(salary,bonus):
    salary*=1.5
    bonus+=salary
    return salary,bonus

salary,bonus=getStuffFund(5000,10000)
stuffDetails=getStuffFund(5000,10000)
# salary=7500.0 bonus=17500.0
print("salary="+str(salary)+" bonus="+str(bonus))
# (7500.0, 17500.0)
print(stuffDetails)

def getStuffFund1(salary,bonus,sum):
    salary*=1.5
    bonus+=salary
    sum+=bonus+salary
    return salary,bonus,sum
# 如果外部接收变量少于返回数量，则外部只能有一个变量接收否则报错
# 如果外部多个变量，则必须与返回值的数量相同
# salary1,bonus1=getStuffFund1(5000,10000,2000)

# 函数参数接收默认值
# 简化重载函数的写法
def getDefaultParm(name="jack",job="manager"):
    return name+" "+job

print(getDefaultParm()) # jack manager
print(getDefaultParm("mary","clerk")) # mary clerk
print(getDefaultParm("mary")) # mary manager

'''
def getDefaultParm1(name,job):
    return name+" "+job
# 错误！
print(getDefaultParm1())
'''

# 接收任意参数
# 1.单个*将所有参数以元组(tuple)的形式导入
def printTuple(*args):
    print(args)

printTuple("01","jack",18,"staff") # ('01', 'jack', 18, 'staff')

# 2.两个*将参数以字典的形式导入
def printDictionary(**args):
    print(args)

printDictionary(id="02",name="michelle",age=18) # {'id': '02', 'name': 'michelle', 'age': 18}

