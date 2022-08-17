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
    return nums


# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10
s = []
for i in range(len(numbers)):
    if numbers[i] > a:
        s.append(numbers[i])

print(sum(s))
# Задайте самост
