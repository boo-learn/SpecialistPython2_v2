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

for _ in employees:
    i = 0
    while i < len(employees) - 1:
        if employees[i].get("surname") > employees[i + 1].get("surname"):
            employees[i], employees[i + 1] = employees[i + 1], employees[j]
        elif employees[i].get("surname") == employees[i + 1].get("surname") \
                and employees[i].get("name") > employees[i + 1].get("name"):
            employees[i], employees[i + 1] = employees[i + 1], employees[i]
        i += 1
for el in employees:
    print(f"{el.get('name')} {el.get('surname')}")
