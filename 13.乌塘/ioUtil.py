import xlwings

if __name__ == '__main__':
    app = xlwings.App(visible=False, add_book=False)
    wb = app.books.open("./demo4.xls")
    print(wb)
    sht = wb.sheets[0]
    print(sht)
    # b2 = sht.range("b2").value
    # print(sht.range("A1").value)

    app.quit()
