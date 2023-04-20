# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10  # Задайте самостоятельно, выбрав произвольное число

# Без сортировки
sum_num = 0
for num in numbers:
    if num > a:
        sum_num += num
print(sum_num)
print()

# С сортировкой
sum_num = 0
greater = False
numbers.sort()
for num in numbers:
    if num > a and greater == False:
        greater = True
    if greater:
        sum_num += num

print(sum_num)
