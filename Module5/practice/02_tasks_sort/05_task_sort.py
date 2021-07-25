# Дан список сотрудников:
staff = [
    {
        'name': 'Алексей',
        'surname': 'Петров',
        'salary': 124300
    },
    {
        'name': 'Николай',
        'surname': 'Петров',
        'salary': 120000
    },
    {
        'name': 'Иван',
        'surname': 'Павлов',
        'salary': 34500
    },
    {
        'name': 'Василий',
        'surname': 'Кукушкин',
        'salary': 162500
    },
    {
        'name': 'Василий',
        'surname': 'Павлов',
        'salary': 34500
    },
]

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
print("Список сотрудников отсортированный по уменьшению ЗП:", )

for _ in range(len(staff)): #Сортировка по уровню з/п
    i = 0
    while i < len(staff) - 1:
        if staff[i].get("salary") < staff[i + 1].get("salary"):
            staff[i], staff[i + 1] = staff[i + 1], staff[i]
        i += 1
for _ in staff: #Сортировка по имени и фамилии (сначала сравниваются фамилии потом имена у однофамильцев)
    j = 0
    while j < len(staff) - 1:
        if staff[j].get("salary") == staff[j + 1].get("salary"):
            if staff[j].get("surname") > staff[j + 1].get("surname"):
                staff[j], staff[j + 1] = staff[j + 1], staff[j]
            elif staff[j].get("surname") == staff[j + 1].get("surname") \
                    and staff[j].get("name") > staff[j + 1].get("name"):
                staff[j], staff[j + 1] = staff[j + 1], staff[j]
        j += 1
for el in staff:
    print(f"{el.get('name')}, {el.get('surname')}, {el.get('salary')}")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

sum_min_salaries = 0
for el in staff[-3:]:
    sum_min_salaries += el.get("salary")
    
print(f"Cумма зарплат трех самых низкооплачиваемых сотрудников равне: {sum_min_salaries}")

