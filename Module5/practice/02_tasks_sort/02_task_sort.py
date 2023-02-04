# Сумма из диапазона
# Дан список чисел.
# Найти: сумму элементов списка, больших данного числа А, но меньше B.
from base_sort import sort_choice

numbers = [-2.5, 13.6, 13, -22.4, -12.8, 12.8, 21, 4, 22.1, 3]
#print(numbers)
a = 0
b = 15

#Отсортируем список по возрастанию
sort_choice(numbers)
#развернём список в обратную сторону
numbers.reverse()
#print(numbers)
#Вводим переменную суммы
sumv = 0
#Считаем все переменные в списке. Как дойдём до переменной меньше а - прекращаем цикл for
for var in numbers:
    if var > a:
        if var < b:
            sumv += var
    else:
        break
print(sumv)
