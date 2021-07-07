# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]


def sort_choice(lst, reverse=False):
    i = 0
    while i < len(lst) - 1:
        m = i
        j = i + 1
        while j < len(lst):
            if reverse:
                cond = lst[j] > lst[m]
            else:
                cond = lst[j] < lst[m]
            if cond:
                m = j
            j += 1
        lst[i], lst[m] = lst[m], lst[i]
        i += 1


print(phones)
sort_choice(phones)
print(phones)
