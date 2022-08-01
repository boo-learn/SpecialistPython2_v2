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

print("Список сотрудников отсортированный по уменьшению ЗП:")
staff.sort(reverse=True, key=lambda x: (x['salary'], x['surname']))
for person in staff:
    print(person['surname'], person['name'], person['salary'])
#
# # 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

staff.sort(key=lambda x: (x['salary'], x['surname']))
total = 0
for person in staff[:3]:
    total += person['salary']

print(total)

