# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]

def sort_choice(employees):
    i = 0
    while i < len(employees) - 1:
        m = i
        j = i + 1
        while j < len(employees):
            if employees[j]["surname"] < employees[m]["surname"]: #Скрипт сортировки скорректиров в части фамилий
                m = j
            elif employees[j]["surname"] == employees[m]["surname"]: #Скрипт сортировки скорректиров в части фамилий
                if employees[j]["name"][0] < employees[m]["name"][0]: #Скрипт сортировки скорректиров в части имён
                    m = j
            j += 1
        employees[i], employees[m] = employees[m], employees[i]
        i += 1
sort_choice(employees)
#print(employees)
employees_names = []
for man in employees:
    employees_names.append(man["surname"] + " " + man["name"])
print(*employees_names, sep=', ')
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.
