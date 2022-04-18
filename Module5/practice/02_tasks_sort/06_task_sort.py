prise_list = [5, 2, 1, 10, 50, 10]
sort_lst = []
for value in prise_list:
    sort_lst.append(prise_list.sort())

c = len(prise_list)//2

max_bill = sum(prise_list[-c:])
print(max_bill)
