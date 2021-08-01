import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits import mplot3d

sd = plt.axes(projection='3d')

# 用sd.plot3D绘制线图，用sd.scatter3D绘制散点图
z_line = np.linspace(0, 15, 1000)
x_line = np.sin(z_line)
y_line = np.cos(z_line)
sd.plot3D(x_line, y_line, z_line, 'red')  # 绘制线图
plt.show()
