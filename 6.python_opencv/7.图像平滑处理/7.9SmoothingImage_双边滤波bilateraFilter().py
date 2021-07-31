import cv2
import numpy as np
from utils import addSaltNoise


lena=cv2.imread("../lena.jpg",0)
lenaNoise=addSaltNoise(lena)
lenaNoNoise=cv2.bilateralFilter(lenaNoise,55,100,100)

cv2.imshow("lena_addSaltNoise",lenaNoise)
cv2.imshow("lena_NoNoise",lenaNoNoise)

cv2.waitKey(0)