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
        'surname': 'Иванов',
        'salary': 34500
    },
]

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
staff.sort(key=lambda x: x['surname'])
staff.sort(reverse=True, key=lambda x: x['salary'])
print("Список сотрудников отсортированный по уменьшению ЗП:")
for person in staff:
    print(person['name'], person['surname'], person['salary'])

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
staff.sort(key=lambda x: x['salary'])
sum_salary = 0
for person in staff[:3]:
    sum_salary += person['salary']
print("Сумма зарплат трех самых низкооплачиваемых сотрудников:", sum_salary)
