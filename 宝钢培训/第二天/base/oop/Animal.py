class Animal:
    '''
    1.变量开头有2个下划线为私有变量，只有自己可以调用
    2.变量开头有1个下划线为保护变量，只有继承关系的类可以调用
    函数方法的作用域也是如此
    '''
    __eat="进食"
    __drink="喝水"
    __shit="拉屎"
    __piss="撒尿"
    __shout="吼叫"

    # python的构造函数不能重载[函数名称相同而参数个数不同]
    def __init__(self):pass

    '''
    为继承类访问父类的私有变量设置set和get的方法
    '''
    def _setEat(self,eat):self.__eat=eat
    def _getEat(self):return self.__eat

    def _setDrink(self,drink):self.__drink=drink
    def _getDrink(self):return self.__drink

    def _setShit(self,shit):self.__shit=shit
    def _getShit(self):return self.__shit

    def _setPiss(self,piss):self.__piss=piss
    def _getPiss(self):return self.__piss

    def _setShout(self,shout):self.__shout=shout
    def _getShout(self):return self.__shout