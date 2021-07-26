import cv2
import numpy as np

# src=np.zeros((5,5),dtype=np.uint8)
# src[0:6,0:6]=123
# src[2:6,2:6]=126

src=cv2.imread("../hazh.jpg",0)

t1,thd=cv2.threshold(src,127,255,cv2.THRESH_BINARY)
print(thd)
cv2.imshow("thd",thd)

t1,otsu=cv2.threshold(src,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print(otsu)
cv2.imshow("otsu",otsu)

cv2.waitKey(0)