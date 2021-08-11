import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# 样本数据
X = np.array([160,165,158,172,159,176,160,162,171])
Y = np.array([58,63,57,65,62,66,58,59,62])

# 偏差函数, 计算以p为参数的直线和原始数据之间的误差
def residuals(p):
    k, b = p
    return Y-(k*X+b)

'''
optimize模块提供了实现最小二乘拟合算法的函数leastsq()
leastsq()使得residuals()的输出数组的平方和最小，参数的初始值为[1, 1]
'''
ret = optimize.leastsq(residuals, [1, 1])
k, b = ret[0]
print("k = ", k, "b = ", b)

#画样本点
plt.figure(figsize=(8, 6)) #指定图像比例： 8：6
plt.scatter(X, Y, color="green", label="Samples", linewidth=2)
#画拟合直线
x = np.linspace(150, 190, 100) #在150-190直接画100个连续点
y = k*x + b #函数式
plt.plot(x,y,color="red", label="Fit",linewidth=2)
plt.legend() #绘制图例
plt.show()