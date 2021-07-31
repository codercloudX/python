import datetime
'''
在实践中, "from module import *" 不是良好的编程风格，
如果使用from导入变量，且那些变量碰巧和作用域中现有变量同名，那么变量名就会被悄悄覆盖掉。
使用import语句的时候就不会发生这种问题，因为是通过模块名才获取的变量名，像module.attr不会和现有作用域的attr冲突。
'''
# from attr import class # 直接引入class类中的attr属性
# 比如 from datetime import datetime

'''字典，就是json格式'''
# 如果采用from datetime import datetime
# birthday=datetime.strptime("1929-05-04","%Y-%m-%d").date()
birthday=datetime.datetime.strptime("1995-02-01","%Y-%m-%d").date()
stuffDict={
        "name":"jack",
        "jobPosition":"manager",
        "birthday":birthday}
print(stuffDict) # {'name': 'jack', 'jobPosition': 'manager', 'birthday': datetime.date(1995, 2, 1)}
print(stuffDict["jobPosition"]) # manager
print(stuffDict["birthday"]) # 1995-02-01
stuffDict["jobPosition"]="CEO" # 修改字典属性值
print(stuffDict["jobPosition"]) # CEO
stuffDict=sorted(stuffDict) # 根据key排序
print("stuffDict sorted=")
print(stuffDict) # ['birthday', 'jobPosition', 'name']

# 字典单属性设置
clerkDict={} # 创建空字典
clerkDict["id"]="01"
clerkDict["type"]="clerk"
clerkDict["salary"]=5000
print(clerkDict)
print(clerkDict["type"]) # 等同于clerkDict.get("type")
print(clerkDict.keys()) # dict_keys(['id', 'type', 'salary'])
print(clerkDict.values()) # dict_values(['01', 'clerk', 5000])
print(clerkDict.items()) # dict_items([('id', '01'), ('type', 'clerk'), ('salary', 5000)])
clerkDict.update({"mobile":"18930964799","city":"shanghai"}) # 追加新项合并到clerkDict
print(clerkDict) # {'id': '01', 'type': 'clerk', 'salary': 5000, 'mobile': '18930964799', 'city': 'shanghai'}
clerkDict.pop("city") # 删除city项
print(clerkDict) # {'id': '01', 'type': 'clerk', 'salary': 5000, 'mobile': '18930964799'}

# 通配符在字典中使用
print("工号%(id)s，职位类型%(type)s,工资%(salary)d" % clerkDict) # 工号01，职位类型clerk,工资5000

print(len(clerkDict)) # 获取字典长度 3
otherDict=clerkDict.fromkeys(["type","salary"]) # 用type和salary作为键值构造新的字典
print(otherDict) # {'type': None, 'salary': None}

# 字典嵌套
birthday=datetime.datetime.strptime("1929-05-04","%Y-%m-%d").date()
person={"name":{"firstName":"Audrey","lastName":"Hepburn"},
        "three_dimensional":{" chest":"88","waist":"20"," hip":"89"},
        "birthday":birthday}
# {'name': {'firstName': 'Audrey', 'lastName': 'Hepburn'},
# 'three_dimensional': {' chest': '88', 'waist': '20', ' hip': '89'},
# 'birthday': datetime.date(1929, 5, 4)}
print(person)
print(person["three_dimensional"]["waist"]) # 20