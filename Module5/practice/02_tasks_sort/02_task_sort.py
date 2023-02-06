# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

def sort(nums) -> list:
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

    return nums


numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = -12.8  # Задайте самостоятельно, выбрав произвольное число
b = 21  # Задайте самостоятельно, выбрав произвольное число

number_a = 0
number_b = 0

sort_numbers = sort(numbers)

for i, j in enumerate(sort_numbers):
    if a == j:
        number_a = i
    if b == j:
        number_b = i

print(sum(sort_numbers[number_a + 1: number_b]))
