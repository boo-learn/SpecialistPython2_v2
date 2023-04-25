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


# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
# def rule(employee: dict) -> tuple:
#     return -employee['salary'], employee['surname'], employee['name']


# staff.sort(key=rule)
staff.sort(key=lambda employee: (-employee['salary'], employee['surname'], employee['name']))

print("Список сотрудников отсортированный по уменьшению ЗП:")
for emp in staff:
    print(f"{emp['surname']} {emp['name']} {emp['salary']}")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
sum_salary = 0
for emp in staff[-3:]:
    sum_salary += emp['salary']

print(sum_salary)
