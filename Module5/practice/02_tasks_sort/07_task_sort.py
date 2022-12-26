# Призеры олимпиады
# По результатам олимпиады участники награждаются дипломами.
# Набравшие одинаковые  баллы  получают дипломы  одинаковой степени.
# Призером олимпиады считается участник, получивший диплом  не хуже III степени.
# По результатам олимпиады определите количество призеров.
# Вход: натуральное число участников(N < 100) и далее N натуральных# чисел – результаты участников.
# Выход: одно число – число призеров.
# Пример:
# Вход
#
# 10 1 3 4 3 5 6 7 7 6 1
# Выход
# 5
from itertools import groupby
from random import randint


def benchmark(iters=1):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f'[*] Среднее время выполнения: {total / iters} секунд.')
            return return_value

        return wrapper

    return actual_decorator


@benchmark()
def sort_wrapper(numbers):
    numbers.sort()


# способ 1 - с itertools.groupby
@benchmark()
def count_with_groupby(points_list):
    points_list .sort(reverse=True)
    winners = 0
    for i, group in enumerate(groupby(points_list), 1):
        if i > 3:  # призеры - не хужe 3 степени
            break
        points, group_item = group
        for person in group_item:
            winners += 1
    return winners


# cпособ 2 - без itertools.groupby
@benchmark()
def count_simple(points_list):
    points_list.sort(reverse=True)
    i = 1
    winners = 0
    previous_points = points_list[0]
    for points in points_list:
        if points == previous_points:
            winners += 1
        else:
            i += 1
            if i > 3:  # призеры - не хужe 3 степени
                break
            winners += 1
            previous_points = points
    return winners


# способ 3 - без сортировки всего списка
@benchmark()
def count_without_sort(points_list):
    unique_points = list(set(points_list))
    winners = 0
    for i in range(3):  # призеры - не хужe 3 степени
        maximum = max(unique_points)
        winners += points_list.count(maximum)
        unique_points.remove(maximum)
    return winners


n = 100_000_000
points_list = [randint(20, 100) for i in range(n)]
#points_list = [10, 1, 3, 4, 3, 5, 6, 7, 7, 6, 1]
points_list_1 = points_list.copy()
points_list_2 = points_list.copy()
points_list_3 = points_list.copy()

#sort_wrapper(points_list)

print(count_simple(points_list_1))

print(count_with_groupby(points_list_2))

print(count_without_sort(points_list_3))  # в ~3 раза быстрее чем способы с сортировкой
