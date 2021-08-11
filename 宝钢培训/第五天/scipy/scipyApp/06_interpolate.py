import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate as intp
from scipy.interpolate import UnivariateSpline

'''
例1:
interp1d类可以根据输入的点，创建拟合函数
'''
x = np.linspace(0, 4, 12)
y = np.cos(x**2/3 + 4)
print (x)
print (y)
plt.plot(x, y,'o')
#plt.show()

'''
kind表示插值使用的技术类型:
Linear
Nearest 
Zero
Slinear 
Quadratic 
Cubic
'''
f1 = intp.interp1d(x, y, kind = 'linear')
f2 = intp.interp1d(x, y, kind = 'cubic')
xnew = np.linspace(0, 4, 30)
plt.plot(x, y,'o')
plt.plot(xnew, f1(xnew), '-')
plt.plot(xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')
plt.show()

'''
例2:
噪声数据插值
'''
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50) # 通过random方法添加噪声数据
plt.plot(x, y, 'ro', ms=5) #ms为markersize,ro为red circle marker
# 平滑参数使用默认值
spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'b', lw=3) # 蓝色曲线,lw为linewidth
# 设置平滑参数
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'g', lw=3) # 绿色曲线
# 设置平滑参数为0不去除噪声
spl.set_smoothing_factor(0)
plt.plot(xs, spl(xs), 'yellow', lw=3) # 黄色曲线
plt.show()