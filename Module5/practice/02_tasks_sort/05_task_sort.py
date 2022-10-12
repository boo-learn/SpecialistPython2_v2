def sort_choice(staff):
    print("before sort = ", staff)
    i = 0
    while i < len(staff) - 1:
        m = i
        j = i + 1
        while j < len(staff):
            if (staff[j]['salary'] > staff[m]['salary']) or ((staff[j]['salary'] == staff[m]['salary']) and (staff[j]['surname'] < staff[m]['surname'])):
                m = j
            j += 1
        staff[i], staff[m] = staff[m], staff[i]
        i += 1
    print("after sort = ", staff)


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
        'surname': 'Юрьев',
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
sort_choice(staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:

sum = staff[-1]['salary'] + staff[-2]['salary'] + staff[-3]['salary']
print(f"SUM = {sum}")
