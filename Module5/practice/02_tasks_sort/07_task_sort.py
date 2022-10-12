lst = [ 10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 9, 1]
n_lst = list(set(lst))
col=0
for i in n_lst[-3:]:
    col+=lst.count(i)
