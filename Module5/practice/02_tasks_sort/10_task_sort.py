# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

from base_sort import sort_choice

vesa = input("Введите веса камней: ")
vesa_arr = []
vesa_arr = vesa.split(" ")
for i in range(len(vesa_arr)):
    vesa_arr[i] = int(vesa_arr[i])
sort_choice(vesa_arr)
vesa_arr.reverse()

vesa1 = []
vesa2 = []

for i in range(len(vesa_arr)):
    if ((i % 2 == 0) or (i == 0)) and sum(vesa1) < (sum(vesa2)):
        vesa1.append(vesa_arr[i])
    elif (i % 2 == 0) and sum(vesa1) > (sum(vesa2)):
        vesa2.append(vesa_arr[i])
    elif (i % 2 == 1) and sum(vesa1) > (sum(vesa2)):
        vesa2.append(vesa_arr[i])
    else:
        vesa1.append(vesa_arr[i])
if sum(vesa1) < (sum(vesa2) * 2):
    print("Первая куча камней:")
    print(*vesa1, sep=', ')
    print("Вторая куча камней:")
    print(*vesa2, sep=', ')
else:
    print("Невозможно разделить поровну кучи камней.")
