import numpy as np
import pandas as pd
import scipy

df = pd.read_csv('pokemon.csv', encoding='gbk')
data = df[['name', 'defense', 'height_m', 'weight_kg', 'speed', 'hp']].head(20)

print('----------------------------第一题-------------------------------')
print('-----1.宝可梦列表-----')
print(data)
print('-----2.平均体重-----')
print(data['weight_kg'].mean())
print('-----3.体重标准偏差-----')
print(data['weight_kg'].std())
print('-----4.重量统计摘要-----')
print(data['weight_kg'].describe())
print('-----5.必要信息的参数-----')
print(data.describe(include=['object']))
print('-----6.统计信息的摘要追加freq最高的对象信息统计-----')
print(data.describe(include='all'))
print('----------------------------第一题-------------------------------')

print('----------------------------第二题-------------------------------')


def adder(ele1, ele2):
    return ele1 + ele2


print('-----2.1 数据修改，pipe的使用-----')
data = data[['defense', 'height_m', 'weight_kg', 'speed', 'hp']].head(20).pipe(adder, 20)
print(data)
print('-----2.2 求列均值-----')
mean = data.apply(np.mean)
# mean = data.apply(np.mean, axis=0)
print(mean)
print('-----2.3 求行均值-----')
mean = data.apply(np.mean, axis=1)
print(mean)
print('-----2.4 通过map函数仅对指定列运算-----')
res = data.apply(lambda x: x.max() - x.min(), axis=1)  # 行最大值减最小值
print(res)
print('-----2.5 通过lambda嵌入函数算法求解行最大值减最小值-----')
res = data['defense'].map(lambda x: x * 100)
print(res)
print('-----2.6 通过applymap函数对DataFrame所有可计算数据运算-----')
res = data.applymap(lambda x: x * 100)  # 等同于用管道 df*=100
print(res)

print('----------------------------第二题-------------------------------')

print('----------------------------第三题-------------------------------')
N = 10
df = pd.DataFrame({
    'A': pd.date_range(start='2020-08-01', periods=N, freq='D'),
    'x': np.linspace(0, stop=N - 1, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Medium', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
})
print(df)
df_reindexed = df.reindex(index=[0, 2, 5], columns=['A', 'C', 'B'])
print(df_reindexed)
df1 = pd.DataFrame(np.random.randn(10, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['col1', 'col2', 'col3'])
print('df1:')
print(df1)
print('********************************************')
print('df2:')
print(df2)
print('********************************************')
df1 = df1.reindex_like(df2)
print('df1_reindex_like:')
print(df1)
print('-----------------------------------------------------')
df1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
df2 = pd.DataFrame(np.random.randn(2, 3), columns=['col1', 'col2', 'col3'])
print('原df1:')
print(df1)
print('原df2:')
print(df2)
print('df2_reindex_like:')
print(df2.reindex_like(df1))
print("向前填充值:")
print(df2.reindex_like(df1, method='ffill'))
print("向前填充值1行数据:")
print(df2.reindex_like(df1, method='ffill', limit=1))
print('-----------------------------------------------------')
df1 = pd.DataFrame(np.random.randn(6, 3), columns=['col1', 'col2', 'col3'])
print(df1)
print("重命名行列:")
print(df1.rename(columns={'col1': 'c1', 'col2': 'c2', 'col3': 'c3'}, index={0: 'China', 1: 'USA', 2: 'JAPAN'}))
print('----------------------------第三题-------------------------------')
