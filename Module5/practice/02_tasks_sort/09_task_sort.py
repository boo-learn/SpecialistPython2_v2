# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]
names = []
surnames = []
fullname = []
i = 0
for var in employees:
    names.append(var.get('name'))
    surnames.append(var.get('surname'))
    fullname.append(f'{surnames[i]} {names[i]}')
    i += 1
fullname.sort()
print(fullname)
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.
