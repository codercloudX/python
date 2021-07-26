import cv2
import numpy as np

src=cv2.imread("../lena.jpg",0)
#cv2.THRESH_BINARY_INV 反二值化阈值处理
#cv2.THRESH_BINARY 二值化阈值处理
#cv2.THRESH_TRUNC 截断阈值化处理
#cv2.THRESH_TOZERO_INV 超阈值零处理
#cv2.THRESH_TOZERO 低阈值零处理
retval,dst=cv2.threshold(src,50,255,cv2.THRESH_TOZERO)

print("retval",retval)
print("dst",dst)

cv2.imshow("dst",dst)
cv2.waitKey(0)