import cv2
import numpy as np

#加噪函数
def addSaltNoise(img):
    print(img.ndim)#img.ndim是图片的色彩通道数，可以用来判断是不是灰度图
    #add Salt Noise
    for k in range(0,1000):
        #随机生成一点的横,纵坐标
        xi = int(np.random.uniform(0,img.shape[1]))
        xj = int(np.random.uniform(0,img.shape[0]))
        
        if img.ndim == 2:
            img[xj,xi] = 255
        elif img.ndim == 3:
            img[xj,xi,0] = 25
            img[xj,xi,1] = 20
            img[xj,xi,2] = 20
    return img