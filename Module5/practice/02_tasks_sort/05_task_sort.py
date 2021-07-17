def sort_choice(nums, key=lambda x: x):
    i = 0
    while i < len(nums) - 1:
        m = i
        j = i + 1
        while j < len(nums):
            if nums[j]['salary'] == nums[m]['salary']:
                if nums[j]['surname'] < nums[m]['surname']:
                    m = j
                elif nums[j]['surname'] == nums[m]['surname'] and nums[j]['name'] < nums[m]['name']:
                    m = j
            elif nums[j]['salary'] < nums[m]['salary']:
                m = j
            j += 1
        nums[i], nums[m] = nums[m], nums[i]
        i += 1


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

staff.sort(key=lambda x: (x['salary'], x['surname'], x['name']))
# sort_choice(staff)
print("Список сотрудников отсортированный по уменьшению ЗП:")
for el in staff:
    print(el)
print()

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
print("Сумма зарплат трех самых низкооплачиваемых сотрудников:")
print(sum((el['salary'] for el in staff[:3])))

