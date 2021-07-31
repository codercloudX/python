import numpy as np
import pandas as pd

df1 = pd.read_excel('test.xlsx')
df2 = pd.DataFrame(np.random.rand(5, 5))

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行

# print(df1.append(df2))  # 将df2中的行添加到df1的尾部