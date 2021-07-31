import cv2
import numpy as np

# cv2.flip()
#第二个参数：flipCode，翻转类型，0->x轴翻转，正数->y轴翻转，负数->x,y同时翻转

src=cv2.imread("../lena.jpg")
dst=cv2.flip(src,-9)

cv2.imshow("dst",dst)
cv2.waitKey(0)
