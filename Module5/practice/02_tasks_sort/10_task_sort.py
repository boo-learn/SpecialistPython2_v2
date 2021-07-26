# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

import random

stones = [random.randint(2, 50) for _ in range(25)]
print(stones)
stones.sort()
bunch_1 = 0
bunch_2 = 0
flag = True
for stone in stones:
    if flag:
        bunch_1 += stone
    else:
        bunch_2 += stone
    flag = not flag
print('Вес 1-ой кучи камней: ', bunch_1)
print('Вес 2-ой кучи камней: ', bunch_2)
if bunch_1/bunch_2 > 2 or bunch_2/bunch_1 > 2:
    print('Не удалось разделить камни на две кучи с отличием в весе меньше 2-х раз')
else:
    print('Соотношение весов куч составило: ', bunch_1/bunch_2 if bunch_1/bunch_2 > 1 else bunch_2/bunch_1)
