#跟集合、列表功能幾乎一樣，但是元組不能修改，可以使資料更安全，用於固定數據

from operator import index


ston = (10,20,30,40,90,70)#無法修改，可以查詢
print (ston)
print (ston[1:3])
print (ston[2])
print (len(ston)) #列表長度
print (max(ston))
print (min(ston))
print (sum(ston))
print(ston.index(10))