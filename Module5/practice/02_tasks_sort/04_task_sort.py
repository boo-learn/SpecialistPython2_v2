# задача 4

# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

sort_choice(numbers)

print(numbers)

biggest = 0

for i in range(1,6):

    if abs(numbers[0]) > abs(numbers[-1]):
        biggest += numbers[0]
        numbers.pop(0)
    elif abs(numbers[0]) < abs(numbers[-1]):
        biggest += numbers[-1]
        numbers.pop(-1)
    else:
        biggest += numbers[0]
        biggest += numbers[-1]
        numbers.pop(0)
        numbers.pop(-1)
        i += 1

print(biggest)
