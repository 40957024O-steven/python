import numpy as np
import pandas as pd
import csv
import statistics
path = "C:/Users/steve/Downloads/珺.csv"
path_1 = "C:/Users/steve/Downloads/珺_1.csv"
# 資料整理
file = []

with open(path,encoding="UTF-8",newline='') as csvfile:

    rows = csv.reader(csvfile,delimiter=',') #delimiter = 以啥符號分隔資料

    for row in rows:
            # print(row)
            file.append(row)
# print(file)
File = [[],[],[],[]] #少年犯年齡,性別,日期,統計值
for i in range(1,len(file)):
    File[0].append(file[i][0])
    File[1].append(file[i][1])
    if len(file[i][2]) == 3:
        File[2].append(file[i][2])
    else:
        File[2].append(file[i][2][:3])    

    File[3].append(file[i][3])

# print(File[2])

f = {
    '少年犯年齡':File[0],
    '性別':File[1],
    '年':File[2],
    '統計值':File[3]
}
F = pd.DataFrame(f).to_csv(path_1)

# 資料整理

#QA
df = pd.read_csv(path_1,encoding='UTF-8')
# print(df.describe)


# 各年齡犯罪人數？
Q_1 = df.groupby(['少年犯年齡'])['統計值'].sum().reset_index()
# print(Q_1)


# 每年的犯罪人數？
Q_2 = df.groupby(['年'])['統計值'].sum().reset_index()
# print(Q_2)

sax = df.groupby(['性別'])['統計值'].sum().reset_index()
# print(sax)
# 總共有多少男生？
Q_3 = sax[sax['性別'] == '男性']['統計值'].values[0]
# print(Q_3)


# 總共有多少女生？
Q_4 = sax[sax['性別'] == '女性']['統計值'].values[0]
# print(Q_4)


# 男女比例？
b = int(Q_3)
g = int(Q_4)
Q_5 = str(round(b/(b+g)*100)) + ':' + str(100-round(b/(b+g)*100))
# print(Q_5)


# 平均年齡是多少？
# print(Q_1)
totleage = 0
for Age in Q_1['少年犯年齡']:
    # print(Age)
    # print(len(Age))
    if len(Age)  == 5:
        age = int(Age[:2])
    elif len(Age) == 8:
        age = int(Age[:2]) +0.5
    else:
        age = 0
    # print(age)
    # print(Q_1[Q_1['少年犯年齡'] == Age]['統計值'].values[0])
    # print(age*Q_1[Q_1['少年犯年齡'] == Age]['統計值'].values[0])
    totleage += age*Q_1[Q_1['少年犯年齡'] == Age]['統計值'].values[0]
    
Q_6 = round(totleage/Q_1[Q_1['少年犯年齡'] == '少年犯年齡合計']['統計值'].values[0],1)
# print(Q_6)


# print(Q_1)
maxnb = 0
minnb = 99999999999999999
Q_1 = Q_1.drop(Q_1[Q_1['少年犯年齡'] == '少年犯年齡合計'].index)
for i in Q_1['統計值']:
        # print(i)
        if i > maxnb:
            # print(Q_1[Q_1['統計值'] == i]['少年犯年齡'].values[0])
            max = Q_1[Q_1['統計值'] == i]['少年犯年齡'].values[0]
            maxnb = i
        if i < minnb:
            min = Q_1[Q_1['統計值'] == i]['少年犯年齡'].values[0]
            minnb  = i
#哪一個年齡犯罪人數最多?
Q_7 = max
# print(Q_7)


# 哪個年齡犯罪人數最少
Q_8 = min
# print(Q_8) 

# 各年齡的男女分布？
Q_9 = df.groupby(['少年犯年齡','性別'])['統計值'].sum().reset_index()
# print(Q_9)


# 每年人數平均？
nb = df.groupby(['年'])['統計值'].sum().reset_index()
# print(nb)
count = nb['統計值'].values
# print(count)
Q_10 = statistics.mean(count)
# print(Q_10)


# QA

print('Q1:各年齡犯罪人數?\nA1:\n'+ str(Q_1))
print('Q2:每年的犯罪人數?\nA2:\n'+ str(Q_2))
print('Q3:總共有多少男生?\nA3:\n'+ str(Q_3))
print('Q4:總共有多少女生?\nA4:\n'+ str(Q_4))
print('Q5:男女比例?\nA5:\n'+ str(Q_5))
print('Q6:平均年齡是多少?\nA6:\n'+ str(Q_6))
print('Q7:哪一個年齡犯罪人數最多?\nA7:\n'+ str(Q_7))
print('Q8:哪個年齡犯罪人數最少?\nA8:\n'+ str(Q_8))
print('Q9:各年齡的男女分布?\nA9:\n'+ str(Q_9))
print('Q10:每年人數平均?\nA10:\n'+ str(Q_10))