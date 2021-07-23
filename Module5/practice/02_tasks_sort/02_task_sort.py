# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.
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
numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = 4  # Задайте самостоятельно, выбрав произвольное число
b = 13.6  # Задайте самостоятельно, выбрав произвольное число

sort_choice(numbers)
ind_a=numbers.index(a)
ind_b=numbers.index(b)
print(numbers)
print(numbers[ind_a+1:ind_b])
print(sum(numbers[ind_a+1:ind_b]))
