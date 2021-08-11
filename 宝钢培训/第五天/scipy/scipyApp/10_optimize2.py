import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# 定义函数,该函数有多个局部最小值
def g(x):
  return x**2 + 20*np.sin(x)

# x取值：-10到10之间，间隔0.1
x = np.arange(-10, 10, 0.1)
# 画出函数曲线
plt.plot(x, g(x))

#xopt = optimize.fmin_bfgs(g, 7) #返回7附近的局部最小值
xopt = optimize.fmin_bfgs(g, 0) #返回全局最小值
xmin = xopt[0] # x值
ymin = g(xmin) # y值，即函数最小值
print('xmin: ', xmin)
print('ymin: ', ymin)

# 画出最小值的点, s=20设置点的大小，c='r'设置点的颜色
plt.scatter(xmin, ymin, s=20, c='r')
plt.show()
