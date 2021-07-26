import numpy as np

# 输出np版本号
print(np.__version__)

# 2.zeros构建零矩阵
z = np.zeros((2, 3))
print(z)

# 3.上面的零向量的第二行第三列元素置为1
z[1, 2] = 1
print(z)

# 4.arange函数，创建一个在给定范围的向量
a = np.arange(0, 100)
print(a)

# 5.reshape函数，将array变形为矩阵
b = np.arange(6)
b = b.reshape(3, 2)
print(b * np.ones((3, 2)))

# 6.nonzero函数，寻找非0元素的下标
c = np.nonzero([0, 0, 0, 1, 2, 3, 4])
print(c)

# 7.eye函数，生成单位向量
d = np.eye(3)
print(d)

# 8.diag函数，diagonal对角线。
e = np.diag([1, 2, 3, 4], k=2)
print(e)

# 9.random模块的random函数，生成随机数
f = np.random.random((3, 2))
print(f)
