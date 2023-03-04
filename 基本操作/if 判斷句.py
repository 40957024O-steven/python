hungry = True
if hungry:  #若hungry(布林值)是True 則執行if中程式碼
    print ( "吃飯去" )#if中的程式碼

hungry = False
if hungry:  #若hungry(布林值)是False 則"不"執行if中程式碼
    print ( "吃飯去" )#if中的程式碼

print ( "不吃了" )     #if外的程式碼

rainy =True
if rainy:        #True執行if，False執行else
    print ( '帶雨傘')

else:
    print ( "打球去")

print("--------------------------------------------------------------------------------------------")

def text(nb):
    if nb==100:
        print("100分")
    elif nb>=90:
        print("90分以上")
    elif nb>=60:
        print("60分以上")
    else:
        print ("不及格")
    
text(59.996)
