import  xlwings as xw

app = xw.App(visible=False,add_book=False)
wb = app.books.open("./test.xlsx")
sht = wb.sheets["test"]

print(sht.range("A1").value)
print(sht.range("B1").value)