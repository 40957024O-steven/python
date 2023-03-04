def hello():#函式名稱(英文、數字、底線、開頭不能是數字)
    print("hello")#函式內部，需縮排



def hello(name,age):
    print("hello", name + "，今年" + str(age) +"歲")

hello("steven",17)


def add(first,sceond):
    #print (str(first) + "+" + str(sceond) + "=" + str(first+sceond))<==這只是畫面上呈現，並不是回傳(定義)
    return str(first) + "+" + str(sceond) + "=" + str(first+sceond) #這個才是回傳(並且將add(10,20)定義為"10+20=50")

print(add(10,20))


def add(a,b):
    print ( str(a+b))
    return 10

print (add(2,3)) 



def add(a,b):
    print ( str(a+b))
    #沒寫return就等於return None

print (add(2,3))#這時add(2,3)就變成None 



def add(a,b):
    print (a+b)
    #print (add(a,b))#這個會出現無限多個5
    return 10
    print ("這不會出來")#程式遇到return會直接停止

print(add(3,2))
