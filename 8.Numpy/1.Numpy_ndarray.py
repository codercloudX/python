import numpy as np

a = np.arange(24)
c = a.reshape(2,4,3)
b = np.array([[1, 2, 3], [3, 4, 5]])
# c = np.array([1, 2, 3, 4, 5], ndmin =2)
# d = [1,2,3]
print(range(10))
print(a)
print(b)
print(c)
print("返回维度:"+str(b.ndim))  # 返回维数，等于秩
print("返回几行几列:"+str(b.shape))  # 返回维度，
print("返回数组元素总个数:"+str(b.size))  # 返回数组元素总个数
print("返回对象的元素类型:"+str(b.dtype)) #返回对象的元素类型
print("返回对象的每个元素大小:"+str(b.dtype)) #返回对象的每个元素大小
print("返回对象的内存信息:\n"+str(b.flags)) #返回对象的内存信息
print("返回ndarray元素的实部:\n"+str(b.real)) #返回ndarray元素的实部
print("返回ndarray元素的虚部:\n"+str(b.imag)) #返回ndarray元素的虚部

