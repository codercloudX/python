import numpy as np

'''
无复制 
简单的赋值不会创建数组对象的副本。相反它使用原始数组的相同id()来访问它。 
id()返回Python对象的通用标识符，类似于C中的指针。
'''
a = np.arange(6)
print('原数组:')
print(a)
print('调用id()函数:')
print(id(a))
print('a赋值给b:')
b = a
print(b)
print('b拥有相同id():')
print(id(b))
print('修改b的形状:')
b.shape = 3,2
print(b)
print('a的形状也发生修改:')
print(a)
print('-----------------------------------------------------')
'''
原数组:
[0 1 2 3 4 5]
调用id()函数:
2058598872608
a赋值给b:
[0 1 2 3 4 5]
b拥有相同id():
2058598872608
修改b的形状:
[[0 1]
 [2 3]
 [4 5]]
a的形状也发生修改:
[[0 1]
 [2 3]
 [4 5]]
'''

'''
视图或浅拷贝 
ndarray.view()方会创建一个新的数组对象，该方法创建的新数组的维数更改不会更改原始数据的维数。
'''
a = np.arange(6).reshape(3,2)
print('数组a:')
print(a)
print('创建a的视图:')
b = a.view()
print(b)
print('两个数组的id()不同:')
print('a的id():')
print(id(a))
print('b的id():')
print(id(b))
# 修改b的形状，并不会修改a
b.shape = 2,3
print ('b的形状:')
print (b)
print ('a的形状:')
print (a)
print('-----------------------------------------------------')
'''
数组a:
[[0 1]
 [2 3]
 [4 5]]
创建a的视图:
[[0 1]
 [2 3]
 [4 5]]
两个数组的id()不同:
a的id():
2401323705808
b的id():
2401323419648
b的形状:
[[0 1 2]
 [3 4 5]]
a的形状:
[[0 1]
 [2 3]
 [4 5]]
'''

'''
使用切片创建视图修改数据会影响到原始数组
变量a,b都是arr的一部分视图，对视图的修改会直接反映到原数据中。但是a,b的id不同，视图虽然指向原数据，但是他们和赋值引用还是有区别的。
'''
arr = np.arange(12)
print('原数组:')
print(arr)
print ('创建切片:')
a=arr[3:]
b=arr[3:]
a[1]=123
b[2]=234
print(arr)
print(id(a),id(b),id(arr[3:]))
print('-----------------------------------------------------')
'''
原数组:
[ 0 1 2 3 4 5 6 7 8 9 10 11]
创建切片:
                 a修改 b修改
[0   1   2   3   123   234   6   7   8   9   10   11]
a的id         b的id         arr[3:]的id
2274567028864 2274566338080 2274566338560
'''

'''
副本或深拷贝 
ndarray.copy()函数创建一个副本。对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。
'''
a = np.array([[10,10],
              [2,3],
              [4,5]])
print('数组a:')
print(a)
print('创建a的深层副本:')
b = a.copy()
print('数组b:')
print(b)
# b与a不共享任何内容
print('能够通过写入b来写入a吗?')
print (b is a)
print ('修改b的内容:')
b[0,0] = 100
print('修改后的数组b:')
print(b)
print('a保持不变:')
print(a)
print('-----------------------------------------------------')
'''
数组a:
[[10 10]
 [ 2  3]
 [ 4  5]]
创建a的深层副本:
数组b:
[[10 10]
 [ 2  3]
 [ 4  5]]
能够通过写入b来写入a吗?
False
修改b的内容:
修改后的数组b:
[[100  10]
 [  2   3]
 [  4   5]]
a保持不变:
[[10 10]
 [ 2  3]
 [ 4  5]]
'''