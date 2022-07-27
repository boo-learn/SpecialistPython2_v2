def bubble_sort(nums):
    print("before sort = ", nums)
    swapped = True
    while swapped:
        swapped = False
        # print("*****")
        for i in range(len(nums) - 1):
            # print("i = ", i)
            if nums[i]['salary'] < nums[i + 1]['salary']:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    print("after sort = ", nums)

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

bubble_sort(staff)
print("Список сотрудников отсортированный по уменьшению ЗП: ", staff)

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
least_salaries= sum(x['salary'] for x in staff[-3:])
print(least_salaries)
