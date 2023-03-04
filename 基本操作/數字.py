from cmath import sqrt
import math 
import random
import numpy as np

print ( 11 )#輸出數字(可正or負or小數點)
print ( 10+3-2*(2+2)+4/2 )#加減乘除(符合先乘除後加減)(和括號內先執行)
print ( 8//3 )#"//"代表整數除法
eight = 8
print ( eight%5 )#"%"代表取餘數
print ( str(eight) )#將數字轉換為字串
a = str(22)
print (int(a))#字串轉換為數字(整數)
b = a.zfill(4) #在數字(必須是字串形式)前面補0 .zfill(n) ==> n = 全部幾位數 ex b=0022
print(b)
print (float(1.77)) #將字串轉為數字(有小數)
eight = -8
print ( abs(eight) )#取絕對值
print ( pow(4,-1/2) )#次方(pow(a,b)=>a^b)a的b次方
print ( max(2,3,4,5,6,10))#取最大值
print ( min(2,3,4,5,6,10))#取最小值
print ( round(4.5555,2) )#四捨五入(數字,到小數點後幾位(沒寫就是整數位))(偶數會有bug)
from math import * #要用根號時要import的東東
print ( floor(2.1323424) )#無條件捨去
print ( ceil(2.1323424) )#無條件進位
print ( sqrt(81) )#開根號
a = random.randint(-100,100) #產生隨機數字
print(a)
print(math.cos(75*np.pi/180)) # 這才是角度