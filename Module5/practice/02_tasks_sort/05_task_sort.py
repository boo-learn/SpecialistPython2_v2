
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


def sort_by_salary(staff, reverse=False):
    salary_list = []
    result = []
    for person in staff:
        if person['salary'] not in salary_list:
            salary_list.append(person['salary'])
    if reverse:
        salary_list = sorted(salary_list, reverse=True)
    else:
        salary_list = sorted(salary_list, reverse=False)
    print(salary_list)
    for salary in salary_list:
        for person in staff:
            if salary == person['salary']:
                result.append(person)
    return result


print("Список сотрудников отсортированный по уменьшению ЗП:", sort_by_salary(staff, reverse=True))

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
result = sort_by_salary(staff)
summa = 0
for person in result[:3]:
    summa += person['salary']
print(f'{summa} рублей')

