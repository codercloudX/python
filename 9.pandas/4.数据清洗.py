import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.rand(5, 6))  # 5行6列的DataFrame对象

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
s = pd.Series(np.array(np.random.randn(10)))  # 只接受一维数组


df.loc[4, 4] = None

df.iat[3, 3] = None # 根据行列定位更改元素值;这里将该位置的元素值置空
# df.columns = ['a','b','c']# 重命名列名
# pd.isnull()# 检查DataFrame对象中的空值，并返回一个Boolean数组;参数是一个DataFrame对象
# pd.notnull()# 检查DataFrame对象中的非空值，并返回一个Boolean数组
# df.dropna(axis=0)# 删除所有包含空值的行
# df.dropna(axis=1)# 删除所有包含空值的列
# df.fillna(x)：# ***用x来替换DataFrame对象中所有的空值***
# s.astype(float)# 将Series中的数据类型更改为float类型
# s.replace(1,'one')# 用‘one’代替所有等于1的值
# s.replace([1,3],['one','three'])# 用'one'代替1，用'three'代替3
# df.rename(columns=lambda x: x + 1)# 批量更改列名
# df.rename(columns={'old_name': 'new_ name'})# 选择性更改列名
# df.set_index('column_one')# 更改索引列
# df.rename(index=lambda x: x + 1)# 批量重命名索引
print(df)

print(df.fillna('0'))

print(pd.isnull(df))
print(df.fillna(99))

