# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.

def bubble_sort(nums, key=lambda x: x, reverse=False):
    count = 0
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if reverse:
                cond = key(nums[i]) < key(nums[i + 1])
            else:
                cond = key(nums[i]) > key(nums[i + 1])
            if cond:
                count += 1
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1
    print(f'{count=}')


def gen_list(size, at=-100, to=100):
    import random
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


nums = gen_list(10)

bubble_sort(nums)
print(nums)

bubble_sort(nums, key=abs)
print(nums)

bubble_sort(nums, key=abs, reverse=True)
print(nums)
