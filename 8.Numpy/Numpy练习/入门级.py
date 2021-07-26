import numpy as np

# 1.切片和棋盘矩阵
a = np.zeros((8, 8), dtype=int)
a[0:6:, 0:6:2] = 1
print("1.")
print(a)

# 2.min()、max()函数
b = np.random.random((3, 2))
bMax, bMin = b.max(), b.min()
print("2.")
print(bMax)
print(bMin)

# 3.函数tile(A,reps),reps即重复的次数，不仅可以是数字，还可以是array。比如构造棋盘矩阵
c = np.tile(np.array([[0, 1], [0, 1]]), (4, 4))
print('3.')
print(c)
