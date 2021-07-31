import base.oop.Animal as Animal
import base.oop.Cat as Cat
import base.oop.Bird as Bird
import base.oop.HumanBeing as HumanBeing
import base.oop.SuperMan as SuperMan

animal=Animal.Animal() # 调用无参构造函数
print("Animal.py*****************************")
print(animal._getEat())
print(animal._getDrink())
print(animal._getShit())
print(animal._getPiss())
print(animal._getShout())

print("Cat.py*****************************")
cat=Cat.Cat()
cat._setShout("猫喵喵叫")
print(cat._getEat()) # 调用父类方法_getEat()
print(cat._getDrink()) # 调用父类方法_getDrink()
print(cat._getShit()) # 调用父类方法_getShit()
print(cat._getPiss()) # 调用父类方法_getPiss()
print(cat._getShout()) # 调用本类覆盖的方法_getShout()

print("Bird.py*****************************")
bird=Bird.Bird()
bird._setShout("鸟吱吱叫")
bird._setNest("鸟儿筑巢")
bird._setHatch("鸟儿孵蛋")
print(bird._getEat()) # 调用父类方法_getEat()
print(bird._getDrink()) # 调用父类方法_getDrink()
print(bird._getShit()) # 调用父类方法_getShit()
print(bird._getPiss()) # 调用父类方法_getPiss()
print(bird._getShout()) # 调用本类覆盖的方法_getShout()
print(bird._getNest()) # 调用本类新的方法_getNest()
print(bird._getHatch()) # 调用本类新的方法_getHatch()
print(bird._flySpeed(5)) # 设置鸟每秒飞行5米

print("HumanBeing.py*****************************")
humanBeing=HumanBeing.HumanBeing()
humanBeing._setThinking("人类思考")
humanBeing._setEnmotion("人类情感")
humanBeing._setShout("人类歇斯底里地叫喊")
print(humanBeing._getEat()) # 调用父类方法_getEat()
print(humanBeing._getDrink()) # 调用父类方法_getDrink()
print(humanBeing._getShit()) # 调用父类方法_getShit()
print(humanBeing._getPiss()) # 调用父类方法_getPiss()
print(humanBeing._getShout()) # 调用本类覆盖的方法_getShout()
print(humanBeing._getThinking()) # 调用本类新的方法_getThinking()
print(humanBeing._getEnmotion()) # 调用本类新的方法_getEnmotion()

print("SuperMan.py*****************************")
superMan=SuperMan.SuperMan()
superMan._setStopBullet("超人徒手抓飞弹")
print(superMan._getEat()) # 调用父类方法_getEat()
print(superMan._getDrink()) # 调用父类方法_getDrink()
print(superMan._getShit()) # 调用父类方法_getShit()
print(superMan._getPiss()) # 调用父类方法_getPiss()
print(superMan._getShout()) # 调用父类方法_getShout()
print(superMan._getThinking()) # 调用父类方法_getThinking()
print(superMan._getEnmotion()) # 调用父类方法_getEnmotion()
print(superMan._getStopBullet()) # 调用本类新的方法_getStopBullet()
print(superMan._flySpeed(200)) # 设置超人每秒飞行200米

print(superMan.showDetail("老王")) # 调用重载方法def showDetail(self,name,None)
print(superMan.showDetail("老王","捍卫地球")) # 调用重载方法def showDetail(self, name,task)

# 静态方法调用
result=SuperMan.SuperMan.staticMethod(10,25)
print(result)

# 测试多态，函数接收父类
def testPolymorphism(animal:Animal):
    print(animal._getShout())
print("测试多态*****************************")
# 调用函数时根据继承关系降维处理每个子类的个性化结果
testPolymorphism(animal)
testPolymorphism(cat)
testPolymorphism(bird)
testPolymorphism(humanBeing)