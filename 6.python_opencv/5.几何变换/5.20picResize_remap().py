import cv2
import numpy as np

# src=np.random.randint(0,255,size=[4,5],dtype=np.uint8)
src=cv2.imread("../lena.jpg",0)
rows,cols=src.shape
mapX=np.zeros(src.shape,dtype=np.float32)
mapY=np.zeros(src.shape,dtype=np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25*cols<i<0.75*cols and 0.25*rows<j<0.75*rows:
            mapX.itemset((i,j),2*(j-cols*0.25)+0.5)
            mapY.itemset((i,j),2*(i-rows*0.25)+0.5)
        else:
            mapX.itemset((i,j),0)
            mapY.itemset((i,j),0)
dst=cv2.remap(src,mapX,mapY,cv2.INTER_LINEAR)
print(src,src)
print(mapX,mapX)
print(mapY,mapY)
print(dst,dst)


cv2.imshow("lena",dst)
cv2.waitKey(0)