import pandas as pd

import pandasUtil
import ioUtil

excelNameAll = "demo.xls"
sheetName = "乌塘镇"
if __name__ == '__main__':
    pandasUtil.getDic(excelNameAll, sheetName)
    data = []

    writer = pandasUtil.pd.ExcelWriter('demo4.xls')
    for i in range(len(pandasUtil.dataList)):
        pandasUtil.dataList[i]["data"].to_excel(writer, sheet_name=pandasUtil.dataList[i]["name"])
    writer.save()
    writer.close()


