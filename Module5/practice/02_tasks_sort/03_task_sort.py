# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов
def bubble_sort(nums):
    swapped = True
    cnt = 1
    while swapped:
        swapped = False
        for i in range(len(nums) - cnt):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        cnt += 1


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

bubble_sort(numbers)
summa = sum(numbers[-5:])
print(summa)
