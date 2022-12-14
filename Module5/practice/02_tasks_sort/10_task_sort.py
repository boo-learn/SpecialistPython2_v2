# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

import random

stones_weight = [random.randint(0,100) for i in range(50)]

first_stones_mass = []
second_stones_mass = []

first_stones_mass.append(max(stones_weight))
stones_weight.remove(first_stones_mass[0])

i = 0

while i <= len(stones_weight) - 1:
    if sum(first_stones_mass) > sum(second_stones_mass):
        second_stones_mass.append(stones_weight[i])
    else:
        first_stones_mass.append(stones_weight[i])
    i += 1

if sum(first_stones_mass) / sum(second_stones_mass) < 2:
    print(f"Разница в весе двух куч менее чем в 2 раза")
else:
    print(f"Сделать две кучи с разницов в весе не более чем в 2 раза")
