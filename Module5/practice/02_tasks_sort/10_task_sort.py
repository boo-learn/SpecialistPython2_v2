#import random

def choice_sort(nums, reverse = False, key = lambda n: n):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if reverse:
                condition = key(nums[j]) > key(nums[m])
            else:
                condition = key(nums[j]) < key(nums[m])
            if condition:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1

stones = [3, 5, 9, 4, 39, 4, 23, 15, 18]
#stones = [random.randint(1, 1000) for _ in range(2)]
stones1 = []
stones2 = []
choice_sort(stones, True)

for stone in stones:
    if sum(stones1) <= sum(stones2):
        stones1.append(stone)
    else:
        stones2.append(stone)


if 0.5 <= sum(stones1) / sum(stones2) <= 2:
    print("Суммарный вес камней в первой куче: ", sum(stones1))
    print("Суммарный вес камней во второй куче: ", sum(stones2))
else:
    print("Разбить кучи нельзя")



# Камни*
# Имеется N камней веса А1,А2,...,АN.
#
# Необходимо разбить их на две кучи таким образом, чтобы веса куч отличались не более чем в 2 раза.
# Если этого сделать нельзя, то указать это
