from openpyxl import load_workbook
try: #嘗試執行以下程式
    print('123')
except: #若無法完整執行 則執行以下程式
    print('try error')

try:
    wb = load_workbook('456.xlsx')
except: #若無法完整執行 則不執行任何事
    pass