
name = input ( "請輸入你的名字：" )#從用戶端定義name
age = input ( "年紀?" )#得到的是字串(無論輸入為和都會預設成字串)
print ( name ,"今年" + age +"歲")
#基本計算機(支援家法)
nb1 = input ("第一個數")
nb2 = input ("第二個數")
#print ( nb1 + nb2 )#會定義nb1以及nb2為文字，並執行文字的相加
print ( int(nb1) + float(nb2) )#int=將字串轉換為整數、float=將字串轉換為有小數點的數字

print("--------------------------------------------------------------------------------------------")
#進階計算機(支援加減乘除)
f1 = float(input ("請輸入第一個數字："))
op = input ("請輸入運算符號：")
s2 = float(input ("請輸入第二個數字："))
if op == "+":
    print (f1+s2)
elif op == "-":
    print (f1-s2)
elif op == "*":
    print (f1*s2)
elif op == "/":
    print (f1/s2)
elif op == "^":
    print (pow(f1,s2))
else: 
    print ("無效運算元")