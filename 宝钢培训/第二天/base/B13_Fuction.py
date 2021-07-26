# 定义乘法函数结构
def times(x,y):
    return x*y

print(times(10,12)) # def

# 定义获取2个序列交集的函数
def intersect(list1,list2):
    resultList=[]
    for tmp in list1:
        if tmp in list2:
            resultList.append(tmp)
    return resultList

list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
print(intersect(list1,list2)) # [3, 4, 5]

# intersect函数多态，因为python并不指定参数类型
tuple=(3,4,5,6,7)
print(intersect(list1,tuple)) # [3, 4, 5]