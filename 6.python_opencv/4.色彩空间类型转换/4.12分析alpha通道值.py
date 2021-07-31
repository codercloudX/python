import cv2 
import numpy as np

src=cv2.imread("../lena.jpg")
bgra=cv2.cvtColor(src,cv2.COLOR_BGR2BGRA)
b,g,r,a=cv2.split(bgra)
a[:,:]=128
dst=cv2.merge([b,g,r,a])


cv2.imshow("src",src)
cv2.imshow("bgra",bgra)
cv2.imshow("dst",dst)
cv2.imwrite("lenaAlpha.png",dst)#这里只有保存为png才能显示透明效果

cv2.waitKey(0)