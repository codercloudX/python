import numpy as np
import pandas as pd

# df = pd.DataFrame(np.random.rand(5, 5))
df = pd.read_excel('test.xlsx')
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)
# print(df[df[3] > 0.4])  # 选择第 n 列中大于0.4的行
# print(df.sort_values(1))  # 根据第一列进行升序排列
# print(df.sort_values(1, ascending=False))  # 根据第一列进行降序排列
# print(df.sort_values([1, 2], ascending=[True, False])) # 先根据第一列进行升序排列，再根据第二列进行降序排序

# groupby分组聚合函数
for key in df.groupby('序号'):
    print(key)

print(df)


