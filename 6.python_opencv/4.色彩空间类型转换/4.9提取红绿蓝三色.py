import cv2
import numpy as np

src=cv2.imread("../LOGO.jpg")
logoHSV=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

#蓝色
maskBlue=cv2.inRange(logoHSV,np.array([110,100,100]),np.array([130,255,255]))
logoBlue=cv2.bitwise_and(logoHSV,logoHSV,mask=maskBlue)

#红色
maskRed=cv2.inRange(logoHSV,np.array([0,100,100]),np.array([10,255,255]))
logoRed=cv2.bitwise_and(logoHSV,logoHSV,mask=maskRed)

#绿色
maskGreen=cv2.inRange(logoHSV,np.array([50,100,100]),np.array([70,255,255]))
logoGreen=cv2.bitwise_and(logoHSV,logoHSV,mask=maskGreen)

cv2.imshow("src",src)
cv2.imshow("logoBlue",logoBlue)
cv2.imshow("logoRed",logoRed)
cv2.imshow("logoGreen",logoGreen)

cv2.waitKey(0)
