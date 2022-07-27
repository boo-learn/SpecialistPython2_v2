def bubble_sort_staff(employee):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(staff) - 1):
            if employee[i]['salary'] > employee[i + 1]['salary']:
                # Меняем элементы
                employee[i], employee[i + 1] = employee[i + 1], staff[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
            elif employee[i]['salary'] == employee[i + 1]['salary'] and employee[i]['surname'] > employee[i + 1][
                'surname']:
                # Меняем элементы
                employee[i], employee[i + 1] = employee[i + 1], staff[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return employee


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
    }
]

# 1. Выведите список сотрудников, отсортированный по уменьшению их заработной платы.
# Если у нескольких сотрудников одинаковая ЗП, то добавьте сортировку по Фамилии
print(f"Список сотрудников отсортированный по уменьшению ЗП: {bubble_sort_staff(staff)}")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
sal_antitop_sum = 0
i = 0
while i in range(3):
    sal_antitop_sum += bubble_sort_staff(staff)[i]['salary']
    i += 1
print(sal_antitop_sum)
