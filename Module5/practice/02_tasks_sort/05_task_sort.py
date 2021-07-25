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
def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i]['salary'] < nums[i + 1]['salary']:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
            elif nums[i]['salary'] == nums[i + 1]['salary'] and nums[i]['surname'] > nums[i + 1]['surname']:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True


bubble_sort(staff)
print(staff)
print("Список сотрудников отсортированный по уменьшению ЗП:")

# 2. Найдите сумму зарплат трех самых низкооплачиваемых сотрудников:
