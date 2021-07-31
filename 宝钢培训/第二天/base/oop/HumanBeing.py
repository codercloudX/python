import base.oop.Animal as Animal

class HumanBeing(Animal.Animal):
    __thinking="思考"
    __enmotion="情感"

    # 生成人特有的思考和情感get和set方法
    def _setThinking(self, thinking): self.__thinking = thinking
    def _getThinking(self): return self.__thinking

    def _setEnmotion(self, enmotion): self.__enmotion = enmotion
    def _getEnmotion(self): return self.__enmotion