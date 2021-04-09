# Телефонная база
# Отсортируйте список телефонов по возрастанию и используя сортировку выбором.
# Телефон задан в виде строки формата nn-nn-nn. Например, 23-45-67

#!/usr/bin

def choice_sort(arr):
    for j in range(len(arr)):
        max = "00-00-00"
        max_index = 0
        for i in range(len(arr) - j):
            if arr[i] > max:
                max = arr[i]
                max_index = i
        arr[max_index] = arr[-1 - j]
        arr[-1 - j] = max
    return arr

phones = ["25-17-58", "11-34-85", "54-61-56", "34-61-72", "25-17-55", "34-56-56"]
print(choice_sort(phones))
