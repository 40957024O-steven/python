def timebigsmall(T): #比較時間大小(支援格式 ==> 時:分:秒)
    return int(T[:2] + T[3:5] + T[6:8])

t = '00:20:30'
print(t[:2])
print(t[3:5])
print(t[6:8])
print(timebigsmall(t))