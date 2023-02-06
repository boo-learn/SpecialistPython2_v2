# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

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


numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 2.5  # Задайте самостоятельно, выбрав произвольное число

number = 0
sort_numbers = sort(numbers)

for i, j in enumerate(sort_numbers):
    if a == j:
        number = i
        print(sum(sort_numbers[number + 1:]))


