import numpy as np
import pandas as pd

df = pd.read_excel('test.xlsx')
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

# pd.read_csv(filename)：#从CSV文件导入数据
# pd.read_table(filename)：#从限定分隔符的文本文件导入数据
# pd.read_sql(query, connection_object)#从SQL表/库导入数据
# pd.read_json(json_string)：#从JSON格式的字符串导入数据
# pd.read_html(url)：#解析URL、字符串或者HTML文件，抽取其中的tables表格
# pd.read_clipboard()：#从你的粘贴板获取内容，并传给read_table()
# pd.DataFrame(dict)：#从字典对象导入数据，Key是列名，Value是数据

print(type(df))

print(df)

