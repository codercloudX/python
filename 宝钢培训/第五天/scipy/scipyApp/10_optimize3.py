import numpy as np
from scipy import optimize

# 定义函数
def g(x):
  return x**2 + 20*np.sin(x)

# 求取最小值，初始值为7
'''
basinhopping()方法把局部优化方法与起始点随机抽样相结合，求出全局最小值，
代价是耗费更多计算资源
'''
ret = optimize.basinhopping(g, 7)
print(ret)
#fun: 0.15825752683178962，x: array([4.27109533])