from openpyxl import Workbook, load_workbook

wb = load_workbook ("new2.xlsx")
ws = wb["789"]

ws.move_range("A1:E5",rows= 7 ,cols= 9) #(移動範圍,上下移動(負號 = 往上移),左右移動(負號 = 往左移))

wb.save("new2.xlsx")