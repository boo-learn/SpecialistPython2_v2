# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 10-ти самых больших элементов по модулю.
import random

lst_input = [random.randrange(-20, 20) for _ in range(20)]
print('Исходный список', lst_input)

lst_input = sorted(lst_input, key=lambda x: abs(x))
print('Сортировка по модулю', lst_input)

print('Сумма 10 самых больших чисел', sum(lst_input[-10:]))
