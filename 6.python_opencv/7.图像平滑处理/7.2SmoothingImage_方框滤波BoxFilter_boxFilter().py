import cv2
import numpy as np
from utils import addSaltNoise


lena=cv2.imread("../lena.jpg",0)
lenaNoise=addSaltNoise(lena)
lenaNoNoise=cv2.boxFilter(lenaNoise,-1,(2,2),normalize=0)
# lenaNoNoise=cv2.boxFilter(lenaNoise,-1,(5,5))# normalize默认为1
#参数2，处理结果图像的图像深度，一般使用-1表示与原始图像使用相同的图像深度


cv2.imshow("lena_addSaltNoise",lenaNoise)
cv2.imshow("lena_NoNoise",lenaNoNoise)

cv2.waitKey(0)