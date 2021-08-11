import numpy as np
#从fftpack中导入fft(快速傅里叶变化)和ifft(快速傅里叶逆变换)函数
from scipy.fftpack import fft,ifft

#创建一个随机值数组
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])
#对数组数据进行傅里叶变换
y = fft(x)
print('fft: ')
print(y)
print('\n')
#快速傅里叶逆变换
yinv = ifft(y)
print('ifft: ')
print(yinv)
print('\n')

'''
在离散傅里叶变换中，频域信号由一系列不同频率的谐波（频率成倍数）组成。
fft返回值是一个复数数组，每个复数表示一个正弦波。
通常一个波形由振幅，相位，频率三个变量确定，可以从fft的返回值里，获取这些信息。
'''
# 采样点数
N = 4000
# 采样频率 (根据采样定理，采样频率必须大于信号最高频率的2倍，信号才不会失真)
Fs = 8000
x = np.linspace(0.0, N/Fs, N)
# 时域信号，包含：直流分量振幅1.0，正弦波分量频率100hz/振幅2.0, 正弦波分量频率150Hz/振幅0.5/相位np.pi
y = 1.0 + 2.0 * np.sin(100.0 * 2.0*np.pi*x) + 0.5*np.sin(150.0 * 2.0*np.pi*x + np.pi)
# 进行fft变换
yf = fft(y)
# 获取振幅，取复数的绝对值，即复数的模
abs_yf = np.abs(yf)
# 获取相位，取复数的角度
angle_y=np.angle(yf)
# 直流信号
print('\n直流信号')
print('振幅:', abs_yf[0]/N) # 直流分量的振幅放大了N倍
# 100hz信号
index_100hz = 100 * N // Fs # 波形的频率 = i * Fs / N，倒推计算索引：i = 波形频率 * N / Fs
print('\n100hz波形')
print('振幅:', abs_yf[index_100hz] * 2.0/N) # 弦波分量的振幅放大了N/2倍
print('相位:', angle_y[index_100hz])
# 150hz信号
index_150hz = 150 * N // Fs # 波形的频率 = i * Fs / N，倒推计算索引：i = 波形频率 * N / Fs
print('\n150hz波形')
print('振幅:', abs_yf[index_150hz] * 2.0/N) # 弦波分量的振幅放大了N/2倍
print('相位:', angle_y[index_150hz])
print('100hz与150hz相位差:',  angle_y[index_150hz] - angle_y[index_100hz])
print('\n')
'''
直流信号
振幅: 1.0

100hz波形
振幅: 1.9989359813189005
相位: -1.5315264186250062

150hz波形
振幅: 0.5008489983048181
相位: 1.6297011890497095
100hz与150hz相位差: 3.1612276076747157
'''

'''
SciPy.fftpack中，提供了离散余弦变换(DCT)与离散余弦逆变换(IDCT)的实现。
'''
from scipy.fftpack import dct,idct

arr=np.array([4., 3., 5., 10., 5., 3.])
print('离散余弦变换(DCT)')
print(dct(arr))
print('离散余弦逆变换(IDCT)')
print(idct(arr))
