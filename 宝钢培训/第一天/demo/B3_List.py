'''序列操作'''
myList = [123, 'abc', 4.56]  # 序列可以包括不同的数据类型
print(len(myList))  # 显示序列长度 3
print(myList[1])  # 显示第2个索引值 abc
myList1 = myList[:-1]  # [123, 'abc']
print(myList1)
myList += [789, 'def']  # 追加新的序列
print(myList)  # [123, 'abc', 4.56, 789, 'def']
# 通过append方法最佳，不能像java一样级联多个append
# 如果要添加多项用myList.extend([789,'def'])
myList.append('append')
print(myList)  # [123, 'abc', 4.56, 789, 'def', 'append']
myList.pop(2)  # 第3项4.56被删除，不加参数默认删除最后一项
print(myList)  # [123, 'abc', 789, 'def', 'append']
myList.insert(1, 666)  # 第二项插入666 [123, 666, 'abc', 789, 'def', 'append']
print(myList)
myList.reverse()  # 反转 ['append', 'def', 789, 'abc', 666, 123]
myList.remove(666)  # 移除666 ['append', 'def', 789, 'abc', 123]
print(myList)
myList[0:2] = ["A", "B"]  # 将前2项修改['A', 'B', 789, 'abc', 123]
print(myList)
del myList[2:]  # 删除第二项后所有的元素['A', 'B']
print(myList)

square = []
for x in [1, 2, 3, 4, 5]:
    square.append(x ** 2)
print(square)
myList2 = ['x', 'n', 'b', 'a']
myList2.sort()  # 升序排序
# myList2.sort(reverse=True) # 降序排序
print(myList2)  # ['a', 'b', 'n', 'x'] 不能直接连在一起写print(myList2.sort()) 否则结果为None
myList2.reverse()  # 翻转排序
print(myList2)
print(myList2[2])  # 打印第3个索引值 b
# print(myList2[10]) # 报错，不存在第10个索引值

'''序列嵌套'''
nestList = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
print(nestList)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nestList[1])  # [4, 5, 6]
print(nestList[1][1])  # 5

'''序列嵌套列操作，更多可以学习NumPy工具包'''
col2 = [col[1] for col in nestList]  # 将nestList竖向第2列赋值给col2,[2, 5, 8]
print(col2)
col2 = [col[1] + 1 for col in nestList]  # 将nestList竖向第2列均加1后赋值给col2,[3, 6, 9]
print(col2)
col2 = [col[1] for col in nestList if col[1] % 2 == 0]  # 将nestList竖向第2列可以整除2的项赋值给col2,[2, 8]
print(col2)
