import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

'''
例1:
使用BFGS函数，找出抛物线函数的最小值
'''
# 定义函数
def f(x):
  return x**2 + 2*x + 9

# x取值：-10到10之间，间隔0.1
x = np.arange(-10, 10, 0.1)
# 画出函数曲线
plt.plot(x, f(x))

'''
计算该函数最小值的有效方法之一是使用带起点的BFGS算法。
该算法从参数给定的起始点计算函数的梯度下降，并输出梯度为零、二阶导数为正的极小值。
'''
# 第一个参数是函数名，第二个参数是梯度下降的起点。返回值是函数最小值的x值(ndarray数组)
xopt = optimize.fmin_bfgs(f, 0)
xmin = xopt[0] # x值
ymin = f(xmin) # y值，即函数最小值
print('xmin: ', xmin)
print('ymin: ', ymin)

# 画出最小值的点, s=20设置点的大小，c='r'设置点的颜色
plt.scatter(xmin, ymin, s=20, c='r')
plt.show()
'''
Optimization terminated successfully.
         Current function value: 8.000000
         Iterations: 2
         Function evaluations: 9
         Gradient evaluations: 3
xmin:  -1.00000000944232
ymin:  8.0
'''

