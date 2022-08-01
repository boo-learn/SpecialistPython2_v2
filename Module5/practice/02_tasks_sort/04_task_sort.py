# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

from base_sort import sort_choice
numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
numbers2 = numbers
index=[]


for i in range(len(numbers)):
    if numbers2[i] < 0:
        numbers2[i] = abs(numbers[i])
        index.append(i)

sort_choice(numbers2, reverse = True)

for i in index:
    numbers[i] = numbers[i] * -1

print(numbers[:5])

print(index)

sum_num = sum(numbers[:5])

print(sum_num)
