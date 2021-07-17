# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
a = -3
b = 7
sum = 0
if a <= b:
    for i in range(len(numbers)-1):
        if b > numbers[i] > a:
            sum = sum + numbers[i]
    print(f"{sum=}")
