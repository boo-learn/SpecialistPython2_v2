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

count_el=len(employees)
employees_sort_name=[]
employees_sort_surname=[]
for el in range(count_el):
    min_name=min(employees,key=lambda el:el["name"])
    employees_sort_name.append(min_name)
    employees.remove(min_name)
for el in range(count_el):
    min_surname=min(employees_sort_name,key=lambda el:el["surname"])
    employees_sort_surname.append(min_surname)
    employees_sort_name.remove(min_surname)
for el in employees_sort_surname:
    print(el["surname"], el["name"])
