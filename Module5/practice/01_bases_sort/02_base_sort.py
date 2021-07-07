# Все алгоритмы сортировки из examples/ оберните в функции

import random

def quick_sort(data, lindex, rindex):
    i = lindex
    j = rindex
    p = (lindex + rindex) // 2
    while True:
        while data[i] < data[p]:
            i += 1
        while data[j] > data[p]:
            j -= 1
        if i <= j:
            if i < j:
                if p == i:
                    p = j
                elif p == j:
                    p = i
                l[i], l[j] = l[j], l[i]
            i += 1
            j -= 1
        if i > j:
            break
    if j > lindex:
        quick_sort(data, lindex, j)
    if i < rindex:
        quick_sort(data, i, rindex)


# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    l = [0 for i in range(size)]
    for i in range(len(l)):
        l[i] = random.randint(at, to)
    return l

l = gen_list(100, -100, 100)
print(l)
quick_sort(l, 0, len(l) - 1)
print(l)
