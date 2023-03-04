def split_list(l, n):
  # 將list分割 (l:list, n:每個matrix裡面有n個元素)
  for idx in range(0, len(l), n):
    yield l[idx:idx+n]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(split_list(l, 3)) #將list分割成每份中有3個元素
print(result)