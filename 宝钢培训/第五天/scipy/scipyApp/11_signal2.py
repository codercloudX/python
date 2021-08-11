import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 100)
x = t + np.random.normal(size=100)

x_detrended = signal.detrend(x) #从信号中去除线性趋势

plt.plot(t, x)
plt.plot(t, x_detrended)
plt.show()