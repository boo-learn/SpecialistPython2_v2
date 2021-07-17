# Сумма наибольших по модулю
# Дан массив(список) чисел.
# Найти: сумму 5-ти самых больших элементов по модулю.
# Пояснение: сравниваем элементы по модулю, а в сумму добавляем сами значения элементов(без модуля)
# В примере ниже, два самых больших по модулю числа это: -22.4 и 21.1. Они самые большие по модулю, а их сумма = -1.3

def bubble_sort(lst):
    swapped = True
    not_process = 0
    while swapped:
        swapped = False
        for i in range(len(lst) - 1 - not_process):
            if abs(lst[i]) > abs(lst[i + 1]):
                # Меняем элементы
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, 21.1, 0]
bubble_sort(numbers)
summa = sum(numbers[-5:])
print(f"{summa:G}")
