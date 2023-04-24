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
sorted_staff = sorted(staff, key=lambda x: (-x['salary'], x['surname'], x['name']))

print("Список сотрудников отсортированный по уменьшению ЗП:")
for s in sorted_staff:
    print(s['surname'], s['name'], s['salary'])

lowest_salaries = [s['salary'] for s in sorted_staff[-3:]]
total_salary = sum(lowest_salaries)
print("Сумма зарплат трех самых низкооплачиваемых сотрудников:", total_salary)
