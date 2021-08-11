import pandas as pd
import numpy as np
import matplotlib.pyplot as plt






#散点图形
#饼状图
df = pd.DataFrame(3*np.random.rand(4),index=['a','b','c','d'],columns=['x'])
df.plot.pie(subplots=True)
plt.show()
