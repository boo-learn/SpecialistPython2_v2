# Анализ алгоритма сортировки “пузырьком”
# Массив(список) отсортирован алгоритмом “пузырька”.
# Определите, сколько обменов сделает алгоритм по возрастанию.
import random

def bubble_sort(lst):
    swapped = True
    unsorted_border = len(lst) - 1
    count = 0
    while swapped:
        swapped = False
        for i in range(unsorted_border):
            if lst[i] > lst[i + 1]:
                # Меняем элементы
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                count += 1
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
        unsorted_border -= 1
    print(f"Performed {count} exchanges in list of {len(lst)} elements.")


N = 10
array = [random.randint(-10, 10) for _ in range(N)]
#array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(array)
bubble_sort(array)
