# Дан список сотрудников:
staff = [
    {
        'name': 'Григорий',
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

names_list = []
surname_list = []
salary_list = []

for entry in staff:
    _ = []
    for key, value in entry.items():
        _.append(value)
    names_list.append(_[0])
    surname_list.append(_[1])
    salary_list.append(_[2])

for i in range(len(salary_list) - 1):
    for j in range(len(salary_list) - 1):
        if salary_list[j] > salary_list[j + 1]:
            salary_list[j], salary_list[j + 1] = salary_list[j + 1], salary_list[j]
            surname_list[j], surname_list[j + 1] = surname_list[j + 1], surname_list[j]
            names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]
        if salary_list[j] == salary_list[j + 1]:
            if surname_list[j] > surname_list[j + 1]:
                salary_list[j], salary_list[j + 1] = salary_list[j + 1], salary_list[j]
                surname_list[j], surname_list[j + 1] = surname_list[j + 1], surname_list[j]
                names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]
        if salary_list[j] == salary_list[j + 1] and surname_list[j] == surname_list[j + 1]:
            if names_list[j] > names_list[j + 1]:
                salary_list[j], salary_list[j + 1] = salary_list[j + 1], salary_list[j]
                surname_list[j], surname_list[j + 1] = surname_list[j + 1], surname_list[j]
                names_list[j], names_list[j + 1] = names_list[j + 1], names_list[j]

print(f"{names_list}")  ##
print(f"{surname_list}")  ##
print(f"{salary_list}")  ##
print("------------------------------")
# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
print(f"Список сотрудников отсортированный по уменьшению ЗП:{names_list[::-1]}")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
print(f"сумма зарплат трех самых низкооплачиваемых сотрудников: {sum(salary_list[:3])}")
