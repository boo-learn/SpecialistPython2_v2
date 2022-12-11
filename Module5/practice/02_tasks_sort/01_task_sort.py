# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a
import random

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = random.uniform(-30,30)  # Задайте самостоятельно, выбрав произвольное число
total = 0
print(f"{a=}")
for _ in range(len(numbers) - 1):
    if numbers[_] > a : total += numbers[_]

print(total)
