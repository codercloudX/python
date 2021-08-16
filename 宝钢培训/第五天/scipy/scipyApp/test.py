from numpy import vstack, array
from numpy.random import rand
from scipy.cluster.vq import kmeans, vq, whiten
import pandas as pd

df = pd.read_csv('../../sportPlayerSalary.csv')
pd.set_option("display.max_column", None)
pd.set_option("display.max_row", None)
pd.set_option("display.width", 500)  # 指定显示最大宽度
print(df)


