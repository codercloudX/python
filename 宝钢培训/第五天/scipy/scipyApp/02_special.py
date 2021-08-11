#立方根函数
from scipy.special import cbrt
res = cbrt([10, 9, 0.1254, 234])
print(res)

#指数函数
from scipy.special import exp10
res = exp10([2,9])
print(res)

'''
相对误差指数函数(exp(x) -  1)/x
当 x 接近零时，exp(x)接近1，所以exp(x)-1的数值计算可能会遭受灾难性的精度损失.
然后实现exprel(x)以避免精度损失，这在 x 接近零时发生.
'''
from scipy.special import exprel
res = exprel([-0.25, -0.1, 0, 0.1, 0.25])
print(res)

'''
对数和指数函数
计算输入元素的指数之和的对数
'''
from scipy.special import logsumexp
import numpy as np
a = np.arange(10)
res = logsumexp(a)
print(res)