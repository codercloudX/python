def getListValue(myList,index): return myList[index]

# 1.exception常用格式，一般抛出系统异常
def catchListSafety():
    try:
        print(getListValue(myList,4))
    except IndexError:
        print("index out of bound!")
    except NameError: pass
    except KeyError: pass
    # 多种异常合并处理
    except (AttributeError,TypeError,SyntaxError): pass
    else: # 如果没有发生异常时做的动作
        print("get the list value!")
    # 始终会做finally
    finally: print("release memory!!")
    print("do the next action...")

myList=[123,'abc',4.56]
# 直接调用边界越界
# getListValue(myList,3)
catchListSafety()

# try/except/else/finally可以内部嵌套

x=80
y=200
print("x="+str(x))
# 2.exception抛出错误，一般抛出逻辑异常
if x>90:
    # 抛出错误，后面语句全部不被执行
    raise Exception("x必须小于90")
else:print("y="+str(y))

# 3.exception自定义错误，一般也用于逻辑异常
# 变成错误字典？
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        # repr函数:返回一个对象的string格式
        return repr(self.value)

try:
    raise MyError(4*2)
except MyError as e:
    print('My exception occurred, value=', e.value)

# 4.assert断言触发，后面语句全部不被执行
assert 1>2,"assert occurred"
print("finish")