# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

l = [1, 0, 1, 2, 10]
print(l)
max_num = max(l)
l1 = []
l2 = []
l1.append(max_num)
l.remove(max_num)
for num in l:
    if sum(l1) > sum(l2):
        l2.append(num)
    else:
        l1.append(num)
if sum(l1) > sum(l2) * 2:
    print ('Задача не имеет решения')
else:
    print(f'Куча 1:{l1} Куча 2:{l2}')
