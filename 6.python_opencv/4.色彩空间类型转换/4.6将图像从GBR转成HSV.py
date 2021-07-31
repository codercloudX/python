import cv2
import numpy as np

src=np.zeros([100,100,3],dtype=np.uint8)
src[:,:,2]=255
dst=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

print(src)
print(dst)

cv2.imshow("src",src)
cv2.imshow("dst",dst)


cv2.waitKey(0)