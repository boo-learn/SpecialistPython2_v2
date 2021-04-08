import random


def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1 - j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1


def gen_list(size, at=0, to=100):
    data = []
    for _ in range(size):
        data.append(random.randint(at, to))
    return data


nums = gen_list(20)
print(nums)
abs_nums = list(map(abs, nums))
bubble_sort(abs_nums)
print(abs_nums)
print(sum(abs_nums[-10:]))


