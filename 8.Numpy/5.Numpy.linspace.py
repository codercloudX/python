import numpy as np

# numpy.arange(start, stop, step, dtype)
# 根据 start 与 stop 指定的范围以及 step 设定的步长，生成一个 ndarray
a = np.arange(1, 5)
print(a)

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# 创建一个一维数组，数组是一个等差数列构成的
# start	序列的起始值
# stop	序列的终止值，如果endpoint为true，该值包含于数列中
# num	要生成的等步长的样本数量，默认为50
# endpoint	该值为 true 时，数列中包含stop值，反之不包含，默认是True。
# retstep	如果为 True 时，生成的数组中会显示间距，反之不显示。
# dtype	ndarray 的数据类型
b = np.linspace(1, 10, 10)
print(b)

# numpy.logspace
# np.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# start	序列的起始值为：base ** start
# stop	序列的终止值为：base ** stop。如果endpoint为true，该值包含于数列中
# num	要生成的等步长的样本数量，默认为50
# endpoint	该值为 true 时，数列中中包含stop值，反之不包含，默认是True。
# base	对数 log 的底数。
# dtype	ndarray 的数据类型
# base 参数意思是取对数的时候 log 的下标
c = np.logspace(1.0, 2.0, num=10)
print(c)
