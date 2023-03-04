from turtle import color
import matplotlib.pyplot as plt


X = [1,2,3,4,5,6,7]
Y = [2,11,56,156,67,123,8]
ax = plt.subplots()
plt.plot(X,Y,color =  'black',marker = "*",linestyle = '--')
#color = 顏色 ; marker = 點標記 ; linestyle = 線條樣式

plt.xlabel('X座標名稱')
plt.ylabel('Y座標名稱')
plt.axvline(x = 2,c = "r" , ls = "--" , lw = 2) #垂直輔助線 (x/y  = 輔助線位置,c=線條顏色,ls = 線型,lw = 線寬)
plt.axhline(x = 2,c = "r" , ls = "--" , lw = 2) #水平輔助線
plt.savefig('123.png')
plt.yticks(rotation = 0) #旋轉字體角度 ('vertical'=垂直)
plt.show()