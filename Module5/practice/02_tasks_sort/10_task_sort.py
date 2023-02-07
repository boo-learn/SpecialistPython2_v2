from random import randint

N = int(input())
rocks = list(set([randint(1, 50) for _ in range(N)]))

rocks.sort(reverse=True)
print(rocks)

middle = sum_rocks // 2
bunch_of_rocks = []

if max(rocks) / (sum(rocks) - max(rocks)) > 2:
    print('Этого сделать нельзя')


while sum(bunch_of_rocks) < middle:
    bunch_of_rocks.append(rocks[0])
    rocks = rocks[1:]

if sum(bunch_of_rocks) < sum(rocks):
    check = sum(bunch_of_rocks) / sum(rocks)
else:
    check = sum(rocks) / sum(bunch_of_rocks)

print(rocks)
print(bunch_of_rocks)
print(check)

