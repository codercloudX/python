# 1.列表的基本使用
name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list)# 1.1 输出 该列表的所有元素
print(name_list.index("wangwu"))# 1.2 知道数据的内容，想确定数据在列表中的位置。如果传递的数据不在列表中，程序会报错！
name_list[1]="李四"# 1.3 修改
name_list.append("cyl")# 1.4 增加
name_list.insert(1,"chb")# 1.5 插入
name_list.extend(["qhn","pxb"])# 1.6 将其他列表的元素追加到末尾
# 删除指定元素时，若没有该元素则会报错
name_list.remove("qhn")# 1.7 删除指定数据
name_list.pop()# 1.8 删除最后一位
name_list.pop(2)# 1.9 删除指定位
name_list.clear()# 1.10 清空列表
print(id(name_list))
print()

# 2.del关键字
# 要从列表删除数据，建议使用列表提供的方法
# del 关键字本质上是用来将一个变量从内存中删除的
name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list)
del name_list[1]
print()

# name = "小明"
# del name
# print(name)# 报错

# 3.列表的数据统计
name_list = ["zhangsan", "lisi", "wangwu","zhangsan"]
print("列表中包含 %d 个元素" % len(name_list))# 3.1 len(length 长度) 函数可以统计列表中元素的总数
print("zhangsan出现了 %d 次" % name_list.count("zhangsan"))# 3.2 count 方法可以统计列表中某一个数据出现的次数
print()

# 4. 列表排序
num_list = [6, 8, 4, 1, 10]
# 4.1 升序
num_list.sort()
print(num_list)
# 4.2 降序
num_list.reverse()
print(num_list)
print()

# 5. 列表遍历
num_list = [6, 8, 4, 1, 10]
num_list.sort()
for num in num_list:
    print("*"*num)
print()