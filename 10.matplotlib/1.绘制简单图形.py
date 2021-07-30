import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#  1.plt.plot(x, y, format_string)
# plt.axis([0, 8, 0, 16])  # 设定横坐标起始 以及 纵坐标起始
# a = np.arange(0., 8., 0.2)  # 创建一个从0到8，步长为0.2的等差数组
# plt.plot(a, a, 'g:', a, a ** 2, 'b-', a, a ** 3, 'rv')  # 分别绘制y=x,y=x^2,y=x^3的三条线段
# plt.plot([1, 2, 3, 4, ], [5, 6, 7, 8], 'g|')


#  2.plt.subplot(1,  2,  1)
x = np.linspace(-np.pi, np.pi)
x1 = np.sin(x)
x2 = np.cos(x)
# 绘制第一个图像
plt.subplot(1, 2, 1)  # 建立 subplot 网格，长为 1，宽为 2
plt.plot(x, x1)
plt.title('Sin(x)')  # 对第一个图像命名
# 绘制第二个图像
plt.subplot(1, 2, 2)  # 建立第二个 subplot 网格，长为 1，宽为 2
plt.plot(x, x2)
plt.title('Cos(x)')  # 对第二个图像命名

plt.show()
