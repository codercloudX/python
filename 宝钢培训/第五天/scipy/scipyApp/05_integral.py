import scipy.integrate
from numpy import exp
from math import sqrt

#一重积分例1：求0到5范围内的积分
f = lambda x:exp(-x**2)
i = scipy.integrate.quad(f, 0, 5)
print(i)
'''
(0.8862269254513955, 2.3183115159980698e-14)
quad函数返回两个值，第一个值是积分的值，第二个值是对积分值的绝对误差估计。
'''

#一重积分例2：带参数
def f(x, a, b):
    return a * (x ** 2) + b

ret = scipy.integrate.quad(f, 0, 1, args=(3, 1))
print (ret)
#(2.0, 2.220446049250313e-14)

#二重积分
f = lambda x, y : 19*x*y
g = lambda x : 0
h = lambda y : sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print (i)
