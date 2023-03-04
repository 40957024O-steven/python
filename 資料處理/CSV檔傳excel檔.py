import csv
from openpyxl import Workbook, load_workbook

wb = Workbook()
ws = wb.active

with open('C:/Users/steve/Downloads/relatedQueries.csv',encoding="utf-8",newline='') as csvfile:

    rows = csv.reader(csvfile,delimiter=';') #delimiter = 以啥符號分隔資料

    for row in rows:
        ws.append(row)

wb.save('123.xlsx')