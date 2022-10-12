
lst = [2, 1 ,33 ,10 , 50 , 10]
lst.sort()
print(sum(lst[- ( len(lst)//2 + len(lst)%2):]))
