#!/usr/bin

# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.


nums = list(input().split(" "))
for i in range(len(nums)):
    nums[i] = int(nums[i])
max_list = []
for _ in range(10):
    max_list.append(0)
for i in range(10):
    for num in nums:
        if abs(num) > max_list[i]:
            max_list[i] = num
sum = 0
for elem in max_list:
    sum += elem

