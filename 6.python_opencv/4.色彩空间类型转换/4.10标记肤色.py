import cv2
import numpy as np

src=cv2.imread("../triss.jpg",1)
lenaHSV=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

h,s,v=cv2.split(lenaHSV)

hueMask=cv2.inRange(h,5,170)
satMask=cv2.inRange(s,25,166)
mask=hueMask&satMask
roi=cv2.bitwise_and(src,src,mask=mask)

cv2.imshow("lenaHSV",lenaHSV)
cv2.imshow("ROI",roi)



cv2.waitKey(0)