import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

labels = ['努力','运气','天赋','人品','金钱','其它'] #设置每块饼的标签
sizes = [40,10,20,20,10,10]  #设置每块饼所占比例
explode = (0.1,0,0,0,0,0)  #表示饼图每个饼的突出程度
# sizes:每块饼所占比例；
# explode：每个饼的’突出程度；
# autopct 表示显示数据的格式；
# shadow表示二维饼图；
# startangle表示起始的角度。
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("成功是怎么炼成的") #标题
plt.show()