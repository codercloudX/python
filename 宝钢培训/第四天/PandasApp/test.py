import pandas as pd
import numpy as np

pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

s = pd.Series([1, 3, 5, np.nan, 6, 8])
dates = pd.date_range('20200101', periods=7)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20170102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df)
# print(df.index)

3
# print(df.columns)
# print(df.values)
# print(df.describe(()))

# print(df.sort_index(axis=1, ascending=False))  # 列倒序
# print(df.sort_index(axis=0, ascending=False))  # 行倒序
# print(df.sort_values(by='C'))  # C列排序

# print(df['B'])  # 选择一列
# print(df[2:5])  # 选择切片行
# print(df['20200102':'20200104'])  # 选择指定索引列

# print(df.loc[dates[3]])  # 使用标签获取横截面1
# print(df.loc['20200105'])  # 使用标签获取横截面2
# print(df.loc[: , ['A', 'C']])  # 通过标签选择多轴,不能通过数字
# print(df.loc['20200105':'20200107', ['A','D']])  # 标签索引、列切片
# print(df.loc[dates[0], 'A'])  # 等同于print(df.at[dates[0],'A']),获取标量值

# print(df.iloc[2:4, 3:4])  # 通过数字选择多轴,不能通过标签
# print(df.iloc[2, 3])  # 通过数字选择多轴获取某个值

#  at 和 iat 的区别，与 loc 和loc一样
# at 函数：通过行名和列名来取值（取行名为a, 列名为A的值）
# iat 函数：通过行号和列号来取值（取第1行，第1列的值）

