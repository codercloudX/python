class GetSetSample1:
    '''
        1.变量开头有2个下划线为私有变量，只有自己可以调用
        2.变量开头有1个下划线为保护变量，只有继承关系的类可以调用
        函数方法的作用域也是如此
    '''
    __eat="进食"

    # python的构造函数不能重载[函数名称相同而参数个数不同]
    def __init__(self,eat):self.__eat=eat

    '''
    为继承类访问父类的私有变量设置set和get的方法
    '''
    def setEat(self,eat):self.__eat=eat
    def getEat(self):return self.__eat

gss=GetSetSample1("GetSetSample1吃")
print(gss.getEat())