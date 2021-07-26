import cv2
import numpy as np

src=np.random.randint(0,256,size=[4,5],dtype=np.uint8)
rows,cols=src.shape[:2]
mapX=np.ones(src.shape,dtype=np.float32)*3
mapY=np.ones(src.shape,dtype=np.float32)*0
dst=cv2.remap(src,mapX,mapY,cv2.INTER_LINEAR)
print("src",src)
print("mapX",mapX)
print("mapY",mapY)
print("dst",dst)