import scipy.io as sio
import numpy as np

# 保存mat文件
vect = np.arange(20)
sio.savemat('array.mat', {'vect':vect})

# 加载文件
mat_file_content = sio.loadmat('array.mat')
print (mat_file_content)

mat_file_content = sio.whosmat('array.mat')#在不加载文件的情况下，查看文件中的概要内容
print (mat_file_content)