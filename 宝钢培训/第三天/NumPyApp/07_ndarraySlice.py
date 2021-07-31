import numpy as np

a1 = np.arange(10)
print(a1)
s = slice(2,7,2)  # 从索引2开始到索引7停止,间隔为2
print('a1数组:')
print(a1[s])
'''
a1数组:
[2 4 6]
'''
print('-----------------------------------------------------')
#也可以通过冒号分隔切片参数start:stop:step来进行切片操作
a2 = a1[2:7:2]
print('a2数组:')
print(a2)
'''
a2数组:
[2 4 6]
'''
print('-----------------------------------------------------')
'''
冒号 : 的解释：如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。
如果为 [2:]，表示从该索引开始以后的所有项都将被提取。如果使用了两个参数，
如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。
'''
a3 = a1[5]
print('a3数组:')
print(a3)
'''
a3数组:
5
'''
print('-----------------------------------------------------')
a4=a1[6:]
print('a4数组:')
print(a4)
'''
a4数组:
[6 7 8 9]
'''
print('-----------------------------------------------------')
a5=a1[4:8]
print('a5数组:')
print(a5)
'''
a5数组:
[4 5 6 7]
'''
print('-----------------------------------------------------')
a6 = np.array([[1,2,3],
               [3,4,5],
               [4,5,6]])
print('a6数组:')
print(a6)
#从索引处开始切割
print('a7从数组索引 a[1:] 处开始切割')
a7=a6[1:]
print(a7)
'''
[[1 2 3]
 [3 4 5]
 [4 5 6]]
a7从数组索引 a[1:] 处开始切割
[[3 4 5]
 [4 5 6]]
'''
print('-----------------------------------------------------')
'''
切片还可以包括省略号…,来使选择元组的长度与数组的维度相同
如果在行位置使用省略号，它将返回包含行中元素的ndarray
'''
print('a6数组:')
print(a6)
print('a6数组第2列:')
print(a6[...,1])#第2列元素
print('a6数组第2行:')
print(a6[1,...]) #第2行元素
print('a6数组第2列及剩下的所有元素:')
print(a6[...,1:])#第2列及剩下的所有元素
'''
a6数组:
[[1 2 3]
 [3 4 5]
 [4 5 6]]
a6数组第2列:
[2 4 5]
a6数组第2行:
[3 4 5]
a6数组第2列及剩下的所有元素:
[[2 3]
 [4 5]
 [5 6]]
'''