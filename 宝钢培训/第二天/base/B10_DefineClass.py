'''用户定义类'''
class Worker:
    def __init__(self,name,salary): # 定义类的属性
        self.name=name
        self.salary=salary
    # 定义类的方法
    # 无参方法
    def getDetails(self): return "details="+self.name+" "+str(self.salary)
    # 有参方法
    def getBonus(self,basePay): return self.salary+basePay
jack=Worker("jack",5000)
# str()和repr()都可以转换成字符串
print(jack)
print(jack.name+' '+str(jack.salary)) # jack 5000
print(jack.getDetails()) # details=jack 5000
print(jack.getBonus(800)) # 5800