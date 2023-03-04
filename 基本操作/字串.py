word='Hay Google'
print ( word.lower() )#"字串.lower()"代表將字串內字母全部改成小寫
print ( word.upper() )#"字串.upper()"代表將字串內字母全部改成大寫
print ( word.islower() )#判斷字串內是否全部是小寫字母(是的話回傳True)
print ( word.isupper() )#判斷字串內是否全部是大寫字母(是的話回傳True)
print ( word.lower().islower() )#函式可疊加 p.s print(word.islower().lower())<=無法執行
word='Hay Google'
     #0hit
print ( word[2])#[目標位置]字串中目標位置的字母
print ( word[2:6])#[a:b]代表從第a未開始取，取到第b位(不包含第b位)
print ( word[1:])#[a:]代表取a位數之後的文字(包含第a位)
print ( word[:3])#[:a]代表取a位數之前的文字(不包含第a位)
print (word.index('G') )#index('目標字母')字串中目標字母所處位置(若有多個目標，只會回傳最前面的位置)
print (word.replace('o',"0" ))#replacr('替換目標',"替換物")用替換物替換字串中"所有的"替換目標
print (sum(word))