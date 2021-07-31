import cv2
import numpy as np

src=cv2.imread("../lena.jpg",0)
retval,dst=cv2.threshold(src,50,255,cv2.THRESH_BINARY)
athdMEAN=cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,3)#自适应方法，ADAPTIVE_THRESH_MEAN_C
athdGAUS=cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,3)#自适应方法，ADAPTIVE_THRESH_GAUSSIAN_C

cv2.imshow("src",src)
cv2.imshow("dst",dst)
cv2.imshow("athdMEAN",athdMEAN)
cv2.imshow("athdGAUS",athdGAUS)
cv2.waitKey(0)