import pandasUtil

excelNameAll = "demo.xls"
sheetName = "乌塘镇"
if __name__ == '__main__':

    dataLis = pandasUtil.getDic(excelNameAll, sheetName)

    writer = pandasUtil.pd.ExcelWriter('demo4.xls')
    for i in range(len(dataLis)):
        dataLis[i]["data"].to_excel(writer, sheet_name=pandasUtil.dataList[i]["name"])
    writer.save()
    writer.close()


