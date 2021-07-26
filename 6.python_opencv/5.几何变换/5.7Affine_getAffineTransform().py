import cv2
import numpy as np

src=cv2.imread("../lena.jpg")
rows,cols=src.shape[:2]
p1=np.float32([[0,0],[cols-1,0],[0,rows-1]])
p2=np.float32([[0,rows*0.33],[cols*0.85,rows*0.25],[cols*0.15,rows*0.7]])
M=cv2.getAffineTransform(p1,p2)
dst=cv2.warpAffine(src,M,(cols,rows))

cv2.imshow("src",src)
print(M)
print(p2)
print(p1)
cv2.imshow("dst",dst)
cv2.imshow("M",M)

cv2.waitKey(0)