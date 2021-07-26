import cv2
import numpy as np

img=np.random.randint(0,255,[100,100],dtype=np.uint8)
dst=cv2.inRange(img,100,200)

print(dst)
cv2.imshow("img",img)
cv2.imshow("dst",dst)
cv2.waitKey(0)