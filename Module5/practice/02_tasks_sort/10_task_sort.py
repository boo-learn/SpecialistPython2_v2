# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

kamni = [50, 2, 24, 8, 5, 56, 17, 85, 29, 10]
kamni.sort()
split_index = len(kamni) // 2
lst1 = kamni[:split_index]
lst2 = kamni[split_index:]
while True:
    if sum(lst2) > sum(lst1) * 2:
        lst1.append(lst2.pop(0))
    elif sum(lst1) > sum(lst2) * 2:
        lst2.append(lst1.pop(-1))
    else:
        break

print(lst1, lst2)
