# Сумма наибольших
# Дан список чисел.
# Найти: сумму 5-ти самых больших элементов

numbers = [-2.5, 13.6, -13, -22.4, -12.8, -6.7, 12.8, -21, 4, -22.1, 0]


def sort_choice(lst):
    i = 0
    while i < len(lst) - 1:
        m = i
        j = i + 1
        while j < len(lst):
            if lst[j] < lst[m]:
                m = j
            j += 1
        lst[i], lst[m] = lst[m], lst[i]
        i += 1


sort_choice(numbers)
total = sum(numbers[-6:-1])
print(total)

