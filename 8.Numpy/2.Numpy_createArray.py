import numpy as np

# numpy.empty
a = np.empty([2, 3], dtype=int)
print(a)  # 数组元素为随机值，因为它们未初始化

# numpy.zeros
b = np.zeros([2, 3], dtype=int)
print(b)  # 数组元素为0,遇上者相比是已经初始化

# numpy.ones
c = np.ones([2, 3], dtype=int)
print(c)  # 数组元素为1,遇上者相比是已经初始化
