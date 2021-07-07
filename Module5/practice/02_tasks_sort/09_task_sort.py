# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
employees = [
   {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
   {"name": "Иван", "surname": "Петров", "position": "Прораб"},
   {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
   {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.

f_lambda = lambda name: name.lower()
swapped = True

while swapped:
    swapped = False
    for i in range(len(employees) - 1):
        if employees[i]['surname'].lower() > employees[i+1]['surname'].lower():
            employees[i], employees[i+1] = employees[i+1], employees[i]
            swapped = True
        elif employees[i]['surname'].lower() == employees[i+1]['surname'].lower():
            if employees[i]['name'].lower() > employees[i+1]['name'].lower():
                employees[i], employees[i + 1] = employees[i + 1], employees[i]
                swapped = True


for emp in employees:
    print(emp['surname'], emp['name'])
