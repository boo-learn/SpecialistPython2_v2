import random


def stone_generator(numb):
    dct = {}
    for i in range(numb):
        lst = random.sample(range(1, 100), numb)
        dct[i+1] = lst[i]
    return dct


stones = stone_generator(28)
lst_of_weight = [weight for weight in stones.values()]
lst_of_weight.sort(reverse=True)

part1 = lst_of_weight[len(lst_of_weight)//2:]
part2 = lst_of_weight
for i in part1:
    part2.remove(i)

if part1 == [0] or part2 == [0]:
    print("Недостаточно камней для 2-х куч")
elif not part1 or not part2:
    print("Недостаточно камней для 2-х куч")

while sum(part1)*2 >= sum(part2):
        stone = part1.pop()
        part2.insert(0, stone)


while True:
    if sum(part2[:-1]) >= (sum(part1)+part2[-1])*2:
        stone = part2.pop()
        part1.insert(0, stone)
    else:
        break


print(sum(part1), sum(part2))
