import cv2
import numpy as np

src=cv2.imread("../lena.jpg")
# cv2.getRotationMatrix2D(center,angle,scale)
rows,cols=src.shape[:2]
M=cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst=cv2.warpAffine(src,M,(cols,rows))


cv2.imshow("dst",dst)
cv2.waitKey(0)