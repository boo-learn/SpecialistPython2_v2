from random import randint
from base_sort import sort_choice

# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это.


a = int(input(f'Введите количество камней: '))

stone = []

for i in range(a):
    stone.append(randint(1, 1000))


sort_choice(stone)
stone.reverse()

s1 = [stone[0]]
s2 = []
a = sum(stone)

for i in stone[1:]:
    if sum(s1) + i < a/2:
        s1.append(i)
    else:
        s2.append(i)

if sum(s2) / sum(s1) >= 0.5 and sum(s2) / sum(s1) <= 2:
    print(sum(s1))
    print(sum(s2))
else:
    print(sum(s1))
    print(sum(s2))
    print(f'Невозможно разбить на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза')
