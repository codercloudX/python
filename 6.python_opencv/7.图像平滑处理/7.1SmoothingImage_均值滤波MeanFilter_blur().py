import cv2
import numpy as np
# 适用于导入上级目录的模块
# import sys
# sys.path.append("..")
from utils import addSaltNoise


lena=cv2.imread("../lena.jpg",0)
#parameter1:原图像
#parameter2:卷积核
#parameter3:锚点Anchor，默认(-1,-1)，表示当前计算均值的点位于核的中心点位置
#parameter4:边界样式borderType，决定了以何种方式处理边界
#卷积核越大，图像失真越严重，去噪效果越好
lenaNoise=addSaltNoise(lena)
lenaNoNoise=cv2.blur(lenaNoise,(10,10))


cv2.imshow("lena_addSaltNoise",lenaNoise)
cv2.imshow("lena_NoNoise",lenaNoNoise)

cv2.waitKey(0)