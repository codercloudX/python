
# import numpy as np
# import pandas as pd
#
# df = pd.DataFrame(np.random.rand(5, 5))  # 5行6列的DataFrame对象
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
# s = pd.Series(np.array(np.random.rand(3)), name='cyl', index=['i1', 'i2', 'i3'])  # 只接受一维数组
# print(s)
# '''
#     3.1 查看数据
# '''
#
# # df.head(10) # 查看前10行
# # df.tail(10) # 查看最后10行
# # df.shape # 查看行数和列数
# # df.info # 查看索引、数据类型和内存信息
# # df.describe() # 查看数值型列的汇总统计
#
# # s.value_counts(dropna=False) # 查看Series对象的唯一值和计数
# # df.apply(pd.Series.value_counts) # 查看DataFrame对象中每一列的唯一值和计数
# '''
#     3.2 数据选取
# '''
# # df[col]#根据列名，并以Series的形式返回列
# # df[[col1, col2]]#以DataFrame形式返回多列
# # s.iloc[0] # 按位置选取数据
# # s.loc['index_one']#按索引选取数据
# # df.iloc[0,:]#返回第一行
# # df.iloc[0,0]#返回第一列的第一个元素
# # print(df)
# # df.loc[0,2] = None
# # print(df.loc[0,2])

import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5, 6))  # 5行6列的DataFrame对象
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
s = pd.Series(np.array(np.random.randn(10)))  # 只接受一维数组
'''
    3.1 查看数据 
'''

# df.head(10) # 查看前10行
# df.tail(10) # 查看最后10行
# df.shape # 查看行数和列数
# df.info # 查看索引、数据类型和内存信息
# df.describe() # 查看数值型列的汇总统计
# s.value_counts(dropna=False) # 查看Series对象的唯一值和计数
# df.apply(pd.Series.value_counts) # 查看DataFrame对象中每一列的唯一值和计数
'''
    3.2 数据选取 
'''
# df[col]#根据列名，并以Series的形式返回列
# df[[col1, col2]]#以DataFrame形式返回多列
# s.iloc[0] # 按位置选取数据
# s.loc['index_one']#按索引选取数据
# df.iloc[0,:]#返回第一行
# df.iloc[0,0]#返回第一列的第一个元素

print(s.iloc[0:])

