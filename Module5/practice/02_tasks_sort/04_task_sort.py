# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]

sum = 0
for i in range(5):
    max = numbers[1]
    index_max = 0
    i = 0
    for num in numbers:
        if abs(num) > abs(max):
            max = num
            index_max = i
        i += 1
    sum = sum + max
    numbers.pop(index_max)

print(f"SUM = {sum}")

stri = ''
for num in numbers:
    stri = stri + ',' + str(num)
print(stri[1:])
