from random import randint

def mass(stones):
    massa = 0
    for stone in stones:
        massa += stone
    return massa


count_stones = 4
list_stones = [randint(1, 100) for stone in range(count_stones)]
list_stones.sort(reverse=True)
print(f"Все камни: {list_stones}")
stones1 = []
stones2 = []
mass1 = 0
mass2 = 0
for i in range(len(list_stones)):
    if mass(stones1) > mass(stones2):
        stones2.append(list_stones[i])
        mass2 += list_stones[i]
    else:
        stones1.append(list_stones[i])
        mass1 += list_stones[i]
if mass1 / mass2 > 2 or mass2 / mass1 > 2:
    print('Сортировка не возможна')
else:
    print(f"Куча №1: {stones1}")
    print(f"Куча №2: {stones2}")
    print(f"Масса кучи №1: {mass1}")
    print(f"Масса кучи №2: {mass2}")
