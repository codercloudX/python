import cv2
import numpy as np

lena=cv2.imread("../lena.jpg",1)[100:200,300:400]
#src=np.zeros((30,30,3),dtype=np.uint8)
#for i in range(0,30):
 #   for j in range(10,20):
 #       src[i,j,0]=0
#        src[i,j,1]=255
#        src[i,j,2]=255




src=cv2.imread("cyl2.jpg")
#src = cv2.resize(src, (295, 413), interpolation=cv2.INTER_LINEAR)
#rows,cols=src.shape[:2]
#for i in range(rows):
#    for j in range(cols):
#        #if(src[i,j,0]>220 and src[i,j,0]<235 and src[i,j,1]>170 and src[i,j,1]<180 and src[i,j,2]>70 and src[i,j,2]<80):
#           #src[i,j]=[255,255,255]
#       print(src[i,j])

face=src[549:1050,415:785]

cv2.imwrite("cyl.jpg",face)

cv2.imshow("src",face)
cv2.waitKey(0)