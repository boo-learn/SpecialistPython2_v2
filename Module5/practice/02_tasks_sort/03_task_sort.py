# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]

n = 0
swapped = True
while swapped:
    swapped = False
    n += 1
    for i in range(len(numbers) - n):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

summ = 0
for numb in numbers[:5:-1]:
    summ += numb
