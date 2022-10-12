# Сумма с условием
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа a

numbers = [2.5, 13.6, 13, -22.4, -12.8, 6.7, 12.8, 21, 4, -22.1]
a = 10  # Задайте самостоятельно, выбрав произвольное число
numbers_sum = 0
i=0
for i in range(len(numbers)):
    if numbers[i] > a:
        numbers_sum += numbers[i]
    i +=1
    
print(numbers_sum)
