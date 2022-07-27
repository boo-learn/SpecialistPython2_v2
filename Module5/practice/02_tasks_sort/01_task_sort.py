# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 30

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1):
        if j != i and (numbers[i] + numbers[j] > a):
            print(f"{numbers[i]} + {numbers[j]} > {a}")
