import sys

'''共享引用'''
a=3
b=a # b通过a被赋值=3后，a的值后续发生任何改动也不会影响b已经被赋予的值
a+=1
print("a="+str(a)+" b="+str(b)) # a=4 b=3

# 共享引用的对象内部发生修改则变量全部发生修改，因为它们都同时指向了这个对象
list1=[2,3,4]
list2=list1
list1[0]=22
print("list1="+str(list1)+" list2="+str(list2)) # list1=[22, 3, 4] list2=[22, 3, 4]

# 共享引用比较
a=3
b=a
print(a==b) # True 值相等
print(a is b) # True 数字和字符串可以被缓存复用，所以python认为a和b是同一个对象

print(list1==list2) # True
print(list1 is list2) # True
list1=[2,3,4]
list2=[2,3,4]
print(list1==list2) # True list1和list2值相等
'''
但list1和list2是2个对象，
我们认为list1占用的内存中的数据是[2,3,4]
list2占用的内存中的数据也是[2,3,4]
但list1和list2的内存地址是不一样的
'''
print(list1 is list2) # False

print(sys.getrefcount(3)) # 查询整数3被重复引用的次数