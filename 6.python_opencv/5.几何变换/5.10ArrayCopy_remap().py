import cv2
import numpy as np

# src=np.random.randint(0,255,size=[4,5],dtype=np.uint8)
src=cv2.imread("../lena.jpg",0)
rows,cols=src.shape
mapX=np.zeros(src.shape,dtype=np.float32)
mapY=np.zeros(src.shape,dtype=np.float32)
for i in range(rows):
    for j in range(cols):
        # mapX.itemset((i,j),j)#复制
        mapX.itemset((i,j),i)#x,y互换
        # mapX.itemset((i,j),cols-j-1)#绕Y轴翻转
        # mapY.itemset((i,j),i)#复制
        mapY.itemset((i,j),j)#x,y互换
        # mapY.itemset((i,j),rows-1-i)#绕X轴翻转
dst=cv2.remap(src,mapX,mapY,cv2.INTER_LINEAR)
print("src",src)
print("mapX",mapX)
print("mapY",mapY)
print("dst",dst)


cv2.imshow("lena",dst)
cv2.waitKey(0)