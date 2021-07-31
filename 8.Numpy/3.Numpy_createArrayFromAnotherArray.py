import numpy as np

# 将列表转换为 ndarray
x = [1, 2, 3]
a = np.asarray(x)
print(x)
print(a)

# 将元组转换为 ndarray
y = (1, 2, 3)
b = np.asarray(y)
print(y)
print(b)

# 将元组列表转换为 ndarray
z = [(1, 2, 3), (4, 5)]
c = np.asarray(z)
print(z)
print(c)
