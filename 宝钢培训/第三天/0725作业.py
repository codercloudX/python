"""
    create by cloud
    2021-07-30
    将对应题目的输出注释取消，即可看到效果
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1.
a1 = np.arange(1, 10).reshape((3, 3))
a2 = np.arange(1, 4)
a3 = a1 + a2
# print(a3)

# 2.
b1 = np.arange(1, 26).reshape((5, 5))
b2 = np.arange(1, 21).reshape((5, 4))
b3 = np.hstack((b1, b2))
# print(b3)

#  3.
#  1.指定刻度范围
# plt.xlim(2.2, 19.2)  # 刻度起始点不在刻度间隔内，所以不显示
# plt.ylim(17, 70)
#  2.指定横纵坐标的题注
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.title('Matplotlib demo')
#  3.指定横纵坐标的刻度
ax = plt.gca()  # 获取坐标轴实例
ax.xaxis.set_major_locator(plt.MultipleLocator(2))  # 把x轴的刻度间隔设置为1，并拥set_major_locator方法进行设置
ax.yaxis.set_major_locator(plt.MultipleLocator(10))
#  4.设置横纵坐标起始点以及步长（ndarray对象）
x = np.arange(3, 20, 1)
y = 3 * x + 11
plt.plot(x, y, '.')
plt.show()


#  4.
idx = np.arange(20, 60, 10)
s = pd.Series(np.array(['aa', 'bb', 'cc', 'dd']), name='cyl', index=idx)
# print(s)

#  5.
dic = dict({"index1": {"one": 10.0, "two": 40},
            "index2": {"one": 20.0, "two": 50},
            "index3": {"one": 30.0, "two": 60},
            "index4": {"one": None, "two": 70}})

# dic2 = dict({"one": {"index1": 10.0, "index2": 20.0, "index3": 30.0, "index4": None},
#              "two": {"index1": 40, "index2": 50, "index3": 60, "index4": 70}})
df = pd.DataFrame(dic).T
# print(df)

