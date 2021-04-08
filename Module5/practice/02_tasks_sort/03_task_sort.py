
# Сумма наибольших
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов
nums = [2, 10, 55, 12, 8, 77, 17, 15, 99, 11, 23, 56, 66]

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

bubble_sort(nums)
#print(nums)
#print(nums[-10:])
print(sum(nums[-10:]))
