import numpy as np
import pandas as pd
import csv
from openpyxl import Workbook

path = "C:/Users/steven.LAPTOP-8A1BDJC6/Downloads/try.csv"


wb = Workbook()
ws = wb.active
with open(path,encoding="utf-8",newline='') as csvfile:

    rows = csv.reader(csvfile,delimiter=',') #delimiter = 以啥符號分隔資料

    for row in rows:
        ws.append(row)
wb.save("C:\Users\steven.LAPTOP-8A1BDJC6\OneDrive\桌面\我的電腦\python\123.xlsx")

df = pd.read_csv(path)
# print(df.info())
inf = df[['少年犯年齡','性別','日期','統計值']]
# print(inf)



#哪一個年齡犯罪人數最多?


# 哪一年的犯罪人數最多？



# 哪個月的人數最多？


gp1 = inf.groupby(['性別'])['統計值'].sum().reset_index() 
# print(gp1)

# 總共有多少男生？
b = int(gp1[gp1['性別'] == '男性']['統計值'])
# print(b)

# 總共有多少女生？
g = int(gp1[gp1['性別'] == '女性']['統計值'])
# print(g)

# 男女比例？
bg = str(round(b/(b+g)*100)) + ':' + str(100-round(b/(b+g)*100))
# print(bg)

# 平均年齡是多少？
# 各年齡的平均犯罪人數？
# 各年齡的男女比率？
# 每個月人數的標準差？


g = str(g)
b = str(b)
bg = str(bg)

# QA
qa = [
    ['Q:總共有多少女生? A:' + g + '人'],
    ['Q:總共有多少男生? A:' + b + '人'],
    ['Q:男女比例？ A:' + bg],

]

# print(qa)