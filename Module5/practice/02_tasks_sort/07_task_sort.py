lst = [ 10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1, 8, 9]
lst.sort(reverse=True)
n_lst = list(set(lst))
n_lst.sort(reverse=True)
col=0
for i in range(3):
    col+=lst.count(n_lst[i])

print(col)
