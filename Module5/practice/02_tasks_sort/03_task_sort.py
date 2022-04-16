# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]


def bubble_sort(nums):
    n = 0
    swapped = True
    while swapped:
        swapped = False
        n += 1
        for i in range(len(nums) - n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


bubble_sort(numbers)
summ = sum(numbers[len(numbers)-5:])
print(summ)
