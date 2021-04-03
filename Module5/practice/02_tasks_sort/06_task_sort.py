import random


def bubble_sort(nums, key=lambda x: x, reverse=False):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1


def gen_list(size, at=0, to=100):
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))
    return data


nums = gen_list(20)
bubble_sort(nums, reverse=True)
print(nums)

place = nums[0]
steps = 0
num_peoples = 0
for el in nums:
    num_peoples+=1
    if el < place:
        steps+=1
        place = el
    if steps > 2:
        break

print(num_peoples)


