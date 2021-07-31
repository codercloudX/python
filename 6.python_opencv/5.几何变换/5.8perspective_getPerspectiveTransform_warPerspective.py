import cv2
import numpy as np

src=cv2.imread("../lena.jpg")
rows,cols=src.shape[:2]

pts1=np.float32([[150,50],[400,50],[60,450],[310,450]])
pts2=np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])

M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(src,M,(cols,rows))

cv2.imshow("dst",dst)
cv2.imshow("src",src)

cv2.waitKey(0)