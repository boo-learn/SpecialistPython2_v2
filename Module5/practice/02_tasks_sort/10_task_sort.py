# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

stones = [1, 2, 5, 7, 50, 8, 5, 3, 9, 34, 2, 17, 200]
stones.sort(reverse=True)
pile_1 = []
pile_2 = []
weight_1 = 0
weight_2 = 0
for stone in stones:
    if weight_1 <= weight_2:
        pile_1.append(stone)
        weight_1 += stone
    else:
        pile_2.append(stone)
        weight_2 += stone
if max(weight_1, weight_2) / min(weight_1, weight_2) <= 2:
    print(f'pile: {pile_1}\nweight: {weight_1}\npile: {pile_2}\nweight: {weight_2}')
else:
    print(f'Веса куч отличаются более чем в два раза\n{weight_1} {weight_2}')
