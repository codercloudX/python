from abc import ABCMeta,abstractmethod

class IFly:
    # 抽象方法无实体，子类必须继承实现
    # 飞行速度
    @abstractmethod
    def _flySpeed(self,speed):pass