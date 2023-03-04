from openpyxl import Workbook, load_workbook


wb = load_workbook ("new2.xlsx")
ws = wb["123"]

ws.delete_cols(1) #刪除直排
ws.delete_rows(6) #刪除橫排
ws.insert_cols(2) #插入直排
ws.insert_rows(5) #插入橫排


wb.save("new2.xlsx")