import math


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

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
s = []
c = []
print(numbers)
for number in numbers:
    s.append(abs(number))

    for number in numbers:
        c.append(abs(number))

ind = []
print(s)
print(sort_choice(s))

s.reverse()
s[:5]
print(s[:5])
for number in s[:5]:
    ind.append(c.index(number))


# Задайте самостоятельно, выбрав произвольное число
print(ind)
a = 0
for res in ind:
    a += numbers[res]


print('Ответ ', a)

print("Знаю, что решение не оптимальное, я его доработаю")
