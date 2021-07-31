import base.oop.Animal as Animal
import base.oop.IFly as IFly

# 实现多继承
class Bird(Animal.Animal,IFly.IFly):
    __shout="吼叫"
    __nest="筑巢"
    __hatch="孵蛋"

    # 因为鸟的叫声不一样，所以覆盖父类shout的get和set的方法
    def _setShout(self,shout):self.__shout=shout
    def _getShout(self):return self.__shout

    # 生成鸟特有的筑巢和孵蛋get和set方法
    def _setNest(self,nest):self.__nest=nest
    def _getNest(self):return self.__nest

    def _setHatch(self,hatch):self.__hatch=hatch
    def _getHatch(self):return self.__hatch

    # 必须实现IFly父类中的抽象方法
    def _flySpeed(self, speed): return speed


