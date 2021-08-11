from scipy.optimize import fsolve
from math import sin,cos

'''
方程组求解
4x+9=0
3y^2–sin(yz)=0
yz–2.5=0
'''
def f(x):
    x0 = float(x[0])
    x1 = float(x[1])
    x2 = float(x[2])
    return [
        4*x1 + 9,
        3*x0*x0 - sin(x1*x2),
        x1*x2 - 2.5
    ]
result = fsolve(f, [1,1,1])
print (result)
