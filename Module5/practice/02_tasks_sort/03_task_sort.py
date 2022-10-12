# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]


num_summ = 0
numbers.sort(reverse=True)

for i in range(5):
    num_summ += numbers[i]
    
print(num_summ)
