from typing import Any

class GetSetSample2:
    eat="默认值"

    # python的构造函数不能重载[函数名称相同而参数个数不同]
    def __init__(self):pass

    '''
    为继承类访问父类的私有变量设置set和get的方法
    '''
    # 通过Generate->Override Methods生成
    # 比如不存在getEat和setEat的方法，那么调用内置函数__getattribute__和__setattr__尝试
    def __setattr__(self, name: str, value: Any) -> None:
        print("当变量不存set方法时使用setattr设置变量值")
        self.__dict__[name]=value

    def __getattr__(self, name):
        print("当变量不存在时使用getattr获取返回值")
        name="调用getattr获取吃的方法"
        return name

gss=GetSetSample2()
# __setattr__测试
gss.eat="GetSetSample2吃"

# __getattr__测试
# 注释 eat="默认值"后测试
print(gss.eat)