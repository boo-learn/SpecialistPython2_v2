# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = -2  # Задайте самостоятельно, выбрав произвольное число
b = 13  # Задайте самостоятельно, выбрав произвольное число


def sort_choice(nums):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j] < nums[m]:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


sort_choice(numbers)
list = []
for num in numbers:
    if b > num > a:
        list.append(num)
print(sum(list))
