import xlwings

if __name__ == '__main__':
    app = xlwings.App(visible=False, add_book=False)
    wb = app.books.open("demo4.xls")
    sht = wb.sheets[0]

    #  删除首列
    # sht.range('A1').api.EntireColumn.Delete()  # 会删除 ’A1‘ 单元格所在的列。

    #  表头，插入行
    # sht.api.Rows(1).Insert()
    # sht.api.Rows(2).Insert()
    # sht.api.Rows(4).Insert()
    # sht.api.Rows(5).Insert()



    #  填写表头
    #  第1 ， 2 行
    sht.range("A1").value = '遂溪县乌塘镇2022年储备农村人居环境整治项目工作情况统计表'
    sht.range('A1:K1').api.Merge()
    sht.range("J2").value = '单位：万元'
    sht.range('J2:K2').api.Merge()

    # 第3 - 5行
    sht.range('H3:J3').api.Merge()
    sht.range("H4").value = '总计'
    sht.range('H4:H5').api.Merge()
    sht.range("I4").value = '涉农资金'
    sht.range('I4:I5').api.Merge()
    sht.range("J4").value = '自筹资金'
    sht.range('j4:j5').api.Merge()
    sht.range("K4").value = '备注'
    sht.range('K4:K5').api.Merge()

    sht.range('A3:A5').api.Merge()
    sht.range('B3:B5').api.Merge()
    sht.range('C3:C5').api.Merge()
    sht.range('D3:D5').api.Merge()
    sht.range('E3:E5').api.Merge()
    sht.range('F3:F5').api.Merge()
    sht.range('G3:G5').api.Merge()

    # 表尾，小计
    allRows = sht.used_range.last_cell.row #  获取此时数据总行数
    # sht.range("A"+str(allRows+1)).value = '小计'
    sht.range('A'+str(allRows+1)+':G'+str(allRows+1)).api.Merge()
    sht.range('H'+str(allRows+1)).formula = '=SUM(H6:H'+str(allRows)+')'  # 总计列，插入公式
    sht.range('I' + str(allRows + 1)).formula = '=SUM(I6:I' + str(allRows) + ')'  # 涉农资金列，插入公式


    wb.save()
    app.quit()
