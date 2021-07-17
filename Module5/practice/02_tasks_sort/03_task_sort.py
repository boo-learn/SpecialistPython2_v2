# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

def bubble_sort(lst):
    swapped = True
    not_process = 0
    while swapped:
        swapped = False
        for i in range(len(lst) - 1 - not_process):
            if lst[i] > lst[i + 1]:
                # Меняем элементы
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True


numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]
bubble_sort(numbers)
sum = sum(numbers[-5:])
print(f"{sum:G}")
