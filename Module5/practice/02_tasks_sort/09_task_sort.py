# Список сотрудников
# Дан список, элементами которого являются сотрудники, представленные в виде словаря(dict).
# Пример данных:
from pprint import pprint

employees = [
    {"name": "Петр", "surname": "Алексеев", "position": "Инженер"},
    {"name": "Иван", "surname": "Петров", "position": "Прораб"},
    {"name": "Алексей", "surname": "Петров", "position": "Строитель"},
    {"name": "Иван", "surname": "Сидоров", "position": "Строитель"},
]
# Выведите список сотрудников(без указания должности) в формате: Фамилия Имя, в отсортированном порядке.
# Примечание: если фамилии сотрудников совпадают, при сортировке учесть имя.

# Вариант 1 - с созданием списка и его сортировка
emp_list = [f'{item["surname"]} {item["name"]}' for item in employees]
emp_list.sort()
print(emp_list)

# Вариант 2 - сортировка словаря перед выводом
employees = sorted(employees, key=lambda item: item["name"])
employees = sorted(employees, key=lambda item: item["surname"])
pprint(employees, sort_dicts=False)
