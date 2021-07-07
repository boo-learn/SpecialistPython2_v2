import random

count = 0
def quick_sort(data, lindex, rindex):
    count = 0
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
                count += 1
            i += 1
            j -= 1
        if i > j:
            break
    if j > lindex:
        quick_sort(data, lindex, j)
    if i < rindex:
        quick_sort(data, i, rindex)
    return count

# Напишите функцию для заполнения списка случайными числами
def gen_list(size, at=-100, to=100):
    return [random.randint(at, to) for _ in range(size)]

# 1000 - 499500

l = gen_list(1000, -100, 100)
print(l)
print("count:", quick_sort(l, 0, len(l) - 1))
print(l)
