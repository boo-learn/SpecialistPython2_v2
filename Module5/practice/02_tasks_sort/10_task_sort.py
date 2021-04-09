# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.

def gen_list(size, at=-100, to=100):
    import random
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


rocks = gen_list(5, 1, 100)
print(rocks)
max_weight = max(rocks)
pile1 = []
pile2 = []
pile1.append(max_weight)
rocks.remove(max_weight)
for rock in rocks:
    if sum(pile1) > sum(pile2):
        pile2.append(rock)
    else:
        pile1.append(rock)
if sum(pile1) > sum(pile2) * 2:
    print('Нельзя распределить камни указанным образом')
else:
    print(f'{pile1=} {pile2=}')
