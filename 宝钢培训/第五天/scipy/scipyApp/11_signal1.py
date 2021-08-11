import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 100)
x = np.sin(t)

x_resampled = signal.resample(x, 25) #使用FFT将信号重采样成n个点

plt.plot(t, x)
plt.plot(t[::4], x_resampled, 'ko') # ko 就是黑色圆点
plt.show()
