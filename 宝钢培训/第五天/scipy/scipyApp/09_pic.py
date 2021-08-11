from scipy import ndimage
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# 加载图片必须是png
face = mpimg.imread('pic.png')
# 旋转图片
rotate_face = ndimage.rotate(face, 45)
# 处理图片
face1 = ndimage.gaussian_filter(face, sigma=2) #sigma代表模糊度

#plt.imshow(face) #1.显示图片
#plt.imshow(face1) #2.显示模糊图片
#plt.imshow(rotate_face) #3.显示旋转图片
#plt.savefig('save.png') # 保存要显示的图片

im = np.zeros((256, 256))
im[64:-64, 64:-64] = 1
im[90:-90,90:-90] = 2
im = ndimage.gaussian_filter(im, 8)

sx = ndimage.sobel(im, axis = 0, mode = 'constant') #获取x轴边缘
sy = ndimage.sobel(im, axis = 1, mode = 'constant') #获取y轴边缘
sob = np.hypot(sx, sy) #Hypot函数将这两个矩阵合并为一个矩阵

#plt.imshow(im) #4.显示高斯模糊图片
#plt.imshow(sob) #5.显示边缘检测#图片
plt.show()