prise_list = [5, 2, 1, 10, 50, 10]

prise_list = prise_list.sort()

c = len(prise_list)//2

max_bill = sum(prise_list[-c:])
