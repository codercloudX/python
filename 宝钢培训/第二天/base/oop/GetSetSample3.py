class GetSetSample3:
    # python的构造函数不能重载[函数名称相同而参数个数不同]
    def __init__(self):pass

    # 注解设置变量属性
    # @property等同于get方法，外部类直接调用.eat即可获取__eat值
    # @property必须声明在@setter之前，否则setter会报错
    @property
    def eat(self): return self.__eat
    @eat.setter
    def eat(self, eat): self.__eat = eat

gss=GetSetSample3()
'''
没有
@eat.setter
def eat(self, eat): self.__eat = eat
的话
gss.eat="吃"报错
'''
gss.eat="吃"
print(gss.eat)