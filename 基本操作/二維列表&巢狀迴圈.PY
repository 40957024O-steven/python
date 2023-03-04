dblist=[
    [0,1,2,3],
    [1,2,3,4],
    [2,3,4],
    [19]
]#二維列表=列表中還有一個列表；中括號越多 維度越高
print (dblist[2][1])


for row in dblist :#列表中抓出大單元==>[0,1,2,3]
    for col in row :#大單元中抓出元素==>0
        print (col)
img = [[]for i in range(10)] #創建10行的二維列表