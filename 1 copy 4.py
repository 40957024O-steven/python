import numpy as np
import pandas as pd
# from openpyxl import load_workbook 

path = "C:/Users/steven.LAPTOP-8A1BDJC6/Downloads/try.csv"

df = pd.read_csv(path)
# print(df.info())
inf = df[['少年犯年齡','性別','日期','統計值']]
# print(inf)

#哪一個年齡犯罪人數最多?
gp1 = inf.groupby(['性別'])['統計值'].sum().reset_index() 
# print(gp1)

# 哪一年的犯罪人數最多？
gp2 = inf.groupby(['日期'])['統計值'].sum().reset_index()

print(gp2)
gp2
# 哪個月的人數最多？
# 總共有多少男生？
# 總共有多少女生？
# 男女比例？
# 平均年齡是多少？
# 各年齡的平均犯罪人數？
# 各年齡的男女比率？
# 每個月人數的標準差？