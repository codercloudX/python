import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

'''
函数模型用于生成数据
f(x)=50cos(x)+2
'''
def g(x, a, b):
   return a*np.cos(x) + b

# 产生含噪声的样本数据
x_data = np.linspace(-5, 5, 100) # 采样点
y_data = g(x_data, 50, 2) + 5*np.random.randn(x_data.size) # 加入随机数作为噪声

'''
假设有一批数据样本，要创建这些样本数据的拟合曲线/函数，
可以使用Scipy.optimize模块的curve_fit()函数。
使用curve_fit()函数来估计a和b的值
'''
variables, variables_covariance = optimize.curve_fit(g, x_data, y_data)

# 输出结果
'''
variables是给定模型的最优参数，
variables_covariance可用于检查拟合情况，其对角线元素值表示每个参数的方差。
'''
print('\n求出的系数a, b: ')
print(variables)
print('\nvariables_covariance: ')
print(variables_covariance)
'''
求出的系数a, b: 
[48.97034891  1.60817938]

variables_covariance: 
[[0.7446803  0.1391576 ]
 [0.1391576  0.34923071]]
'''

#画出拟合曲线和样本点位
y = g(x_data, variables[0], variables[1])
plt.plot(x_data, y_data, 'o', color="green", label = "Samples")
plt.plot(x_data, y, color="red", label = "Fit")
plt.legend(loc = "best")
plt.show()