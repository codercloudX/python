import cv2
import numpy as np

src=cv2.imread("../lena.jpg")
rows,cols=src.shape[:2]
dsize=(int(cols*0.9),int(rows*0.5))

dst=cv2.resize(src,dsize)

print("src.shape",src.shape)
print("dst.shape",dst.shape)