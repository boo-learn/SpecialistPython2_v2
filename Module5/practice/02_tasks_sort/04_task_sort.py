#!/usr/bin

# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.

def bubble_sort(nums):
    j = 1
    count = 0
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - j):
            count += 1
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        j += 1
    print(count)

nums = list(input().split(" "))
for i in range(len(nums)):
    nums[i] = int(nums[i])
nums = bubble_sort(nums)
nums = nums[-10:]
sum = 0
for num in nums:
    sum += abs(num)
print(sum)

