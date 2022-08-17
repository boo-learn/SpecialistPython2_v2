stones = [2, 5, 7, 9, 4, 1, 11, 14, 19]
stones.sort()
print(stones)
first = []
second = []
if stones[-1] > 2 * sum(stones[:len(stones) - 1]):
    print('Нельзя реализовать')
else:
    first.append(stones[-1])
    for weight in stones[:len(stones) - 1]:
        if sum(first) > sum(second):
            second.append(weight)
        else:
            first.append(weight)

if len(first) != 0:
    print(first)
    print(second)
