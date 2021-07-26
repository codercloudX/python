import cv2
import numpy as np

src=cv2.imread("../lena.jpg")
#计算公式：dst(x,y)=src(1*x+0*y+100,0*x,1*y+200)
M=np.float32([[1,0,100],[0,1,200]])#100和200是x，y分别要移动的像素
rows,cols=src.shape[:2]

dst=cv2.warpAffine(src,M,(cols,rows))

cv2.imshow("dst",dst)
cv2.waitKey(0)