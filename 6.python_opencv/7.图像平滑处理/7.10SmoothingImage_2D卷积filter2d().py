import cv2
import numpy as np
from utils import addSaltNoise


lena=cv2.imread("../lena.jpg",0)
lenaNoise=addSaltNoise(lena)
kernel=np.ones((9,9),np.float32)/81
lenaNoNoise=cv2.filter2D(lenaNoise,-1,kernel)

cv2.imshow("lena_addSaltNoise",lenaNoise)
cv2.imshow("lena_NoNoise",lenaNoNoise)

cv2.waitKey(0)