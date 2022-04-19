# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:

def names(employees):
    employees.sort(key=lambda employee: (employee['surname'], employee['name']))
    for employee in employees:
        print(employee['surname'], employee['name'])

employees = [
    {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
    {"name": "Иван", "surname": "Петров", "position": "Прораб"},
    {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
    {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]

# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.
names(employees)
