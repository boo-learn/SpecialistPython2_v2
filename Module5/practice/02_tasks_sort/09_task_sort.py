#!/usr/bin

def bubble_sort(arr):
    for j in range(len(arr)):
        flag = False
        for i in range(len(arr) - j - 1):
            if arr[i] > arr[i + 1]:
                flag = True
                buf = arr[i + 1]
                arr[i + 1] = arr[i]
                arr[i] = buf
        if not flag:
            break
    return arr

def to_list(keytoval):
    outpt = []
    outpt.append(keytoval['surname'])
    outpt.append(keytoval['name'])
    outpt.append(keytoval['position'])
    return outpt

# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]

lst = []
for elem in employees:
    lst.append(to_list(elem))
print(bubble_sort(lst))
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.
