import cv2 
import numpy as np

src=cv2.imread("../lena.jpg",1)
srcHSV=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(srcHSV)
s[:,:]=255
art=cv2.cvtColor(cv2.merge([h,s,v]),cv2.COLOR_HSV2BGR)


cv2.imshow("srcHSV",srcHSV)
cv2.imshow("h",h)
cv2.imshow("s",s)
cv2.imshow("v",v)
cv2.imshow("art",art)

cv2.waitKey(0)