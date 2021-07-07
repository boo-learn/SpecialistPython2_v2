# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов

def gen_list(size):
    import random
    return [random.randint(-100, 100) for _ in range(size)]

def bubble_sort(nums):
    swapped = True
    j = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - j):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        j += 1


nums = [2, 4, 1, 4, -10, 5, -20, 5, 3, 2]
print("nums =", nums)
bubble_sort(nums)
k = 0
sum_max = 0
while k < 5:
    max_n = max(nums)
    sum_max = sum_max + max_n
    k += 1
    nums.remove(max_n)

print(sum_max)
