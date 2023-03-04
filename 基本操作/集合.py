
alpha = set()#建立空集合
beta = {1,2,3,4,5.6,7/8}#建立集合
taget = range(10,20,2)#range(起始數字,末位數字,間格)
gamma = set([i for i in taget] )
delta = set((1,1,2,3,2,3,3,5,-1))#若數字重複只會出現一次
print (alpha)
print (beta)
print (taget)
print (gamma)
print (delta)

delta.add(1/2)#在集合中增加元素(1/2)
print (delta)
delta.remove(2)#移除集合中的元素(無論有多少個)
print (delta)

print (len(delta))#集合長度
print (sum(delta))#集合總和
print (max(delta))#集合最大直
print (min(delta))#集合最小值

print (delta)
print (2 in delta)#判斷數字在集合中是否為真
print (2 not in delta)#判斷數字不在集合中是否為真

print(delta)
for i in delta:
    print(i,end='')#輸出集合(輸出為字串)

print()#不加這個29行會跟33行輸出在同一個結果行上
A = {1, 6, 8, 10, 20}
B = {1, 3, 8, 10}
print ( A.union(B) )#聯集
print ( A | B )#聯集
print ( A.intersection(B) )#交集
print ( A & B )#交集
print ( A.difference(B) )#差集(A比B多出的元素)
print ( A - B )#差集(A比B多出的元素)
print ( A.symmetric_difference(B) )#對稱差集
print ( A ^ B )#對稱差集

print ( A.issubset(B) )#判斷A是否為B的子集合
print ( B.issuperset(A) )#判斷B是否為A的超集合
setA = {1, 6, 8}
setB = {1, 6, 8, 10, 20}
print ( setA.issubset(setB) )
print ( setB.issuperset(setA) )
print(setA == setB)#集合相等是否為真
print(setA != setB)#集合不相等是否為真