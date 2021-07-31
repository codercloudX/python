# 1.字典的定义
xiaoming = {
                "name": "小明",
                "age": 18,
                "gender": True,
                "height": 1.75,
                "weight": 75.5
            }
lisi={
        "name": "李四",
        "qq": "54321",
        "phone": "10086"
     }
print(xiaoming)
print()

# 2.字典的基本使用
print(xiaoming["name"])
xiaoming["sex"]="男"#如果没有该键，则新增，如果有则修改
xiaoming.pop("name")#如果没有该键值，则会报错
print(xiaoming)
print()

# 3.字典的其他操作
print(len(xiaoming))# 计算字典键值对数量
temp={
        "height": 1.75,
        "age": 20,
        "name":"cyl"
     }
xiaoming.update(temp)#合并键值对，如果键相同则会覆盖
print(xiaoming)
#xiaoming.clear()# 3. 清空字典
print()

# 4.字典的应用场景
# 使用 多个键值对，存储 描述一个 物体 的相关信息 —— 描述更复杂的数据信息
# 将 多个字典 放在 一个列表 中，再进行遍历
card_list = [
    xiaoming,
    lisi
]

for card_info in card_list:
    print(card_info)













