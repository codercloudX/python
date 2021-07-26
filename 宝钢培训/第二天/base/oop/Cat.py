import base.oop.Animal as Animal

# 实现继承关系(Animal.Animal)
class Cat(Animal.Animal):
    __shout = "吼叫"

    # 因为猫的叫声不一样，所以覆盖父类shout的get和set的方法
    def _setShout(self,shout):self.__shout=shout
    def _getShout(self):return self.__shout

