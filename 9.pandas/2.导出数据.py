import numpy as np
import pandas as pd

df = pd.read_excel('test.xlsx')
df.to_excel('filename.xlsx')#  导出数据到Excel文件
# df.to_csv(filename)#    导出数据到CSV文件

# df.to_sql(table_name, connection_object)#   导出数据到SQL表
# df.to_json(filename)#   以Json格式导出数据到文本文件