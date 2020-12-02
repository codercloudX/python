# 1.元组基本使用
info_tuple = ("zhangsan", 18, 1.75, "zhangsan")
print(info_tuple[0])# 6.1 取值和取索引
print(info_tuple.index("zhangsan"))# 6.2 已经知道数据的内容，希望知道该数据在元组中的索引
print(info_tuple.count("zhangsan"))# 6.3统计出现次数
print(len(info_tuple))# 6.4 统计元组长度
print()

# 2.元组遍历
for i in info_tuple:
    print(i)

# 3.元组格式化字符串
info_tuple = ("小明", 21, 1.85)
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)
print()

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
print()