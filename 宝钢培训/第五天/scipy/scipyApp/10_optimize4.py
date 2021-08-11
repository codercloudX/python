import numpy as np
from scipy import optimize

# 定义函数
def g(x):
  return x**2 + 20*np.sin(x)

'''
要求取一定范围之内的函数最小值，可使用fminbound方法
求取-10到-5之间的函数最小值。full_output=True表示返回详细信息。
'''
ret = optimize.fminbound(g, -10, -5, full_output=True)
print(ret)
'''
函数最小值是：35.82273589215206，对应的x值：-7.068891380019064
(-7.068891380019064, 35.82273589215205, 0, 12)
'''