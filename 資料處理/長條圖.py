import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Taipei Sans TC Beta'] # 這可以讓中文正常顯示



#------長條圖---------
name = ['早1', '安2', '你3', '好4']
nb = [78, 67, 90, 81]

x = np.arange(len(name)) # arange(4) = [0,1,2,3] 
plt.bar(x,nb, color=['red', 'green', 'blue', 'yellow'])
plt.xticks(x,name)
plt.xlabel('Students')
plt.ylabel('Math')
plt.title('Final Term')
plt.axvline(x = 2,c = "r" , ls = "--" , lw = 2) #輔助線 (x/y  = 輔助線位置,c=線條顏色,ls = 線型,lw = 線寬)
plt.xticks(rotation = 75) #旋轉字體角度 ('vertical'=垂直)
plt.show() 


#-----累積長條圖---------
x = range(0,5)
y1 = [2,8,3,12,6]
y2 = [12,3,7,11,4]
y3 = [1,2,3,4,5]
plt.bar(x, y1)
plt.bar(x, y2, bottom=np.array(y1))
plt.bar(x, y3, bottom=np.array(y1)+np.array(y2))
plt.show()
