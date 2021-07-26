import cv2
import numpy as np

src=cv2.imread("../lena.jpg")
dst=cv2.resize(src,None,fx=2,fy=0.5)#需要加上fx=...

print("src.shape",src.shape)
print("dst.shape",dst.shape)

cv2.imshow("dst",dst)
cv2.waitKey(0)