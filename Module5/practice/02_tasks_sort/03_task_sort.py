# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов


def bubble_sort(nums):
    swapped = True
    stage = 0
    while swapped:
        swapped = False
        for i in range(len(nums) - 1 - stage):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
        stage += 1


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
cnt = 5

# print(numbers)
# bubble_sort(numbers)
# print(numbers)
sum_max = sum(numbers[:cnt])
print(sum_max)
