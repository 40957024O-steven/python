import pandas as pd

# 建立一個 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4.5, 5.6, 6.7],
    'C': ['foo', 'bar', 'baz']
})

# 將第一列的資料型態轉換成字串
df.iloc[0] = df.iloc[0].astype(str)

# 查看轉換後的 DataFrame
print(df)