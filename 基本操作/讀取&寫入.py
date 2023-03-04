# open("檔案路徑",mode="開啟模式",encoding="編碼方式") <==開啟檔案

# mode = "r" 讀取
# mode = "w" 覆寫
# mode = "a" 增加

# file = open ("try.txt" , mode= "r")
# print(file.read())
# print(file.readline())
# print(file.readlines())
# file.close

# file = open ("try.txt" , mode= "w")
# file.write("複寫內容")
# file.close

file = open ("try.txt" , mode= "a",encoding="utf-8")
file.write("增加內容")
file.write("\n還可以在下一行")
file.close

with open ("try.txt" , mode= "a",encoding="utf-8") as file:#自動關閉
    file.write("自動關閉的東東")