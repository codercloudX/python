import numpy as np
from scipy import optimize

# 定义函数
def g(x):
  return x**2 + 20*np.sin(x)

# 单方程求解
ret = optimize.fsolve(g, 4)
print(ret)