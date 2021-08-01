import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.randn(10000)
# data:必选参数，绘图数据
# bins:直方图的长条形数目，可选项，默认为10
# facecolor:长条形的颜色
# edgecolor:长条形边框的颜色
# alpha:透明度
plt.hist(data, bins=40, facecolor="green", edgecolor="black", alpha=0.7)
# 显示横轴标签
plt.xlabel("count")
# 显示纵轴标签
plt.ylabel("Probability")
# 显示图标题
plt.title("gram")
plt.show()
