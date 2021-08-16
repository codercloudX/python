import pandas as pd

# pd.set_option("display.max_columns", None)
# pd.set_option('display.max_rows', None)
# pd.set_option('display.width', 1000)

nameList = []
dataList = []


#  根据字典名称获取该字典元素在该列表的下标
def getDataByName(name):
    for i in range(len(dataList)):
        if dataList[i]["name"] == name:
            return i


#  根据目标excel与目标工作簿，获取 根据列名为行政村的分组数据
def getDic(excelName, sheetName):
    #  1.选出总表有效数据
    df = pd.read_excel(excelName, sheet_name=sheetName)
    df.columns = list(df.iloc[2])
    data = df.iloc[5:348]

    #  2.遍历df.groupby()，得到行政村列表nameList并输出
    for key in data.groupby(by=["行政村"]):
        nameList.append(key[0])

    #   3.使用df.loc[]获取每个行政村的数据,放入dataList内
    for i in range(len(nameList)):
        dataList.append({"name": nameList[i], "data": data.loc[data['行政村'] == nameList[i]]})

    return dataList
