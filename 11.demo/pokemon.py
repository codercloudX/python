import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy

df = pd.read_csv('pokemon.csv', encoding='gbk')
pd.set_option("display.max_column", None)
pd.set_option("display.max_row", None)
pd.set_option("display.width", 500)  # 指定显示最大宽度


# data = df.at[8, 'abilities']# 第8行，列名为abilities的数据
# data = df.loc[df['abilities'] == "['Overgrow', 'Chlorophyll']"]  # 筛选出，abilities值为['Overgrow', 'Chlorophyll']的数据（DataFrame对象）
# data['speed'].mean()  #  求某一列的均值
# data.sort_values('speed',ascending=False)  #  求speed列的降序排列
# data.sort_values('speed',ascending=False).to_csv("result.csv")  #  保存进新的csv文件
# data[['name','speed']]  #选出name列与speed列
# data = df.loc[df['type1'] == "grass"]
# data = data[['name', 'speed']]
data = df[['name', 'defense', 'height_m', 'weight_kg', 'speed', 'hp']].head(20)
print(data)
