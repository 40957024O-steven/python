import pandas as pd


path = "C:/Users/steven.LAPTOP-8A1BDJC6/Downloads/ExchangeRate@202303141527.csv"
df = pd.read_csv(path)
file = df['現金'] #即期(檔案title有問題)
# print(file)
M = round(file.mean(),2) #平均數(預期收益)
# print(M)
S = round(file.std(),3) #標準差(預期風險)
print(S)