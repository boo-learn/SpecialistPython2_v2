# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
import random


def gen_list(size, at=-100, to=100):
    nums = []
    for _ in range(size):
        nums.append(random.randint(at, to))
    return nums


def bubble_sort(nums):
    swapped = True
    j = len(nums) - 1
    while swapped:
        swapped = False
        # print("*****")
        for i in range(j):
            # print("i = ", i)
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j -= 1


nums = gen_list(20)
print(nums)
abs_nums = list(map(abs, nums))
bubble_sort(abs_nums)
print(abs_nums)
print(sum(abs_nums[-10:]))
