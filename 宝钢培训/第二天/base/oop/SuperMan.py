# 就近继承而不是继承动物
import base.oop.HumanBeing as HumanBeing
import base.oop.IFly as IFly

class SuperMan(HumanBeing.HumanBeing,IFly.IFly):
    __stopBullet="空手抓子弹"

    def _setStopBullet(self,stopBullet):self.__stopBullet=stopBullet
    def _getStopBullet(self):return self.__stopBullet

    # 重载方法，task参数是否存在决定不同的返回
    # 不能像java一样写重载多个相同的方法名而参数不同
    '''
    如果想实现几个参数类型不同的情况如下面所示
    def showDetail(a, b): XXX
    showDetail(1, 1.0) # a=1 b=1.0
    showDetail(1.0, 1) # a=1.0 b=1
    if type(a) == int and type(b) == float:
        pass
    elif type(a) == float and type(b) == int:
        pass
    '''
    # 参数数量不同时的处理方法
    def showDetail(self,name, task=None):
        tmp=""
        if task is None:
            tmp="超人的名字叫" + name
        else:
            tmp="超人的名字叫" + name + ",责任要" + task
        return tmp

    # 静态方法 可以以类名直接调用，无需引用实例
    @staticmethod
    def staticMethod(x,y):return x+y

    # 必须实现IFly父类中的抽象方法,全部覆盖，不能只覆盖一部分
    def _flySpeed(self, speed): return speed

    # 封装 对外暴露简单的参数入口，内部实现复杂的逻辑
    def caleFebLastDay(self,year):
        # 计算闰年判断逻辑
        pass

