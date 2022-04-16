# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
bubble_sort(numbers)
print(numbers)
sum = 0
for i in range (5):
    sum += numbers[len(numbers) - 1 - i]
print(sum)
