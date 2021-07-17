# Дан список сотрудников:
from pprint import pprint

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
staff.sort(key=lambda emp: (emp['salary'], emp['surname'], emp['name']), reverse=True)

print("Список сотрудников отсортированный по уменьшению ЗП:")
pprint(staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
res = sum(map(lambda emp: emp['salary'], staff[-3:]))
print(res)
# Или
sum_salary = 0
for emp in staff[-3:]:
    sum_salary += emp['salary']
print(sum_salary)
