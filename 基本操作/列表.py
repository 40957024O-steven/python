alpha = [10,20,'中文字','english',True,False]#列表可以存放這些 (True = 1 , False = 0)
print (alpha)
beta = [10,20,30,40,50]
print (beta[0])#查詢列表中某一位資料
print (beta[-1])#負號代表從後面算起
print (beta[1:4])#[a:b]代表從第a未開始取，取到第b位(不包含第b位)
print (beta[1:])#[a:]代表取a位數之後的數字(包含第a位)
print (beta[:3])#[:a]代表取a位數之前的數字(不包含第a位)
alpha[3]=70#[a]改第a位的東西
print (alpha)
print("----------------------------------------------------------------------")
alpha = [10,20,'中文字','english',True,False]
beta = [10,20,30,40,50]
gamma = ['a','b','c','d']
alpha.extend(beta)#銜接兩個列表(新列表名稱為extend前面的列表)
print (alpha)
alpha = [10,20,'中文字','english',True,False]
alpha.append(30) #在列表後面加值
print (alpha)
alpha = [10,20,'中文字','english',True,False]
alpha.insert(2,30)#(a,b)代表在第a位插入一個b
print (alpha)
alpha = [10,20,'中文字','english',True,False,10]
alpha.remove(10)#移除某個值
alpha.remove("中文字")
print (alpha)
alpha.remove(10)
print (alpha)#一次只會移除一項值(跟集合的差別在這)
alpha = [10,20,'中文字','english',True,False]
alpha.clear()#把列表清空
print (alpha)
alpha = [10,20,'中文字','english',True,False]
alpha.pop(2)#pop(a)=清除第a位的值(若為空白則清除最後一位)
print (alpha)
alpha = [10,20,5,90,20,30]
alpha.sort()#排列列表(由小到大)
print (alpha)
alpha = [10,20,'中文字','english',True,False]
alpha.reverse()#反轉列表
print (alpha)
alpha = [10,20,'中文字','english',True,False,10]
print (alpha.index(10))#只會回傳最前面的值
alpha = [10,20,'中文字','english',True,False,10,20,10]
print (alpha.count(10))#count(a)=計算有幾個a值