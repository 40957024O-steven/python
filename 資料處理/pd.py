import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/steve/Desktop/學校/大三下/學習分析工具實務應用/README.md/text.csv",encoding = 'BIG5')
print(df)
team = df[['類別','參加人數']]
print(team) # 印出**欄位的資料
gb = team.groupby(['類別'])['參加人數'].sum().reset_index() #team.groupby(['A'])['B'].sum().reset_index() ==> 將A類別相同的B類別中的資料做統計(加總(可作多種統計 例:取最大最小值).重新設定index )
print(gb)



list1 = [11,22,33,44,55]
list2 = ['鄭','王','華','明','西']

mark1 = pd.Series(list1) #顯示索引標籤
# print(mark1)

group = pd.Series(list1,index=list2) #將索引標籤設定為目標矩陣
# print(group)

# print(mark1[1:3])
# print(group['王'])


g = '@gmail.com'
date1 = {
    'name' : ['王','張','廖','丁'],
    'email': ['wan'+g,'jon'+g,'lew'+g,'den'+g],
    'group': [60,70,80,90],
    'nb'   : [1,2,3,4]
}
student_df = pd.DataFrame(date1) #將資料格式改為DataFrame
# print(student_df) 
# print(student_df.info())#欄位資料行資訊
# print(student_df.describe())#統計資訊
# print(student_df.index) #標籤資料
# print(student_df.columns) #Title
# print(student_df.head(2)) #列出前2資料
# print(student_df.tail(2)) #列出後2資料

date2 = {
    'name' : ['黃','忘','包','江'],
    'email': ['hong'+g,'wane'+g,'bow'+g,'jen'+g],
    'group': [6,7,8,9],
    'nb'   : [1.1,2.1,3.1,4.1]
}

student_df2 = pd.DataFrame(date2)
student_df_con = pd.concat([student_df,student_df2],ignore_index=True)#合併資料,ignore_index = Ture(重新排列index)
# print(student_df_con)

# student_df_con.to_csv('try.csv')#儲存檔案成csv檔    

student_df_del = student_df.drop(['nb'],axis=1) #刪除攔或列 、 axis==>1(欄)/0(列)
# print(student_df_del)

npnan = pd.DataFrame([[np.nan, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [np.nan, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD')) #np.nan = 將無資料設為NaN , columns = 資料Title
# print(npnan)
# print(npnan.fillna('noinf')) #fillna('a') = 將NaN設為a