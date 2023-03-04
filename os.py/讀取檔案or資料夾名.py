import os
import glob

path = 'C:/Users/steve/Desktop/python/松山剖風儀/2019-11-24/wind_reconstruction_data/00-00'
# print(os.listdir(path)) #列出某個資料夾中所有的檔案名稱

path = 'C:/Users/steve/Desktop/python/松山剖風儀/2019-11-24/wind_reconstruction_data/00-00/*.csv'
result  =glob.glob(path)
for f in result:
    print(f)