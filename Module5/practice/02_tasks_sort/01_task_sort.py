# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a
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

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 6.7  # Задайте самостоятельно, выбрав произвольное число
sort_choice(numbers)
ind=numbers.index(a)
print(numbers)
print(numbers[ind+1:])
print(sum(numbers[ind+1:]))
