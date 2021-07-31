import cv2
import numpy as np
from utils import addSaltNoise


lena=cv2.imread("../lena.jpg",0)
lenaNoise=addSaltNoise(lena)
lenaNoNoise=cv2.GaussianBlur(lenaNoise,(5,5),0,0)

#参数3:卷积核在水平方向的标准差，控制权重比例


cv2.imshow("lena_addSaltNoise",lenaNoise)
cv2.imshow("lena_NoNoise",lenaNoNoise)

cv2.waitKey(0)